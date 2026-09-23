# Created by Pritanshu on 2025-05-31
# Updated to v2.0.0 by Pritanshu on 2026-09-23

import os
import re
from datetime import datetime, date
from functools import reduce

import numpy as np
import numexpr as ner
import pytz

from app.utils.memory_utils import log_memory
from app.utils.logger import logger
from app.utils import commands
from app.utils.findNews import fetchLatestNews

from app.utils.embedding_service import EmbeddingService
from app.utils.command_embeddings import (
    load_command_embeddings,
)
from app.utils.semantic_search import (
    find_best_match,
)


# ============================================================
# STARTUP MEMORY BENCHMARK
# ============================================================

log_memory(
    "makeReply.py - before imports"
)


# We intentionally do NOT import:
#
# from sentence_transformers import SentenceTransformer, util
#
# The production application should not load SentenceTransformer.
#
# SentenceTransformer is used only by:
#
# scripts/generate_embeddings.py
#
# to generate xeno_commands.npz during development/build time.


log_memory(
    "makeReply.py - after lightweight imports"
)


# ============================================================
# INITIALIZATION
# ============================================================

log_memory(
    "makeReply.py - before ONNX EmbeddingService"
)


# ------------------------------------------------------------
# Load ONNX embedding service
# ------------------------------------------------------------

onnx_load_start = (
    __import__("time").perf_counter()
)

embedding_service = (
    EmbeddingService()
)

onnx_load_time = (
    __import__("time").perf_counter()
    - onnx_load_start
)


log_memory(
    "makeReply.py - after ONNX EmbeddingService"
)


logger.info(
    "[ONNX] EmbeddingService initialized | "
    "load_time=%.3f seconds",
    onnx_load_time,
)

logger.info(
    "[ONNX] Input names: %s",
    embedding_service.input_names,
)

logger.info(
    "[ONNX] Output names: %s",
    embedding_service.output_names,
)


# ============================================================
# LOAD PRE-GENERATED COMMAND EMBEDDINGS
# ============================================================

log_memory(
    "makeReply.py - before command embeddings load"
)


command_embeddings_start = (
    __import__("time").perf_counter()
)


(
    topicCommandKeys,
    topicCommandEmbeddings,
    basicCommandKeys,
    basicCommandEmbeddings,
) = load_command_embeddings()

allTopicCommandsDict = {
    **commands.windows_cmds,
    **commands.linux_cmds,
    **commands.macos_cmds,
    **commands.github_cmds,
    **commands.mysql_queries,
    **commands.random_facts,
    **commands.powershell_cmds,
    **commands.cs_concepts,
    **commands.news_queries,
    **commands.time_date_queries,
}


initialCommandsDict = {
    **commands.basic_cmds,
    **commands.assistant_role_responses,
    **commands.creator_queries,
    **commands.identity_responses,
    **commands.internet_info,
    **commands.tech_info,
    **commands.common_searches,
    **commands.nature_facts,
    **commands.most_searches,
}


command_embeddings_load_time = (
    __import__("time").perf_counter()
    - command_embeddings_start
)


log_memory(
    "makeReply.py - after command embeddings load"
)


logger.info(
    "[EMBEDDINGS] Command embedding file loaded | "
    "load_time=%.3f seconds",
    command_embeddings_load_time,
)

logger.info(
    "[EMBEDDINGS] Topic commands: %d",
    len(topicCommandKeys),
)

logger.info(
    "[EMBEDDINGS] Topic embedding shape: %s",
    topicCommandEmbeddings.shape,
)

logger.info(
    "[EMBEDDINGS] Topic embedding dtype: %s",
    topicCommandEmbeddings.dtype,
)

logger.info(
    "[EMBEDDINGS] Basic commands: %d",
    len(basicCommandKeys),
)

logger.info(
    "[EMBEDDINGS] Basic embedding shape: %s",
    basicCommandEmbeddings.shape,
)

logger.info(
    "[EMBEDDINGS] Basic embedding dtype: %s",
    basicCommandEmbeddings.dtype,
)


# ============================================================
# VALIDATE LOADED EMBEDDINGS
# ============================================================

if (
    topicCommandEmbeddings.ndim != 2
    or topicCommandEmbeddings.shape[1] != 384
):

    raise ValueError(
        "Invalid topic command embedding shape: "
        f"{topicCommandEmbeddings.shape}"
    )


if (
    basicCommandEmbeddings.ndim != 2
    or basicCommandEmbeddings.shape[1] != 384
):

    raise ValueError(
        "Invalid basic command embedding shape: "
        f"{basicCommandEmbeddings.shape}"
    )


if (
    len(topicCommandKeys)
    != len(topicCommandEmbeddings)
):

    raise ValueError(
        "Topic command count does not match "
        "topic embedding count."
    )


if (
    len(basicCommandKeys)
    != len(basicCommandEmbeddings)
):

    raise ValueError(
        "Basic command count does not match "
        "basic embedding count."
    )


logger.info(
    "[EMBEDDINGS] Validation successful."
)


log_memory(
    "makeReply.py - after embedding validation"
)


# ============================================================
# FINAL STARTUP MEMORY
# ============================================================

log_memory(
    "makeReply.py - fully loaded"
)


# ============================================================
# TOPIC / COMMAND REPLY
# ============================================================

def fetchBestReply(userInput):

    # --------------------------------------------------------
    # User query embedding
    # --------------------------------------------------------

    query_embedding_start = (
        __import__("time").perf_counter()
    )

    userInputEmbedding = (
        embedding_service.encode(
            userInput
        )
    )

    query_embedding_time = (
        __import__("time").perf_counter()
        - query_embedding_start
    )


    log_memory(
        "fetchBestReply - after query embedding"
    )


    logger.info(
        "[ONNX] Query embedding | "
        "input_length=%d | "
        "embedding_shape=%s | "
        "time=%.3f ms",
        len(userInput),
        userInputEmbedding.shape,
        query_embedding_time * 1000,
    )


    # --------------------------------------------------------
    # Semantic search
    # --------------------------------------------------------

    similarity_start = (
        __import__("time").perf_counter()
    )


    bestMatchKey, score = (
        find_best_match(
            userInputEmbedding,
            topicCommandEmbeddings,
            topicCommandKeys,
        )
    )

    bestMatchCommand = allTopicCommandsDict[
        bestMatchKey
    ]

    similarity_time = (
        __import__("time").perf_counter()
        - similarity_start
    )


    logger.info(
        "[SEMANTIC SEARCH] "
        "score=%.6f | "
        "time=%.3f ms | "
        "command=%s",
        score,
        similarity_time * 1000,
        bestMatchCommand,
    )

    if score < 0.5:  # adjust this as needed
        return "Sorry, I couldn't assist with that topic.\nI'm a lightweight AI style chatbot, not a fully developed AI tool! But feel free to ask me about things like Windows commands, Linux commands, macOS commands, PowerShell, GitHub commands, MySQL queries, computer science concepts, jokes, random facts, and mysteries.\nI can perform some calculations, or even find the latest news for you.\nI'd love to help where I can!"
    
    if bestMatchCommand == 'FETCH LATEST NEWS':
        bestMatchCommand = fetchLatestNews()
    elif bestMatchCommand == "GET CURRENT TIME":
        bestMatchCommand = f"Current time in India is {datetime.now(pytz.timezone('Asia/Kolkata')).time().strftime('%H:%M:%S')}"
    elif bestMatchCommand == "GET CURRENT DATE":
        bestMatchCommand = f"Today's date in India is {datetime.now(pytz.timezone('Asia/Kolkata')).date().strftime('%Y-%m-%d')}"
    elif bestMatchCommand == "GET TIME AND DATE":
        bestMatchCommand = f"Current date and time in India is {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%H:%M:%S %Y-%m-%d')}"

    return bestMatchCommand

# ============================================================
# BASIC REPLY
# ============================================================

def fetchBasicReply(userInput):

    # --------------------------------------------------------
    # User query embedding
    # --------------------------------------------------------

    query_embedding_start = (
        __import__("time").perf_counter()
    )

    userInputEmbedding = (
        embedding_service.encode(
            userInput
        )
    )

    query_embedding_time = (
        __import__("time").perf_counter()
        - query_embedding_start
    )


    log_memory(
        "fetchBasicReply - after query embedding"
    )


    logger.info(
        "[ONNX] Basic query embedding | "
        "input_length=%d | "
        "embedding_shape=%s | "
        "time=%.3f ms",
        len(userInput),
        userInputEmbedding.shape,
        query_embedding_time * 1000,
    )


    # --------------------------------------------------------
    # Semantic search
    # --------------------------------------------------------

    similarity_start = (
        __import__("time").perf_counter()
    )


    bestMatchKey, score = (
        find_best_match(
            userInputEmbedding,
            basicCommandEmbeddings,
            basicCommandKeys,
        )
    )

    bestMatchCommand = initialCommandsDict[
        bestMatchKey
    ]
    
    similarity_time = (
        __import__("time").perf_counter()
        - similarity_start
    )


    logger.info(
        "[BASIC SEMANTIC SEARCH] "
        "score=%.6f | "
        "time=%.3f ms | "
        "command=%s",
        score,
        similarity_time * 1000,
        bestMatchCommand,
    )


    return (
        score,
        # The old implementation used:
        #
        # initialCommandsDict[basicCommandKeys[index]]
        #
        # Since our .npz currently stores only keys,
        # we need to map this key back to commands.
        #
        # We will fix this cleanly below.
        bestMatchCommand,
    )

def numberClaculationReply(userInput,operator=None):
    
    calculatedResult = 0
    numberList = re.findall(r'\d+', userInput)

    if operator == 'NOT':
        calculatedResult = f"The bitwise ~ of {numberList[0]} is {~int(numberList[0])}"

    else:
        if 'add' in userInput or 'added' in userInput or 'addition' in userInput or '+' in userInput or 'plus' in userInput:
            calculatedResult = f"Addtion of numbers is {sum(list(map(int,numberList)))}"

        elif 'multiply' in userInput or 'multiplied' in userInput or 'multiplication' in userInput or '*' in userInput or 'times' in userInput:
            calculatedResult = f"Multiplication of numbers is {reduce(lambda a,b: a*b,list(map(int,numberList)))}"

        elif 'sub' in userInput or 'subtract' in userInput or 'subtracted' in userInput or 'subtraction' in userInput or 'minus' in userInput or '-' in userInput:
            if 'from' in userInput:
                calculatedResult = f"The result of subtraction is {int(numberList[1]) - int(numberList[0])}"
            else:
                calculatedResult = int(numberList[0]) - int(numberList[1])

        elif 'mod' in userInput or 'modulo' in userInput or 'remainder' in userInput or '%' in userInput:
            calculatedResult = f"The remainder we get is {int(numberList[0])%int(numberList[1])}"

        elif 'divide' in userInput or 'divided' in userInput or 'division' in userInput or '/' in userInput or 'quotient' in userInput or 'by' in userInput:
            calculatedResult = f"The quotient is {int(numberList[0])/int(numberList[1])}"

        elif 'power' in userInput or 'exponent' in userInput or '**' in userInput:
            calculatedResult = f"The exponential result is {int(numberList[0])**int(numberList[1])}"
            
        elif 'bitwise xor' in userInput or 'bitwise ^' in userInput or 'bitwisexor' in userInput or 'bitwise^' in userInput or 'xor' in userInput or '^' in userInput:
            calculatedResult = f"The bitwise XOR of numbers is {int(numberList[0])^int(numberList[1])}"

        elif 'left shift' in userInput or '< <' in userInput or '<<' in userInput or 'leftshift' in userInput or 'bitwise left shift' in userInput or 'bitwise <<' in userInput or 'bitwiseleftshift' in userInput or 'bitwise<<' in userInput or 'bitwise leftshift' in userInput or 'bitwiseleft shift' in userInput or 'bitwise < <' in userInput or 'bitwise< <' in userInput:
            calculatedResult = f"The bitwise << of numbers is {int(numberList[0])<<int(numberList[1])}"

        elif 'right shift' in userInput or '> >' in userInput or '>>' in userInput or 'rightshift' in userInput or 'bitwise right shift' in userInput or 'bitwise >>' in userInput or 'bitwiserightshift' in userInput or 'bitwise>>' in userInput or 'bitwise rightshift' in userInput or 'bitwiseright shift' in userInput or 'bitwise > >' in userInput or 'bitwise> >' in userInput:
            calculatedResult = f"The bitwise >> of numbers is {int(numberList[0])>>int(numberList[1])}"

        elif 'bitwise' in userInput or 'bitwise and' in userInput or 'bitwise &' in userInput or 'bitwiseand' in userInput or 'bitwise&' in userInput:
            calculatedResult = f"The bitwise & of numbers is {int(numberList[0])&int(numberList[1])}"

    return calculatedResult

def expressionCalculationReply(userInput):
    tokenExpression = re.findall(r'\d+|\*\*|<=|>=|==|!=|[+\-*/%<>]',userInput)
    expressionString = " ".join(tokenExpression)
    calculatedResult = ner.evaluate(expressionString)
    return f"The result of the expression is {calculatedResult.item()}"
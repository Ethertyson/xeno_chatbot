# Created by Pritanshu on 2025-05-31

from sentence_transformers import SentenceTransformer, util
from app.utils import commands
from app.utils.findNews import fetchLatestNews
from datetime import datetime,date
import re
from functools import reduce

model = SentenceTransformer('all-MiniLM-L6-v2')

allTopicCommandsDict = {**commands.windows_cmds,**commands.linux_cmds,**commands.macos_cmds,**commands.github_cmds,**commands.mysql_queries,**commands.random_facts,**commands.powershell_cmds,**commands.cs_concepts,**commands.news_queries,**commands.time_date_queries}

allCmdSemanticKeys = list(allTopicCommandsDict.keys())
allCmdSemanticEmbeddings = model.encode(allCmdSemanticKeys,convert_to_tensor=True)

def fetchBestReply(userInput):

    userInputEmbedding = model.encode(userInput,convert_to_tensor=True)
    matchScores = util.cos_sim(userInputEmbedding,allCmdSemanticEmbeddings)
    bestMatchIntIndex = matchScores.argmax().item()

    score = matchScores[0][bestMatchIntIndex].item()
    if score < 0.5:  # adjust this as needed
        return "Sorry, I couldn't assist with that topic. I'm a lightweight AI style chatbot, not a fully developed AI tool! But feel free to ask me about things like Windows commands, Linux commands, macOS commands, PowerShell, GitHub commands, MySQL queries, computer science concepts, jokes, random facts, some basic arithmetic calculations, or even the latest tech news. I'd love to help where I can!"


    bestMatchCommand = allTopicCommandsDict[allCmdSemanticKeys[bestMatchIntIndex]]
    
    if bestMatchCommand == 'FETCH LATEST NEWS':
        bestMatchCommand = fetchLatestNews()
    elif bestMatchCommand == "GET CURRENT TIME":
        bestMatchCommand = datetime.now().time().strftime("%H:%M:%S")
    elif bestMatchCommand == "GET CURRENT DATE":
        bestMatchCommand = date.today().strftime("%Y-%m-%d")
    elif bestMatchCommand == "GET TIME AND DATE":
        bestMatchCommand = datetime.now().strftime("%H:%M:%S %Y-%m-%d")

    return bestMatchCommand

initialCommandsDict = {**commands.basic_cmds,**commands.assistant_role_responses,**commands.creator_queries,**commands.identity_responses,**commands.internet_info,**commands.tech_info,**commands.common_searches,**commands.nature_facts,**commands.most_searches}

basicCommandKeys = list(initialCommandsDict.keys())
basicCmdSemanticEmbeddings = model.encode(basicCommandKeys,convert_to_tensor=True)

def fetchBasicReply(userInput):

    userInputEmbedding = model.encode(userInput,convert_to_tensor=True)
    matchScores = util.cos_sim(userInputEmbedding,basicCmdSemanticEmbeddings)
    bestMatchIntIndex = matchScores.argmax().item()
    score = matchScores[0][bestMatchIntIndex].item()
    
    return score,initialCommandsDict[basicCommandKeys[bestMatchIntIndex]]

def numberClaculationReply(userInput):

    calculatedResult = 0
    numberList = re.findall(r'\d+', userInput)

    if 'add' in userInput or 'added' in userInput or 'addition' in userInput or '+' in userInput or 'plus' in userInput:
        calculatedResult = sum(list(map(int,numberList)))

    elif 'multiply' in userInput or 'multiplied' in userInput or 'multiplication' in userInput or '*' in userInput or 'times' in userInput:
        calculatedResult = reduce(lambda a,b: a*b,list(map(int,numberList)))

    elif 'sub' in userInput or 'subtract' in userInput or 'subtracted' in userInput or 'subtraction' in userInput or 'minus' in userInput or '-' in userInput:
        if 'from' in userInput:
            calculatedResult = int(numberList[1]) - int(numberList[0])
        else:
            calculatedResult = int(numberList[0]) - int(numberList[1])

    elif 'mod' in userInput or 'modulo' in userInput or 'remainder' in userInput or userInput in '%':
        calculatedResult = int(numberList[0])%int(numberList[1])

    elif 'divide' in userInput or 'divided' in userInput or 'division' in userInput or userInput in '/' or 'quotient' in userInput or 'by' in userInput:
        calculatedResult = int(numberList[0])/int(numberList[1])

    elif 'power' in userInput or 'exponent' in userInput or '**' in userInput:
        calculatedResult = int(numberList[0])**int(numberList[1])

    return calculatedResult
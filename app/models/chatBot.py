#Created by Pritanshu on 2025-05-28

from flask import jsonify
import re
from app.utils.makeReply import fetchBestReply,fetchBasicReply,numberClaculationReply,expressionCalculationReply
from word2number import w2n
class startChat:

    notOperatorKeywords = ['bitwise not', 'bitwise ~','bitwisenot', 'bitwise~','~']
    semanticOperatorKeywords = [
    # Addition   
    'add','added', 'addition', '+', 'plus',

    # Subtraction
    'sub', 'subtract','subtracted', 'subtraction', '-', 'minus',

    # Multiplication
    'multiply','multiplied', 'multiplication', '*', 'times',

    # Division
    'divide', 'divided', 'division', '/','quotient','by',

    # Exponentiation
    'power', 'exponent', '**',

    # Modulo
    'mod', 'modulo', 'remainder', '%',

    # Bitwise AND
    'bitwise and', 'bitwise &','bitwiseand', 'bitwise&','bitwise',

    # Bitwise XOR
    'bitwise xor', 'bitwise ^','bitwisexor', 'bitwise^','xor','^',

    # Left Shift
    'left shift', '< <', '<<','leftshift','bitwise left shift','bitwise <<','bitwiseleftshift','bitwise<<','bitwise leftshift','bitwiseleft shift','bitwise < <','bitwise< <',

    # Right Shift
    'right shift', '> >', '>>','rightshift','bitwise right shift','bitwise >>','bitwiserightshift','bitwise>>','bitwise rightshift','bitwiseright shift','bitwise > >','bitwise> >'
    ]

    symbolOperatorKeywords = ['+','-','*','/','**','%','<','<=','>','>=','==','!=']

    @staticmethod
    def chatBotResponseByTopic(postRequestData):
        try:

            user_msg = postRequestData.get("Message","").lower().strip()
            
            if user_msg:

                # return jsonify({"Num":user_msg})
                user_msg2 = user_msg.replace(',',' ')
                user_msg2 = user_msg2.split()
                for key1,value1 in enumerate(user_msg2):
                    try:
                        convertedNum = w2n.word_to_num(value1)
                        user_msg2[key1] = str(convertedNum)
                    except ValueError:
                        pass
                
                user_msg2 = " ".join(user_msg2)

                if bool(re.search(r'\d+',user_msg2)) and len(re.findall(r'\d+',user_msg2)) > 1:

                    calculationReply = 0

                    if len(list(filter(lambda q: q in user_msg2,startChat.symbolOperatorKeywords))) > 1:
                        calculationReply = expressionCalculationReply(user_msg2)

                    elif any(i in user_msg2 for i in startChat.semanticOperatorKeywords):
                        calculationReply = numberClaculationReply(user_msg2)

                    response = {"Status":"Success","Message":f"{calculationReply}.\nIf the result is unexpected, try to use '-' between the numbers > 20 if you're writing number in words."}

                elif (any(i in user_msg2 for i in startChat.notOperatorKeywords) or ('bitwise' in user_msg2 and 'not' in user_msg2)) and len(re.findall(r'\d+',user_msg2)) == 1:

                    calculationReply = 0

                    calculationReply = numberClaculationReply(user_msg2,'NOT')
                    response = {"Status":"Success","Message":f"{calculationReply}.\nIf the result is unexpected, try to use '-' between the numbers > 20 if you're writing number in words."}

                else:
                    basicReplyAndScore = fetchBasicReply(user_msg)
                    basicReplyScore,basicReply = basicReplyAndScore[0],basicReplyAndScore[1]

                    if basicReplyScore > 0.5:
                        response = {"Status":"Success","Message":basicReply}
                    else:
                        user_msg = re.sub(r"\b(hi|hello|please|give me|could you|show me|what's up|hey|bye|goodbye|see you|help|support|assist|issue)\b", "", user_msg)
                        user_msg = re.sub(r"\s+"," ",user_msg).strip()

                        botSemanticBasedReply = fetchBestReply(user_msg)
                        
                        response = {"Status":"Success","Message":botSemanticBasedReply}
            else:
                # response = {"Status":"Success","Message":user_msg}
                response = {"Status":"Success","Message":"Hey, sorry I didn't got your query, this is Xeno Version1.\nYou can ask me different topics like Windows commands, Linux commands, macOS commands, PowerShell, GitHub commands, MySQL queries, computer science concepts, jokes, random facts, and mysteries.\nAlso I can do some basic calculations, or find the latest news for you.\nI'd love to help where I can!"}

        except Exception as error:
            response = {"Status":"Failed","Message":f"Sorry, I'm getting error in generating response: {error}"}

        if response['Status'] == 'Failed':
            return jsonify(response), 500
        else:
            return jsonify(response), 200

        
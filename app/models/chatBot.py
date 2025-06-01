#Created by Pritanshu on 2025-05-28

from flask import jsonify
import re
from app.utils.makeReply import fetchBestReply,fetchBasicReply,numberClaculationReply
from word2number import w2n
class startChat:

    arithmeticKeywords = [
    'add','added', 'addition', '+', 'plus',
    'sub', 'subtract','subtracted', 'subtraction', '-', 'minus',
    'multiply','multiplied', 'multiplication', '*', 'times',
    'divide', 'divided', 'division', '/','quotient','by',
    'power', 'exponent', '**',
    'mod', 'modulo', 'remainder', '%'
    ]

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

                if any(i in user_msg2 for i in startChat.arithmeticKeywords) and bool(re.search(r'\d+',user_msg2)) and len(re.findall(r'\d+',user_msg2)) > 1:
                    calculationReply = numberClaculationReply(user_msg2)
                    response = {"Status":"Success","Message":f"The result is {calculationReply}. If the result is unexpected, try to use '-' between the numbers > 20 if you're writing number in words. Then, I'll try to give you the expected result."}
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
                response = {"Status":"Success","Message":"Hey, sorry I didn't got your query, this is Xeno Version1. You can ask me different topics like Windows commands, Linux commands, macOS commands, PowerShell, GitHub commands, MySQL queries, computer science concepts, jokes, random facts, some basic arithmetic calculations, or even the latest tech news. I'd love to help where I can!"}

        except Exception as error:
            response = {"Status":"Failed","Message":f"Sorry, I'm getting error in generating response: {error}"}

        if response['Status'] == 'Failed':
            return jsonify(response), 500
        else:
            return jsonify(response), 200

        
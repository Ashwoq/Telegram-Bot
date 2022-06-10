from datetime import datetime
from email import message
# import time
import random

def wrong():
    n = random.randint(0,15)
    if(n<=1):
        return "Moodevi Command ah Olunga type pannu!!!"
    if(n>1 and n<=2):
        return "Un Istathukku type panatha"
    if(n>2 and n<=3):
        return "Command Thappu 10thu fail ah ne?"
    if(n>3 and n<=4):
        return "Yeanga yen time ah yethukku waste panuringa COMMAND THAPPU!!!"
    if(n>5 and n<=6):
        return "Konjamachum Kuchathoda Vaalu Command Thappu!!!"
    if(n>6 and n<=7):
        return "Oru Command ah kuda correct ah poda theriyala Ne yella Yenga .... .... Romba Kastam "
    if(n>7 and n<=8):
        return "CHI!!! Command Thappu"
    if(n>8 and n<=9):
        return "Intha Command ah Ajay ta kelunga (Command Wrong)"
    if(n>9 and n<=10):
        return "Ajay ah keta tha sollunga (Wrong Command)"
    if(n>10 and n<=11):
        return "Unagalukku Ajay Theriyuma bro (Wrong Command)"
    if(n>11 and n<=12):
        return "How do I tell you!!! (Wrong Command)"
    if(n>12 and n<=13):
        return "Unaku Ooorei Kotthu Command Thappu"
    # if(n>14 and n<=15):
    #     return "share your knowledge "
    else:
        return "Command Thappu Anna"


def sample_responses(input_text,update):
    user_msg = str(input_text).lower()    
    if user_msg in ('/hello',"/hi","/hai"):
        return "Vanakkam!!!"

    if (user_msg) == ('/instacode'):
        # if(update.message.chat.type =='group'):
        #     # return update.message.from_user.username supergroup
        #     if(update.message.from_user.username == ("AshwoqDedathS" or "kishore0127" or "srk_1511")):
        #         return "#slicep@ndrom_chi#"
        #     else:
        #         return """You are not authorised to know this information For more details contact HEDITH founders 
        #         : @srk_1511 / @kishore0127""" 
        if(update.message.chat.id == -1001555941262):
            # return update.message.from_user.username supergroup 
            # print(update.message['from']['username'])
            if(update['message']['from']['username'] != "AshwoqDedathS"):
                return "#slicep@ndrom_chi#"
            else:
                return """You are not authorised to know this information For more details contact HEDITH founders 
                : @srk_1511 / @kishore0127"""

        if(update.message.chat.id == -630277599):
            a = update['message']['from'][0]
            if(a == 1378667532):
                return "dot"

        return ("update['message']['from']['username']")
        #  Update {'message': {'channel_chat_created': False, 'group_chat_created': False, 'caption_entities': [], 'message_id': 540, 'date': 1646157776, 'delete_chat_photo': False, 'chat': {'id': -1001555941262, 'title': 'HEDITH (CONSTRUCTION GEN-2 / FEB-14)', 'type': 'supergroup'}, 'text': '/instacode', 'new_chat_members': [], 'new_chat_photo': [], 'entities': [{'length': 10, 'type': 'bot_command', 'offset': 0}], 'photo': [], 'supergroup_chat_created': False, 'from': {'last_name': 'Dedath_S_', 'language_code': 'en', 'first_name': 'Ashwoq', 'username': 'AshwoqDedathS', 'id': 1378667532, 'is_bot': False}}, 'update_id': 762553116} caused error Object of type Message is not JSON serializable
                
# Update {'message': {'group_chat_created': False, 'message_id': 530, 'caption_entities': [], 'chat': {'title': 'HEDITH (CONSTRUCTION GEN-2 / FEB-14)', 'type': 'supergroup', 'id': -1001555941262 }, 'new_chat_members': [], 'text': '/instacode', 'photo': [], 'new_chat_photo': [], 'date': 1646155898, 'supergroup_chat_created': False, 'entities': [{'type': 'bot_command', 'offset': 0, 'length': 10}], 'channel_chat_created': False, 'delete_chat_photo': False, 'from': {'is_bot': False, 'last_name': 'Dedath_S_', 'username': 'AshwoqDedathS', 'language_code': 'en', 'first_name': 'Ashwoq', 'id': 1378667532}}, 'update_id': 762553109} caused error Message text is empty

        # if(update.message.chat.type =='private'):
        #     if(update.message.chat.username == ("AshwoqDedathS" or "kishore0127" or "srk_1511")):
        #         return "#slicep@ndrom_chi#"
        #     else:
        #         return """You are not authorised to know this information For more details contact HEDITH founders 
        #         : @srk_1511 / @kishore0127"""

    if user_msg in ('/time','/time?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    
    if user_msg in ('/adhvik','/mala','/anna'):
        return "mala mala malaaaaaaaaa..."

    if user_msg in ('/athish','/thambi'):
        return "Koyetta erukanum daw!!!"

    # if user_msg in ('/help'):
    #     return """Just Die it will be helpful
    # /react - To Get the react,firebase referrence Links
    # /css - To Get the css reference Links
    #     """
    if user_msg in ('/nakku'):
        return "Do you mean Lick ?"

    if user_msg in ('/kishore','/kumar','/kp'):
        # time.sleep(5)
        return "47 kombu pothuma"
    
    if user_msg in ('/shameem','/shameta','/zomata'):
        return "Excuse Me !!!"
    
    if user_msg in ('/faria','/manuel','/man'):
        return "Aari podu"
        
    if user_msg in ('/praghadheesh','/yeanga','/prags'):
        return "Payasam sapdringala Frand ? "
    
    # if user_msg in ('/vasan','/vasanbro','/keerthi','/keerthibro','/srk','/sr'):
    #     return "Konjamachum Kuchathodu vaalu daw"
    
    if user_msg in ('/meet','/Meet','/meet link','/Meet Link',"/link"):
        return "https://meet.google.com/cbb-xwtg-ztd?authuser=2"
        # return "https://meet.google.com/jjc-hcqr-jcr?pli=1&authuser=2"

    # if( user_msg)in ('/gen1'):
    #     return "mugavari-foundation-pt3.web.app"

    # if( user_msg)in ('/gen2'):
    #     return "https://mugavari-foundations-gen-2.web.app/"

    if user_msg in ('/todaymotivation'):
        return "Arrear Clear Panurom!!!"

    return wrong()
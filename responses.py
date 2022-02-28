from datetime import datetime
import time
import random

def wrong():
    n = random.randint(0,12)
    if(n<=1):
        return "Moodevi Command ah Olunga type pannu!!!"
    if(n>1 and n<=2):
        return "Un Istathukku type panatha"
    if(n>2 and n<=3):
        return "Command Thappu 10thu fail ah ne?"
    if(n>3 and n<=4):
        return "Yeanga yen time ah waste pannanthinga COMMAND THAPPU!!!"
    if(n>5 and n<=6):
        return "Konjamachum Kuchathoda Vaalu Command Thappu!!!"
    if(n>6 and n<=7):
        return "Oru Command ah kuda correct ah poda theriyala Ne yella Yenga .... .... Romba Kastam "
    if(n>7 and n<=8):
        return "CHI!!! Command Thappu"
    if(n>8 and n<=9):
        return "Intha Command ah Ajay ta kelunga (Command Wrong)"
    if(n>9 and n<=10):
        return "Ajay ah keta tha sollunga (Command Wrong)"
    if(n>10 and n<=11):
        return "Unagalukku Ajay Theriyuma bro (Command Wrong)"
    if(n>11 and n<=12):
        return "How do I tell you!!! (Command Wrong)"


def sample_responses(input_text,update):
    user_msg = str(input_text).lower()    
    if user_msg in ('/hello',"/hi","/hai"):
        return "Vanakkam!!!"

    if user_msg == ('/instacode'):
        if(update.message.chat.type =='group'):
            # return update.message.from_user.username
            if(update.message.from_user.username == ("AshwoqDedathS" or "kishore0127" or "srk_1511")):
                return "#slicep@ndrom_chi#"
            else:
                return """You are not authorised to know this information For more details contact HEDITH founders 
                : @srk_1511 / @kishore0127"""

        if(update.message.chat.type =='private'):
            if(update.message.chat.username == ("AshwoqDedathS" or "kishore0127" or "srk_1511")):
                return "#slicep@ndrom_chi#"
            else:
                return """You are not authorised to know this information For more details contact HEDITH founders 
                : @srk_1511 / @kishore0127"""

    if user_msg in ('/time','/time?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    
    if user_msg in ('/str'):
        return "Wat , Wat do you mean ?"

    # if user_msg in ('/help'):
    #     return """Just Die it will be helpful
    # /react - To Get the react,firebase referrence Links
    # /css - To Get the css reference Links
    #     """
    if user_msg in ('/nakku'):
        return "Why are You GAY ?"

    if user_msg in ('/kishore' , '/kumar'):
        time.sleep(5)
        return "PS(After 5 sec) : Reply Varathu"
    
    if user_msg in ('/shameem'):
        return "Na yarayum DEPENDENT Panni ila"
    
    if user_msg in ('/faria','/manuel'):
        return "Aambala"
        
    if user_msg in ('/praghadheesh','/yeanga'):
        return "Na therinju thaa panune but Intentional ah and wanted ah panala !!!"
    
    if user_msg in ('/vasan','/vasanbro','/keerthi','/keerthibro','/srk'):
        return "Konjamachum Kuchathodu vaalu daw"
    
    if user_msg in ('/meet','/Meet','/meet link','/Meet Link',"/link"):
        return "https://meet.google.com/jjc-hcqr-jcr"

    if( user_msg)in ('/gen1'):
        return "mugavari-foundation-pt3.web.app"

    if( user_msg)in ('/gen2'):
        return "https://mugavari-foundations-gen-2.web.app/"


    return wrong()
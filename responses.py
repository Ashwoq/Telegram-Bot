from datetime import datetime
import time
import random

def wrong():
    n = random.randint(0,8)
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
        return "Oru Command ah kuda correct ah poda theriyala Ne yella Yenga Pass agi .... Romba Kastam "
    if(n>6 and n<=7):
        return "CHI!!! Command Thappu daw"
    


def sample_responses(input_text,update):
    user_msg = str(input_text).lower()    
    if user_msg in ('/hello',"/hi","/hai"):
        return "Vanakkam!!!"

    if user_msg in ('/username'):
        if(update.message.chat.type =='group'):
            return update.message.from_user.username
        if(update.message.chat.type =='private'):
            return update.message.chat.username

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

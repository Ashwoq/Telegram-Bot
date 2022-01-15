from datetime import datetime
import random

def wrong():
    n = random.randint(0,5)
    if(n<=1):
        return "Moodevi Command ah Olunga type pannu!!!"
    if(n>1 and n<=2):
        return "Un Istathukku type panatha"
    if(n>2 and n<=3):
        return "Command Thappu 10thu fail ah ne?"


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

    if user_msg in ('/help'):
        return """Just Die it will be helpful
        /react - To Get the react,firebase referrence Links
        /css - To Get the css reference Links
        """
    if user_msg in ('/nakku'):
        return "yenga"

    if user_msg in ('/kishore'):
        return "Atha Reply Varathunu Theriyum la Apram yenna?"

    return wrong()



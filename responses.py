from datetime import datetime
from email import message
import time
import random

def wrong():
    n = random.randint(0,18)
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
        return """Oru Command ah kuda correct ah poda theriyala Ne yella Yenga .... .... 
        Romba Kastam """
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
        return "Unaku Ooorei Kutthu (Command Thappu)"
    if(n>13 and n<=14):
        return "Excuse Me it's a wrong command"
    if(n>14 and n<=15):
        return "What ra ??? (Wrong command)"
    if(n>15 and n<=16):
        return "Yenna thaan Solla vara??? (wrong command)"
    # if(n>17 and n<=18):
    #     return ""
    else:
        return "Command Thappu Anna"


def sample_responses(input_text,update):
    user_msg = str(input_text).lower()    
    if user_msg in ('/hello',"/hi","/hai"):
        return "Vanakkam!!!"

    if user_msg in ('/command'):
        return "Command na singular so /Commands nu type pannu"
    
    if user_msg in ('/commands'):
        return """
        
        Here are the Few Commands Listed

        /time
        /help
        /nakku
        /lick
        /lickers
        /slogan
        /adhvik
        /mala
        /anna
        /athish
        /thambi
        /ramaiya
        /kishore
        /kumar
        /kp
        /ss
        /kombu
        /47kombu
        /saree
        /8lakh
        /shameem
        /shameta
        /zomata
        /faria
        /man
        /manuel
        /dr
        /dhinesh
        /rajan
        /senkathir
        /sengu
        /kathir
        /praghadheesh
        /yeanga
        /prags
        /todaymotivation
        /motivation
        /mudiyathu
        /no
        /dei
        /daw
        /da
        /sadsir
        /sir
        /sad
        /ash
        /ashwoq
        /meet
        /link

        """

    if user_msg in ('/time'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    
    if user_msg in ('/adhvik','/mala','/anna'):
        return "mala mala malaaaaaaaaa..."

    if user_msg in ('/athish','/thambi','/ramaiya'):
        return "Koyetta erukanum daw!!!"

    # if user_msg in ('/help'):
    #     return """Just Die it will be helpful 
    #     """

    if user_msg in ('/slogan'):
        return "NAKKU"
        
    if user_msg in ('/nakku','/lick','/lickers'):
        return "What ra, do you mean Lick ah?"

    if user_msg in ('/kishore','/kumar','/kp'):
        # time.sleep(5)
        return "Interest Illa !!!"
    
    if user_msg in ('/shameem','/shameta','/zomata'):
        return "Excuse Me !!!"
    
    if user_msg in ('/faria','/manuel','/man'):
        return "Aari podu"
    
    if user_msg in ('/ss','/kombu','saree','/8lakh','/47kombu'):
        return "Unwanted Topic... Kindly avoid it"

    if user_msg in ('/praghadheesh','/yeanga','/prags'):
        return "Payasam sapdringala Frand ? "

    if user_msg in ('/senkathir','/sengu','/kathir'):
        return "Antha Kili yenakku thaa !!!"

    if user_msg in ('/dr','/dhinesh','/rajan'):
        return "Well bro, yena sourathunu theriyala"
    
    if user_msg in ('/meet',"/link"):
        return "https://meet.google.com/cbb-xwtg-ztd?authuser=2"

    if user_msg in ("/link"):
        return """
        What Link are you Expecting ???
        Meet Link - /meet

        *#@$* Link - https://www.youtube.com/shorts/Y8E72HUf_X0 
        """

    if user_msg in ('/ash','/ashwoq'):
        s = random.randint(0,5)
        if(s<=1):
            return "Iri !!!"
        else:
            return "Sollu daw?"

    if user_msg in ('/sad'):
        return """
        Yennathu SAD ah !!!

        It's Sir 
        call me /sir or /sadsir
        """

    if user_msg in ('/sir','/sadsir'):
        return """Yes, what can i do for you???
        
        
        
        Athukunu Un Ishta ____ ku Kekatha 😄
        """

    if user_msg in ('/dei','/daw','da'):
        return "Call Me SIR !!! OKIE!!!"

    if user_msg in ('/mudiyathu','/no'):
        return "Mudiyathu na Muditu poda"

    if user_msg in ('/todaymotivation','/motivation'):
        return "Arrear Clear Panurom!!!"

    return wrong()


# ------------------------------------------------------------------------------------------------------------------------

    # if user_msg in ('/vasan','/vasanbro','/keerthi','/keerthibro','/srk','/sr'):
    #     return "Konjamachum Kuchathodu vaalu daw"
    
    # if user_msg in ('/meet','/Meet','/meet link','/Meet Link',"/link"):
        # return "https://meet.google.com/jjc-hcqr-jcr?pli=1&authuser=2"

    # if( user_msg)in ('/gen1'):
    #     return "mugavari-foundation-pt3.web.app"

    # if( user_msg)in ('/gen2'):
    #     return "https://mugavari-foundations-gen-2.web.app/"
    
    # if (user_msg) == ('/instacode'):
    #     if(update.message.chat.id == -1001555941262):
    #         if(update['message']['from']['username'] != "AshwoqDedathS"):
    #             return "#slicep@ndrom_chi#"
    #         else:
    #             return """You are not authorised to know this information For more details contact HEDITH founders 
    #             : @srk_1511 / @kishore0127"""

    #     if(update.message.chat.id == -630277599):
    #         a = update['message']['from'][0]
    #         if(a == 1378667532):
    #             return "dot"
    #     return ("update['message']['from']['username']")

# ------------------------------------------------------------------------------------------------------------------------

from flask import Flask,request
from twilio.twiml.messaging_response import Message, MessagingResponse
import datetime
from xmlrpc.client import _strftime


appbot=Flask(__name__)
@appbot.route("/sms", methods=["get","post"])
def reply():
    msg = request.form.get("Body")
    msg1 = request.form.get("From")
    #greet = ["hello"or"holla"or"hyy"or"wadup"or"sup"or"xup"or"hey"or"heyy"]
    
    if(msg.lower() == 'hello' or msg.lower() == 'holla' or msg.lower() == 'hyy' or msg.lower() == 'wadup' or msg.lower() == 'sup' or msg.lower() == 'xup' or msg.lower() == 'hey' or msg.lower() == 'heyy'):
        reply = msg + ", Welcome to Napsta Hotel.\nHow can I help you?"
 
    else:
        reply = "do not understand the input"
    dt=datetime.datetime.now().strftime("%d %h %Y")
    data=msg+", "+msg1+", "+dt
    resp=MessagingResponse()
    respond = resp.message(reply)
    respond.media("http://napstalimited.bravesites.com/files/resized/584615/250;333;9637983905496e372b26bae8f6a55045315b071c.jpg")
    print("Messg: "+ msg +" From "+ msg1 + " on " + dt)
    return(str(resp))

    
            

        

if (__name__=="__main__"):   
    appbot.run()




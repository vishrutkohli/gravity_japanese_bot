import apiai as ai
import json 
import requests


## This is the token you can obtain from your app's dashboard
from messengerbot.models import user , status_code , status , type_of_service , mode_of_contact , type_of_shipment , type_of_collection , type_of_box , address , language , country , place , order

def natural_text(sender_id,text):
    CLIENT_ACCESS_TOKEN="518b8c00e75d4739aa323e631c8cbc1b"

    ## instantiate an api.ai parser object 
    # parser=ai.ApiAI(CLIENT_ACCESS_TOKEN)

    # #Instantiating a test text request 
    # textRequest=parser.text_request() ## Created a default intent to respond to this user text on api.ai console
    # textRequest.query=text
    # base_url = "https://api.api.ai/v1/"
    url  = "https://api.api.ai/api/query?v=20150910&query=" + text + "&lang=en&sessionId=" + sender_id + "&timezone=2017-07-15T22:54:48+0530"

    ## Parsing the response 
    # response = json.loads(textRequest.getresponse().read().decode('utf-8'))
    headers = {"Authorization" : "Bearer 518b8c00e75d4739aa323e631c8cbc1b"}
    response = requests.get(url, headers=headers)
    response = json.loads(response.text)


    print response
    # print "hihihihihi"
    
    text = response['result']['fulfillment']['speech']
    reply = {"text":text}
    try:

        quickreply = response['result']['fulfillment']['messages'][1]['payload']

        response_object =   {
                          "recipient":{
                            "id":sender_id
                          },
                          "message":quickreply
                        }

        # quickreplies  = json.dumps(response_object)


        reply.update({"quickreplies" : response_object})

    except Exception as e:
                    print e
                    pass

    # try:


    #     if message["message"]["attachments"][0]["type"] == "image":
    #                   p = eresume.objects.get_or_create(fbid =sender_id)[0]
                                        
            
    #     except Exception as e:
    #         print e
    #         pass 


                
    
    print "this is reply" + str(reply)
    return reply




def event_name(sender_id,event):
    CLIENT_ACCESS_TOKEN="518b8c00e75d4739aa323e631c8cbc1b"

    ## instantiate an api.ai parser object 
    # parser=ai.ApiAI(CLIENT_ACCESS_TOKEN)

    # #Instantiating a test text request 
    # textRequest=parser.text_request() ## Created a default intent to respond to this user text on api.ai console
    # textRequest.query=text
    # base_url = "https://api.api.ai/v1/"
    url  = "https://api.api.ai/api/query?v=20150910&e=" + event + "&lang=en&sessionId=" + sender_id + "&timezone=2017-07-15T22:54:48+0530"

    ## Parsing the response 
    # response = json.loads(textRequest.getresponse().read().decode('utf-8'))
    headers = {"Authorization" : "Bearer 518b8c00e75d4739aa323e631c8cbc1b"}
    response = requests.get(url, headers=headers)
    response = json.loads(response.text)


    print response
    # print "hihihihihi"
    
    text = response['result']['fulfillment']['speech']
    reply = {"text":text}
    try:

        quickreply = response['result']['fulfillment']['messages'][1]['payload']

        response_object =   {
                          "recipient":{
                            "id":sender_id
                          },
                          "message":quickreply
                        }

        # quickreplies  = json.dumps(response_object)


        reply.update({"quickreplies" : response_object})

    except Exception as e:
                    print e
                    pass

   


                
    
    print "this is reply" + str(reply)
    return reply


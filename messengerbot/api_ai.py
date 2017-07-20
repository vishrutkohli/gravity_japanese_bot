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

    # url  = "https://api.api.ai/api/query?v=20150910&query=" + text + "&lang=en&sessionId=" + sender_id + "&timezone=2017-07-15T22:54:48+0530"

    # ## Parsing the response 
    # # response = json.loads(textRequest.getresponse().read().decode('utf-8'))
    headers = {"Authorization" : "Bearer 518b8c00e75d4739aa323e631c8cbc1b"  , "Content-Type": "application/json; charset=utf-8"}
    # response = requests.get(url, headers=headers)
    # response = json.loads(response.text)

    url  = "https://api.api.ai/api/query?v=20150910"
    data  = {
                "query": [
                    text 
                ],
                
                "timezone": "America/New_York",
                "lang": "en",
                "sessionId": sender_id 
            }

    data = json.dumps(data)
    response = requests.post(url, headers=headers , data = data )
    response = json.loads(response.text)
    print "this is response" + str(response)

    try:
        context = response['result']['contexts'][0]["name"]
        print "this is context"  + str(context)
        database_intercept(context , response, sender_id)

    except Exception as e:
                        print e
                        pass  

    # print "hihihihihi"
    
    # text = response['result']['fulfillment']['speech']
    # reply = {"text":text}
    # try:

    #     quickreply = response['result']['fulfillment']['messages'][1]['payload']

    #     response_object =   {
    #                       "recipient":{
    #                         "id":sender_id
    #                       },
    #                       "message":quickreply
    #                     }

    #     # quickreplies  = json.dumps(response_object)


    #     reply.update({"quickreplies" : response_object})

    # except Exception as e:
    #                 print e
    #                 pass

    text_array = []
    attachments_array = []
    for text in response['result']['fulfillment']["messages"]:
        try:
            # reply = {"text":text}
            text_array.append(text['speech'])

        except Exception as e:
                        print e
                        pass    


        try:

            # quickreply = response['result']['fulfillment']['messages'][1]['payload']

            response_object =   {
                              "recipient":{
                                "id":sender_id
                              },
                              "message":text['payload']
                            }

            # quickreplies  = json.dumps(response_object)

            attachments_array.append(response_object)
            # reply.update({"quickreplies" : response_object})



        except Exception as e:
                        print e
                        pass

   

    reply  = {"text" : text_array , "attachments":attachments_array }


    # try:


    #     if message["message"]["attachments"][0]["type"] == "image":
    #                   p = eresume.objects.get_or_create(fbid =sender_id)[0]
                                        
            
    #     except Exception as e:
    #         print e
    #         pass 


                
    
    print "this is reply" + str(reply)
    return reply




def event_name(sender_id,event):
    print "entered event_name"
    CLIENT_ACCESS_TOKEN="518b8c00e75d4739aa323e631c8cbc1b"
    user_instance = user.objects.get_or_create(fbid =sender_id)[0]
    name  = user_instance.name 

    order_instance = order.objects.get_or_create(fbid = sender_id)[0]


    ## instantiate an api.ai parser object 
    # parser=ai.ApiAI(CLIENT_ACCESS_TOKEN)

    # #Instantiating a test text request 
    # textRequest=parser.text_request() ## Created a default intent to respond to this user text on api.ai console
    # textRequest.query=text
    # base_url = "https://api.api.ai/v1/"
    headers = {"Authorization" : "Bearer 518b8c00e75d4739aa323e631c8cbc1b"  , "Content-Type": "application/json; charset=utf-8"}

    url  = "https://api.api.ai/v1/query?v=20150910"
    data  = {
            
                "event":{"name":event , "data" : {"name" : name , "box":order_instance.type_of_box , "service" :order_instance.type_of_service  , "address_from":order_instance.address_from , "address_to" : order_instance.address_to , "price" : order_instance.price}},
                
                "timezone": "GMT-5",
                "lang": "en",
                "sessionId": sender_id 
            }

    data = json.dumps(data)        
    response = requests.post(url, headers=headers , data = data )
    response = json.loads(response.text)


    print "this is response" + str(response)
    try:
        context = response['result']['contexts'][0]["name"]
        database_intercept(context , response ,sender_id )

    except Exception as e:
                        print e
                        pass

    try:
        context = response['result']['resolvedQuery']
        database_intercept(context , response ,sender_id )

    except Exception as e:
                        print e
                        pass                         

    # print "hihihihihi"
    text_array = []
    attachments_array = []
    for text in response['result']['fulfillment']["messages"]:
        try:
            # reply = {"text":text}
            text_array.append(text['speech'])

        except Exception as e:
                        print e
                        pass    


        try:

            # quickreply = response['result']['fulfillment']['messages'][1]['payload']

            response_object =   {
                              "recipient":{
                                "id":sender_id
                              },
                              "message":text["payload"]
                            }

            # quickreplies  = json.dumps(response_object)

            attachments_array.append(response_object)
            # reply.update({"quickreplies" : response_object})



        except Exception as e:
                        print e
                        pass

   

    reply  = {"text" : text_array , "attachments":attachments_array }

                
    
    print "this is reply" + str(reply)
    return reply



def database_intercept(context,response ,sender_id):

    order_instance = order.objects.get_or_create(fbid = sender_id)[0]
    
    if context == "order-placing-location-from":
        print "checking database intercept"  + str(response['result']['contexts'][0]["parameters"]["geo-country"])
        order_instance.address_to = response['result']['contexts'][0]["parameters"]["geo-country"]
        order_instance.save()

    elif context == "box-size":
        print "checking database intercept"  + str(response['result']['contexts'][0]["parameters"]["geo-country"])
        order_instance.address_from = response['result']['contexts'][0]["parameters"]["geo-country"]
        order_instance.save()

    # elif context == "parcel-type":
    #     print "checking database intercept"  + str(response['result']['contexts'][0]["parameters"]["location"])
    #     order_instance.address_from = json.dumps(response['result']['contexts'][0]["parameters"]["location"])
    #     order_instance.save()

    elif context in ["Envelope-1" ,"Box-2"  , "Box-3" , "Box-4" , "Box-5" , "Box-6" , "Box-7"  ]:
        print "checking database intercept"  + str(context)
        order_instance.type_of_box = str(context)
        order_instance.save()

    elif context in ["door-to-door " ,"next-day"  , "3-working-day" , "5-working-day"   ]:
        print "checking database intercept"  + str(context)
        order_instance.type_of_service = str(context)
        order_instance.save()                




    else:
        pass

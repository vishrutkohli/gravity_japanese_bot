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
        order_instance.price = cost(context , order_instance.address_to)
        print "this is price" + str(cost(context , order_instance.address_to))

        order_instance.save()

    elif context in ["door-to-door " ,"next-day"  , "3-working-day" , "5-working-day"   ]:
        print "checking database intercept"  + str(context)
        order_instance.type_of_service = str(context)
        order_instance.save()                




    else:
        pass


def cost(box_name , destination_country ):
    cost = ''
    EuropeEU  = ['Austria','Belgium','Bulgaria','Croatia','Cyprus','Czech Republic','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Ireland','Italy','Latvia','Lithuania','Luxembourg','Malta','Netherlands','Poland','Portugal','Romania','Slovakia','Slovenia','Spain','Sweden']

    Europe_Non_EU = ['Albania','Andorra','Belarus','Bosnia and Herzegovina','Canary Islands','Faroe Islands','Gibraltar','Greenland','Guernsey','Iceland','Jersey','Kosovo','Liechtenstein','Macedonia','Moldova, Republic of','Montenegro, Republic of','Norway','Russian Federation','San Marino','Serbia, Republic of','Switzerland','Turkey','Ukraine']

    country = ['USA' , 'Canada' , 'Mexico']

    if box_name == 'Envelope-1':
        if destination_country == 'United Kingdom':
            cost = '£7.95'
        elif destination_country in EuropeEU:
            cost = '£26.95'
        elif destination_country in Europe_Non_EU:
            cost = '£28.95'
        elif destination_country in country:
            cost = '£30.95'
        else:
            cost = '£38.95'


    if box_name == 'Box-2':
        if destination_country == 'United Kingdom':
            cost = '£13.95  '
        elif destination_country in EuropeEU:
            cost = '£34.95'
        elif destination_country in Europe_Non_EU:
            cost = '£36.95'
        elif destination_country in country:
            cost = '£37.95'
        else:
            cost = '£49.95'


    if box_name == 'Box-3':
        if destination_country == 'United Kingdom':
            cost = '£15.95'
        elif destination_country in EuropeEU:
            cost = '£38.95'
        elif destination_country in Europe_Non_EU:
            cost = '£39.95'
        elif destination_country in country:
            cost = '£40.95'
        else:
            cost = '£57.95'


    if box_name == 'Box-4':
        if destination_country == 'United Kingdom':
            cost = '£16.95'
        elif destination_country in EuropeEU:
            cost = '£45.95'
        elif destination_country in Europe_Non_EU:
            cost = '£49.95'
        elif destination_country in country:
            cost = '£55.95'
        else:
            cost = '£78.95'


    if box_name == 'Box-5':
        if destination_country == 'United Kingdom':
            cost = '£19.95'
        elif destination_country in EuropeEU:
            cost = '£67.95'
        elif destination_country in Europe_Non_EU:
            cost = '£79.95'
        elif destination_country in country:
            cost = '£89.95'
        else:
            cost = '£138.95'


    if box_name == 'Box-6':
        if destination_country == 'United Kingdom':
            cost = '£21.95'
        elif destination_country in EuropeEU:
            cost = '£88.95'
        elif destination_country in Europe_Non_EU:
            cost = '£104.95'
        elif destination_country in country:
            cost = '£109.95'
        else:
            cost = '£172.95'


    if box_name == 'Box-7':
        if destination_country == 'United Kingdom':
            cost = '£23.95'
        elif destination_country in EuropeEU:
            cost = '£105.95'
        elif destination_country in Europe_Non_EU:
            cost = '£119.95'
        elif destination_country in country:
            cost = '£125.95'
        else:
            cost = '£199.95'

    else:
        cost = "£23.95"       

    return cost



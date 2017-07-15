import apiai as ai
import json 
## This is the token you can obtain from your app's dashboard

def natural_text(sender_id,text):
    CLIENT_ACCESS_TOKEN="518b8c00e75d4739aa323e631c8cbc1b"

    ## instantiate an api.ai parser object 
    # parser=ai.ApiAI(CLIENT_ACCESS_TOKEN)

    # #Instantiating a test text request 
    # textRequest=parser.text_request() ## Created a default intent to respond to this user text on api.ai console
    # textRequest.query=text
    base_url = "https://api.api.ai/v1/"

    ## Parsing the response 
    response = json.loads(textRequest.getresponse().read().decode('utf-8'))
    print response
    print "hihihihihi"
    
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

    #     cards = response['result']['fulfillment']['messages'][1]['payload']

    #     response_object =   {
    #                       "recipient":{
    #                         "id":sender_id
    #                       },
    #                       "message":cards
    #                     }

    #     # quickreplies  = json.dumps(response_object)


    #     reply.update({"cards" : cards})

    # except Exception as e:
    #                 print e
    #                 pass                
    
    print "this is reply" + str(reply)
    return reply

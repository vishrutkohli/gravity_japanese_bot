
"""
Documentation for this module:
This module of django handles all the requets from the Facebook bot and works via a webhook to get an instant update of a message recieved and replies instantly by parsing specific conditions mentioned in this module for appropriate reply. 
"""
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import urllib2
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
from googletrans import Translator
from api_ai import natural_text , event_name
from messengerbot.models import user , status_code , status , type_of_service , mode_of_contact , type_of_shipment , type_of_collection , type_of_box , address , language , country , place , order

def user_details(fbid):
    url = 'https://graph.facebook.com/v2.6/' + fbid + '?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=' + PAGE_ACCESS_TOKEN
    resp = requests.get(url=url)
    data =json.loads(resp.text)
    return data   

# api.ai webhook integration
@csrf_exempt
def api_ai_webhook(request):
    try:
        print request.body
        x = json.loads(request.body)
        print request.body
        print json.loads(request.body)
    
    except Exception as e:
        print e
        return HttpResponse(e)
    return HttpResponse("Post Succcessful")

VERIFY_TOKEN = 'dhlchatbot'  #verify token for facebook webhook

# Our facebook page acces token 
PAGE_ACCESS_TOKEN = 'EAAjPx66gOdwBAKBQBkIFZAqsz0n6YFvfIjo4XvvtETEj0PdEAlImxYrOQah7AQygUYys8Y45vm0YZAEjr2xEZCU4kw5KxiqxieZCpeGYRrErgGfrT5bqX5xRKnjXJNFLx5uEolZAEFh8ahcX3aAKXSWa6iI4AsfBBB4bgYBdLnibrnWZC59lq1'


def post_facebook_message(fbid,message_text):
    """Function to invoke the facebook API to send message to the dedicated user"""
    translator = Translator()
    message_text = translator.translate(message_text, dest='ja').text
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    print("message_text")
    try:
        response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
        print status.json()
    except Exception as e:
        
        print e
        pass
    try:
        response_msg = json.dumps(message_text)
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
        print status.json()
    except Exception as e:
        
        print e
        pass        

#full implementation of facebook messenger api , facebook grpah api to send a recieve messages to handle user requests . 
class MyChatBotView(generic.View):
    """
    This class handles all types of messages text , quickreplies,postback buttons , cards and images.
    """
    def get (self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Oops invalid token')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        incoming_message= json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                print "this is message" + str(message)
                try:
                    sender_id = message['sender']['id']
                    message_text = message['message']['text']
                    translator = Translator()
                    message_text = translator.translate(message_text, dest='en').text
                    print "just going to  invoke natural_text"
                    user_instance = user.objects.get_or_create(fbid =sender_id)[0]
                    user_detail = user_details(sender_id)
                    name = '%s %s'%(user_detail['first_name'],user_detail['last_name'])
                    user_instance.name = name
                    user_instance.save()
                    if message_text.lower() in "hey,hi,supp,hello".split(','):
                        reply = event_name(sender_id , "welcome")
                    else:
                        reply = natural_text(sender_id , message_text)
                        print "this is reply " + str(reply)
                    
                    try:
                        
                        for message in reply['text']:
                            post_facebook_message(sender_id,message )
                    except Exception as e:
                        print e
                        pass
                    
                    try:    

                        for message in reply['attachments']:
                            post_facebook_message(sender_id, message )
                    except Exception as e:
                        print e
                        pass    
                    
                except Exception as e:
                    print e
                    pass

                try:
                    sender_id = message['sender']['id']
                    print "just going to  invoke postback"
                    user_instance = user.objects.get_or_create(fbid =sender_id)[0]
                    user_detail = user_details(sender_id)
                    name = '%s %s'%(user_detail['first_name'],user_detail['last_name'])
                    user_instance.name = name
                    user_instance.save()
                    print "entered event_name"
                    message_text  = message['postback']['payload']
                    print message_text
                    reply = event_name(sender_id , message_text)
                    try:
                        for message in reply['text']:
                            post_facebook_message(sender_id,message )
                    except Exception as e:
                        print e
                        pass
                    
                    try:    
                        for message in reply['attachments']:
                            post_facebook_message(sender_id, message )
                    except Exception as e:
                        print e
                        pass  

                except Exception as e:
                    print e
                    pass
                try:
                    print "entered event_name"
                    message_text  = message['message']['quick_reply']['payload']
                    print message_text
                    reply = event_name(sender_id , message_text)
                    try:
                        for message in reply['text']:
                            post_facebook_message(sender_id,message )
                    except Exception as e:
                        print e
                        pass
                    
                    try:    
                        for message in reply['attachments']:
                            post_facebook_message(sender_id, message )
                    except Exception as e:
                        print e
                        pass    
                except Exception as e:
                    print e
                    pass
                    
                try:
                  if message["message"]["attachments"][0]["type"] == "image":
                    order_instance = order.objects.get_or_create(fbid = sender_id)[0]
                    if order_instance.picture_state == 1:
                        order_instance.picture_1 = message["message"]["attachments"][0]["payload"]["url"]
                        order_instance.picture_state =2
                        order_instance.save()

                    elif order_instance.picture_state == 2:
                        order_instance.picture_2 = message["message"]["attachments"][0]["payload"]["url"]
                        order_instance.picture_state =1
                        order_instance.save()
                        payload = {'url1':order_instance.picture_2 , 'url2':order_instance.picture_2}
                        payload = json.dumps(payload)
                        r = requests.post("http://139.59.40.238:8080/about" , data = payload)
                        r = json.loads(r.text)
                        print "this is box"  + str(r['boxName'])
                        order_instance.type_of_box = r['boxName']
                        order_instance.save() 
                              
                    reply = event_name(sender_id , "photo")
                    try:
                        for message in reply['text']:
                            post_facebook_message(sender_id,message )
                    except Exception as e:
                        print e
                        pass
                
                    try:    
                        for message in reply['attachments']:
                            post_facebook_message(sender_id, message )
                    except Exception as e:
                        print e
                        pass
                          
                          
                                
                            
                  else:
                    pass                
                    
                   
                except Exception as e:
                    print "this is image exception" + str(e)
                    pass 
        return HttpResponse()  

def index(request):
    greeting_text()
    greeting_button()
    return HttpResponse('Hello world')

def otp_form(request):
    return render(request,'messengerbot/otpForm.html')

def receipt(request):

    return render(request,'messengerbot/smartReciept.html')

def track(request):
    return render(request,'messengerbot/track.html')

def identity_confirm(request):
    """
    This function gets a request from javascript sdk of /otp_form(whitelisted domain for identity confirmation) to check for authenticity of the user .  
    """
    sender_id = request.GET.get('user_id')
    post_facebook_message(sender_id,"thanks , your order is confirmed")


def help(request):
    return HttpResponse('Your Id Has Been Confirmed')



def greeting_text():
    """
    This function acts as a starting button when someone tries the bot for this first time .
    """
    post_message_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s'%PAGE_ACCESS_TOKEN
   
    response_object =   {
         "setting_type":"greeting",
             "greeting":{
             "text":"Hi {{user_first_name}}! Welcome to the prototype version of DHL Chat Bot. This bot showcases a solution to DHL user centric problems for United by HCL Hackathon. USER NOTICE: This bot will extract specific data using context like a country name from addresses, users name for conversation training purposes and has price data scraped from dhl website(https://parcel.dhl.co.uk/dhl-service-point/size-and-price-guide) to give an exact quotation of shipping."
                }
            }

    menu_object = json.dumps(response_object)
    status = requests.post(post_message_url,
          headers = {"Content-Type": "application/json"},
          data = menu_object)


def greeting_button():
    post_message_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s'%PAGE_ACCESS_TOKEN
    
    response_object =   {
        "setting_type":"call_to_actions",
        "thread_state":"new_thread",
        "call_to_actions":[
        {
            "payload":"welcome"
            }
        ]
        }

    menu_object = json.dumps(response_object)
    status = requests.post(post_message_url,
          headers = {"Content-Type": "application/json"},
          data = menu_object)


 
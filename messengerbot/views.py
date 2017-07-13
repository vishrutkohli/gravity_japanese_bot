from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import urllib2
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
from api_ai import natural_text


#api.ai webhook integration
@csrf_exempt
def api_ai_webhook(request):
	# Create your views here.


	try:
		########################### EITHER YOU WILL HAVE YOUR POST REQUEST DATA IN REQUEST.BODY AND REQUEST.POST FROM WHERE YOU CAN PARSE it #######
		print request.body
		print "hihihihihihihihihihihihihii"
		x = json.loads(request.body)
		print request.body
		print json.loads(request.body)

		

		
		




			
	except Exception as e:
		print e
		return HttpResponse(e)
	return HttpResponse("Post Succcessful")


# Create your views here.

VERIFY_TOKEN = 'dhlchatbot'  #verify token for facebook webhook

# Our facebook page acces token 
PAGE_ACCESS_TOKEN = 'EAAGW93sNgsgBAKn6MeSmLHQQBrSFoJZBa3ZCpAZBiSDxMLXshNd7PK1dRSDO1XH4dZBnfBsZBPxsAwh9BNzHKy94aHPaL4WoqdxYvWovstiYleJZC09FEkOoenAFoWxss5NLyXGdcPz1VI46OaEW5LlTZApVlnwFzfF3nGl1wW5tgZDZD'






#Function to invoke the facebook API to 
def post_facebook_message(fbid,message_text):
	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})
	status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
	print status.json()


class MyChatBotView(generic.View):
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
		print  incoming_message

		for entry in incoming_message['entry']:
			for message in entry['messaging']:
				print message
				try:
					sender_id = message['sender']['id']
					message_text = message['message']['text']
					reply = natural_text(sender_id , message_text)
					
					post_facebook_message(sender_id, reply['text'])
					print "hihihihihhi"  + str(reply['quickreplies'])

					quickreply = json.dumps(reply['quickreplies'])
					print "hihihihihhi"  + quickreply
					post_facebook_message(sender_id,quickreply )


						 

					 
				except Exception as e:
					print e
					pass

		return HttpResponse()  

def index(request):
	return HttpResponse('Hello world')
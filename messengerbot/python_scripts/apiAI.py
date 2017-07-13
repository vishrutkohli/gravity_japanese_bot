import apiai as ai
import json 
## This is the token you can obtain from your app's dashboard

CLIENT_ACCESS_TOKEN="518b8c00e75d4739aa323e631c8cbc1b"

## instantiate an api.ai parser object 
parser=ai.ApiAI(CLIENT_ACCESS_TOKEN)

#Instantiating a test text request 
textRequest=parser.text_request() ## Created a default intent to respond to this user text on api.ai console
textRequest.query="Shipment"

## Parsing the response 
response = json.loads(textRequest.getresponse().read().decode('utf-8'))
print response

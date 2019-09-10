


import dialogflow_v2 as dialogflow
session_client = dialogflow.SessionsClient()

session = session_client.session_path("gravity-odutws", "12345")
print('Session path: {}\n'.format(session))



text_input = dialogflow.types.TextInput(
    text="recent order", language_code="en")

query_input = dialogflow.types.QueryInput(text=previous_orders)

response = session_client.detect_intent(
    session=session, query_input=query_input)

print('=' * 20)
print(response.query_result)
print('Query text: {}'.format(response.query_result.query_text))
print('Detected intent: {} (confidence: {})\n'.format(
    response.query_result.intent.display_name,
    response.query_result.intent_detection_confidence))
print('Fulfillment text: {}\n'.format(
    response.query_result.fulfillment_text))
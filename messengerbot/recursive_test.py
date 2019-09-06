from googletrans import Translator




a = {'attachments': [{'recipient': {'id': u'1911270278975783'}, 'message': {u'attachment': {u'type': u'template', u'payload': {u'elements': [{u'title': u'Place Order', u'subtitle': u'Place an order', u'image_url': u'https://assets.materialup.com/uploads/42841b60-cb78-4d5d-b323-5b1a1858e09d/278b52168d5b7c1eee471434fdf8cb0b.gif', u'buttons': [{u'title': u'Place Order', u'type': u'postback', u'payload': u'place-order'}]}, {u'title': u'Previous Order', u'subtitle': u'Manage your previous order', u'image_url': u'http://bashooka.com/wp-content/uploads/2015/12/infographic-timeline-templates-20.jpg', u'buttons': [{u'title': u'Previous Order', u'type': u'postback', u'payload': u'previous-orders'}]}, {u'title': u'Incoming Orders', u'subtitle': u'Manage your incoming order', u'image_url': u'http://www.cmsplus.bbbweb.be/imagenes/ec-order-1.jpg', u'buttons': [{u'title': u'Incoming Orders', u'type': u'postback', u'payload': u'incoming-orders'}]}, {u'title': u'Ask For Quatation', u'subtitle': u'Quatation', u'image_url': u'https://cdn.lynda.com/course/456350/456350-636274412048097806-16x9.jpg', u'buttons': [{u'title': u'Ask For Quatation', u'type': u'postback', u'payload': u'ask-for-quatation'}]}, {u'title': u'Services', u'subtitle': u'services', u'image_url': u'https://www.ansi.org/standards_activities/images/services-systems.jpg', u'buttons': [{u'title': u'Services', u'type': u'postback', u'payload': u'services'}]}], u'template_type': u'generic'}}}}], 'text': [u'Good day Vishrut Kohli ! This is  BitCapBot(DHL prototype Bot). how can can i help you today?']}
# print(type(a))
# def replace_titles(a):
# 	translator = Translator()

# 	for i in a:
# 		print("blah lhahaha1")
# 		# print(i)
# 		if(i == "title"):
# 			print("check check")

# 			a['title'] = translator.translate(a['title'], dest='ja').text
# 			return 0 

# 		else:
# 			if(len(a) == 1):
# 				print("blah lhahaha4")
# 				return 0

# 			else:
# 				print(i)
# 				print("blah lhahaha2")
# 				print(a[i])
# 				replace_titles(a[i])

# 			# else:
# 			# 	print("blah lhahaha3")
# 			# 	replace_titles(a[i])	



# replace_titles(a)


# print(a)
a = str(a)


a = a.split("'title': ")
# print(a[1])

for i in range(1, len(a)):
	b = a[i].split("'")
	translator = Translator()
	b[1] =  translator.translate(b[1], dest='ja').text 
	string = ''

	for j in range(len(b)-1):
		string = string + b[j] + "'"


	string = string + b[-1]




	a[i] = string


# for i in range(1, len(a)):


# print(a)

c = ''
for i in range(len(a)-1):
	c = c + a[i] + "'title': "


c = c + a[-1]




print(c)






# 	if()
# 		a['title'] = translator.translate(a['title'], dest='ja').text
# 		return 0  
# 	except Exception as e:
# 		print("blah blah")

# 		print(a)
# 		try:
# 			for i in a.keys():
# 				replace_titles(a[i])

# 		except Exception as e:

# 			for i in a:
# 				replace_titles(i)
# 				print(e)
		


# print(replace_titles(a))

# print(a)

# a = str(string)

# for "titles" in a :


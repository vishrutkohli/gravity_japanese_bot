from django.test import TestCase

# Create your tests here.

#Testing the facebook verify token end point 

class TestVerifyToken(TestCase):

	## testing for the correct response
	def test_VerifyToken(self):
		test_string="TestCase"
		resp=self.client.get("/facebook_auth/?hub.verify_token=dhlchatbot&hub.challenge=%s"%test_string)
		self.assertEqual(resp.status_code,200)
		print dir(resp)
		self.assertEqual(resp.text,test_string)
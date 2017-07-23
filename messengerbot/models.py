from django.db import models

# Create your models here.

"""
Documentation for this module:
This module of django contains all tables of the databse .
"""




class user(models.Model):
    """user data of the people interacting with the bot """
    mobile = models.CharField(max_length = 250 , default = 'NULL')
    fbid = models.CharField(max_length = 250 , default = 'NULL')


    name = models.CharField(max_length = 250 , default = 'NULL')
    email = models.CharField(max_length = 250 , default = 'NULL')
    

    def __str__(self):
        return self.fbid



class status_code(models.Model):
    """for all the status messages provided by dhl for eg: The instruction data for this shipment have been provided by the sender to DHL electronically"""    

    status = models.CharField(max_length = 250 , default = 'NULL')   

    def __str__(self):
        return self.status



class status(models.Model):
    status = models.ForeignKey(status_code , related_name='statusMessage', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank = True , null = True)
    location = models.CharField(max_length = 250 , default = 'NULL')
    # orderID = models.ForeignKey(order, on_delete=models.CASCADE)

    def __str__(self):
        return self.location 
       



    
class type_of_service(models.Model):
    """for services like "door-to-door","next-day","2-working-day","5-working-day","""

    type_of_service = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.type_of_service


    


class mode_of_contact(models.Model):
    """for mode of conact for the user like "phone " or "online"""

    mode_of_contact = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.mode_of_contact

class type_of_shipment(models.Model):
    #for shipments "Domestic" or "International"

    type_of_shipment = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.type_of_shipment

class type_of_collection(models.Model):
    """for type of collection of parcel "Drop Off" or "Pick up"""

    type_of_collection = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.type_of_collection

class type_of_box(models.Model):
    """for type of containers like envolope , box 1 , box 2 , box 3 etc."""

    type_of_box = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.type_of_box

class address(models.Model):
    """ for address of the user mapped with user id . """

    fbid = models.ManyToManyField(user, null = True)
    name = models.CharField(max_length = 250 , default = 'NULL')
    address = models.CharField(max_length = 250 , default = 'NULL')
    zipCode = models.CharField(max_length = 250 , default = 'NULL')
    email = models.CharField(max_length = 250 , default = 'NULL')
    phone = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.name



class language(models.Model):
    """languages users of the bot speaks . """


    name = models.CharField(max_length = 250 , default = 'NULL')
    

    def __str__(self):
        return self.name







class country(models.Model):
    """data of the countries DHL works in with there timezone and languages spoken"""
    """countries DHL work in"""

    name = models.CharField(max_length = 250 , default = 'NULL')
    

    def __str__(self):
        return self.name                

class place(models.Model):
    """places DHL work in """

    name = models.CharField(max_length = 250 , default = 'NULL')
    timezone = models.CharField(max_length = 250 , default = 'NULL')
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    languages = models.ManyToManyField(language, null = True)
    

    def __str__(self):
        return self.name




class order(models.Model):
    """for all the orders placed by the bot""" 

    date = models.CharField(max_length = 250 , default = 'NULL')
    signature_on_delivery = models.CharField(max_length = 250 , default = 'NULL') 
    description = models.CharField(max_length = 250 , default = 'NULL') 

    order_id = models.CharField(max_length = 250 , default = 'NULL') 
    fbid = models.CharField(max_length = 250 , default = 'NULL') 
    type_of_service = models.CharField(max_length = 250 , default = 'NULL') 
    status = models.CharField(max_length = 250 , default = 'NULL') 
    address_from = models.CharField(max_length = 250 , default = 'NULL') 
    address_to = models.CharField(max_length = 250 , default = 'NULL') 
    type_of_shipment = models.CharField(max_length = 250 , default = 'NULL') 
    mode_of_contact = models.CharField(max_length = 250 , default = 'NULL') 
    type_of_collection = models.CharField(max_length = 250 , default = 'NULL') 
    type_of_box = models.CharField(max_length = 250 , default = 'NULL')
    price = models.CharField(max_length = 250 , default = 'NULL') 
    picture_state = models.IntegerField(max_length = 250 , default = 1)
    picture_1 = models.CharField(max_length = 250 , default = 'NULL')
    picture_2 = models.CharField(max_length = 250 , default = 'NULL')



    

    def __str__(self):
        return self.fbid

    
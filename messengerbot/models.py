from django.db import models

# Create your models here.


#user data of the people interacting with the bot 

class user(models.Model):
    mobile = models.CharField(max_length = 250 , default = 'NULL')
    fbid = models.CharField(max_length = 250 , default = 'NULL')


    name = models.CharField(max_length = 250 , default = 'NULL')
    email = models.CharField(max_length = 250 , default = 'NULL')
    

    def __str__(self):
        return self.fbid


#for all the status messages provided by dhl for eg: "The instruction data for this shipment have been provided by the sender to DHL electronically"    

class status_code(models.Model):
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
       



    
#for services like "door-to-door","next-day","2-working-day","5-working-day",
class type_of_service(models.Model):
    type_of_service = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.type_of_service


    


# for mode of conact for the user like "phone " or "online"
class mode_of_contact(models.Model):
    mode_of_contact = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.mode_of_contact

#for shipments "Domestic" or "International"
class type_of_shipment(models.Model):
    type_of_shipment = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.type_of_shipment

#for type of collection of parcel "Drop Off" or "Pick up"
class type_of_collection(models.Model):
    type_of_collection = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.type_of_collection

# for type of containers like envolope , box 1 , box 2 , box 3 etc.
class type_of_box(models.Model):
    type_of_box = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.type_of_box

#  for address of the user mapped with user id . 
class address(models.Model):
    fbid = models.ManyToManyField(user, null = True)
    name = models.CharField(max_length = 250 , default = 'NULL')
    address = models.CharField(max_length = 250 , default = 'NULL')
    zipCode = models.CharField(max_length = 250 , default = 'NULL')
    email = models.CharField(max_length = 250 , default = 'NULL')
    phone = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.name


#languages users of the bot speaks . 
class language(models.Model):
    name = models.CharField(max_length = 250 , default = 'NULL')
    

    def __str__(self):
        return self.name



#data of the countries DHL works in with there timezone and languages spoken




#countries DHL work in
class country(models.Model):
    name = models.CharField(max_length = 250 , default = 'NULL')
    

    def __str__(self):
        return self.name                

#places DHL work in 
class place(models.Model):
    name = models.CharField(max_length = 250 , default = 'NULL')
    timezone = models.CharField(max_length = 250 , default = 'NULL')
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    languages = models.ManyToManyField(language, null = True)
    

    def __str__(self):
        return self.name




#for all the orders placed by the bot 
class order(models.Model):
    date = models.DateField(blank = True , null = True) 
    signature_on_delivery = models.CharField(max_length = 250 , default = 'NULL') 
    description = models.CharField(max_length = 250 , default = 'NULL') 

    order_id = models.CharField(max_length = 250 , default = 'NULL') 
    fbid = models.ForeignKey(user, on_delete=models.CASCADE)
    type_of_service = models.ForeignKey(type_of_service, on_delete=models.CASCADE)
    status = models.ForeignKey(status, on_delete=models.CASCADE)
    address_from = models.ForeignKey(address, related_name='addressFrom', on_delete=models.CASCADE)
    address_to = models.ForeignKey(address, related_name='addressTo', on_delete=models.CASCADE)
    type_of_shipment = models.ForeignKey(type_of_shipment, on_delete=models.CASCADE)
    mode_of_contact = models.ForeignKey(mode_of_contact, on_delete=models.CASCADE)
    type_of_collection = models.ForeignKey(type_of_collection, on_delete=models.CASCADE)
    type_of_box = models.ForeignKey(type_of_box, on_delete=models.CASCADE)

    

    def __str__(self):
        return self.order_id

    
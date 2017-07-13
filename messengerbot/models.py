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

class statusCode(models.Model):
    status = models.CharField(max_length = 250 , default = 'NULL')   

    def __str__(self):
        return self.status



class status(models.Model):
    status = models.ForeignKey(statusCode , related_name='statusMessage', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank = True , null = True)
    location = models.CharField(max_length = 250 , default = 'NULL')
    # orderID = models.ForeignKey(order, on_delete=models.CASCADE)

    def __str__(self):
        return self.location 
       



    
#for services like "door-to-door","next-day","2-working-day","5-working-day",
class typeOfService(models.Model):
    typeOfService = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.typeOfService


    


# for mode of conact for the user like "phone " or "online"
class modeOfContact(models.Model):
    modeOfContact = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.modeOfContact

#for shipments "Domestic" or "International"
class typeOfShipment(models.Model):
    typeOfShipment = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.typeOfShipment

#for type of collection of parcel "Drop Off" or "Pick up"
class typeOfCollection(models.Model):
    typeOfCollection = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.typeOfCollection

# for type of containers like envolope , box 1 , box 2 , box 3 etc.
class typeOfBox(models.Model):
    typeOfBox = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.typeOfBox

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
    signatureOnDelivery = models.CharField(max_length = 250 , default = 'NULL') 
    description = models.CharField(max_length = 250 , default = 'NULL') 

    orderID = models.CharField(max_length = 250 , default = 'NULL') 
    fbid = models.ForeignKey(user, on_delete=models.CASCADE)
    typeOfService = models.ForeignKey(typeOfService, on_delete=models.CASCADE)
    status = models.ForeignKey(status, on_delete=models.CASCADE)
    addressFrom = models.ForeignKey(address, related_name='addressFrom', on_delete=models.CASCADE)
    addressTo = models.ForeignKey(address, related_name='addressTo', on_delete=models.CASCADE)
    typeOfShipment = models.ForeignKey(typeOfShipment, on_delete=models.CASCADE)
    modeOfContact = models.ForeignKey(modeOfContact, on_delete=models.CASCADE)
    typeOfCollection = models.ForeignKey(typeOfCollection, on_delete=models.CASCADE)
    typeOfBox = models.ForeignKey(typeOfBox, on_delete=models.CASCADE)

    

    def __str__(self):
        return self.orderID

    
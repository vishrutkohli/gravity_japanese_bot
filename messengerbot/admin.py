from django.contrib import admin

# Register your models here.
from messengerbot.models import user , statusCode , status , typeOfService , modeOfContact , typeOfShipment , typeOfCollection , typeOfBox , address , language , country , place , order

admin.site.register(user)
admin.site.register(statusCode)
admin.site.register(status)
admin.site.register(typeOfService)
admin.site.register(modeOfContact)
admin.site.register(typeOfShipment)
admin.site.register(typeOfCollection)
admin.site.register(typeOfBox)
admin.site.register(address)
admin.site.register(language)
admin.site.register(country)
admin.site.register(place)
admin.site.register(order)


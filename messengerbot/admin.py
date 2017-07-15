from django.contrib import admin

# Register your models here.
from messengerbot.models import user , status_code , status , type_of_service , mode_of_contact , type_of_shipment , type_of_collection , type_of_box , address , language , country , place , order

admin.site.register(user)
admin.site.register(status_code)
admin.site.register(status)
admin.site.register(type_of_service)
admin.site.register(mode_of_contact)
admin.site.register(type_of_shipment)
admin.site.register(type_of_collection)
admin.site.register(type_of_box)
admin.site.register(address)
admin.site.register(language)
admin.site.register(country)
admin.site.register(place)
admin.site.register(order)


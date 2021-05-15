from django.contrib import admin
from .models import *


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'Client_Name', 'Phone_number', 'Email', 'Time')


admin.site.register(ContactUs)
admin.site.register(portfolio)
admin.site.register(Package)
admin.site.register(Carousel)
admin.site.register(Statistics)
admin.site.register(Review)
admin.site.register(About)
admin.site.register(About_2)
admin.site.register(Team)
admin.site.register(Reservation, ReservationAdmin)

from django.contrib import admin

from django.contrib import admin

from .models import Criminal, Crime, Casuality, Witness, Offence


class CriminalAdmin(admin.ModelAdmin):
    list_display = ("criminal_name", "gender", "age", "next_of_kin" ,"criminal_photo")


class CrimeAdmin(admin.ModelAdmin):
    list_display = ("crime_date",  "offence",  "location")

class CasualityAdmin(admin.ModelAdmin):
    list_display = ("crime", "casuality_name", "gender", "effect")



class WitnessAdmin(admin.ModelAdmin):
    list_display = ("crime", "witness_name", "gender", "contact")

class OffenceAdmin(admin.ModelAdmin):
    list_display = ("offence_name", "penalty", "description")







admin.site.register(Criminal, CriminalAdmin)
admin.site.register(Crime, CrimeAdmin)
admin.site.register(Casuality, CasualityAdmin)
admin.site.register(Witness, WitnessAdmin)
admin.site.register(Offence, OffenceAdmin)


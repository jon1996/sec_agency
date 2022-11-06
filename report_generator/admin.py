from django.contrib import admin
from .models import addReport

# Register your models here.
@admin.register(addReport)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('heure','mouve','nom_Visiteur','fonction','service','motif','phoneNumber','utilisateur')

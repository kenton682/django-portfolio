from django.contrib import admin

from .models import Card
# Register your models here.

class CardAdmin(admin.ModelAdmin):
    fields=['pub_date', 'title', 'content', 'image']
    
admin.site.register(Card, CardAdmin)
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import Card
# Register your models here.

class CardAdmin(SortableAdminMixin, admin.ModelAdmin):
    # fields=['pub_date', 'title', 'content', 'image']
    pass
    
admin.site.register(Card, CardAdmin)
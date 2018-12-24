from django.contrib import admin
from .models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_mvp','hire_date','email')
    list_display_links = ('id','name')
    list_editable = ('is_mvp',)
    search_fields = ('name','email','phone','description')
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
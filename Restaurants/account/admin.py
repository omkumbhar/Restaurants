from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account




class AccountAdmin(UserAdmin):
    list_display = ['cust_id','email','first_name','last_name','phone','is_admin' ]
    search_fields = ['cust_id','email']
    readonly_fields = [ 'date_joined','last_login','cust_id','phone']



    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []



admin.site.register(Account,AccountAdmin)

# Register your models here.

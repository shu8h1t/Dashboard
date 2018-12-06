from django.contrib import admin

from .models import User, AccountDetails,Transac






class TransacInLine(admin.TabularInline):
    model = Transac
    extra = 1  

class AccountInLine(admin.TabularInline):
    model = AccountDetails
    extra = 1
    
    inlines = [TransacInLine]    

class UserAdmin(admin.ModelAdmin):
    #fields = ['acc_det', 'user_name']

    fieldsets = [
        ('User',  {'fields': ['user_name']}),
        ('Account Number', {'fields': ['acc_det']}),
        ]
    
    inlines = [AccountInLine]
    list_display = ('user_name', 'acc_det')
    

admin.site.register(User, UserAdmin)
# Register your models here.

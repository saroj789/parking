from django.contrib import admin
from django.utils.html import format_html
from .models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.profile_image.url))

    list_display = ('id','email','username','myphoto', 'is_staff','is_admin')
    search_fields=('email','username')
    readonly_fields= ('id','date_joined','last_login')
    list_filter=('is_admin','is_staff','is_superuser')
    list_display_links=('id','email','username')

admin.site.register(Account,AccountAdmin)
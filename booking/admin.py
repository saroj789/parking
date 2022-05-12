from django.contrib import admin
from .models import BookSlot
# Register your models here.

class BookSlotAdmin(admin.ModelAdmin):
  list_display = ['slot','status','entry_time', 'exit_time', 'car_number']
  list_filter  = ['slot','status']
  search_fields= ['slot','status','car_number']
  list_per_page= 20

admin.site.register(BookSlot, BookSlotAdmin)


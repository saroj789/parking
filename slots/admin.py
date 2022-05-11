from django.contrib import admin
from .models import Parking, Slot

# Register your models here.
class SlotInline(admin.TabularInline):
  model = Slot
  readonly_fields = ('parking', 'position', 'entry_time', 'exit_time', 'is_avail')
  extra = 0

class ParkingAdmin(admin.ModelAdmin):
  list_display = ['name', 'city']
  list_filter  = ['name', 'city']
  search_fields= ['name', 'city']
  list_per_page= 20
  inlines      = [SlotInline]   

class SlotAdmin(admin.ModelAdmin):
  list_display = ['parking', 'position',"is_avail"]
  list_filter  = ['parking',"is_avail"]
  search_fields= ['parking',"is_avail"]
  list_per_page= 20



admin.site.register(Parking, ParkingAdmin)
admin.site.register(Slot, SlotAdmin)

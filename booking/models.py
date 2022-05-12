from django.db import models
from accounts.models import Account
from slots.models import Slot

# Create your models here.

class BookSlot(models.Model):

  status_choices=(
        ('booked','booked'),
        ('running','running'),
        ('completed','completed'),       
    )

  user = models.ForeignKey(Account, on_delete=models.CASCADE)
  slot = models.OneToOneField(Slot, on_delete=models.CASCADE)
  car_number = models.CharField(max_length=50)
  entry_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
  exit_time  = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
  status  = models.CharField( choices=status_choices ,max_length=255, blank=True, default='booked')


  def __str__(self):
    return self.car_number
  

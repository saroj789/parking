from django.db import models
from accounts.models import Account

class Parking(models.Model):
  user  = models.ForeignKey(Account, on_delete=models.CASCADE)
  name  = models.CharField( max_length=100)
  city  = models.CharField( max_length=100)
  
  def __str__(self):
    return self.name
  

class Slot(models.Model):
  parking    = models.ForeignKey(Parking, on_delete=models.CASCADE)
  entry_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
  exit_time  = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
  is_avail   = models.BooleanField(default=True)
  position   = models.CharField( max_length=50, blank=True, null=True)

  def __str__(self):
    return self.position

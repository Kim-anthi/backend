from django.db import models

# Create your models here.




# Create your models here.

class Users(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  age = models.IntegerField(null=True, blank=True)
  email = models.EmailField()
  phone_number = models.CharField(max_length=10, null = True, blank = True)
  gender = models.CharField(max_length=10, null = True, blank = True)
  pic = models.ImageField()
  date = models.DateField(null = True, blank = True)
  password = models.CharField(max_length=15) 
  
  
  def __str__(self):
    return self.first_name + '' + self.last_name + '' + self.email
 
 
from django.db import models

# Create your models here.
class Enquiry(models.Model):
    email = models.EmailField(max_length=70,blank=True)
    message = models.CharField(max_length=180, null=True)



    
    

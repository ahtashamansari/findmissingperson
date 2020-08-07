from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class Missing_Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200)
    Contact_no = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='',blank=True)
    image_name = models.CharField(max_length=200)
    file_type = models.CharField(max_length=256, choices=[('image', 'image')])
    def __str__(self):
        return self.image_name  

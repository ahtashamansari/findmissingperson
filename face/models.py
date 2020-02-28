from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=200)
    age = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200)
    Contact_no = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='missing_faces/Known',blank=True)
    def __str__(self):
        return self.name
        
class Unknown(models.Model):
    image = models.ImageField(upload_to='missing_faces/Unknown',blank=True)     
    
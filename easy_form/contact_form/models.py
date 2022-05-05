from django.db import models

class MyForm(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    score = models.CharField(max_length=200, default=-1)
    
    def __str__(self):
        return self.email
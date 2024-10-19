from django.db import models

class product(models.Model):
    name=models.CharField(max_length=100,null=True,)
    age=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=100,null=False)
    
    def __str__(self):
        return self.name +"-"+self.password

class parthadb(models.Model):
    name=models.CharField(max_length=100,null=True) 
    age=models.IntegerField(null=False)
    product=models.IntegerField(default=0)
    password=models.CharField(null=True,max_length=20)
    def __str__(self):
        return self.name +"-"+self.password
    
    
    
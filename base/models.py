from django.db import models
import uuid

# Create your models here.
# models.py

class AboutSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    bullet_points = models.TextField()
    
    def __str__(self):
        return self.title

class Home_Section(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='header_images/')
    def __str__(self):
        return self.title
    
    

class Service(models.Model):
    icon = models.ImageField(upload_to='service_icons/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
    

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name
    

class Feature(models.Model):
    title = models.CharField(max_length=200)
    
    description = models.TextField()
    image = models.ImageField(upload_to='feeatures_images')

    def __str__(self):
        return self.title
    
    

class TokenSale(models.Model):
    days = models.IntegerField(default=0)
    hours = models.IntegerField()
    minutes = models.IntegerField()
    seconds = models.IntegerField()

    def __str__(self):
        return f"Token Sale Countdown - {self.days}d {self.hours}h {self.minutes}m {self.seconds}s"
    
    
    
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question








  
  
      
   
     
     

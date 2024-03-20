from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
gender=(
    ('Male','Male'),

    ('Femlale','Femlale')
)
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    birthday = models.CharField(max_length=10,null=True,blank=True)
    gender= models.CharField(choices=gender,max_length=10)


    def __str__(self):
        return str(self.user)
    
@receiver(post_save, sender=User)
def created_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
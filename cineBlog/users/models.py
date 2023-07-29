from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='user_files', default='default-user.png')
    
    USER_COLLABORATOR = 'Collaborator'
    USER_VISITOR = 'Visitor'
    USER_MEMBER = 'Member'
    SUPER_USER = 'SuperUser'

    TYPES_OF_USER = [
        (USER_COLLABORATOR, 'Collaborator'),
        (USER_VISITOR, 'Visitor'),
        (USER_MEMBER, 'Member'),
        (SUPER_USER, 'Superuser'),
    ]
    
    user_type = models.CharField(max_length=20, choices=TYPES_OF_USER, default=USER_MEMBER)

    def __str__(self):
        return self.username

@receiver(post_save, sender=User)
def asign_user_type(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        instance.user_type = User.SUPER_USER
        instance.save()

@receiver(post_save, sender=User)
def asign_member(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        instance.user_type = User.USER_MEMBER
        instance.save()
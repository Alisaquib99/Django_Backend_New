from django.db import models
from django.contrib.auth.models import AbstractUser
import random
# Create your models here.
    # print(random.randint(123123123123,947258369125))
# def create_new_ref_number():
#       global rand_num
#       rand_num = random.randint(123123,947258)
#       print("this is a random number",rand_num)
#       return rand_num

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length= 100,unique=True)
    username = models.CharField(max_length= 100,unique=True)
    branch = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    account_number = models.IntegerField(default=random.randint(0,99999),blank=True)
    balance = models.IntegerField(default=random.randint(0,99999), blank=True)         
                                                         
                                                 
 
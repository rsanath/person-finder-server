from django.db import models

# Create your models here.


class User(models.Model):
    CLIENT = 'CLIENT'
    APPROVER = 'APPROVER'
    ADMIN = 'ADMIN'
    USER_TYPES = (
        (CLIENT, 'Client'),
        (APPROVER, 'Approver'),
        (ADMIN, 'Admin')
    )

    MALE = 'MALE'
    FEMALE = 'FEMALE'
    NON_BINARY = 'NON_BINARY'
    NOT_PROVIDED = 'NOT_PROVIDED'
    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NON_BINARY, 'Non Binary'),
        (NOT_PROVIDED, 'Not Provided')
    )

    full_name = models.CharField(max_length=200)
    dob = models.DateField('date of birth')
    sex = models.CharField(max_length=20,choices=GENDERS,null=True)
    email_id = models.CharField(max_length=200, unique=True)
    ph_num = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=16)
    address = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=20,choices=USER_TYPES,default=CLIENT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

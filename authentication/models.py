from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class TableCreationInfo(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,  related_name='+', null=True, blank=True)

	updated_at = models.DateTimeField(auto_now=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,  related_name='+', null=True, blank=True)

	class Meta:
		abstract = True

class Permission(TableCreationInfo):
	label = models.CharField(max_length=100)

	def save(self, *args, **kwargs):
		self.label = self.label.upper().replace(' ', '_')
		super().save(*args, **kwargs)

	def __str__(self):
		return self.label
	

class Role(TableCreationInfo):
	label = models.CharField(max_length=50)
	permissions = models.ManyToManyField(Permission, related_name='roles')

	def save(self, *args, **kwargs):
		self.label = self.label.upper().replace(' ', '_')
		super().save(*args, **kwargs)
	
	def __str__(self):
		return self.label


class UserType(models.TextChoices):
		ADMIN = 'admin'
		STUFF = 'stuff'
		CUSTOMER = 'customer'
		VENDOR = 'vendor'
		DELIVERYMAN = 'deliveryman'

class Gender(models.TextChoices):
		MALE = 'male'
		FEMALE = 'female'
		OTHERS = 'others'

class User(AbstractUser, TableCreationInfo):

	gender = models.CharField(max_length=6, choices=Gender.choices, default=None, null=True, blank=True)

	user_type = models.CharField(max_length=12, choices=UserType.choices, default=None, null=True, blank=True)




class Customer(User):
	primary_phone = PhoneNumberField(null=True, blank=True)
	alternative_phone = PhoneNumberField(null=True, blank=True)

	def save(self, *args, **kwargs):
		self.user_type = UserType.CUSTOMER
		super().save(*args, **kwargs)


class Vendor(User):
	primary_phone = PhoneNumberField(null=True, blank=True)
	alternative_phone = PhoneNumberField(null=True, blank=True)

	def save(self, *args, **kwargs):
		self.user_type = UserType.VENDOR
		super().save(*args, **kwargs)


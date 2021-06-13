from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Customer, Permission, Role, User, Vendor

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
	list_display = [field.name for field in User._meta.fields]

# admin.site.register(Customer)

@admin.register(Customer)
class CustomerAdmin(UserAdmin):
	list_display = [field.name for field in Customer._meta.fields]

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Vendor._meta.fields]

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Role._meta.fields]

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Permission._meta.fields]









admin.site.unregister(Group)

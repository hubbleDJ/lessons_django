from django.contrib import admin
from users.models import User
from products.admin import BusketAdmin

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )
    inlines = (BusketAdmin, )
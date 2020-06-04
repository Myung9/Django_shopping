from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', ) # 튜플로 인식하려면 ','를 써줘야 한다

admin.site.register(User, UserAdmin)
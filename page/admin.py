from django.contrib import admin
from .models import Collect

# Register your models here.
# word 있다고 admin에게 알려주기
admin.site.register(Collect)
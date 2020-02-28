from django.contrib import admin
from .models import Question, Unknown
# Register your models here.
admin.site.register(Question)
admin.site.register(Unknown)
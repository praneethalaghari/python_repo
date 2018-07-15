from django.contrib import admin

from .models import Question,Choices

admin.site.register(Question)
admin.site.register(Choices)
# Register your models here.

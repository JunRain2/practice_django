from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# /admin 페이지에서 Question table 관리 가능
admin.site.register(Question, QuestionAdmin)
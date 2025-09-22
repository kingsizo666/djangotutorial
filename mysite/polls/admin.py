from django.contrib import admin

# Register your models here.
from .models import Question

# Default way of registering a model for admin
# admin.site.register(Question)

# Custom way to register a model for admin
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text", "question_topic"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

admin.site.register(Question, QuestionAdmin)
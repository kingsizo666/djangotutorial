from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# TabularInLine is the way it will be displayed. Can also be StackedInLine
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

# Default way of registering a model for admin
# admin.site.register(Question)

# Custom way to register a model for admin
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text", "question_topic"]}),
        #classes collapse makes it as a drop-down menu
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInLine]

    # used to display multiple attributes
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # adds a filter sidebar
    list_filter = ["pub_date"]
    # adds search box on top
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    fieldsets = [
        ("Question information", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]

    list_filter = ["pub_date"]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
    # save_on_top = True
admin.site.register(Choice)
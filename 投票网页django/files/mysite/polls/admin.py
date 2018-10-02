from django.contrib import admin

from .models import Question, Choice


class ChoiceStackInline(admin.TabularInline):
    model = Choice


class ChoiceAdmin(admin.ModelAdmin):
     inlines = [ChoiceStackInline,]


admin.site.register(Question, ChoiceAdmin)

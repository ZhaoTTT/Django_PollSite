from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    """
    This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”
    """


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["question_text","pub_date"] # Defines the sequence of fields to be maintained.
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    # By default, Django displays the str() of each object. But sometimes it’d be more helpful if we could display individual fields. To do that, use the list_display admin option, which is a tuple of field names to display, as columns, on the change list page for the object:
    # sorting by the output of an arbitrary method is not supported
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_per_page = 2
    # date_hierarchy = "pub_date"

admin.site.register(Question, QuestionAdmin)


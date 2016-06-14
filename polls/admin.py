from django.contrib import admin
from .models import Question, Choice
# Register your models here.

#admin.site.register(Question)
class ChoiceAdmin(admin.TabularInline):
	model = Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_editable = ['question_text']
	list_display =['id','question_text', 'pub_date']
	inlines = (ChoiceAdmin,)

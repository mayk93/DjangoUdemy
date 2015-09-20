from django.contrib import admin
from polls.models import Question, Answer

# Register your models here.

class AnswerInline(admin.StackedInline):
    extra = 3
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [ ('Section 1' , {'fields':['questionText']}) , ('Section 2' , {'fields':['publishDate']}) ]
    inlines = [AnswerInline]
    list_display = ('questionText','publishDate' , 'lastSevenDays')
    list_filter = ['publishDate']
    search_fields = ['questionText']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)

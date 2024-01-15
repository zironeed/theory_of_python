from django.contrib import admin
from tester_app.models import Question, Answer, Category


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question')

    def question(self, obj):
        return obj.question.text

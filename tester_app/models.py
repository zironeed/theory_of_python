from django.db import models


class Question(models.Model):
    """
    Модель вопроса, включающая в себя текст вопроса, ответа и категорию
    """
    question = models.TextField(max_length=200, unique=True, verbose_name='question_text')
    answer = models.TextField(verbose_name='text')
    category = models.CharField(max_length=200, verbose_name='category_name')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

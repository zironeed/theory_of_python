from django.db import models


class Category(models.Model):
    """
    about question, too
    """
    name = models.CharField(max_length=200, unique=True, verbose_name='category_name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Question(models.Model):
    """
    about question
    """
    text = models.TextField(max_length=200, unique=True, verbose_name='question_text')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='question_theme',
                                 related_name='question_category')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answer(models.Model):
    """
    about right answer
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='question',
                                 related_name='question_answer')
    text = models.TextField(verbose_name='text')
    is_right = models.BooleanField(default=True, verbose_name='is_answer_right')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

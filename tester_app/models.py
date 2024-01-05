from django.db import models


class Themes(models.TextChoices):
    oop = 'OOP'
    python = "PYTHON's FEATURES"
    sql = 'SQL'
    solid = 'SOLID'
    db = 'DATABASES'
    rest = 'REST'
    git = 'GIT'
    fw_django = 'DJANGO'
    

class Question(models.Model):
    """
    about question
    """
    text = models.TextField(max_length=200, unique=True, verbose_name='question_text')
    theme = models.CharField(choices=Themes.choices, verbose_name='question_theme')


class Answer(models.Model):
    """
    about right answer
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='question')
    text = models.TextField(verbose_name='text')
    is_right = models.BooleanField(default=True, verbose_name='is_answer_right')


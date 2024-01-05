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


class RightAnswer(models.Model):
    """
    about right answer
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='ra_question')
    text = models.TextField(verbose_name='ra_text')


class WrongAnswer(models.Model):
    """
    about wrong answer
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='wa_question')
    text = models.TextField(verbose_name='wa_text')

from django.db import models


class Language(models.Model):
    """
    name
    """
    pass


class Question(models.Model):
    """
    text
    lang - foreign key
    theme
    type
    """
    pass


class Answer(models.Model):
    """
    question - foreign key
    text
    is_right
    """
    pass

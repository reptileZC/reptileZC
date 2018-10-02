from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField()

    def __str__(self):
        return fmt_text(self.question_text)

    def __repr__(self):
        return self.__str__()


class Choice(models.Model):
    choice_text = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey('Question')

    def __str__(self):
        return fmt_text(self.choice_text)

    def __repr__(self):
        return self.__str__()


def fmt_text(text):
    if len(text) <= 50:
        return text
    else:
        return text[:50] + '...'

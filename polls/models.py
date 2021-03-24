import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Staff(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=200)
    bio = models.CharField(max_length=1200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='staff-pics', default="staff-pics/default.jpg")
    

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(_("Date"), default=datetime.date.today)
    description = models.CharField(max_length=1200)

    def __str__(self):
        return self.name


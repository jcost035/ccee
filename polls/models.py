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
    tags = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='Virtual')
    K_12 = 'K'
    EDUCATOR = 'E'
    GRADE_LEVEL_CHOICES = [
        (K_12, _('K-12')),
        (EDUCATOR, _('Educator'))
    ]
    grade_level = models.CharField(
        max_length=2,
        choices=GRADE_LEVEL_CHOICES,
        default=K_12,
    )

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(_("Date"), default=datetime.date.today)
    description = models.CharField(max_length=1200, null=True, blank=True)
    tags = models.CharField(max_length=200, default='', blank=True)
    external = models.BooleanField(default=False)
    external_url = models.CharField(max_length=1200, null=True, blank=True)
    
    thumb_photo = models.ImageField(upload_to='programs', default="staff-pics/default.jpg", blank=True)
    content = models.CharField(max_length=10000, null=True, blank=True)

    CCEE_NEWS = 'N'
    MEDIA_RELEASE = 'M'
    OTHER = 'O'
    GRADE_LEVEL_CHOICES = [
        (CCEE_NEWS, _('CCEE in the News')),
        (MEDIA_RELEASE, _('Media Release')),
        (OTHER, _('Other'))
    ]
    category = models.CharField(
        max_length=2,
        choices=GRADE_LEVEL_CHOICES,
        default=CCEE_NEWS,
    )

    def __str__(self):
        return self.title

class Program(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)
    dates = models.JSONField()
    logo_path = models.CharField(max_length=200)
    about = models.CharField(max_length=1200)
    testimonial = models.CharField(max_length=1200)
    video_path = models.CharField(max_length=200)
    faq = models.JSONField()

    def __str__(self):
        return self.name

class Center(models.Model):
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)

class Mission(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)

    def __str__(self):
        return self.name

class DailyDose(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(_("Date"), default=datetime.date.today)
    description = models.CharField(max_length=1200)
    tags = models.CharField(max_length=200, default='')

    name = models.CharField(max_length=200, null=True)
    key_question = models.CharField(max_length=2000, null=True)
    grade_band = models.CharField(max_length=100, null=True)

    first_article_url = models.CharField(max_length=200, null=True)
    second_article_url = models.CharField(max_length=200, null=True)
    third_article_url = models.CharField(max_length=200, null=True)
    fourth_article_url = models.CharField(max_length=200, null=True)

    first_panel_image = models.BooleanField(null=True)
    first_image_path = models.CharField(max_length=200, null=True, blank=True)
    first_video_path = models.CharField(max_length=200, null=True, blank=True)
    second_panel_image = models.BooleanField(null=True)
    second_image_path = models.CharField(max_length=200, null=True, blank=True)
    second_video_path = models.CharField(max_length=200, null=True, blank=True)

   

    def __str__(self):
        return self.title


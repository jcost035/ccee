from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.forms import model_to_dict

from datetime import date, timedelta

from .models import Question
from .models import Staff
from .models import Event
from .models import Program
from .models import News
from .models import Mission
from .models import DailyDose
from .models import Director
from .models import Officer
from .models import Donor
from .models import Contact
from django.core.mail import send_mail
from django.template import loader
from django.views.generic import ListView


from django.utils.safestring import mark_safe

from django.db.models import Q
import json
import requests



def mail_contact_form(request):

    email_address = request.POST['email_address']
    content = request.POST['content']
    # send_mail(
    #     'Contact form submission',
    #     content,
    #     email_address,
    #     ['contact@ccee.org',
    #     'jcost035@fiu.edu'],
    #     fail_silently=False,
    # )
    Contact.objects.create(email_address=email_address, content=content)


    return HttpResponseRedirect('/')
def subscribe(request):
    
    email_address =  request.POST['address']
    data = {"email_address" : email_address, "first_name": "jorge", "last_name" : "costa" }
    if("@" in email_address and email_address != ''):
        json_data = json.dumps(data)
        # payload = {'json_payload': json_data, 'apikey': '65905886-48af-477f-b935-de5536f22764'}
        # r = requests.get('https://api.cc.email/v3/account/emails', data=payload)
        
        url = 'https://api.cc.email/v3/contacts'
        payload = json.dumps(data)
        headers = {'Content-Type': 'application/json', 'Authorization' : 'Bearer 3af06171-02ee-4fa9-97e9-f36f3924c254', "cache-control": "no-cache"}
        r = requests.post(url, data=payload, headers=headers)
        print(r.text)

    return HttpResponseRedirect('/')

def donors(request):
    donor_list = Donor.objects.all()

    context = {
        "donor_list" : donor_list,
    }
    return render(request, "polls/donors.html", context)

def news_article(request, article_url):
    news = News.objects.filter(title__icontains=article_url)
    articles_list = News.objects.order_by('-date')
    
    context = {
        "news": news[0],
        "first_article": articles_list[0],
        "second_article": articles_list[1],
        "third_article": articles_list[2],
    }
    
    return render(request, "polls/article.html", context)

def dose_article(request, article_url):
    dose = DailyDose.objects.filter(topic__icontains=article_url)
    dose_list = DailyDose.objects.order_by('-date')
    
    context = {
        "dose": dose[0],
        "first_dose": dose_list[0],
        "second_dose": dose_list[1],
        "third_dose": dose_list[2],
    }
    
    return render(request, "polls/daily-dose-article.html", context)

def daily_dose(request):
    return render(request, "polls/daily-dose.html")

def map(request):
    return render(request, "polls/map.html")

def report(request):
    return render(request, "polls/report.html")

def contact(request):
    return render(request, "polls/contact.html")

def donate(request):
    return render(request, "polls/donate.html")

def volunteer(request):
    return render(request, "polls/volunteer.html")

def programs(request, prog_name):
    program = Program.objects.filter(name__icontains=prog_name)
    programs_list = Program.objects.all()
    event_list = Event.objects.filter(program__icontains=prog_name)
    
    context = {
        "program": program[0],
        "faq": program[0].faq["set"],
        "first_program": programs_list[0],
        "second_program": programs_list[1],
        "third_program": programs_list[2],
        "event_list": event_list
    }
    
    return render(request, "polls/programs.html", context)

def calendar_table(request):
    return render(request, "polls/calendar-table.html")

class Calendar(ListView):
    model = Event
    context_object_name = "events"
    
    template_name = "polls/calendar.html"
    paginate_by = 5

    def get_queryset(self):
        location_query = self.request.GET.get('q')
        if location_query == None:
            location_query = ''
        tags_query = self.request.GET.get('r')
        if tags_query == None:
            tags_query = ''
        
        return Event.objects.order_by("-date").filter(
            Q(location__icontains=location_query) , Q(tags__icontains=tags_query)
        )

def event_list(request):
    
    
    events_dict = Event.objects.order_by("date")
    event_list = []

    for event in events_dict:
        additional_fields = {}
        old_date = str(event.date)
        new_date = old_date[5:7] + '/' + old_date[8:10] + '/' + old_date[0:4]
        additional_fields['formatted_date'] = new_date
        additional_fields['thumb_url'] = event.thumb_photo.url
        event_list.append({
            **additional_fields,
            **model_to_dict(event, exclude=['date', 'thumb_photo'])
        })
        
    
    

    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    context = {
        "event_list": json.dumps(event_list),
    }
    return HttpResponse(json.dumps(event_list), content_type="application/json")

def news(request):
    return render(request, "polls/news.html")

def news_list(request):
    

    news_dict = News.objects.order_by("-date")

    news_list = []

    for news in news_dict:
        additional_fields = {}
        old_date = str(news.date)
        new_date = old_date[5:7] + '/' + old_date[8:10] + '/' + old_date[0:4]
        additional_fields['formatted_date'] = new_date
        additional_fields['thumb_url'] = news.thumb_photo.url
        news_list.append({
            **additional_fields,
            **model_to_dict(news, exclude=['date', 'thumb_photo', 'banner_photo'])
        })

        
    # news_list = serializers.serialize('json', news_list)

    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    context = {
        "news_list": json.dumps(news_list),
    }
    return HttpResponse(json.dumps(news_list), content_type="application/json")

def dose_list(request):
    
    dose_list = serializers.serialize('json', DailyDose.objects.order_by("-date"))

    dose_dict = json.loads(dose_list)

    for dose in dose_dict:
        additional_fields = {}
        old_date = dose['fields']['date']
        new_date = old_date[5:7] + '/' + old_date[8:10] + '/' + old_date[0:4]
        dose['fields']['date'] = new_date
        additional_fields['fields']['thumb_url'] = dose.fields.thumb_photo.url
        dose_list.append({
            **additional_fields,
            **model_to_dict(dose, exclude=['thumb_photo'])
        })

        
    dose_list = json.dumps(dose_dict)

    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    context = {
        "dose_list": dose_list,
    }
    return HttpResponse(dose_list, content_type="application/json")

def dose_list_date(request, date_range):
    startdate = date.today()
    enddate = startdate + timedelta(days=date_range)
    dose_list = serializers.serialize('json', Event.objects.filter(date__range=[startdate, enddate]))

    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    context = {
        "dose_list": dose_list,
    }
    return HttpResponse(dose_list, content_type="application/json")

def news_list_date(request, date_range):
    startdate = date.today() - timedelta(days=date_range)
    enddate = date.today() + timedelta(days=1)
    news_list = serializers.serialize('json', Event.objects.filter(date__range=[startdate, enddate]))
    print(startdate)
    print(enddate)

    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    context = {
        "news_list": news_list,
    }
    return HttpResponse(news_list, content_type="application/json")

def event_list_date(request, date_range):
    startdate = date.today()
    enddate = startdate + timedelta(days=date_range)
    event_list = serializers.serialize('json', Event.objects.filter(date__range=[startdate, enddate]))

    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    context = {
        "event_list": event_list,
    }
    return HttpResponse(event_list, content_type="application/json")
    

def student_programs(request):
    return render(request, "polls/student-programs.html")

def community_programs(request):
    return render(request, "polls/community-programs.html")

def k12_programs(request):
    return render(request, "polls/k12-programs.html")

def history_mission(request):
    return render(request, "polls/history-mission.html")

def our_team(request):
    staff_list = Staff.objects.all()
    director_list = Director.objects.all()
    officer_list = Officer.objects.all()
    context = {
        "staff_list": staff_list,
        "director_list": director_list,
        "officer_list": officer_list
    }
    return render(request, "polls/our-team.html", context)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

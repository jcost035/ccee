from django.shortcuts import render
from django.core.paginator import Paginator


from django.http import HttpResponse

from .models import Question
from .models import Staff
from .models import Event
from django.template import loader
from django.views.generic import ListView

from django.db.models import Q

class Calendar(ListView):
    model = Event
    context_object_name = "events"
    
    template_name = "polls/calendar.html"
    paginate_by = 5

    def get_queryset(self):
        location_query = self.request.GET.get('q')
        tags_query = self.request.GET.get('r')
        if location_query == None:
            location_query = ''
        if tags_query == None:
            tags_query = ''
        return Event.objects.order_by("-date").filter(
            Q(location__icontains=location_query) | Q(tags__icontains=tags_query)
        )
    
    

def student_programs(request):
    return render(request, "polls/student-programs.html")

def community_programs(request):
    return render(request, "polls/community-programs.html")

def k12_programs(request):
    return render(request, "polls/k12-programs.html")

def history_mission(request):
    return render(request, "polls/history-mission.html")

def our_team(request):
    staff_list = Staff.objects.order_by("name")
    context = {
        "staff_list": staff_list,
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

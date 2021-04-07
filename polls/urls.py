from django.urls import path
from . import views
from polls.views import Calendar

urlpatterns = [
    path("programs", views.programs, name="programs"),
    path("calendar_table", views.calendar_table, name="calendar_table"),
    path("event_list_date/<int:date_range>", views.event_list_date, name="event_list_date"),
    path("event_list", views.event_list, name="event_list"),
    path("calendar", Calendar.as_view(), name="calendar"),
    path("student-programs", views.student_programs, name="student-programs"),
    path("community-programs", views.community_programs, name="community-programs"),
    path("k12-programs", views.k12_programs, name="k12-programs"),
    path("history-mission", views.history_mission, name="history-mission"),
    path("our-team", views.our_team, name="our-team"),
    path(
        "", views.index, name="index"
    ),  # we're taken here by the include() function in the main urls.py file. #the path function has two required arguments: route (string indicating url pattern) #and view (name of the function in views.py that displays content)
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),  
]

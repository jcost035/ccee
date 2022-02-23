from django.urls import path
from . import views
from polls.views import Calendar, ddoe_redirect

urlpatterns = [
    path('mail_contact_form/', views.mail_contact_form, name='mail_contact_form'),
    path('donors/', views.donors, name='donors'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path("news/<str:article_url>", views.news_article, name="news"),
    path("daily-dose/<str:article_url>", views.dose_article, name="daily-dose"),
    path("dose_list_date/<int:date_range>", views.dose_list_date, name="dose_list_date"),
    path("dose_list/", views.dose_list, name="dose_list"),
    path("dose_list/<int:page_num>", views.dose_list, name="dose_list"),
    path("daily-dose", views.daily_dose, name="daily_dose"),
    path("map", views.map, name="map"),
    path("report", views.report, name="report"),
    path("report-2021", views.report_2021, name="report-2021"),
    path("news_list_date/<int:date_range>", views.news_list_date, name="news_list_date"),
    path("news_list", views.news_list, name="news_list"),
    path("news", views.news, name="news"),
    path("contact", views.contact, name="contact"),
    path("donate", views.donate, name="donate"),
    path("volunteer", views.volunteer, name="volunteer" ),
    path("programs/<str:prog_name>", views.programs, name="programs"),
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
    path("smartpath", views.smartpath_redirect, name="smartpath"),
    path("caset", views.caset_redirect, name="caset"),
    path("ddoe", views.ddoe_redirect, name="ddoe"),
    path("pfc", views.pfc_redirect, name="pfc"),
    path("nec", views.nec_redirect, name="nec"),
    path("advisers", views.adviser_redirect, name="advisers"),
    path("ffle", views.ffle_redirect, name="ffle"),
    path("gala-2022", views.gala_2022, name="gala-2022"),
]

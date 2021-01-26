from django.urls import path

from . import views

urlpatterns = [
    path(
        "", views.index, name="index"
    ),  # we're taken here by the include() function in the main urls.py file. #the path function has two required arguments: route (string indicating url pattern) #and view (name of the function in views.py that displays content)
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

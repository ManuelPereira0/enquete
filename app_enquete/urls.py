from django.urls import path
from . import views

app_name = "app_enquete"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/results/", views.results, name='results'),
    path("<str:question_id>/vote/", views.vote, name='vote'),
]

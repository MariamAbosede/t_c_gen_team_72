from django.urls import path
from . import views
from .views import CreateView, ListTheView, UpdateTheView, DeleteTheView
from django.views.generic import TemplateView


urlpatterns = [

path("", views.CreateView.as_view(), name="Home"),
    path("list/", ListTheView.as_view()),
    path("<pk>/update", UpdateTheView.as_view()),
    path("<pk>/delete", DeleteTheView.as_view()),
    path("you", TemplateView.as_view(template_name='views/home.html')), # django default router

]
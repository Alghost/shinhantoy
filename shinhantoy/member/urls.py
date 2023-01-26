from django.urls import path
from . import views

urlpatterns = [
    path("", views.MemberRegisterView.as_view()),
]
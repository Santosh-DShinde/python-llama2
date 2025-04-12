from django.urls import re_path

"""View Imports"""
from .views.conversation import ConversationView


"""Routes"""
urlpatterns = [
    re_path(r'^chat', ConversationView.as_view()),
]

from django.forms import ModelForm
from django import forms
from customer.models import *
from django.contrib.auth.models import User


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'contents', 'email']
        exclude = ['author']

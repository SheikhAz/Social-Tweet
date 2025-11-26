from dataclasses import field, fields
from django import forms
from .models import Tweet
class TweetForm(forms.ModelForm):
    class meta:
        model = Tweet
        fields = ['text' ,'image']
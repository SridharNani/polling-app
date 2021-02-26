from  django import forms
from .models import Poll
from django.forms import ModelForm


class CreatePollForm(ModelForm):
    class Meta:
        model=Poll
        fields=['question','option_one','option_two','option_three']

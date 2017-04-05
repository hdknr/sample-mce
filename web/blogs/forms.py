# coding: utf-8
from django import forms
from . import models


class EntryForm(forms.ModelForm):

    class Meta:
        model = models.Entry
        exclude = []

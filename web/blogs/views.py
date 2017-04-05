# coding: utf-8
from django import shortcuts
from django.template import response
from . import forms


def entry_index(request):
    instances = forms.EntryForm.Meta.model.objects.all()
    return response.TemplateResponse(
        request, 'blogs/entry/index.html',
        dict(request=request, instances=instances))


def entry_detail(request, id):
    instance = forms.EntryForm.Meta.model.objects.get(id=id)
    return response.TemplateResponse(
        request, 'blogs/entry/detail.html',
        dict(request=request, instance=instance))


def entry_add(request):
    form = forms.EntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return shortcuts.redirect(form.instance.get_absolute_url())

    return response.TemplateResponse(
        request, 'blogs/entry/add.html',
        dict(request=request, form=form))

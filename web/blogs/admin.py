# coding: utf-8
from django.contrib import admin
#
from django.core.urlresolvers import reverse
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

from . import models


class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={
                    'external_link_list_url': reverse('tinymce-linklist')},
            ))
        return super(
            TinyMCEFlatPageAdmin,
            self).formfield_for_dbfield(db_field, **kwargs)

#
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', ]

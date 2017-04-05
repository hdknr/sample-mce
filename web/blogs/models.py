# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse


class Entry(models.Model):
    subject = models.CharField(max_length=100)
    text = models.TextField()

    def __unicode__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('blogs_entry_detail',  kwargs={'id': self.id})

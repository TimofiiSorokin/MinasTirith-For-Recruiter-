from __future__ import absolute_import, unicode_literals

from celery import shared_task

# from demoapp.models import Widget
from celery.task import periodic_task
from datetime import timedelta


@periodic_task(run_every=(timedelta(seconds=5)), name="first_task")
def first_task():
    print("Привет first_task ")


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

# @shared_task
# def count_widgets():
#     return Widget.objects.count()
#
#
# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()

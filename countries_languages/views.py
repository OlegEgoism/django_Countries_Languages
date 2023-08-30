from django.shortcuts import render

from countries_languages.models import thread_local


def create_person(request):
    thread_local.user = request.user if request.user.is_authenticated else None


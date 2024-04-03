from django.shortcuts import render

from django.http import HttpResponse


def health(request):
    return HttpResponse("seminar server ok!")[]from django.shortcuts import render

from django.http import HttpResponse


def health(request):
    return HttpResponse(status = 200, content = "seminar server ok!")
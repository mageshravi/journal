from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class ListView(View):

    def get(self, request):
        return HttpResponse('Hello')

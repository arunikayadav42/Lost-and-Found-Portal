from django.shortcuts import render
from django.views.generic import ListView


def homeview(request):
	return render(request, 'launch/home.html')

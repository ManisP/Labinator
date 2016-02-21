from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	return HttpResponse("This is a placeholder for labs index")

def test(request):
	return HttpResponse("You're looking at question a test?.")

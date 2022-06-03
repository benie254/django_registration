from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse,Http404,HttpResponseRedirect
# from .email import send_email
# from reg.forms import SubscriberForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def an_existing_view_function(request):
	message = "Testing view function--hello!"

	return render(request, 'index.html', {"message": message})

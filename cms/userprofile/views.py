from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
#from django.core.context_processors import csrf


def login_view(request):

    r_email = request.POST["email"]
    r_password = request.POST["password"]
    user = authenticate(email=r_email, password=r_password)
    if user is not None:
        login(request, user)
        return HttpResponse("You are logged in %s" % user.id)
    else:
        return HttpResponse("bad login")

# Create your views here.

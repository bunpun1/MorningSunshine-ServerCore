from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone

def index(request):
   return render(request, "board/forums.html")

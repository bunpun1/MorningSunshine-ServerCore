from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

from .models import uploadDocuments

def index(request):
   return render(request, "files/index.html")

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files/upload-success.html')
    else:
        form = UploadFileForm()
    return render(request, 'files/upload.html', {'form': form})
from django.shortcuts import render
from django.http import HttpResponse
from .models import MyForm
from .forms import MyFormForm

def index(request):
    if request.method == 'POST':
        form = MyFormForm(request.POST)
        if form.is_valid():
            form.save()

    form = MyFormForm()
    context = {'form' : form}
    return render(request, 'form.html', context)

def output(request):
    form_data = MyForm.objects
    return render(request, 'output.html', {'form_data': form_data})
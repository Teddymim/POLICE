from django.shortcuts import render

def index_view(request):
        return render(request, 'index.html')

def criminal_view(request):
        return render(request, 'criminal.html')



def offence_view(request):
        return render(request, 'offence.html')

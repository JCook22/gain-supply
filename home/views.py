from django.shortcuts import render

def index(request):
    """
    Shows the home page
    """ 
    return render(request, 'home/index.html')

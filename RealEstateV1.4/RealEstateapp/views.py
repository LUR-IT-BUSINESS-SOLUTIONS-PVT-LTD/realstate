from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'REhtml/home.html')

def contact(req):
    return render(req,'REhtml/contact.html')

def happyclients(req):
    return render(req,'REhtml/happyclints.html')

def newsandevent(req):
    return render(req, 'REhtml/newsandevent.html')

def aboutus(req):
    return render(req, 'REhtml/aboutus.html')

def nricorner(req):
    return render(req, 'REhtml/nricorner.html')

def video(req):
    return render(req, 'REhtml/video.html')

def ourproject(req):
    return render(req, 'REhtml/ourproject.html')

def ourprojectVenchar(req):
    return render(req, 'REhtml/ourproject-venchor.html')






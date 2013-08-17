from django.shortcuts import render_to_response

def mainscreen(request):
    return render_to_response('phonebook/mainscreen.html')
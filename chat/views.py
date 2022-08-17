from django.shortcuts import render

# Create your views here.
def show_lobby(request):
    return render(request, 'chat/lobby.html')
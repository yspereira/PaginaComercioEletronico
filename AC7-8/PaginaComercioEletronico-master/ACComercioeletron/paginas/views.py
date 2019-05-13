from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request,"login.html")

def Index(request):
    return render(request,"Index.html")

def Eventos(request):
    return render(request,"Eventos.html")

def Tabeladeprecos(request):
    return render(request,"Tabeladeprecos.html")

def cadastroForm(request):
    return render(request,"cadastroForm.html")

def novoUsuario(request):
    return render(request,"novoUsuario.html")




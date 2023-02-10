from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def main(request):
    # template = loader.get_template('main.html')
    # return HttpResponse(template.render());
    return render(request,"main.html");

def verify(request):
    # template = loader.get_template('verify.html')
    # return HttpResponse(template.render());
    return render(request,"verify.html");

def newverify(request):
    return render(request,"newverify.html");

def password(request):
    # template = loader.get_template('password.html')
    # return HttpResponse(template.render());
    return render(request,"password.html");

def newpassword(request):
    return render(request,"newpassword.html");

def account(request):
    # template = loader.get_template('account.html')
    # return HttpResponse(template.render());
    return render(request,"account.html");

def billing(request):
    # template = loader.get_template('billing.html')
    # return HttpResponse(template.render());
    return render(request,"billing.html");

def findaccount(request):
    return render(request,"findaccount.html");

def provision(request):
    return render(request,"provision.html");

def dashboard(request):
    return render(request,"dashboard.html");
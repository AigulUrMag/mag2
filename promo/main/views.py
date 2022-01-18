from django.shortcuts import render
from django.http import HttpResponse

def index(response):
	#return HttpResponse("<h1>Промоакция</h1>")
	return render(response,"main/index.html")

def action(response):	
	return render(response,"main/action.html")
data={'name':'Сушивок'}
def company(response):	
	return render(response,"main/company.html",data)
#

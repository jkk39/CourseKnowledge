from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>This is homepage for theapp</h1>")
form django.http import HttpResponse

def index(request):
	"""显示首页"""

	return HttpResponse("OK")

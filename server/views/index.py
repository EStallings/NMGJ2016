from django.shortcuts import render

# Create your views here.
def index (request):
	context = {
		#'foo': bar,
	}
	return render(request, 'server/index.html', context)
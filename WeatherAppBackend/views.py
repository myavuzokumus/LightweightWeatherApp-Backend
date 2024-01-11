from django.http import HttpResponseRedirect

def error404(request, exception):
  return HttpResponseRedirect('/')
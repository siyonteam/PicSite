from django.http import HttpResponseBadRequest , JsonResponse
from django.urls import reverse

def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap

def ajax_login_required(f):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            login_url= request.build_absolute_uri(reverse('accounts:login'))
            return JsonResponse({"loginUrl":login_url})
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap

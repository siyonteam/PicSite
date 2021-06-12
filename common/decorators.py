from django.http import HttpResponseBadRequest , HttpResponse


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
            return HttpResponse("not authenticated")
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap

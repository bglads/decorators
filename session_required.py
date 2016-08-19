'''
Decorator is useful when a django app has authentication done outside, for example when integrating with legacy apps
'''
from django.http import HttpResponse
import json

def session_required(view_func):
    def __session_required(request,*args, **kwargs):
        try:
            email=request.session['email']
            if email is None:
                raise ValueError('Cannot use None at session value')
        except KeyError as e:
            print str(e),"str(e)"
            return HttpResponse(json.dumps({"status":'URL is invalid'}), content_type="application/json")
        except ValueError as e:
            print str(e),"str(e)"
            return HttpResponse(json.dumps({"status":'URL is invalid'}), content_type="application/json")
        else:
            return view_func(request,*args, **kwargs)
    return wraps(view_func)(__session_required)

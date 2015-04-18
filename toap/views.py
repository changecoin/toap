from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from changetip_api import ChangeTipApi


def home(request):
    context = {}
    if request.user.is_authenticated():
        # Do we have the extra data pulled in?
        social_auth = request.user.social_auth.filter(provider="changetip").first()
        if social_auth.extra_data.get("username") is None:
            # We haven't filled in the data yet from /me/ api endpoint
            api = ChangeTipApi(request.user)
            extra_data = api.me()
            social_auth.extra_data.update(extra_data)
            social_auth.save()
        else:
            extra_data = social_auth.extra_data

        context["extra_data"] = extra_data

    return render_to_response('home.html', context, context_instance=RequestContext(request))


def logout(request):
    django_logout(request)
    return redirect("/")

def plane(request):
    context = {"tip_url": request.GET.get("tip_url")}
    return render_to_response('plane.html', context, context_instance=RequestContext(request))

from django.conf.urls import url

urlpatterns = [
    # Examples:
    url(r'^plane', 'toap.views.plane', name='plane'),
    url(r'^$', 'toap.views.home', name='home'),
]

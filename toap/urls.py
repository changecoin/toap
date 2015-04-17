from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^plane', 'toap.views.plane', name='plane'),
    url(r'^$', 'toap.views.home', name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
] + static("/public", document_root=settings.BASE_DIR + "/public")

from django.conf.urls import url, include
from .views import response

urlpatterns = [
        url(r'^$', response),
]

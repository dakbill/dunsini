from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^ping$', views.pong),
    url(r'^consult$', views.consult)
]

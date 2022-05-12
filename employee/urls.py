from django.conf.urls import url
from employee import views

urlpatterns = [
    url('OBJECT', views.OBJECT, name='OBJECT'),
]

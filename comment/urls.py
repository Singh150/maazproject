from django.conf.urls import url
from comment.views import home,plan,about,contact,feedback

urlpatterns=[
    url(r'^$',home,name='home'),
    url(r'^plan/$',plan,name='plan'),
    url(r'^about/$',about,name='about'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^feedback/$',feedback,name='feedback'),
]
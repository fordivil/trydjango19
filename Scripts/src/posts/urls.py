
from django.conf.urls import url
from .views import (
    posts_create,
posts_list,
posts_delete,
posts_update,
posts_detail,

)

urlpatterns = [

    url(r'^create/$', posts_create),
    url(r'^detail/$', posts_detail),
    url(r'^$', posts_list),
    url(r'^update/$', posts_update),
    url(r'^delete/$', posts_delete),
]

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from accounts.views import (login_view, register_view, logout_view)
from django.conf import settings
from . import views

urlpatterns=[
    url(r'^shops/$',views.shops, name='shops'),
	#url(r'^admin/$', admin.site.urls),
	url(r'^login/$', login_view, name="login"),
	url(r'^logout/$', logout_view, name="logout"),
	url(r'^register/$', register_view, name="register"),
 	url(r'^like/(?P<id>\d+)$', views.like_shop, name="like_shop"),
 
    url(r'^$',views.home, name='home'),
]

#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from accounts.views import (login_view, register_view, logout_view)
from django.conf import settings


urlpatterns=[
	url(r'^admin/', admin.site.urls),
]
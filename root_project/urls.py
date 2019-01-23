
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('accounts.api.urls')),
    url(r'^api/user/', include('accounts.api.user.urls')),
    url(r'^api/status/', include('status.api.urls'))
]

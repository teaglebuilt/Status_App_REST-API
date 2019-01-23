
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('accounts.api.urls')),
    # url(r'^api/user/', include('accounts.api.user.urls')),
    url(r'^api/status/', include('status.api.urls'))
]

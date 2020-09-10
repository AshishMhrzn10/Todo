from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('app.urls')),
    path('api/', include('app.api.urls')),
    path('admin/', admin.site.urls),

]

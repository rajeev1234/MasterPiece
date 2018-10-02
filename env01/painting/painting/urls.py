"""painting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
# from newuser.views import (createpost, detail_post_view, postpreference)

from paints.views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    PostLikeRedirect,
    PostLikeRedirectAPI
)
from newuser.views import signup,logout

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('', post_list, name='list'),
    path('create/', post_create),
    path('?P<slug>/', post_detail, name='detail'),
    path('?P<slug>/like', PostLikeRedirect.as_view(), name='like'),
    path('api/?P<slug>/like', PostLikeRedirectAPI.as_view(), name='like-api'),
    path('?P<slug>/edit/', post_update, name='update'),
    path('?P<slug>/delete/', post_delete, name= 'delete'),
    path('signup/',signup, name = 'signup'),
    path('logout/',logout, name= 'logout/')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

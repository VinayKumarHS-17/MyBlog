from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("view/",views.view_profile,name='view_profile'),
    path("edit/<int:id>",views.edit_profile,name='edit_profile'),
    path("delete/<int:id>/",views.delete_profile,name='delete_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
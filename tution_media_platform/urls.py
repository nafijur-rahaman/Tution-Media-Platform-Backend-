
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/',include("student.urls")),
    path('api/tutor/',include("tutor.urls")),
    path('api/tution/',include("tution.urls")),
    path('api/application/',include("apply_for_tution.urls")),
    path('api/service/',include("service.urls")),
    path('api/',include("communicate.urls")),
    path('api/contact',include("contact_us.urls")),
    
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
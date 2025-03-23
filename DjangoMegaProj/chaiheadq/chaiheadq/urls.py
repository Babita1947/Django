from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tweet import views  # Import views from the tweet app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls')),
    path('', views.tweet_list, name='home'),  # ✅ Add a default route
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

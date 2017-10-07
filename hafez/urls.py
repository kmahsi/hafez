from django.conf.urls import url
from django.contrib import admin
from hafez_telegram_bot import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hafezFall/', views.HafezFallViewSet.as_view(), name='hafez_fall'),
    url(r'^setUserID/', views.set_user_id, name='setUserId'),
]

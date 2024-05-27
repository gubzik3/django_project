from django.contrib import admin
from django.urls import path

from book.views import BookAPIView

urlpatterns = (
    path('admin/', admin.site.urls),
    path('api/v1/booklist/', BookAPIView.as_view()),
)

from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add),    # 添加傻屌图
]

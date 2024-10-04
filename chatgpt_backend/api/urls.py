from django.urls import path
from .views import query_view  # query_view를 임포트합니다.

urlpatterns = [
    path('query/', query_view, name='query'),  # /api/query/ 경로로 query_view를 연결합니다.
]
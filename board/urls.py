from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('', BlogList.as_view()),
    path('<int:pk>/', BlogDetail.as_view({'get':'retrieve'})),
    path('<int:pk>/update/', BlogViewSet.as_view({'get':'retrieve', 'put': 'update'})),
    path('<int:pk>/destroy/', BlogViewSet.as_view({'get':'retrieve', 'delete':'destroy'})),
    path('<int:pk>/comments/', CommentsList.as_view())
]
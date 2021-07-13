from django.urls import path
from .views import SnackListView, SnackUpdateView ,SnackDeleteView,SnackDetailsView, SnackCreateView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/', SnackDetailsView.as_view(), name='snack_details'),
    path('create/', SnackCreateView.as_view(), name='Snack_create'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name= 'Snack_update'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name= 'Snack_delete'),
]

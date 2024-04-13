from django.urls import path
from .views import LoginView, LogoutView, UserCreateAPIView, MovieListCreate,MovieRetriveUpdateDestroy,TheaterListCreate,TheaterRetriveUpdateDestroy,ShowtimeListCreate,ShowtimeRetriveUpdateDestroy,ReserveListCreate, ReserveRetriveUpdateDestroy, PurchaseListCreate, PurchaseRetriveUpdateDestroy

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('movies/', MovieListCreate.as_view(), name="products-create"),
    path('movies/<int:pk>/', MovieRetriveUpdateDestroy.as_view(), name="product-detail"),
   
    path('theaters/', TheaterListCreate.as_view(), name='customer-list-create'),
    path('theaters/<int:pk>/', TheaterRetriveUpdateDestroy.as_view(), name='customer-detail'),
    
    path('showtime/', ShowtimeListCreate.as_view(), name='showtime-list-create'),
    path('showtime/<int:pk>/', ShowtimeRetriveUpdateDestroy.as_view(), name='showtime-detail'),

    path('reserve/', ReserveListCreate.as_view(), name='reserve-list-create'),
    path('reserve/<int:pk>/', ReserveRetriveUpdateDestroy.as_view(), name='reserve-detail'),

    path('purchase/', PurchaseListCreate.as_view(), name='purchase-list-create'),
    path('purchase/<int:pk>/', PurchaseRetriveUpdateDestroy.as_view(), name='purchase-detail'),
   
 

   
]
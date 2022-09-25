from django.urls import path
from .views import (
    ProductDestroyAPIView,
    ProductDetailAPIView,
    ProductListCreateAPIView,
    ProductUpdataAPIView,

    ProductMixinView,

    product_alt_view,
)

urlpatterns = [

    path('', ProductListCreateAPIView.as_view()),
    # path('', ProductMixinView.as_view()),

    path('<int:pk>/', ProductDetailAPIView.as_view()),
    # path('<int:pk>/', ProductMixinView.as_view()),
    
    path('<int:pk>/update/', ProductUpdataAPIView.as_view()),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view()),

]
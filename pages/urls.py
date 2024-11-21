from django.urls import path
from .views import *

urlpatterns = [
    path('tables/', TableListAPIView.as_view(), name='table-list'),                  
    path('tables/create/', TableCreateAPIView.as_view(), name='table-create'),      
    path('tables/<int:pk>/', TableRetrieveUpdateAPIView.as_view(), name='table-detail'),  
    path('tables/delete/<int:pk>/', DishDestroyAPIView.as_view(), name='table-delete'),

    path('Meal/', MealListAPIView.as_view(), name='Meal-list'),                  
    path('Meal/create/', MealCreateAPIView.as_view(), name='Meal-create'),      
    path('Meal/<int:pk>/', MealRetrieveUpdateAPIView.as_view(), name='Meal-detail'),  
    path('Meal/delete/<int:pk>/', DishDestroyAPIView.as_view(), name='Meal-delete'),

    path('Category/', CategoryListAPIView.as_view(), name='Category-list'),                  
    path('Category/create/', CategoryCreateAPIView.as_view(), name='Category-create'),      
    path('Category/<int:pk>/', CategoryRetrieveUpdateAPIView.as_view(), name='Category-detail'),  
    path('Category/delete/<int:pk>/', DishDestroyAPIView.as_view(), name='Category-delete'),

    path('Order/', OrderListAPIView.as_view(), name='Order-list'),                  
    path('Order/create/', OrderCreateAPIView.as_view(), name='Order-create'),      
    path('Order/<int:pk>/', OrderRetrieveUpdateAPIView.as_view(), name='Order-detail'),  
    path('Order/delete/<int:pk>/', DishDestroyAPIView.as_view(), name='Order-delete'),

    path('Bill/', BillListAPIView.as_view(), name='Bill-list'),                  
    path('Bill/create/', BillCreateAPIView.as_view(), name='Bill-create'),      
    path('Bill/<int:pk>/', BillRetrieveUpdateAPIView.as_view(), name='Bill-detail'),
    path('Bill/delete/<int:pk>/', DishDestroyAPIView.as_view(), name='Bill-delete'),

]

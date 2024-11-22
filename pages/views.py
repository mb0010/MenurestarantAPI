from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import *
from .models import Table
from .Serializers import *

class TableListAPIView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['status', 'table_number']  
    search_fields = ['status', 'table_number']  
    ordering_fields = ['table_number', 'status'] 


class TableCreateAPIView(CreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
class DishDestroyAPIView(DestroyAPIView):
    queryset = Table.objects.all()

class MealListAPIView(ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer   
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category', 'name']
    search_fields = ['category__name', 'name']
    ordering_fields = ['name', 'category_name']

class MealCreateAPIView(CreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealDestroyAPIView(DestroyAPIView):
    queryset = Meal.objects.all()

class CategoryListAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

class CategoryCreateAPIView(CreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()

class BillListAPIView(ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['table', 'customer']
    search_fields = ['table__table_number', 'customer']
    ordering_fields = ['table_number', 'created_at']

class BillCreateAPIView(CreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillDestroyAPIView(DestroyAPIView):
    queryset = Bill.objects.all()

class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['bill', 'meal']
    search_fields = ['bill__table__table_number', 'meal__name']
    ordering_fields = ['meal_name', 'bill_table_number']

class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDestroyAPIView(DestroyAPIView):
    queryset = Order.objects.all()


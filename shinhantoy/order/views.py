from rest_framework import generics, mixins

from .serializers import OrderSerializer
from .models import Order

# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    # '''
    # Serializer를 메서드마다 다르게 사용해야 하는 경우
    # serializer_class 값을 할당하지 않고
    # get_serializer_class 함수로 할당합니다.
    # POST일때와 아닐때 다른 Serializer를 사용해야할 때.
    # '''
    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return OrderCreateSerializer
    #     return OrderSerializer

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


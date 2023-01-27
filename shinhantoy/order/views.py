from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from .serializers import OrderSerializer, CommentSerializer, CommentCreateSerializer
from .models import Order, Comment

# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)


class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        if order_id:
            return Comment.objects.filter(order_id=order_id).order_by('-id')
        
        return Comment.objects.none()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

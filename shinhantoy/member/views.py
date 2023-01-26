from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from .serializers import MemberSerializer

# Create your views here.


class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

# class MemberRegisterView(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         tel = request.data.get('tel')

#         if Member.objects.filter(username=username).exists():
#             return Response({
#                 'detail': 'Already used',
#             }, status=status.HTTP_400_BAD_REQUEST)

#         member = Member(
#             username=username,
#             password=make_password(password),
#             tel=tel,
#         )
#         member.save()
#         return Response({
#             'id': member.id,
#             'username': username,
#             'tel': tel
#         },status=status.HTTP_201_CREATED)
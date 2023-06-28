from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from user.serializers import UserSerializer, UserDetailSerializer
from user.models import User
from blog.serializers import PostSerializer
from blog.models import Post

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="Create a new user.",
        responses={201: UserSerializer()}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserGetView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a specific user.",
        responses={200: UserDetailSerializer()}
    )
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserDetailSerializer(user, many=False, context={'request': request})
        data = serializer.data
        return Response(data)
    

class UserPostsAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve posts of a specific user.",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="User ID",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'start',
                openapi.IN_QUERY,
                description="Start index",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'end',
                openapi.IN_QUERY,
                description="End index",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'sort',
                openapi.IN_QUERY,
                description="Sort order",
                type=openapi.TYPE_STRING,
                enum=['asc', 'desc']
            ),
        ],
        responses={200: PostSerializer()}
    )
    def get(self, request, pk):
        start = request.query_params.get('start')
        end = request.query_params.get('end')

        queryset = Post.objects.filter(owner_id=pk).order_by('-date')

        if start:
            queryset = queryset[int(start):]

        if end:
            queryset = queryset[:int(end)]

        serializer = PostSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
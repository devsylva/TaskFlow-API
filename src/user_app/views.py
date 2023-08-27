from .serializers import *
from .models import *
from django.utils.encoding import smart_str
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import update_session_auth_hash

# Create your views here.

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def signUp(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save(owner=request.user)
            user.is_active = False
            user.save()
        else:
            return Response({
                "status": "500",
                "message": "invalid data provided",
                "data":serializer.errors
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        data = {
            "status": "success",
            "message": "registration successful",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)


class ConfirmEmailView(APIView):

    queryset = get_user_model().objects.all()
    serializer_class = ConfirmEmailSerializer
    permission_classes = [AllowAny]
    
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            return Response({"error": "Invalid user ID"}, status=400)

        print(default_token_generator.check_token(user, token), user, token)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.is_verified = True
            user.save()
            return Response({"message": "Email confirmation successful"})
        else:
            return Response({"error": "Invalid token"}, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
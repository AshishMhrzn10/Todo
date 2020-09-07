from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if (password == password2):
            if User.objects.filter(email=email).exists():
                return Response({"error": "Email already exists"})
            else:
                user = User.objects.create_user(
                    username=name, email=email, password=password)
                user.save()
                return Response({"success": "Account created successfully"})

        else:
            return Response({"error": "Passwords do not match"})

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from user_profile.models import Profile
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from django.db.utils import IntegrityError
from rest_framework.permissions import IsAuthenticated


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        user_id = request.user.id
        profile = Profile(user_id=user_id)
        return Response({
            "success": True,
            "message": "Profile details fetched",
            "data": {
                'id': profile.user.id,
                'username': profile.user.username,
                'phone': profile.phone,
                'bio': profile.bio,
                'created_at': profile.created_at,
                'modified_at': profile.modified_at
            }

        })
        return Response(data)


class SignUpView(APIView):

    def post(self, request, format=None):
        """
        Create a new user profile.
        """
        username = request.data.get('username')
        bio = request.data.get('bio')
        email = request.data.get('email')
        phone = request.data.get('phone')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        created_at = request.data.get('created_at')

        if password == confirm_password:
            try:
                user_object = User(username=username, email=email)
                user_object.set_password(password)
                user_object.save()
                profile = Profile(user_id=user_object.id, bio=bio, phone=phone)
                profile.save()
            except IntegrityError:
                return Response({
                    "success": False,
                    "message": "This username already exits",
                    "data": {}
                }, status=status.HTTP_404_NOT_FOUND)

            return Response({
                "success": True,
                "message": "Your Profile has been created",
                "data": {
                    'id': user_object.id,
                    'username': user_object.username,
                    'email': user_object.email,
                    'phone': profile.phone,
                    'created_at': profile.created_at
                }
            })
        else:
            raise HTTP404("Passwords do not match")
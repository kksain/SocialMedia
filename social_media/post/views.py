from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import Post, Like, Comment
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class PostView(APIView):
    permission_classes = [IsAuthenticated]
    """
    * View to list all posts.
    """

    def get(self, request, format=None):
        """
        * Return a list of all posts.
        """
        data = []
        for post in Post.objects.all():
            data.append({
                'id': post.id,
                'text': post.text,
                'created_at': post.created_at,
                'modified_at': post.modified_at
            })
        return Response(data)

    def post(self, request, format=None):
        """
        * Return a list of all posts.
        """
        text = request.data.get('text')
        user_id = request.data.get('user_id')
        post_object = Post(text=text, user_id=user_id)
        post_object.save()
        return Response({
            "success": True,
            "message": "Your post has been uploaded",
            "data": {
                'id': post_object.id,
                'text': post_object.text,
                'created_at': post_object.created_at,
                'modified_at': post_object.modified_at
            }

        })


class DeletePostView(APIView):
    """
    View to delete a post.
    """

    def get_object(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        post_id = request.data.get('post_id')
        _post = self.get_object(post_id)
        _post.delete()
        return Response({
            "success": True,
            "message": "Post deleted successfully",
            "data": []
        }, status=status.HTTP_204_NO_CONTENT)


class LikeView(APIView):
    """
    View to list all likes on posts.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all posts.
        """
        data = []

        for item in Like.objects.all():
            data.append({
                'user_id': item.user_id,
                'post_id': item.post_id,
                'created_at': item.created_at,
                'modified_at': item.modified_at
            })
        return Response(data)

    def get_object(self, post_id):
        try:
            return Like.objects.get(post_id=post_id)
        except Like.DoesNotExist:
            return None

    def post(self, request, format=None):
        """
        * View to like or unlike a post.
        """
        user_id = request.data.get('user_id')
        post_id = request.data.get('post_id')
        _like = self.get_object(post_id=post_id)
        if not _like:
            like_object = Like(user_id=user_id, post_id=post_id)
            like_object = Like(user_id=user_id, post_id=post_id)
            like_object.save()
            return Response({
                "success": True,
                "message": "Your Like has been saved",
                "data": {}

            })
        else:
            _like.delete()
            return Response({
                "success": True,
                "message": "Post unliked",
                "data": []
            }, status=status.HTTP_204_NO_CONTENT)


class CommentView(APIView):
    """
    View to list all comments on a post.
    """

    def get(self, request, format=None):
        """
        Return a list of all posts.
        """
        data = []

        for item in Comment.objects.all():
            data.append({
                'user_id': item.user_id,
                'post_id': item.post_id,
                'created_at': item.created_at,
                'modified_at': item.modified_at
            })
        return Response(data)

    def get_object(self, post_id):
        try:
            return Comment.objects.get(post_id=post_id)
        except Comment.DoesNotExist:
            return None

    def post(self, request, format=None):
        """
        View to comment on a post.
        """
        user_id = request.data.get('user_id')
        post_id = request.data.get('post_id')
        text = request.data.get('text')
        comment = Comment(user_id=user_id, post_id=post_id, text=text)
        comment.save()
        return Response({
            "success": True,
            "message": "Your comment has been uploaded",
            "data": {
                'user_id': comment.user_id,
                'text': comment.text,
                'created_at': comment.created_at,
                'modified_at': comment.modified_at
            }
        })

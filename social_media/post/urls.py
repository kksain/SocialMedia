from django.urls import path, include, re_path
from post.views import PostView,  LikeView, DeletePostView, CommentView
from .views import Post
urlpatterns = [
    path('post/', PostView.as_view()),
    path('post/like/', LikeView.as_view(), name='like_post'),
    path('post/delete/', DeletePostView.as_view()),
    path('post/comment/', CommentView.as_view(), name='post_comment')

]

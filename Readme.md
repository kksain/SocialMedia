## Create and Activate Virtual Environment:
- python -m venv venv
- venv\Scripts\activate

## Installation

## Clone the repository:
- git clone https://github.com/kksain/SocialMedia.git

## Navigate to the project directory:
- cd  social_media

## Install Requirement
- pip install -r requirements.txt

## Apply database migrations:
- python manage.py migrate

## Run the development server:
- python manage.py runserver

## A Django REST framework API that handles operations related to posts, likes, and comments. Below is a brief documentation for the code:

### PostView
This class defines API endpoints for listing and creating posts.

- GET /api/posts/: Retrieves a list of all posts in the system.
- POST /api/posts/: Creates a new post with the provided text and user ID.

### DeletePostView
This class provides an API endpoint for deleting a post.

- POST /api/posts/delete/: Deletes a post by its ID. Requires the 'post_id' in the request data.

### LikeView
This class defines API endpoints for listing likes and managing post likes.

- GET /api/likes/: Retrieves a list of all likes in the system.
- POST /api/likes/: Toggles a like on a post. If the user has not liked the post, it adds a like, and if the user has already liked it, it removes the like. Requires 'user_id' and 'post_id' in the request data.

### CommentView
This class provides API endpoints for listing and creating comments on posts.

- GET /api/comments/: Retrieves a list of all comments in the system.
- POST /api/comments/: Creates a new comment on a post. Requires 'user_id', 'post_id', and 'text' in the request data.

Please note that this code assumes you have Django and the Django REST framework installed and properly configured in your project. Also, it uses token authentication and permissions to control access to the views. Be sure to set up authentication and permissions as needed in your Django project.

You can use these endpoints in your application to perform CRUD (Create, Read, Update, Delete) operations related to posts, likes, and comments. Don't forget to define the URL patterns to map these views to specific URLs in your Django project's `urls.py` file.


### UserProfileView
This view is used to retrieve the profile details of the authenticated user.

- **Endpoint:** GET /api/user/profile/
- **Authentication:** Requires token authentication (Only authenticated users can access this view).
- **Permissions:** Restricted to admin users (as indicated by the comments).

### SignUpView
This view is used to create a new user profile.

- **Endpoint:** `POST /api/user/signup/`

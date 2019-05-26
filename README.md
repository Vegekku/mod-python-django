# mod-python-django

Practice for Python-Django Module of VI Bootcamp Web

## INSTALLATION

1. Install required modules
    ```bash
    $ pip install -r requirements.txt
    ```
2. Create database
    ```bash
    $ python manage.py migrate
    ```
3. Create superuser
    ```bash
    $ python manage.py createsuperuser
    ```
4. Run dev server
    ```bash
    $ python manage.py runserver
    ```

## WEBSITE

```
# ADMIN DASHBOARD
/admin      Django admin

# USERS
/login      Login
/logout     Logout
/singup     Singup

# BLOGS
/blogs/<username>/<pk>  Post detail
/blogs/<username>       List latest user posts
/blogs                  List user blogs

# POSTS
/new-blog   Save posts from loggued user
/           List latests post
```

## API REST

```
# USERS
POST /api/v1/users          Any user
GET /api/v1/users/<pk>      Authenticated user (self or super)
PUT /api/v1/users/<pk>      Authenticated user (self or super)
DELETE /api/v1/users/<pk>   Authenticated user (self or super)

# BLOGS
GET /api/v1/blogs   Any user.
                    Allowed query params search or/and ordering by username.

# POSTS
GET /api/v1/posts           Published posts for any user, all posts for authenticated user (author or super)
                            Query param search by title or body.
                            Query param ordering by title or publish_date
POST /api/v1/posts          Authenticated user
GET /api/v1/posts/<pk>      Published post for any user, any post for authenticated user (author or super)
PUT /api/v1/posts/<pk>      Authenticated user (author or super)
DELETE /api/v1/posts/<pk>   Authenticated user (author or super)
```

## CHANGELOG

### 1.1

- Improved README.
- Added basic design to website.

### 1.0

- Done [tasks](./docs/REQUIREMENTS.md) for pass practice.

## FUTURE FEATURES

- Make a table of available urls and endpoints on README.
- Change to Model Views
- List posts depend on url parameters (latest, oldest, list)
- Refactor categories as an internal model of posts, if it's possible.
- Manage environment variables with .env file: https://github.com/joke2k/django-environ
- Sign up with confirmation mail: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
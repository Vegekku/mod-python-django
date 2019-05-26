# mod-python-django

Practice for Python-Django Module of VI Bootcamp Web

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
POST /api/v1/users Any user
GET /api/v1/users/<pk> Authenticated user (self or super)
PUT /api/v1/users/<pk> Authenticated user (self or super)
DELETE /api/v1/users/<pk> Authenticated user (self or super)

# BLOGS
GET /api/v1/blogs Any user

# POSTS
GET /api/v1/posts Published posts for any user, all posts for authenticated user (author or super)
POST /api/v1/posts Authenticated user
GET /api/v1/posts/<pk> Published post for any user, any post for authenticated user (author or super)
PUT /api/v1/posts/<pk> Authenticated user (author or super)
DELETE /api/v1/posts/<pk> Authenticated user (author or super)
```

## CHANGELOG

### 1.0

- Done [tasks](./docs/REQUIREMENTS.md) for pass practice.

## FUTURE FEATURES

- Change to Model Views
- List posts depend on url parameters (latest, oldest, list)
- Refactor categories as an internal model of posts, if it's possible.
- Manage environment variables with .env file: https://github.com/joke2k/django-environ
- Sign up with confirmation mail: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
# API Docs

## Auth

### ENDPOINT

    /api/auth/register/

## Method - POST

### Content Type application/json

### Request Body

```
{
    'username': [string],
    'email': [string],
    'password: [string],
    'password2: [string],
}
```

#### Response Body

```
{
    'username': [string],
    'email': [string],
    'token': [string],
    'expires': [timestamp],
    'message': [string],
}
```

## ENDPOINT

    /api/auth/login/

```
Method	POST
Content Type	application/json
Request Body
{
    'username': [string],
    'email': [string],
    'password: [string],
}
Response Body
{
    'username': [string],
    'token': [string],
    'expires': [timestamp],
}
```

# Status Endpoint

    /api/status/

```
Endpoint	/api/status/
Methods	GET
Content Type	application/json
Response Body
{
    "count":        [number],
    "next":         [urlString or None],
    "previous":     [urlString or None],
    "results":      [{
                        "uri": [urlString],
                        "id": [number],
                        "user": {
                            "id": [number],
                            "username": [string],
                            "uri": [urlString]
                        },
                        "content": [string or None],
                        "image": [urlString or None]
                }]
}
```

# Endpoint

     /api/status/

```
Methods	POST
Content Type	application/json
Authorization Header	"Authorization: JWT [token]"
Request Body
{
                            "content": [string or None],
                        "image": [urlString or None]
}
```

```
Response Body
{
                        "uri": [urlString],
                        "id": [number],
                        "user": {
                            "id": [number],
                            "username": [string],
                            "uri": [urlString]
                        },
                        "content": [string or None],
                        "image": [urlString or None]
}
```

# STATUS DETAIL

    /api/status/<:id>/

# User

    /api/user/<:username>/

    /api/user/<:username>/status

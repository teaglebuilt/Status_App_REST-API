import requests
import json

ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"

headers = {
    "Content-Type": "application/json",
    # "token": "JWT" + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTQ4MTg2NjA0LCJlbWFpbCI6ImFkbWluQGFvbC5jb20iLCJvcmlnX2lhdCI6MTU0ODE4NjMwNH0.AggOybrkSfuLG0CP8KnE-cJXmIQlSPZRGaks8wJJRA4"
}

data = {
    "username": "cfe10",
    "email": "cfe10@gmail.com",
    "password": "bob"
}

r = requests.post(ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()
print(token)
# # image_path = '/Users/dillanteagle/business/REST_Api/static_server/media_root/status/admin/r4.jpg'

# get_endpoint = ENDPOINT + str(15)
# post_data = json.dumps({"content": "some random content"})

# r = requests.get(get_endpoint)
# print(r.text)

# post_headers = {
#     "content-type": "application/json"
# }

# post_response = requests.get(ENDPOINT, data=post_data, headers=post_headers)
# def do_img(method='GET', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if image_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT + str(id),
#                                  data=data, files=file_data)
#     else:
#         r = requests.request(method, ENDPOINT + str(id),
#                              data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# do_img(method='post', data={'user': 1, 'content': ""},
#        is_json=False, img_path=image_path)


# def do(method='GET', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT + str(id),
#                          data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

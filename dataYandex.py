url = "https://cloud-api.yandex.net/v1/disk/resources"
token = ""
MAKE_FOLDER = [
    ('test1', 201),
    ('test 2', 201),
    ('test3/test4', 409),
    ('//test4', 404),
    ('test1/test5', 201),
    ('/test6/', 201)
]
DELETE_FOLDER = [
    ('test1', 202),
    ('test 2', 204),
    ('test1/test5', 404),
    ('/test6/', 204)
]


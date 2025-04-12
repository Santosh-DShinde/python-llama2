from rest_framework.response import Response

class APIResponse():
    def __init__(self):
        pass

    def created(self, data, message, code=200):
        return Response(
            data={
                "code": code,
                "message": message,
                "data": data,
            },
            status=code
        )

    def bad_request(self, data, message, code=400):
        return Response(
            data={
                "code": code,
                "message": message,
                "data": data,
            },
            status=code
        )
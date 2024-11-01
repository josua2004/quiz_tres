# mixins.py
from rest_framework.response import Response

class CustomResponseMixin:
    success_message = ""

    def custom_response(self, data, status):
        return Response({
            "message": self.success_message,
            "data": data
        }, status=status)

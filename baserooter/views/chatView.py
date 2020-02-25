from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from baserooter.services import chatServices

class getChatView(APIView):
    """
    This API is used get chat logs.
    """

    def post(self, request, format=None):
        data = chatServices.getChatLogs(request)
        return Response(data, status=HTTP_200_OK)

class createChatView(APIView):
    """
    This API is used get chat logs.
    """

    def post(self, request, format=None):
        data = chatServices.createChatLogs(request)
        return Response(data, status=HTTP_200_OK)
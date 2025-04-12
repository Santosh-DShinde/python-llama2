from rest_framework.views import APIView

from chat.rest_response import APIResponse
from chat_app.utils import chat_with_llama2


class ConversationView(APIView):

    def post(self, request, *args, **kwargs):
        data: dict = request.data

        prompt: str = data.get('prompt')
        if not prompt:
            return APIResponse.bad_request(self, data={"success": False}, message="request is empty.")

        response = chat_with_llama2(prompt)

        return APIResponse.created(self, data={"success": True, "ai": response}, message="conversation complete",)

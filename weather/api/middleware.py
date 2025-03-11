import logging
from django.http import JsonResponse

logger = logging.getLogger('api')

class GlobalErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            logger.exception("A global error occurred.")
            return JsonResponse({"error": "A server error occurred."}, status=500)
        return response

from django.conf import settings
from django.http import HttpResponse
import logging
import os

logging.basicConfig(filename = os.path.join(settings.BASE_DIR, "logs" , "swipe_errors.log"), level = logging.DEBUG)
# print("importing middleware")
class ExceptionLogger(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        # if settings.DEBUG:
        intitle = "{}: {} \n".format(exception.__class__.__name__,  exception)
        logging.debug(intitle)
        return HttpResponse(exception)# will output the error as HttpResponse to the frontend
        # return None # will output the error as it is to the frontend

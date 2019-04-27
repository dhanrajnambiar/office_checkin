from django.conf import settings
from django.http import HttpResponse
import requests

class ExceptionReasonFinder(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if settings.DEBUG:
            print(exception.__class__.__name__)
            intitle = "{}: {}".format(exception.__class__.__name__,  exception)
            # print(dir(exception))
            url = 'https://api.stackexchange.com/2.2/search'
            headers = { 'User-Agent': 'github.com/vitorfs/seot' }
            params = {
                'order': 'desc',
                'sort': 'votes',
                'site': 'stackoverflow',
                'pagesize': 3,
                'tagged': 'python;django',
                'intitle': intitle
            }

            r = requests.get(url, params=params, headers=headers)
            print(r._content, r.status_code, r.json())
        return HttpResponse(exception)

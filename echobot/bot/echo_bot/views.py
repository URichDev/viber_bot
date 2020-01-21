from django.views import View

from django.http import HttpResponse

from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt


from .utils import viber

class SetWebhookView(View):
    def get(self, request, *args, **kwargs):
        viber.set_webhook(
            url='https://ba97ea5a.ngrok.io/viber/callback/',
        )
        return HttpResponse(status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CallbackView(View):
    def post(self, request):
        viber_request = viber.parse_request(request.body)
        print(viber_request)
        viber.send_messages(viber_request.sender.id, viber_request.message)
        return HttpResponse(status=200)

from django.shortcuts import render
from django.views.generic import View


class HomePage(View):

    def get(self, request):
        return render(request, 'index.html')


class CallbackPage(View):

    def get(self, request):
        auth_code = self.request.GET.get('code')

        context = {
            'auth_code': auth_code
        }

        return render(request, 'callback.html', context)

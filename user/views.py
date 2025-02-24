from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings


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


def logout_view(request):
    logout(request)
    return redirect(f"{settings.LOGIN_URL}?next={request.path}")

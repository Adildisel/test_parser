from django.shortcuts import render

from django.views.generic import View


class ParserView(View):
    def get(self, request):
        data = 'Name'
        return render(request, 'app/index.html', context={'data': data})
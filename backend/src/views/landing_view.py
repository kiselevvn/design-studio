from apps.content.forms import MessageForm
from apps.content.models import Portfolio
from django.shortcuts import render
from django.views.generic import View


class LandingView(View):
    """
    Лэндиннг сайта
    """

    template_name = "index.html"

    def get_data_object(self, **kwargs):
        """
        Контекст данных лэндинга
        """
        data = {}
        data["form"] = MessageForm()
        data["projects"] = Portfolio.objects.filter(is_published_index=True)
        return data


    def get(self, request):
        """
        Обработка GET запроса
        """
        data = self.get_data_object()
        form = MessageForm()
        return render(request, template_name=self.template_name, context={**data, "form": form })

    def post(self, request):
        """
        Обработка POST запроса
        """
        data = self.get_data_object()
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save()
            form_instance.save()
            return render(request, template_name="index.html", context={})
        return render(request, template_name=self.template_name, context={**data, "form": form })

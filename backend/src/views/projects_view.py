from apps.content.models import Portfolio
from django.shortcuts import render
from django.views.generic import View


class ProjectsView(View):
    """
    Лэндиннг сайта
    """

    template_name = "projects.html"

    def get_data_object(self, **kwargs):
        """
        Контекст данных лэндинга
        """
        data = {}
        data["projects"] = Portfolio.objects.filter(
            is_published=True
        )
        return data


    def get(self, request):
        """
        Обработка GET запроса
        """
        data = self.get_data_object()
        return render(request, template_name=self.template_name, context={**data, })

    def post(self, request):
        """
        Обработка POST запроса
        """
        data = self.get_data_object()
        return render(request, template_name=self.template_name, context={**data, })

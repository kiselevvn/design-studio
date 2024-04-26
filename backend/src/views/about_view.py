from django.shortcuts import render
from django.views.generic import View


class AboutView(View):
    """
    Лэндиннг сайта
    """

    template_name = "about.html"

    def get_data_object(self, **kwargs):
        """
        Контекст данных лэндинга
        """
        data = {}
        # data["form"] = MessageForm()

        # data["category_service"] = CategoryService.objects.filter(
        #     is_published=True
        # )
        # data["additional_services"] = AdditionalService.objects.filter(
        #     is_published=True
        # )
        # data["offer_slides"] = OfferSlide.objects.filter(is_published=True)
        # data["workers"] = Worker.objects.filter(is_published_landing=True)
        # data["courses"] = Course.objects.filter(is_published=True)
        # data["certificates"] = Сertificate.objects.filter(is_published=True)
        # data["gallery_photo"] = Gallery.objects.filter(is_published=True)
        return data


    def get(self, request):
        """
        Обработка GET запроса
        """
        data = self.get_data_object()
        # form = MessageForm()
        return render(request, template_name=self.template_name, context={**data, })

    def post(self, request):
        """
        Обработка POST запроса
        """
        data = self.get_data_object()
        # form = MessageForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form_instance = form.save()
        #     return render(request, template_name="thanks.html", context={})
        return render(request, template_name=self.template_name, context={**data, })

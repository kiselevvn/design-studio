from django.views.generic import FormView

from ..forms import MessageForm


class MessageFormView(FormView):
    """
    Страница формы отзыва
    """

    template_name = "message.html"
    form_class = MessageForm
    success_url = "/content/thanks/"

    def form_valid(self, form):
        # print(self.request)
        form.save()
        return super().form_valid(form)

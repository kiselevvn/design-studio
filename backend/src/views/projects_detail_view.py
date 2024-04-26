from apps.content.models import Portfolio
from django.views.generic import DetailView


class ProjectsDetailView(DetailView):
    """
    """

    model = Portfolio
    template_name = "projects_detail.html"

    def get_queryset(self):
        return Portfolio.objects.prefetch_related("items")

# /

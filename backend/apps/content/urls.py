from django.urls import path

from .views import CourseBuyFormView, MessageFormView, ThanksView

urlpatterns = [
    path("message/", MessageFormView.as_view(), name="message"),
    path("thanks/", ThanksView.as_view(), name="thanks"),
    path(
        "course-buy/<int:pk>/", CourseBuyFormView.as_view(), name="course-buy"
    ),
]

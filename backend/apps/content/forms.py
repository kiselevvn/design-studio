from django.forms import BooleanField, ModelForm

from . import models


class MessageForm(ModelForm):

    class Meta:
        model = models.Comment
        fields = [
            "name",
            "email",
            "phone",
        ]


# class CourseBuyForm(ModelForm):

#     privacy = BooleanField(required=True)

#     class Meta:
#         model = Comment
#         fields = [
#             "name",
#             "email",
#             "phone",
#             "text",
#             "category",
#             "course",
#         ]

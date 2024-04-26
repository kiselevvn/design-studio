from django.db import models
from django.utils.translation import gettext as _


class Comment(
    models.Model,
):
    """
    Модель Сообщение
    """

    email = models.EmailField(
        _("Электронная почта"), max_length=254, blank=True, null=True
    )
    name = models.CharField(
        verbose_name=_("Имя"),
        max_length=255,
    )
    phone = models.CharField(
        verbose_name=_("Номер телефона"), max_length=25
    )


    date_created = models.DateTimeField(
        verbose_name=_("Дата создания"), auto_now_add=True
    )

    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")
        ordering = ["-date_created"]

    def __str__(self):
        return f"{self.name} " + f"(дата создания: {self.date_created}) "

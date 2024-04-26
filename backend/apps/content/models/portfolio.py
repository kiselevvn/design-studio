from django.db import models
from django.utils.translation import gettext as _


class PortfolioItem(models.Model):
    """
    """

    portfolio = models.ForeignKey("content.Portfolio", verbose_name=_("Портфолио"), on_delete=models.CASCADE, related_name="items")

    picture = models.ImageField(verbose_name=_("Изображение"))
    description = models.CharField(
        verbose_name=_("Описание"),
        max_length=500,
        blank=True, null=True
    )
    is_published = models.BooleanField(
        verbose_name=_("Является опубликованым"), default=True
    )
    order = models.IntegerField(_("Порядок"), default=0)



    class Meta:
        verbose_name = _("Изображение")
        verbose_name_plural = _("Изображения")
        ordering = ["order"]

    def __str__(self):
        return f"Изображение"



class Portfolio(
    models.Model,
):
    """

    """

    title = models.CharField(
        verbose_name=_("Наименование объекта"),
        max_length=500,
    )
    location = models.CharField(
        verbose_name=_("Расположение"),
        max_length=500,
        blank=True, null=True
    )
    square = models.IntegerField(_("Площадь"), blank=True, null=True)
    style = models.CharField(
        verbose_name=_("Стиль"),
        max_length=50,
        blank=True,
        null=True
    )
    year = models.CharField(
        verbose_name=_("Год"),
        max_length=50,
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name=_("Описание"),
        blank=True, null=True
    )

    photo = models.ImageField(_("Фотогорафия"), blank=True, null=True)
    is_published = models.BooleanField(
        verbose_name=_("Опубликовать запись"), default=False
    )
    is_published_index = models.BooleanField(
        verbose_name=_("Запись опубликована на главной"), default=False
    )
    order = models.IntegerField(_("Порядок"), default=0)

    date_created = models.DateTimeField(
        verbose_name=_("Дата создания"), auto_now_add=True
    )


    class Meta:
        verbose_name = _("Портфолио")
        verbose_name_plural = _("Портфолио")
        ordering = ["order","-date_created"]

    def __str__(self):
        return f"{self.title}"

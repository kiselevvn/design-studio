from django.contrib import admin

from . import models


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    """

    list_display = (
        "name",
        "email",
        "phone",
        "date_created",
    )


class PortfolioItemInline(admin.StackedInline):
    model = models.PortfolioItem
    extra = 0


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    """
    """

    list_display = (
        "title",
        "location",
        "square",
    )
    inlines = (PortfolioItemInline,)


# @admin.register(CategoryService)
# class CategoryServiceAdmin(admin.ModelAdmin):
#     """
#     Админ панель
#     Категория услуги
#     """

#     list_display = (
#         "name",
#         "is_published",
#         "order",
#     )
#     list_filter = ("is_published",)


# @admin.register(Worker)
# class WorkerAdmin(admin.ModelAdmin):
#     """
#     Админ панель
#     Сотрудник
#     """

#     list_display = (
#         "name",
#         "is_published_landing",
#     )
#     list_filter = ("is_published_landing",)


# @admin.register(OfferSlide)
# class OfferSlideAdmin(admin.ModelAdmin):
#     """
#     Админ панель
#     Слайд предложения
#     """

#     list_display = (
#         "title",
#         "is_published",
#     )
#     list_filter = ("is_published",)


# @admin.register(AdditionalService)
# class AdditionalServiceAdmin(admin.ModelAdmin):
#     """
#     Админ панель
#     Дополнительная услуга
#     """

#     list_display = (
#         "name",
#         "price",
#         "is_published",
#         "order",
#     )
#     list_filter = ("is_published",)


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     """
#     Админ панель
#     Дополнительная услуга
#     """

#     list_display = (
#         "name",
#         "price",
#         "is_published",
#         "order",
#     )
#     list_filter = ("is_published",)


# @admin.register(Сertificate)
# class СertificateAdmin(admin.ModelAdmin):
#     """
#     Админ панель
#     Сертификаты
#     """

#     list_display = (
#         "__str__",
#         "is_published",
#         "order",
#     )
#     list_filter = ("is_published",)


# @admin.register(Gallery)
# class GalleryAdmin(admin.ModelAdmin):
#     """
#     Админ панель
#     Фото Галереи
#     """

#     list_display = (
#         "__str__",
#         "is_published",
#         "order",
#     )
#     list_filter = ("is_published",)

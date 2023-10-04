from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.PostModel)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CommentModel)
class CommentAdmin(admin.ModelAdmin):
    pass

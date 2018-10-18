from django.contrib import admin
from .models import MusicClip, LikeDislike, Category, MusicTrack
# Register your models here.

admin.site.register(MusicClip)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(LikeDislike)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("user", "object_id")
    list_filter = ("user", 'object_id')
    search_fields = ["object_id"]


@admin.register(MusicTrack)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "reiting")
    search_fields = ["id"]

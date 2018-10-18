from django.contrib import admin
from .models import MusicClip, LikeDislike, Category, MusicTrack
# Register your models here.

admin.site.register(MusicTrack)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(LikeDislike)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("user", "content_type", "object_id", "vote")
    search_fields = ["user"]
    list_filter = ("user", "content_type", 'object_id', 'vote')


@admin.register(MusicTrack)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "reiting")
    search_fields = ["name"]
    list_filter = ("name", "reiting")

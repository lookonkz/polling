from django.contrib import admin
from .models import MusicClip, LikeDislike, Category, MusicTrack
# Register your models here.
admin.site.register(LikeDislike)
admin.site.register(MusicClip)
admin.site.register(MusicTrack)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
from django.contrib.sitemaps import Sitemap
from musics.models import MusicTrack


class MusicTrackSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return MusicTrack.objects.all()

    def lastmod(self, obj):
        return obj.article_date

    def location(self, obj):
        return obj.get_absolute_url()
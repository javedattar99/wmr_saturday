



from django.contrib.sitemaps import Sitemap
from .models import Report


class ReportSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return Report.objects.all()

    def lastmod(self, obj):
        return obj.published_date
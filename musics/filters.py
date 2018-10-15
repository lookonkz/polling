# import django_filters
# from .models import MusicTrack
#
# CHOICES = [
#     ["name", "по алфавиту"],
#     ["reiting", "дешевые сверху"],
#     ["-reiting", "дорогие сверху"]
# ]
#
#
# class MusicTrackFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(name='name', lookup_expr='icontains')
#     ordering = django_filters.OrderingFilter(choices=CHOICES, required=True, empty_label=None, )
#
#     class Meta:
#         model = MusicTrack
#         fields = ['name', 'reiting']
#         order_by_field = 'name'



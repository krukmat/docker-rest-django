# Create your views here.

from rest_framework import serializers, viewsets
from tickets_calendar.models import EventDiscovery
from rest_framework import filters
import django_filters


class EventDiscoveryFilter(filters.FilterSet):
    event_date_from = django_filters.DateTimeFilter(name="event_date", lookup_type='gte')
    event_date_to = django_filters.DateTimeFilter(name="event_date", lookup_type='lt')
    sale_start_from = django_filters.DateTimeFilter(name="sale_start", lookup_type='gte')
    sale_start_to = django_filters.DateTimeFilter(name="sale_start", lookup_type='lt')
    venue_name_start = django_filters.CharFilter(name='venue_name', lookup_type='startswith')
    event_name_start = django_filters.CharFilter(name='event_name', lookup_type='startswith')

    class Meta:
        model = EventDiscovery
        filter_backends = (filters.DjangoFilterBackend,)
        fields = ['event_id', 'venue_id', 'timezone', 'city_state', 'venue_name_start', 'event_date_from', 'event_date_to',
                  'event_name_start', 'price_range', 'event_announced', 'sale_type', 'sale_name', 'sale_start_from',
                  'sale_start_to', 'sale_end', 'last_update', 'date_added', 'tracking', 'domain',
                  'status_id', 'extra1', 'extra2', 'my_last_update']


class EventDiscoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDiscovery
        fields = ('event_id', 'venue_id', 'timezone', 'city_state', 'venue_name', 'event_date', 'event_name',
                  'price_range', 'event_announced', 'sale_type', 'sale_name', 'sale_start', 'sale_end', 'last_update',
                  'date_added', 'tracking', 'domain', 'status_id', 'extra1', 'extra2', 'my_last_update')


class EventDiscoveryViewSet(viewsets.ModelViewSet):
    queryset = EventDiscovery.objects.all()
    serializer_class = EventDiscoverySerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend, filters.SearchFilter)
    filter_class = EventDiscoveryFilter
    ordering_fields = ('event_name', 'event_date')
    ordering = ('event_name', 'event_date')
    search_fields = ('^event_name', '^venue_name')


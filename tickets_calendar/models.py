from django.db import models


class EventDiscovery(models.Model):

    event_id = models.CharField(primary_key=True, db_index=True, db_column='eventID', max_length=16)  # Field name made lowercase.
    venue_id = models.CharField(db_column='venueID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    timezone = models.CharField(max_length=50)
    city_state = models.CharField(db_column='cityState', max_length=100)  # Field name made lowercase.
    venue_name = models.CharField(db_column='venueName', max_length=255)  # Field name made lowercase.
    event_date = models.DateTimeField(db_column='eventDate')  # Field name made lowercase.
    event_name = models.CharField(db_column='eventName', max_length=255)  # Field name made lowercase.
    price_range = models.CharField(db_column='priceRange', max_length=255, blank=True, null=True)  # Field name made lowercase.
    event_announced = models.DateField(db_column='eventAnnounced')  # Field name made lowercase.
    sale_type = models.SmallIntegerField(primary_key=True, db_index=True, db_column='saleType')  # Field name made lowercase.
    sale_name = models.CharField(primary_key=True, db_index=True, db_column='saleName', max_length=50)  # Field name made lowercase.
    sale_start = models.DateTimeField(primary_key=True, db_index=True, db_column='saleStart')  # Field name made lowercase.
    sale_end = models.DateTimeField(db_column='saleEnd', blank=True, null=True)  # Field name made lowercase.
    last_update = models.DateTimeField(db_column='lastUpdate')  # Field name made lowercase.
    date_added = models.DateField(db_column='dateAdded')  # Field name made lowercase.
    tracking = models.IntegerField()
    domain = models.CharField(max_length=10)
    status_id = models.CharField(db_column='statusID', max_length=30)  # Field name made lowercase.
    extra1 = models.CharField(max_length=255, blank=True, null=True)
    extra2 = models.CharField(max_length=255, blank=True, null=True)
    my_last_update = models.DateTimeField(db_column='myLastUpdate')  # Field name made lowercase.

    class Meta:
        db_table = 'eventdiscovery'
        unique_together = (('event_id', 'sale_name', 'sale_type', 'sale_start'),)

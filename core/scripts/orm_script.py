from core.models import Restaurant
from django.utils import timezone
from django.db import connection

def run():
    # restaurant=Restaurant()
    # restaurant.name='my Italian Restaurant'
    # restaurant.latitude=50.2
    # restaurant.longitude=50.2
    # restaurant.date_opened=timezone.now()
    # restaurant.restauranet_type=Restaurant.TypeChoices.ITALIAN
    #
    # restaurant.save()
    # restaurant=Restaurant.objects.first()
    # print(restaurant)
    # """
    # django queries set lizly evaluwaited
    # """
    Restaurant.objects.create(
        name="Pizza Shop",
        date_opened=timezone.now(),
        restauranet_type=Restaurant.TypeChoices.ITALIAN,
        latitude=50.2,
        longitude=50.2

    )
    print(connection.queries)
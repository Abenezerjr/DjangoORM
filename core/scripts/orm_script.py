from core.models import Restaurant , Rating ,Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
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
    # Restaurant.objects.create(
    #     name="Pizza Shop",
    #     date_opened=timezone.now(),
    #     restauranet_type=Restaurant.TypeChoices.ITALIAN,
    #     latitude=50.2,
    #     longitude=50.2
    #
    # )
    # restaurant=Restaurant.objects.all()
    # print(connection.queries)
    # restaurant = Restaurant.objects.first()
    # user=User.objects.first()
    #
    # Rating.objects.create(user=user,restaurant=restaurant ,rating=3)
    # print(Rating.objects.filter(rating__gte=3)) # great than or equeal to
    # print(Rating.objects.filter(rating__lte=3)) # less than or equale to
    # print(Rating.objects.exclude(rating__lte=3)) # exclude not comming in the database ' WHERE NOT'
    # print(Rating.objects.filter(rating=5))
    # restaurant=Restaurant.objects.first()
    # chage the name of the frist restaurant
    # print(restaurant.name)
    # restaurant.name='chage the name'
    # restaurant.save()
    # rating=Rating.objects.first()
    # print(rating.rating)
    # print(rating.restaurant)
    # print(restaurant.rating_set.all())
    # print(restaurant.ratings.all()) # give a related name in order do get the all name
    """ creating a a sale recored """
    #  Sale.objects.create(
    #      restaurant=Restaurant.objects.first(),
    #      income=2.33,
    #      datetime=timezone.now()
    #
    #  )
    #
    #  Sale.objects.create(
    #         restaurant=Restaurant.objects.first(),
    #         income=5.33,
    #         datetime=timezone.now()
    #
    #     )
    #  Sale.objects.create(
    #              restaurant=Restaurant.objects.first(),
    #              income=8.33,
    #              datetime=timezone.now()
    #
    #          )
    # restaurant = Restaurant.objects.first()
    # print(restaurant.sales.all())
    user=User.objects.first()
    restaurant=Restaurant.objects.first()
    # print( Rating.objects.get_or_create(
    #     restaurant=restaurant,
    #     user=user,
    #     rating=4,
    # )
    # )
    rating , created= Rating.objects.get_or_create(
        restaurant=restaurant,
        user=user,
        rating=4,
    )
    # if created:
    #     # sand email



    print(connection.queries)

from django.db.models import Count


def shop_list_size(request):
    count = request.user.purchases.all().count
    return {
        "shop_list_size": count
    }
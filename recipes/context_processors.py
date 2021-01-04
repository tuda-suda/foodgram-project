def shop_list_size(request):
    if not request.user.is_anonymous:
        count = request.user.purchases.all().count
    else:
        count = 0
    return {
        "shop_list_size": count
    }

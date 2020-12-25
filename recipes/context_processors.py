from .models import Tag


def tag_list(request):
    tags = Tag.objects.all()
    return {
        "tag_list": tags
    }
from django.http import JsonResponse


def index_route(request):
    return JsonResponse({
        "status": "ok"
    })

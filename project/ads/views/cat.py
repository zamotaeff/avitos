import json

from django.core.exceptions import ValidationError
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from rest_framework.generics import CreateAPIView

from ads.models import Category
from ads.serializers import CategorySerializer


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListCreateView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []

        for cat in categories:
            response.append({'id': cat.pk,
                             'name': cat.name,
                             'slug': cat.slug})

        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        cat = Category.objects.create(**data)

        return JsonResponse({'id': cat.pk,
                             'name': cat.name,
                             'slug': cat.slug}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.annotate(num_ads=Count('ad')).order_by('name')

    def get(self, request, *args, **kwargs):
        categories = self.get_queryset()

        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
                "ads_number": category.num_ads
            })

        return JsonResponse(response,
                            safe=False,
                            json_dumps_params={"ensure_ascii": False})


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        },
            safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse(
            {
                "status": "ok"
            }, status=204
        )


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    success_url = '/'

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        data = json.loads(request.body)

        if 'name' in data:
            self.object.name = data['name']

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse(
            {
                "id": self.object.pk,
                "name": self.object.name
            },
            safe=False,
            status=204
        )

import json

from django.core.exceptions import ValidationError
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from ads.models import Category


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

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryCreateView(CreateView):
    model = Category

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category(name=category_data.get('name'))
        category.save()

        return JsonResponse({
            "id": category.pk,
            "name": category.name
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse(
            {
                "status": "ok"
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    success_url = '/'

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)

        self.object.name = category_data['name']

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse(
            {
                "id": self.object.pk,
                "name": self.object.name
            }
        )

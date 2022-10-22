import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from ads.models import Category, Ad


def index_route(request):

    return JsonResponse({
        "status": "ok"
    })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        categories = self.get_queryset()

        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
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

    def post(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "status": "ok"
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):

    model = Category
    fields = ['name']

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


class AdListView(ListView):

    model = Ad

    def get(self, request, *args, **kwargs):
        response = []

        for item in self.get_queryset():
            response.append(
                {
                    "id": item.pk,
                    "name": item.name,
                    "author": item.author,
                    "price": item.price
                }
            )

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):

    model = Ad

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        ad = Ad(
            name=ad_data.get('name'),
            author=ad_data.get('author'),
            price=ad_data.get('price'),
            description=ad_data.get('description'),
            address=ad_data.get('address'),
            is_published=bool(ad_data.get('is_bublished'))
        )
        ad.save()

        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        })


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):

        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DeleteView):

    model = Ad

    def post(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "status": "ok"
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):

    model = Ad
    fields = ['name', 'author_id', 'price', 'description', 'category_id']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)

        self.object.name = ad_data['name']
        self.object.author_id = ad_data['author_id']
        self.object.price = ad_data['price']
        self.object.description = ad_data['description']
        self.object.category_id = ad_data['category_id']

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            "id": self.object.pk,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "image": self.object.image
        })


class AdUploadImageView(UpdateView):

    model = Ad
    fields = ['image']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)

        self.object.image = ad_data['image']

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            "id": self.object.pk,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "image": self.object.image
        })

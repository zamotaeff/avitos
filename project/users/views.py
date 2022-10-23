import json

from django.conf import settings
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from users.models import User


class UserListView(ListView):

    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        total_users = self.object_list.count()

        num_pages = total_users // settings.TOTAL_ON_PAGE
        page = int(request.GET.get('page', 0))

        offset = page * settings.TOTAL_ON_PAGE

        if offset > total_users:
            self.object_list = []
        elif offset:
            self.object_list = self.object_list[offset:offset+settings.TOTAL_ON_PAGE]
        else:
            self.object_list = self.object_list[:settings.TOTAL_ON_PAGE]

        items = []

        for item in self.object_list:
            items.append(
                {
                    "id": item.pk,
                    "first_name": item.first_name,
                    "last_name": item.last_name,
                    "username": item.username,
                    "role": item.role,
                    "age": item.age,
                    "location": item.location.name
                }
            )

        response = {
            "items": items,
            "total": total_users,
            "num_pages": num_pages
        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    model = User

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user = User(
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            username=user_data.get('username'),
            password=user_data.get('password'),
            role=user_data.get('role'),
            age=user_data.get('age'),
            location=user_data.get('location')
        )
        user.save()

        return JsonResponse({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "role": user.role,
            "age": user.age,
            "location": user.location.name
        }, safe=False, json_dumps_params={"ensure_ascii": False})


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()

        return JsonResponse({
            "id": user.pk,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "role": user.role,
            "age": user.age,
            "location": user.location.name
        }, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    model = User

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse(
            {
                "status": "ok"
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'age', 'location']
    success_url = '/'

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)

        self.object.first_name = user_data['first_name']
        self.object.last_name = user_data['last_name']
        self.object.username = user_data['username']
        self.object.password = user_data['password']
        self.object.age = user_data['age']
        self.object.location = user_data['location']

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            "id": self.object.pk,
            "first_name": self.object.name,
            "last_name": self.object.last_name,
            "username": self.object.username,
            "role": self.object.role,
            "age": self.object.age,
            "location": self.object.location.name
        }, safe=False, json_dumps_params={"ensure_ascii": False})

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from rest_framework.authtoken.models import Token

from .models import RestaurantItem
from .serializers import RestaurantItemSerializer
from .views import RestaurantItemViewSet

# initialize the APIClient app
client = Client()

class GetAllRestaurantsTestCase(TestCase):
    """ Test module for GET all restaurants API"""

    def setUp(self):
        item_1 = RestaurantItem.objects.create(
            name='Mariot', opens_at="2018-02-04T10:00:00Z",  closes_at="2018-02-04T20:00:00Z")
        item_2 = RestaurantItem.objects.create(
            name='Grandmas', opens_at="2018-02-05T09:00:00Z",  closes_at="2018-02-05T21:00:00Z")
        testuser = User.objects.create(
            username="testuser", email="testuser@gmail.com", is_superuser=True, password="12345678")

    def test_get_all_restaurants(self):
        # get API all response

        factory = APIRequestFactory()
        request = factory.get("/api/restaurant")
        restaurants_view = RestaurantItemViewSet.as_view(actions={"get": "list"})
        response = restaurants_view(request, pk=None)
        # get data from db
        restaurants = RestaurantItem.objects.all()
        serializer = RestaurantItemSerializer(restaurants, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_restaurant(self):
        # get API response

        factory = APIRequestFactory()
        restaurant = RestaurantItem.objects.get(id=1)
        serializer = RestaurantItemSerializer(restaurant)
        request = factory.get("/api/restaurant/1")
        restaurants_view = RestaurantItemViewSet.as_view(actions={"get": "retrieve"})
        testuser = User.objects.get(username='testuser')
        force_authenticate(request, user=testuser)
        response = restaurants_view(request, pk=testuser.pk)
        # get data from db
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_restaurant_successful(self):
        # post API successful response

        factory = APIRequestFactory()
        payload = {
            "name": "new restaurant",
            "opens_at": "2018-02-04T10:00:00Z",
            "closes_at": "2018-02-04T20:00:00Z"
        }
        request = factory.post("/api/restaurant", payload)
        restaurants_view = RestaurantItemViewSet.as_view(actions={"post": "create"})
        testuser = User.objects.get(username='testuser')
        force_authenticate(request, user=testuser)
        response = restaurants_view(request, pk=testuser.pk)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_restaurant_error_on_name_empty(self):
        # post API error response : empy name

        factory = APIRequestFactory()
        payload = {
            "name": "",
            "opens_at": "2018-02-04T10:00:00Z",
            "closes_at": "2018-02-04T20:00:00Z"
        }
        request = factory.post("/api/restaurant/")
        restaurants_view = RestaurantItemViewSet.as_view(actions={"post": "create"})
        testuser = User.objects.get(username='testuser')
        force_authenticate(request, user=testuser)
        response = restaurants_view(request, payload, pk=testuser.pk)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_restaurant_successful(self):
        # patch API successful response

        factory = APIRequestFactory()
        item = RestaurantItem.objects.get(name='Mariot')
        payload = {
            "name": "Mariot updated"
        }
        request = factory.patch("/api/restaurant/" + str(item.id) + "/", payload)
        restaurants_view = RestaurantItemViewSet.as_view(actions={'patch': 'partial_update'})
        testuser = User.objects.get(username='testuser')
        force_authenticate(request, user=testuser)
        response = restaurants_view(request, pk=testuser.pk)
        response.render()
        self.assertEqual(response.data.get("name"), "Mariot updated")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_restaurant_successful(self):
        # delete API successful response

        factory = APIRequestFactory()
        item = RestaurantItem.objects.get(name="Mariot")
        request = factory.delete("/api/restaurant/" + str(item.id) + "/")
        restaurants_view = RestaurantItemViewSet.as_view(actions={"delete": "destroy"})
        testuser = User.objects.get(username='testuser')
        force_authenticate(request, user=testuser)
        response = restaurants_view(request, pk=testuser.pk)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


from django.test import TestCase
from django.utils import timezone
from .models import Movie, Theater, Showtime, Reserve, Purchase
from django.core.exceptions import ValidationError

class APITests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(title="Test Movie", director="Test Director", genre="Test Genre", release_date=timezone.now().date(), duration=120, synopsis="Test Synopsis")
        self.theater = Theater.objects.create(name="Test Theater", location="Test Location", capacity=100)
        self.showtime = Showtime.objects.create(movie=self.movie, theater=self.theater, date_and_time=timezone.now(), available_seats=50)

    def test_create_movie(self):
        movie_count = Movie.objects.count()
        self.assertEqual(movie_count, 1)

    def test_create_theater(self):
        theater_count = Theater.objects.count()
        self.assertEqual(theater_count, 1)

    def test_create_showtime(self):
        showtime_count = Showtime.objects.count()
        self.assertEqual(showtime_count, 1)

    def test_past_showtime(self):
        past_showtime = Showtime(movie=self.movie, theater=self.theater, date_and_time=timezone.now() - timezone.timedelta(hours=1), available_seats=50)
        with self.assertRaises(ValidationError):
            past_showtime.clean()

    def test_create_reserve(self):
        reserve = Reserve.objects.create(name="Test Reserve", movie=self.movie, theater=self.theater, showtime=self.showtime, reserve=2)
        reserve_count = Reserve.objects.count()
        self.assertEqual(reserve_count, 1)

    def test_create_purchase(self):
        reserve = Reserve.objects.create(name="Test Reserve", movie=self.movie, theater=self.theater, showtime=self.showtime, reserve=2)
        purchase = Purchase.objects.create(name="Test Purchase", movie=self.movie, theater=self.theater, showtime=self.showtime, reserve=reserve, purchase=20.00)
        purchase_count = Purchase.objects.count()
        self.assertEqual(purchase_count, 1)


from django.test import TestCase
from django.contrib.auth.models import User
from .serializers import UserSerializer, MovieSerializer, TheaterSerializer, ShowtimeSerializer, ReserveSerializer, PurchaseSerializer
from .models import Movie, Theater, Showtime, Reserve, Purchase

class SerializerTests(TestCase):
    def test_create_user_serializer(self):
        user_data = {'username': 'test_user', 'password': 'test_password'}
        serializer = UserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertIsInstance(user, User)

    def test_movie_serializer(self):
        movie_data = {'title': 'Test Movie', 'director': 'Test Director', 'genre': 'Test Genre', 'release_date': '2024-04-13', 'duration': 120, 'synopsis': 'Test Synopsis'}
        serializer = MovieSerializer(data=movie_data)
        self.assertTrue(serializer.is_valid())

    def test_theater_serializer(self):
        theater_data = {'name': 'Test Theater', 'location': 'Test Location', 'capacity': 100}
        serializer = TheaterSerializer(data=theater_data)
        self.assertTrue(serializer.is_valid())

    def test_showtime_serializer(self):
        movie = Movie.objects.create(title='Test Movie', director='Test Director', genre='Test Genre', release_date='2024-04-13', duration=120, synopsis='Test Synopsis')
        theater = Theater.objects.create(name='Test Theater', location='Test Location', capacity=100)
        showtime_data = {'movie': movie.id, 'theater': theater.id, 'date_and_time': '2024-04-14T12:00:00Z', 'available_seats': 50}
        serializer = ShowtimeSerializer(data=showtime_data)
        self.assertTrue(serializer.is_valid())

    def test_reserve_serializer(self):
        movie = Movie.objects.create(title='Test Movie', director='Test Director', genre='Test Genre', release_date='2024-04-13', duration=120, synopsis='Test Synopsis')
        theater = Theater.objects.create(name='Test Theater', location='Test Location', capacity=100)
        showtime = Showtime.objects.create(movie=movie, theater=theater, date_and_time='2024-04-14T12:00:00Z', available_seats=50)
        reserve_data = {'name': 'Test Reservation', 'movie': movie.id, 'theater': theater.id, 'showtime': showtime.id, 'reserve': 2}
        serializer = ReserveSerializer(data=reserve_data)
        self.assertTrue(serializer.is_valid())

    def test_purchase_serializer(self):
        movie = Movie.objects.create(title='Test Movie', director='Test Director', genre='Test Genre', release_date='2024-04-13', duration=120, synopsis='Test Synopsis')
        theater = Theater.objects.create(name='Test Theater', location='Test Location', capacity=100)
        showtime = Showtime.objects.create(movie=movie, theater=theater, date_and_time='2024-04-14T12:00:00Z', available_seats=50)
        reserve = Reserve.objects.create(name='Test Reservation', movie=movie, theater=theater, showtime=showtime, reserve=2)
        purchase_data = {'name': 'Test Purchase', 'movie': movie.id, 'theater': theater.id, 'showtime': showtime.id, 'reserve': reserve.id, 'purchase': 20.00}
        serializer = PurchaseSerializer(data=purchase_data)
        self.assertTrue(serializer.is_valid())


from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import (
    LoginView, LogoutView, UserCreateAPIView,
    MovieListCreate, MovieRetriveUpdateDestroy,
    TheaterListCreate, TheaterRetriveUpdateDestroy,
    ShowtimeListCreate, ShowtimeRetriveUpdateDestroy,
    ReserveListCreate, ReserveRetriveUpdateDestroy,
    PurchaseListCreate, PurchaseRetriveUpdateDestroy
)

class UrlsTests(SimpleTestCase):
    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.__name__, UserCreateAPIView.as_view().__name__)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.__name__, LoginView.as_view().__name__)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.__name__, LogoutView.as_view().__name__)

    def test_movies_list_create_url_resolves(self):
        url = reverse('products-create')
        self.assertEqual(resolve(url).func.__name__, MovieListCreate.as_view().__name__)

    def test_movies_retrieve_update_destroy_url_resolves(self):
        url = reverse('product-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.__name__, MovieRetriveUpdateDestroy.as_view().__name__)

    def test_theaters_list_create_url_resolves(self):
        url = reverse('customer-list-create')
        self.assertEqual(resolve(url).func.__name__, TheaterListCreate.as_view().__name__)

    def test_theaters_retrieve_update_destroy_url_resolves(self):
        url = reverse('customer-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.__name__, TheaterRetriveUpdateDestroy.as_view().__name__)

    def test_showtime_list_create_url_resolves(self):
        url = reverse('showtime-list-create')
        self.assertEqual(resolve(url).func.__name__, ShowtimeListCreate.as_view().__name__)

    def test_showtime_retrieve_update_destroy_url_resolves(self):
        url = reverse('showtime-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.__name__, ShowtimeRetriveUpdateDestroy.as_view().__name__)

    def test_reserve_list_create_url_resolves(self):
        url = reverse('reserve-list-create')
        self.assertEqual(resolve(url).func.__name__, ReserveListCreate.as_view().__name__)

    def test_reserve_retrieve_update_destroy_url_resolves(self):
        url = reverse('reserve-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.__name__, ReserveRetriveUpdateDestroy.as_view().__name__)

    def test_purchase_list_create_url_resolves(self):
        url = reverse('purchase-list-create')
        self.assertEqual(resolve(url).func.__name__, PurchaseListCreate.as_view().__name__)

    def test_purchase_retrieve_update_destroy_url_resolves(self):
        url = reverse('purchase-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.__name__, PurchaseRetriveUpdateDestroy.as_view().__name__)

        
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Movie, Theater, Showtime, Reserve, Purchase
from .serializers import MovieSerializer, TheaterSerializer, ShowtimeSerializer, ReserveSerializer, PurchaseSerializer
from django.contrib.auth.models import User
import json

class ViewsTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Log in the user
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_view(self):
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_create_api_view(self):
        data = {'username': 'newuser', 'password': 'newpassword'}
        response = self.client.post(reverse('register'), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_movie_list_create_view(self):
        response = self.client.get(reverse('products-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_movie_retrieve_update_destroy_view(self):
        movie = Movie.objects.create(title='Test Movie', director='Test Director', genre='Test Genre', release_date='2024-04-13', duration=120, synopsis='Test Synopsis')
        response = self.client.get(reverse('product-detail', kwargs={'pk': movie.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_theater_list_create_view(self):
        response = self.client.get(reverse('customer-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_theater_retrieve_update_destroy_view(self):
        theater = Theater.objects.create(name='Test Theater', location='Test Location', capacity=100)
        response = self.client.get(reverse('customer-detail', kwargs={'pk': theater.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_showtime_list_create_view(self):
        response = self.client.get(reverse('showtime-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_showtime_retrieve_update_destroy_view(self):
        movie = Movie.objects.create(title='Test Movie', director='Test Director', genre='Test Genre', release_date='2024-04-13', duration=120, synopsis='Test Synopsis')
        theater = Theater.objects.create(name='Test Theater', location='Test Location', capacity=100)
        showtime = Showtime.objects.create(movie=movie, theater=theater, date_and_time='2024-04-14T12:00:00Z', available_seats=50)
        response = self.client.get(reverse('showtime-detail', kwargs={'pk': showtime.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reserve_list_create_view(self):
        response = self.client.get(reverse('reserve-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reserve_retrieve_update_destroy_view(self):
        movie = Movie.objects.create(title='Test Movie', director='Test Director', genre='Test Genre', release_date='2024-04-13', duration=120, synopsis='Test Synopsis')
        theater = Theater.objects.create(name='Test Theater', location='Test Location', capacity=100)
        showtime = Showtime.objects.create(movie=movie, theater=theater, date_and_time='2024-04-14T12:00:00Z', available_seats=50)
        reserve = Reserve.objects.create(name='Test Reservation', movie=movie, theater=theater, showtime=showtime, reserve=2)
        response = self.client.get(reverse('reserve-detail', kwargs={'pk': reserve.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_purchase_list_create_view(self):
        response = self.client.get(reverse('purchase-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_purchase_retrieve_update_destroy_view(self):
        movie = Movie.objects.create(title='Test Movie', director='Test Director', genre='Test Genre', release_date='2024-04-13', duration=120, synopsis='Test Synopsis')
        theater = Theater.objects.create(name='Test Theater', location='Test Location', capacity=100)
        showtime = Showtime.objects.create(movie=movie, theater=theater, date_and_time='2024-04-14T12:00:00Z', available_seats=50)
        reserve = Reserve.objects.create(name='Test Reservation', movie=movie, theater=theater, showtime=showtime, reserve=2)
        purchase = Purchase.objects.create(name='Test Purchase', movie=movie, theater=theater, showtime=showtime, reserve=reserve, purchase=20.00)
        response = self.client.get(reverse('purchase-detail', kwargs={'pk': purchase.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

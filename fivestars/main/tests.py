import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse

from ratings.models import Rating
#Acá se testean views y models

class RatingModelTest(TestCase):

    def post_a_rating(self, pub_date):
        """
        Create Rating 
        
        This function create a rating to run tests
        
        Parameter:
            -pub_date:timezone
        
        Return a rating
        """
        rating = Rating(comments="Hi this is a test comment", pub_date=pub_date)
        return rating
    
    def test_was_publish_recently_with_future_rating(self):
        """was_publish_recently return False for ratings whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_rating=self.post_a_rating(time)
        self.assertIs(future_rating.was_published_recently(), False)

    def test_was_publish_recently_with_present_rating(self):
        """was_publish_recently return False for ratings whose pub_date is in the future"""
        time = timezone.now()
        future_rating=self.post_a_rating(time)
        self.assertIs(future_rating.was_published_recently(), True)

    def test_was_publish_recently_with_past_cuestion(self):
        """was_publish_recently return False for ratings whose pub_date is in the future"""
        time = timezone.now() - datetime.timedelta(days=30)
        future_rating=self.post_a_rating(time)
        self.assertIs(future_rating.was_published_recently(), False)
        
class RatingIndexViewTests(RatingModelTest, TestCase):
    def test_no_ratings(self):
        """If no rating exist, an appropiate message is displayed"""
        # * Hago una petición GET al index de polls y guardo la respuesta en response
        response = self.client.get(reverse('ratings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No ratings are available")
        self.assertQuerysetEqual(response.context['latest_ratings_list'], [])

    # def test_show_only_recent_ratings(self):
    #     """The view should only show recent ratings. It cannot show future questions from the date they are consulted."""
    #     response = self.client.get(reverse('ratings:index'))
    #     self.assertEqual(response.status_code, 200)
    #     future_rating = [self.rating, self.future_time]
    #     self.assertNotContains(response, future_rating)
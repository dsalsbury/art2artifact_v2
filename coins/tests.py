import datetime

from django.utils import timezone
from django.test import TestCase

from coins.models import Coin

# Create your tests here.
class CoinMethodTests(TestCase):

    def test_was_added_recently_with_future_poll(self):
        """
        was_added_recently() should return False for coins whose pub_date
        is in the future
        """
        future_coin = Coin(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_coin.was_added_recently(), False)

    def test_was_added_recently_with_old_poll(self):
        """
        was_added_recently() should return False for coins whose pub_date
        is older than 7 days
        """
        old_coin = Coin(pub_date = timezone.now() - datetime.timedelta(days=30))
        self.assertEqual(old_coin.was_added_recently(), False)

    def test_was_added_recently_with_recent_poll(self):
        """
        was_added_recently() should return True for coins whose pub_date 
        is within 7 days
        """
        recent_coin = Coin(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertEqual(recent_coin.was_added_recently(), True)


def create_coin(title):
    """
    Creates a coin with the given `title`
    """
    return Coin.objects.create(title=title)

class CoinViewTests(TestCase):
    def test_index_with_no_coins(self):
        """
        If no coins exist, an appropriate message should be displayed.
        """
        response = self.client.get('/coins/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No coins have been added recently.")
        self.assertQuerysetEqual(response.context['recently_added_coins_list'],
                                 [])

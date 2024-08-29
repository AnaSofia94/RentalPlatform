from django.test import TestCase
from django.contrib.auth.models import User
from listings.models import HomeListing, TenantListing, SavedSearch


class HomeListingModelTest(TestCase):

    def setUp(self):
        self.home_listing = HomeListing.objects.create(
            title='Beautiful Apartment in Oslo',
            municipality='Oslo',
            rent_amount=12000.00,
            is_wheelchair_friendly=True
        )

    def test_home_listing_creation(self):
        self.assertEqual(self.home_listing.title, 'Beautiful Apartment in Oslo')
        self.assertEqual(self.home_listing.municipality, 'Oslo')
        self.assertEqual(self.home_listing.rent_amount, 12000.00)
        self.assertTrue(self.home_listing.is_wheelchair_friendly)

    def test_home_listing_string_representation(self):
        self.assertEqual(str(self.home_listing), 'Beautiful Apartment in Oslo')


class TenantListingModelTest(TestCase):

    def setUp(self):
        self.tenant_listing = TenantListing.objects.create(
            name='John Doe'
        )

    def test_tenant_listing_creation(self):
        self.assertEqual(self.tenant_listing.name, 'John Doe')

    def test_tenant_listing_string_representation(self):
        self.assertEqual(str(self.tenant_listing), 'John Doe')


class SavedSearchModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.saved_search = SavedSearch.objects.create(
            user=self.user,
            name='Search for Apartments in Oslo',
            municipality='Oslo',
            rent_amount=10000.00,
            is_wheelchair_friendly=True
        )

    def test_saved_search_creation(self):
        self.assertEqual(self.saved_search.user.username, 'testuser')
        self.assertEqual(self.saved_search.name, 'Search for Apartments in Oslo')
        self.assertEqual(self.saved_search.municipality, 'Oslo')
        self.assertEqual(self.saved_search.rent_amount, 10000.00)
        self.assertTrue(self.saved_search.is_wheelchair_friendly)

    def test_saved_search_string_representation(self):
        self.assertEqual(str(self.saved_search), 'Search for Apartments in Oslo')
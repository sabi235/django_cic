from django.test import TestCase
from .models import Testapp
import unittest
import json
from django.test import Client


class TestappTests(TestCase):

    def setUp(self):
        response = Testapp.objects.create(
            name='AAA',
            slug='aaa',
            description="this is the test aaa")

    def test_details(self):
        # Issue a GET request.
        response = Testapp.objects.first()

        # Check that the response is AAA OK.
        self.assertEqual(response.name, "BBB")

    def test_slug(self):
        # Issue a GET request.
        testapp = Testapp.objects.get(name='AAA')
        expected_object_name = f'{testapp.slug}'
        self.assertEquals(expected_object_name, 'aaa')


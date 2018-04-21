import os
from test_plus.test import TestCase
from unittest.mock import patch
from django.conf import settings
from users.models import Poll
from django.urls import reverse



def ViewsTestCase(TestCase):

    def setUp(self):
        # Create 10 poll Objects
        pass

    def test_poll_view_can_fetch_a_list_of_polls(self):

        # Create a Django view that returns all polls and with the reverse URL
        response = self.client.get(reverse("users:polls"))

        self.assertEqual(len(response.context['polls']), 10)


    def test_poll_create_view_can_create_a_poll_instance(self):
        count_before = Poll.objects.count()
        payload = {
            "question":"Who am i?"
        }

        response = self.client.post(reverse("users:create_poll"),payload)
        count_after = Poll.objects.count()

        self.assertEqual(response.status_code,201)
        self.assertEqual(count_after,count_before+1)


def ModelsTestCase(TestCase):

    def setUp(self):

        #Create 10 polls
        pass
 
    def test_model_can_fetch_poll_with_the_longest_question_text(self):
        
        #Poll.objects.get(len('question')=="longest") ==this wont work of course

        pass
# Django
from django.core.urlresolvers import reverse
from django.test import TestCase

# Project
from frontpages.models import Contact


class ContactTest(TestCase):
    def setUp(self):
        self.contact = reverse("contact")
        self.email = "test@email.com"
        self.name = "First_Name"

    def test_contact_form_renders(self):
        response = self.client.get(self.contact)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], "/contact/")
        self.assertIn("contact_form", response.context)


    def test_post_to_form_with_good_data(self):
        data = {"name": self.name,
                "message": "Test the contact Form",
                "email": self.email}

        response = self.client.post(self.contact, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], "/")
        self.assertContains(response, "Thank you we have recieved your message.")

        contact_obj = Contact.objects.get(email=self.email)
        self.assertEqual(contact_obj.name, data["name"])
        self.assertEqual(contact_obj.message, data["message"])

# Django
from django.core.urlresolvers import reverse
from django.test import TestCase

# Project
from frontpages.models import Contact

# Third Party
from mock import patch, Mock

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
        with patch("mandrill.Mandrill") as mandrill_patch:
            # Creating and instance of mandrill
            instance = mandrill_patch.return_value

            # Creating an instance of send
            instance.messages.send = Mock()

            response = self.client.post(self.contact, data=data, follow=True)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.request["PATH_INFO"], "/")
            self.assertContains(response, "Thank you we have recieved your message.")

            contact_obj = Contact.objects.get(email=self.email)
            self.assertEqual(contact_obj.name, data["name"])
            self.assertEqual(contact_obj.message, data["message"])
            self.assertTrue(contact_obj.sent)

    def test_post_to_form_with_no_data(self):
        data = {}
        response = self.client.post(self.contact, data=data, follow=True)
        errors = response.context["contact_form"].errors
        self.assertEqual(errors["message"], [u'This field is required.'])
        self.assertEqual(errors["name"], [u'This field is required.'])
        self.assertEqual(errors["email"], [u'This field is required.'])
        import pdb; pdb.set_trace()
        pass

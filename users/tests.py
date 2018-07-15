from django.test import TestCase
from django.test import Client

from .forms import CustomUserCreationForm
from .models import Locality, School, CustomUser

# class Setup_Class(TestCase):

    # def setUp(self):
    #     pass

# class CustomUserModelTest(TestCase):

    # def setUp(self):

    #
    #     CustomUser.objects.create(
    #         email='foobar@gmail.com',
    #         first_name='Foo',
    #         last_name='Bar',
    #         school=School.objects.get(id=1),
    #         mob_parent='99112233',
    #         mob_student='79112233',
    #         locality=Locality.objects.get(id=1),
    #     )

    # def test_user_has_username(self):
    #     user = CustomUser.objects.get(id=1)
    #     self.assertFalse(user.username ) # check that user.username is not blank
    #

class CustomUserCreationFormTest(TestCase):

    def setUp(self):
        Locality.objects.create(name='Valletta')
        School.objects.create(
            name='Foobar Academy',
            locality=Locality.objects.get(id=1),
            type='public',
        )

    # test_init and test_init_without_kwargs NOT NECESSARY... delete.

    # def test_init(self):
    #     """Ensures that our form's __init__ accepts certain keyword arguments"""
    #     CustomUserCreationForm(
    #         school = self.school,
    #         locality = self.locality,
    #     )
    #
    # def test_init_without_kwargs(self):
    #     """Ensures that our form raises an exception if keyword arguments aren't specified"""
    #     with self.assertRaises(KeyError):
    #         CustomUserCreationForm()

    def test_valid_data(self):
        """This function is complete. :)"""

        form = CustomUserCreationForm(data={
            'first_name': "Matthew",
            'last_name': "Grech",
            'email': "reddevils1998@gmail.com",
            'mob_parent': "99123456",
            'mob_student': "79123456",
            'locality': Locality.objects.get(id=1).pk,
            'school': School.objects.get(id=1).pk,
            'password1': "dsg123FT2",
            'password2': "dsg123FT2",
        })
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.first_name, "Matthew")
        self.assertEqual(user.last_name, "Grech")
        self.assertEqual(user.email, "reddevils1998@gmail.com")
        self.assertEqual(user.mob_parent, "99123456")
        self.assertEqual(user.mob_student, "79123456")
        self.assertEqual(user.locality, Locality.objects.get(id=1))
        self.assertEqual(user.school, School.objects.get(id=1))
        self.assertTrue(user.check_password("dsg123FT2"))

    # def test_blank_data(self):
    #     form = CustomUserCreationForm({})
    #     self.assertFalse(form.is_valid())
    #     print("*" * 50)
    #     print(form.errors.as_json())
    #     print("*" * 50)
    #     # REMINDER: {} is a data dictionary
    #     self.assertEqual(form.errors, {
    #         'first_name': ['This field is required.'],
    #         'last_name': ['This field is required.'],
    #         'email': ['This field is required.'],
    #         'mob_parent': ['This field is required.'],
    #         'mob_student': ['This field is required.'],
    #         'locality': ['This field is required.'],
    #         'school': ['This field is required.'],
    #         'password1': ['This field is required.'],
    #         'password2': ['This field is required.'],
    #     })

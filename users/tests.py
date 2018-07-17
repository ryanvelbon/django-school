from django.test import TestCase
from django.test import Client

from .forms import CustomUserCreationForm
from .models import Locality, School, CustomUser

# class Setup_Class(TestCase):

    # def setUp(self):
    #     pass

class CustomUserModelTest(TestCase):

    def setUp(self):
        # DELETE FROM HERE all this ... this is not DRY code...
        Locality.objects.create(name='Valletta')
        School.objects.create(
            name='Foobar Academy',
            locality=Locality.objects.get(id=1),
            type='public',
        )
        # DELETE TO HERE

    def test_user_has_username(self):
        """Username is not specified by admin or user.
        This function checks that user has been assigned a username."""

        CustomUser.objects.create(
            email='foobar@gmail.com',
            first_name='Thomas',
            last_name='Johnson',
            school=School.objects.get(id=1),
            mob_parent='99112233',
            mob_student='79112233',
            locality=Locality.objects.get(id=1),
        )

        user = CustomUser.objects.get(id=1)
        self.assertTrue(user.username ) # check that username is not blank
        self.assertTrue('tjohnson' in user.username) # check that username is  correct

    def test_create_user_with_one_mobile(self):

        myUser = CustomUser.objects.create(
            email='foobar@gmail.com',
            first_name='Thomas',
            last_name='Johnson',
            school=School.objects.get(id=1),
            mob_parent='99112233',
            locality=Locality.objects.get(id=1),
        )

        self.assertTrue(isinstance(myUser, CustomUser))

    def test_create_user_without_mobile_disallowed(self):

        myUser = CustomUser.objects.create(
            email='foobar@gmail.com',
            first_name='Thomas',
            last_name='Johnson',
            school=School.objects.get(id=1),
            locality=Locality.objects.get(id=1),
        )

        # self.assertRaises()

        self.assertFalse(isinstance(myUser, CustomUser))


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

    def test_blank_data(self):
        form = CustomUserCreationForm({})
        self.assertFalse(form.is_valid())

        errors_dict = form.errors.as_data()

        # Asserts that the erroneous fields were registered
        self.assertTrue('first_name' in errors_dict) # F
        self.assertTrue('last_name' in errors_dict) # F
        self.assertTrue('email' in errors_dict)
        # self.assertTrue('mob_parent' in errors_dict) # F
        # self.assertTrue('mob_student' in errors_dict) # F
        self.assertTrue('locality' in errors_dict)
        self.assertTrue('password1' in errors_dict)
        self.assertTrue('password2' in errors_dict)

        # Asserts that the erroneous fields' errors were registered correctly

        # DEBBUGING
        # print(errors_dict)
        # Note that errors_dict['email'] is a list object
        # This solution is only temporary. We are assuming that the desired error message is stored at index 0 of the list.
        # This might not always be the case. Find a way to search the whole list for the desired error.

        self.assertTrue('This field is required.' in errors_dict['first_name'][0])
        self.assertTrue('This field is required.' in errors_dict['last_name'][0])
        self.assertTrue('This field is required.' in errors_dict['email'][0])
        self.assertTrue('This field is required.' in errors_dict['locality'][0])
        self.assertTrue('This field is required.' in errors_dict['password1'][0])
        self.assertTrue('This field is required.' in errors_dict['password2'][0])

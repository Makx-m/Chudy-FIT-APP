from django.test import TestCase

from chudyapp.models.PersonModel import Person


# Create your tests here.
class PersonTest(TestCase):

    def setUp(self):
        Person.objects.create(name="Jan Kowalski",
                              weight=70,
                              height=170,
                              sex=2,
                              age=25,
                              activePerDay=2
                              )
        Person.objects.create(name="Joanna Kowalska",
                              weight=70,
                              height=170,
                              sex=1,
                              age=25,
                              activePerDay=2
                              )

    def test_is_male(self):
        person = Person.objects.get(sex=2)
        person2 = Person.objects.get(sex=1)

        self.assertTrue(person.is_male())
        self.assertFalse(person2.is_male())

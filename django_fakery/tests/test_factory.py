from django.test import TestCase

from django_fakery.factory import factory

from .blueprints import pizza


class FactoryTest(TestCase):
    def test_model(self):
        margherita = factory.make('tests.Pizza')

        # field.default
        self.assertFalse(margherita.gluten_free)
        # field.null
        self.assertFalse(margherita.price)

        # field.blank
        self.assertEqual(margherita.description, '')

        # required field
        self.assertNotEqual(margherita.name, '')

        self.assertNotEqual(margherita.chef.first_name, '')

    def test_fields(self):
        margherita = factory.make(
            'tests.Pizza',
            fields={'name': 'four cheeses'}
        )
        self.assertEqual(margherita.name, 'four cheeses')

    def test_sequence(self):
        margheritas = factory.make(
            'tests.Pizza',
            fields={'name': 'pizza %(n)s'},
            quantity=10
        )
        self.assertEqual(len(margheritas), 10)
        self.assertEqual(margheritas[0].name, 'pizza 0')
        self.assertEqual(margheritas[1].name, 'pizza 1')

    def test_blueprint(self):
        movie_night = pizza.make(quantity=10)
        self.assertEqual(len(movie_night), 10)
        self.assertEqual(movie_night[0].chef.first_name, 'Chef 0')
        self.assertEqual(movie_night[1].chef.first_name, 'Chef 1')

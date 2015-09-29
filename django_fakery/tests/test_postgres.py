from datetime import datetime
import sys
from unittest import skipIf

from django.test import TestCase
from django_fakery.factory import factory

from ..compat import text_type, django_version, HAS_PSYCOPG2

if HAS_PSYCOPG2:
    from psycopg2.extras import DateTimeTZRange, NumericRange

PYPY3 = hasattr(sys, 'pypy_version_info') and sys.version_info.major >= 3
DJANGO17 = django_version >= (1, 7, 0) and django_version < (1, 8, 0)


@skipIf(not HAS_PSYCOPG2, "Psycopg2 not installed")
@skipIf(DJANGO17, "Django 1.7 does not have contrib.postgres")
@skipIf(PYPY3, "Psycopg2cffi does not support Python3")
class PostgresTest(TestCase):
    def test_postgres_fields(self):
        gigis_special = factory.make('tests.SpecialtyPizza')
        self.assertTrue(isinstance(gigis_special.toppings, list))
        for topping in gigis_special.toppings:
            self.assertTrue(isinstance(topping, text_type))

        self.assertTrue(isinstance(gigis_special.metadata, dict))
        self.assertTrue(isinstance(gigis_special.price_range, NumericRange))
        self.assertTrue(isinstance(gigis_special.price_range.lower, int))
        self.assertTrue(isinstance(gigis_special.sales, NumericRange))
        self.assertTrue(isinstance(gigis_special.sales.lower, int))
        self.assertTrue(isinstance(gigis_special.available_on, DateTimeTZRange))
        self.assertTrue(isinstance(gigis_special.available_on.lower, datetime))
        self.assertNotEqual(gigis_special.available_on.lower.tzinfo, None)

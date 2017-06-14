from django.test import TestCase

class PackageTests(TestCase):

    def setUp(self):
        pass

    def test_imports(self):
        import django
        import pytz
        {% if cookiecutter.use_drf == "y" %}
        import rest_framework
        {% endif %}
        {% if cookiecutter.use_graphql == 'y' %}
        import graphene
        import graphene_django
        {% endif %}
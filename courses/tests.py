from django.test import TestCase
from .models import Course


class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(name="Waterville", eircode="W123")
        Course.objects.create(name="Shannon", eircode="S123")

    def test_course_setting(self):
        """Basic Test For Course"""
        waterville = Course.objects.get(name="Waterville")
        self.assertEqual(waterville.name, "Waterville")

from django.test import TestCase

# Create your tests here.

class TestInstructorViews(TestCase):
        
        def test_instructor_profile(self):
            response = self.client.get('/instructor/profile/1')
            self.assertEqual(response.status_code, 302)
            
        def test_my_applications(self):
            response = self.client.get('/instructor/my_applications/1')
            self.assertEqual(response.status_code, 302)
    
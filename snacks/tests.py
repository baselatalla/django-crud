from django.test import TestCase 
from django.urls import reverse
from  .models import Snack
from django.contrib.auth import get_user_model



class SnacksTests(TestCase):
    def test_snack_list_page_status_code(self):
        url = reverse('snack_list')
        actual_status_code = self.client.get(url).status_code
        expected_status_code = 200
        self.assertEqual(actual_status_code, expected_status_code)

        
    def test_snack_list_page_templete(self):
        url = reverse('snack_list')
        actual_status_code = self.client.get(url)
        self.assertTemplateUsed(actual_status_code, 'snack_list.html')
        self.assertTemplateUsed(actual_status_code, 'base.html')

   
    def test_not_found(self):
        url = '/snacks/hello'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'yasser',
            email = 'yaseer@gmail.com',
            password = 'yyyyy'
        )
        self.snack = Snack.objects.create(
            title = 'mjadara',
            description  = 'rice and lentil',
            purchaser = self.user
        )


    def test_snack_details_status(self):
        response = self.client.get(reverse('snack_details', args='1'))
        self.assertEqual(response.status_code, 200)


    def test_snack_details_content(self):
        response = self.client.get(reverse('snack_details', args='1'))
        self.assertContains(response, 'rice and lentil')


    def test_snack_update(self):
        response = self.client.post(reverse('Snack_update', args='1'), {
            'title':'fool' ,
        })
        self.assertContains(response, 'fool')
        self.assertNotContains(response, 'mjadara')

    def test_snack_delete_view(self):
        response = self.client.get(reverse('Snack_delete', args="1"))
        self.assertEqual(response.status_code, 200)

    def test_thing_create_view(self):
        response = self.client.post(reverse("Snack_create"),
            {
                "title": "Burger",
                "description": 'bread and meat',
                "purchaser": self.user,
            }, follow=True
        )

        self.assertContains(response, 'bread and meat')
   
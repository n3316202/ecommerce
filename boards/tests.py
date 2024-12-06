from django.test import TestCase

from boards.models import Post

# Create your tests here.
#class SmokeTest(TestCase):
#    def test_bad_maths(self):
#        self.assertEqual(1 + 1, 3)

class PostMakeTest(TestCase):
    def test_make_post(self):
        
        for i in range(300):
            Post.objects.create(
                title=f'제목{i}',
                content=f'내용{i}',
            )            
        
        self.assertEqual(Post.objects.count(), 300)

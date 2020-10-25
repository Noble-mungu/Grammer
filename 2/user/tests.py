from django.test import TestCase
from .models import Post, #Customer

# Create your tests here.
class UserTestClass(TestCase):

    #set up method
    def setUp(self):
        self.willy = User(username = 'Willy',bio = "Life ain't that bad")

    #Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.willy,User))

    #Test to save user
    def test_save_method(self):
        self.willy.save_user()
        users = User.objects.all()
        self.assertTrue(len(users)> 0)
    
    def tearDown(self):
        User.objects.all().delete()

class PostTestClass(TestCase):

    #set up method
    def setUp(self):
        #create new user
        self.willy = User(username = 'Willy',bio = "Life ain't that bad")
        self.willy.save_user()

        #create new post
        self.post1 = Post(image_name = 'Living', caption = 'Not bad...', post_date = '9/8/2020', user = self.willy )
        
    #Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.post1,Post))

    # Test saving an post
    def test_save_method(self):                
        self.post1.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts)> 0)

    #Test deleting a post
    def test_delete_method(self):                
        #create a post
        self.post1 = Post(image_name = 'Living', caption = 'Not bad...', post_date = '9/8/2020', user = self.willy )
        self.post1.save_post()
         
        #delete the post
        self.post1.delete_post(id = 1)
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)

    #Test for changing caption
    def test_update_caption(self):
        self.post1 = Post(image_name = 'Living', caption = 'Not bad...', post_date = '9/8/2020', user = self.willy )
        self.post1.save_post()       
        new_caption = 'changed caption'
        self.post1.change_caption(id = 1)        
        self.assertTrue( caption ='changed caption')

    def tearDown(self):
        User.objects.all().delete()
        Post.objects.all().delete()
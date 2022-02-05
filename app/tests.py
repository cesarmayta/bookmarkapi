import datetime

from django.test import TestCase
from django.utils import timezone


from django.contrib.auth.models import User
from .models import *

from django.urls import reverse

# Create your tests here.
class BookmarkModelTests(TestCase):
    
    
    def test_create_bookmark(self):
        """ test for creations of new bookmark """
        user1 = User.objects.create_user(username='admin', password='admin')
        time = timezone.now()
        future_bookmark = Bookmark()
        future_bookmark.title ="NEW BOOKMARK"
        future_bookmark.url = 'link'
        future_bookmark.user = user1
        future_bookmark.access =  'public'
        future_bookmark.save()
        
        self.assertEqual(future_bookmark.create_at,time)
    
    def test_was_publish_recently_with_future_bookmark(self):
        """ was_published_recently returns False for bookmarks whose create_at is in the future """
        user1 = User.objects.create_user(username='admin', password='admin')
        time = timezone.now() + datetime.timedelta(days=30)
        future_bookmark = Bookmark()
        future_bookmark.title ="BOOKMARK FUTURE"
        future_bookmark.url = 'http://www.google.com'
        future_bookmark.create_at = time
        future_bookmark.user = user1
        future_bookmark.access =  'public'
        future_bookmark.save()
        #future_bookmark = Bookmark.objects.get(pk=3)
        self.assertIs(future_bookmark.was_published_recently(),False)
        
class BookmarkViewTests(TestCase):
    
    def setUp(self):
        """ setup of initial data test"""
        """ creating a bookmark in future """
        time = timezone.now() + datetime.timedelta(days=30)
        user1 = User.objects.create_user(username='admin', password='admin')
        
        future_bookmark = Bookmark()
        future_bookmark.title ="BOOKMARK FUTURE"
        future_bookmark.url = 'http://www.google.com'
        future_bookmark.create_at = time
        future_bookmark.user = user1
        future_bookmark.access =  'private'
        future_bookmark.save()
    
    def test_no_bookmarks(self):
        """ if not bookmarks exist , an appriate message is display """
        response = self.client.get(reverse("app:publicbookmark"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"no bookmark are available.")
        #self.assertQuerysetEqual(response.context['content'],[])
        
    def test_future_bookmark(self):
        """ bookmark with future create_at no publish y response"""
        response = self.client.get(reverse("app:publicbookmark"))
        self.assertContains(response,"no bookmark are available.")
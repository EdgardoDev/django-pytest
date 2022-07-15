import pytest

from django.contrib.auth.models import User

# Testing user creation on DB

@pytest.mark.django_db
def test_user_creation():
    User.objects.create_user('test', 'test@test.com', 'test')
    count = User.objects.all().count()
    print(count)
    assert User.objects.count() == 1

@pytest.mark.django_db
def test_user_creation1():
    count = User.objects.all().count()
    print(count)
    assert count == 0
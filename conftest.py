import pytest

from django.contrib.auth.models import User

@pytest.fixture()
def user_1(db):
    user = User.objects.create_user("test-user")
    print("Create user")
    return user

# Factory
@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "test@mail.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_app_user

# Fixture that will utilize the factory above
@pytest.fixture
def new_user_one(db, new_user_factory):
    return new_user_factory("Test_user", "password", "Edgardo")

@pytest.fixture
def new_user_two(db, new_user_factory):
    return new_user_factory("Test_user", "password", "Edgardo", is_staff="True") 
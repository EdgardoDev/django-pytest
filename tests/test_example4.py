import pytest

from django.contrib.auth.models import User

# Working with the DB using fixtures (Arrange - Act - Assert)

# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user("test-user")

# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") is True

# def test_set_check_password(user_1):
#     print("Check User 1")
#     assert user_1.username == "test-user"

# def test_set_check_password2(user_1):
#     print("Check User 2")
#     assert user_1.username == "test-user"

# def test_new_user(new_user):
#     print(new_user.first_name)
#     assert new_user.first_name == "Edgardo"

# def test_new_user(new_user_two):
#     print(new_user_two.is_staff)
#     assert new_user_two.is_staff


# def test_new_user(new_user_one):
#     print(new_user_one.username)
#     assert True

# def test_product(db, product_factory):
#     product = product_factory.create()
#     print(product.description)
#     assert True

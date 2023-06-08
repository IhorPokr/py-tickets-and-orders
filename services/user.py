from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


def create_user(
        username: str,
        password: str,
        **kwargs
) -> None:
    user = get_user_model().objects.create_user(
        username=username,
        password=password
    )
    for field, value in kwargs.items():
        setattr(user, field, value)
    user.save()


def get_user(user_id: int) -> User:
    return get_user_model().objects.get(pk=user_id)


def update_user(user_id: int, password: str = None, **kwargs) -> None:
    user = get_user(user_id)
    user.set_password(password) if password else None
    for field, value in kwargs.items():
        setattr(user, field, value)
    user.save()
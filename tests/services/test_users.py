from unittest.mock import ANY
from models.users import User
from services import users


def test_should_list_users(db_session):

    # Given a user
    new_user = User(
        name="John",
        email="j@abc.com",
        avatar="https://my-avatar.png",
    )
    db_session.add(new_user)
    db_session.commit()

    # When we list users
    my_users = users.list_users()

    # Then
    assert my_users == [
        {
            "avatar": "https://my-avatar.png",
            "created_at": ANY,
            "email": "j@abc.com",
            "id": ANY,
            "name": "John",
        },
    ]

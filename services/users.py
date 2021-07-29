from models.users import User


def list_users():
    users = User.query.all()
    return [user.to_dict() for user in users]

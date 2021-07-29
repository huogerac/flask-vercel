from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import JSONB
import sqlalchemy as sa

from ext.database import db


class User(db.Model):

    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(128), nullable=False)
    email = sa.Column(sa.String(255), nullable=True, unique=True)
    password = sa.Column(sa.String(128), nullable=True)
    avatar = sa.Column(sa.UnicodeText(), nullable=True)
    created_at = sa.Column(
        sa.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "avatar": self.avatar,
            "created_at": self.created_at.isoformat(),
        }

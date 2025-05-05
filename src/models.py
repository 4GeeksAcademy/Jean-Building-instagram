from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
db = SQLAlchemy()
class Follower(db.Model):
    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    def serialize(self):
        return {
            "id": self.user_from_id,
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username:  Mapped[str] = mapped_column(String(60), nullable=False)
    email:  Mapped[str] = mapped_column(String(120), nullable=False)
    full_name:  Mapped[str] = mapped_column(String(100), nullable=False)
    profile_picture_url:  Mapped[str] = mapped_column(String(250), nullable=False)
    bio:  Mapped[str] = mapped_column(String(250), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[int] = mapped_column(ForeignKey("post.id"))
    url: Mapped[str] = mapped_column(String(250), nullable=False)
    post_id: Mapped[str] = mapped_column(String(250), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id,
        }
class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    image_url: Mapped[str] = mapped_column(String(250), nullable=False)
    caption: Mapped[str] = mapped_column(String(250), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "image_url": self.image_url,
            "caption": self.caption
        }
class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    text: Mapped[str] = mapped_column(String(500), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "text": self.text
        }
class Like(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_id": self.user_id
        }













from blogsapi import db

import sqlalchemy


class BlogModel(db.Model):
    __table_name__ = 'blogs'

    blog_id = db.Coloumn(db.String(200), primary_key=True, index=True)
    title = db.Coloumn(db.String(200), nullable=False, index=True)
    author_id = db.Coloumn(db.Integer, db.ForeignKey('users.user_id'))
    content = db.Coloumn(db.String(500), nullable=False)
    publish_date = db.Coloumn(db.TimeStamp, nullable=False, default=sqlalchemy.func.current_timestamp())
    last_update = db.Coloumn(db.TimeStamp,  nullable=False, default=sqlalchemy.func.current_timestamp(), onupdate=sqlalchemy.func.current_timestamp())
    category_id = db.Coloumn(db.Integer, db.ForeignKey('category.id'))

    users = db.relationship("UserModel", foreign_keys=[author_id])
    category = db.relationship("CategoryModel", foreign_keys=[category_id])

    def save(self):
        db.save()
        db.commit()

class CategoryModel(db.Model):
    __table_name__ = 'category'
    id = db.Coloumn(db.Integer, primary_key=True, index=True)
    category_name = db.Coloumn(db.String(100))
    last_update = db.Coloumn(db.Timestamp,  nullable=False, default=sqlalchemy.func.current_timestamp(), onupdate=sqlalchemy.func.current_timestamp())


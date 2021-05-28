from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import models


class Database:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)

    def get_or_create(self, session, model, filter_field, data):
        instance = session.query(model).filter(
            getattr(model, filter_field) == data[filter_field]).first()
        if not instance:
            instance = model(**data)
        return instance

    def add_post(self, data):
        session = self.maker()
        post = self.get_or_create(session, models.Post, "id", data["post_data"])
        author = self.get_or_create(session, models.Author, "url", data['author_data'])
        post.author = author
        session.add(post)
        try:
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()
        print(1)

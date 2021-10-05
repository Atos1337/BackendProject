import graphene
import numpy as np
from dependencies import in_memory_db


class Rating(graphene.ObjectType):
    average_rating = graphene.Float()
    max_rating = graphene.Float()
    min_rating = graphene.Float()


class Book(graphene.ObjectType):
    name = graphene.String()
    rating = graphene.Float()


class AuthorStat(graphene.ObjectType):
    name = graphene.String()
    total_count = graphene.Int()
    top_books = graphene.List(Book, limit=graphene.Int())
    rating_stat = graphene.Field(Rating)

    def resolve_total_count(self, info):
        return len(in_memory_db.author_books[self.name])

    def resolve_top_books(self, info, limit: int):
        return list(map(
            lambda name: Book(name=name, rating=in_memory_db.books_rating[name]),
            sorted(
                in_memory_db.author_books[self.name],
                key=(lambda name: in_memory_db.books_rating[name]),
                reverse=True
            )
        ))[:limit]

    def resolve_rating_stat(self, info):
        books = [in_memory_db.books_rating[name] for name in (in_memory_db.author_books[self.name])]
        return Rating(
            average_rating=np.average(books),
            min_rating=np.min(books),
            max_rating=np.max(books)
        )


class Query(graphene.ObjectType):
    author_stat = graphene.Field(AuthorStat, name=graphene.String())

    def resolve_author_stat(self, info, name: str):
        return AuthorStat(name=name)


schema = graphene.Schema(query=Query)

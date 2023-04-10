from graphene import ObjectType, String


class Book(ObjectType):
    id = String()
    title = String()
    author = String()
    ratings = String()
    reviews = String()

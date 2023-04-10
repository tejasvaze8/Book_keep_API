import graphene
from data import books
from type import Book
import pickle


class CreateBook(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        title = graphene.String()
        author = graphene.String()
        ratings = graphene.String()
        reviews = graphene.String()
    book = graphene.Field(Book)

    def mutate(root, info, id, title, author, ratings, reviews):
        book = Book(id = id, title = title, author = author, ratings = ratings, reviews = reviews)
        file2 = open(r'C:\d.pkl', 'rb')
        new_d = pickle.load(file2)
        file2.close()
        new_d.append(
            {
                "id": id,
                "title": title,
                "author": author,
                "ratings": ratings,
                "reviews": reviews
            }
        )
        afile = open(r'C:\d.pkl', 'wb')
        pickle.dump(new_d, afile)
        afile.close()

        return CreateBook(book = book)


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        title = graphene.String()
        author = graphene.String()
        ratings = graphene.String()
        reviews = graphene.String()

    book = graphene.Field(Book)

    def mutate(root, info, id, title, author, ratings, reviews):
        book = Book(id=id, title=title,author=author, ratings=ratings, reviews=reviews)
        file2 = open(r'C:\d.pkl', 'rb')
        new_d = pickle.load(file2)
        file2.close()
        old_book = list(filter(lambda x: x["id"] == id, new_d))[0]
        new_d.remove(old_book)
        new_d.append(
            {
                "id": id,
                "title": title,
                "author": author,
                "ratings": ratings,
                "reviews": reviews
            }
        )

        afile = open(r'C:\d.pkl', 'wb')
        pickle.dump(new_d, afile)
        afile.close()
        return UpdateBook(book=book)


class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    # lambda
    book = graphene.Field(Book)

    def mutate(root, info, id):
        old_book = list(filter(lambda x: x["id"] == id, books))[0]
        book = Book(id=old_book["id"], title=old_book["title"], author=old_book['author'], ratings=old_book["ratings"],
                    reviews=old_book['reviews'])
        books.remove(old_book)
        return DeleteBook(book=book)

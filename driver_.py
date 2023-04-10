from graphene import Field, String, List
import graphene
from mutation import CreateBook, DeleteBook, UpdateBook
from query import Query
from type import Book


class MyMutations(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()


class MyQuery(Query):
    get_book = Field(Book, id=String())
    get_books = List(Book)


schema = graphene.Schema(query=MyQuery, mutation=MyMutations)



# result = schema.execute(
#     """
#     mutation {
#         createBook(id: "2",title: "P Power", author: "Decathalac Mango",ratings: "3", reviews: "Excellent"){
#             book{
#                 id
#                 title
#                 author
#                 ratings
#                 reviews
#             }
#         }
#     }
#
#     """
# )
# print(result.data)


#
# result = schema.execute(
#     """
#     mutation {
#         update(id: "1", name: "Tejasvi", email: "tvaze23", password: "password22323"){
#             user{
#                 id
#                 name
#                 email
#                 password
#             }
#         }
#     }
#     """
# )
#
# print(result.data)

# result = schema.execute(
#     """
#     mutation{
#         deleteUser(id:"1") {
#             user{
#                 id
#                 name
#                 email
#                 password
#             }
#         }
#     }
#     """
# )
# print(result.data)

# result = schema.execute(
#     """
#     query{
#         getUser(id: "1"){
#             id
#             name
#             email
#             password
#         }
#     }
#     """
# )
# print(result.data)

# result = schema.execute(
#     """
#     query{
# #         getBooks{
# #             id
# #             title
# #             author
# #             ratings
# #             reviews
# #         }
# #     }
#     """
# )
#
# print(result.data)

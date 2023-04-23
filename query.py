from graphene import ObjectType
import pickle


class Query(ObjectType):
    def resolve_get_book(root, info, id):
        file2 = open(r'C:\d.pkl', 'rb')
        new_d = pickle.load(file2)
        file2.close()
        return list(filter(lambda x: x["id"] == id, new_d))[0]

    def resolve_get_books(root, info):
        file2 = open(r'C:\d.pkl', 'rb')
        new_d = pickle.load(file2)
        file2.close()
        return new_d

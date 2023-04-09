from flask import Flask
from graphql_server.flask import GraphQLView
from driver_ import schema


app = Flask(__name__)
def index():
    pass

app.add_url_rule(
    '/',
    view_func= GraphQLView.as_view(
        'graphql',
        schema = schema,
        graphiql = True
    )
)



if __name__ == "__main__":
    app.run(host= "0.0.0.0",debug=True)
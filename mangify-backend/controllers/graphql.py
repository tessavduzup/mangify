import graphene

class Query(graphene.ObjectType):
    id = graphene.Int()
    genre_name = graphene.String()

    def resolve_genre_name(self, info):
        return "Hello"


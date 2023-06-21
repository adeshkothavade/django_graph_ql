import graphene

import quest.queries
import quest.mutations

class Query(quest.queries.Query, graphene.ObjectType):
    pass

class Mutation(quest.mutations.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
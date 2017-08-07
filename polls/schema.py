from graphene_django import DjangoObjectType
import graphene
from polls.models import Question as QuestionModel

class Question(DjangoObjectType):
    class Meta:
        model = QuestionModel

class Query(graphene.ObjectType):
    questions = graphene.List(Question)

    @graphene.resolve_only_args
    def resolve_questions(self):
        return QuestionModel.objects.all()

schema = graphene.Schema(query=Query)

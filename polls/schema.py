from graphene_django import DjangoObjectType
import graphene
from polls.models import Question

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

class Query(graphene.ObjectType):
    questions = graphene.List(QuestionType)

    @graphene.resolve_only_args
    def resolve_questions(self):
        return Question.objects.all()

schema = graphene.Schema(query=Query)

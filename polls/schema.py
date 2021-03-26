from graphene_django import DjangoObjectType
import graphene
from polls.models import Question
from django.utils import timezone


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

class Query(graphene.ObjectType):
    questions = graphene.List(QuestionType)

    @graphene.resolve_only_args
    def resolve_questions(self):
        return Question.objects.all()


class NewQuestion(graphene.Mutation):
    class Input:
        question_text = graphene.String(required=True)
    question = graphene.Field(QuestionType)

    @classmethod
    def mutate(cls, root, info, question_text):
        question = Question.objects.create(question_text=question_text, pub_date=timezone.now())
        return NewQuestion(question=question)


class Mutation(graphene.ObjectType):
    new_question = NewQuestion.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

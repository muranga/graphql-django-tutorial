from graphene_django import DjangoObjectType
import graphene
import datetime
from polls.models import Question

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

class Query(graphene.ObjectType):
    questions = graphene.List(QuestionType)

    @graphene.resolve_only_args
    def resolve_questions(self):
        return Question.objects.all()

class NewQuestion(graphene.relay.ClientIDMutation):
    class Input:
        question_text = graphene.String(required=True)

    question = graphene.Field(QuestionType)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        question_text = input.get("question_text")
        question = Question.objects.create(question_text=question_text, pub_date=datetime.datetime.now())
        return NewQuestion(question=question)

class Mutation(graphene.ObjectType):
    new_question = NewQuestion.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

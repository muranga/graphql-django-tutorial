from polls.models import Question
from polls.schema import schema
from django.test import TestCase
from django.utils import timezone

class QuestionsQueryTestCase(TestCase):

    def test_that_user_can_list_questions(self):
        Question.objects.create(question_text="test 1", pub_date=timezone.now())
        Question.objects.create(question_text="test 2", pub_date=timezone.now())
        test_query = """
        query {
            questions {
                id,
                questionText
            }
        }
        """
        result = schema.execute(test_query)
        questions = result.data["questions"]
        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0]["questionText"], "test 1")

    def test_that_user_can_create_question(self):
        question_text = "what is happening"
        test_mutation = '''
        mutation {
            newQuestion(input: {questionText: "%s"}){
                question {
                    id,
                    questionText
                }
            }
        }
        ''' % question_text
        result = schema.execute(test_mutation)
        self.assertEqual(result.data["newQuestion"]["question"]["questionText"], "what is happening")

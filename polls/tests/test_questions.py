from unittest import TestCase
from polls.models import Question
from polls.schema import schema
import datetime

class QuestionsQueryTestCase(TestCase):

    def test_that_user_can_list_questions(self):
        Question.objects.create(question_text="test 1", pub_date=datetime.datetime.now())
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
        self.assertEqual(len(questions), 1)
        self.assertEqual(questions[0]["questionText"], "test 1")

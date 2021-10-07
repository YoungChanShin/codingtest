from unittest import TestCase

import problem


class Test(TestCase):
    def test_1(self):
        compressed = "one4seveneight"
        result = 1478

        self.assertEqual(problem.solution(compressed), result)

    def test_2(self):
        compressed = "23four5six7"
        result = 234567
        self.assertEqual(problem.solution(compressed), result)

    def test_3(self):
        compressed = "2three45sixseven"
        result = 234567

        self.assertEqual(problem.solution(compressed), result)

    def test_4(self):
        compressed = "123"
        result = 	123

        self.assertEqual(problem.solution(compressed), result)

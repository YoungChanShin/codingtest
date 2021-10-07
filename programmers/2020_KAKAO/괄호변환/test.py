from unittest import TestCase

import parentheses


class Test(TestCase):
    def test_1(self):
        p = "(()())()"
        result = "(()())("

        self.assertEqual(parentheses.solution(p), result)

    def test_2(self):
        p = ")("
        result = "()"

        self.assertEqual(parentheses.solution(p), result)

    def test_3(self):
        p = "()))((()"
        result = "()(())()"

        self.assertEqual(parentheses.solution(p), result)
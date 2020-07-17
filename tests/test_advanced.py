# -*- coding: utf-8 -*-

from .context import days

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(days.hmm())


if __name__ == '__main__':
    unittest.main()

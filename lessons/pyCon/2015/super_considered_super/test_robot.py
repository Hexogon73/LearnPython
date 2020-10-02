import unittest

from lessons.super_considered_super.robot import CleaningRobot


class MockBot(object):

    def __init__(self):
        self.tasks = []

    def fetch(self, tool):
        self.tasks.append(f'Fetching {tool}')

    def move_forward(self, tool):
        self.tasks.append(f'forward {tool}')

    def move_backward(self, tool):
        self.tasks.append(f'backward {tool}')

    def replace(self, tool):
        self.tasks.append(f'replace {tool}')


class MockedCleaningRobot(CleaningRobot, MockBot):
    """Inject a mock bot into the robot dependency"""


class TestCleaningRobot(unittest.TestCase):
    def test_clean(self):
        t = MockedCleaningRobot()
        t.clean('map')
        expected = (['fetching map'] +
                    ['forward map', 'backward map'] * 10 +
                    ['replace map'])
        self.assertEqual(t.tasks, expected)


if __name__ == '__main__':
    unittest.main()

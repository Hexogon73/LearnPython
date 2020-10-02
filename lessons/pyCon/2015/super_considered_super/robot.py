class Robot(object):
    def fetch(self, tool):
        print('Fetching')

    def move_forward(self, tool):
        print('Moving forward')

    def move_backward(self, tool):
        print('Moving backward')

    def replace(self, tool):
        print('Replacing')


class CleaningRobot(Robot):
    def clean(self, tool, times=10):
        super().fetch(tool)
        for i in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)


if __name__ == '__main__':
    t = CleaningRobot()
    t.clean('broom')

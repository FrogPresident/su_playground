class Logger:
    LEVEL_DEBUG = 0
    LEVEL_INFO = 1

    def __init__(self, *args):
        level, = args
        print("init")
        self.level = level

    def debug(self, msg):
        if self.level <= self.LEVEL_DEBUG:
            print(f'[DEBUG] {msg}')

    def info(self, msg):
        if self.level <= self.LEVEL_INFO:
            print(f'[INFO] {msg}')

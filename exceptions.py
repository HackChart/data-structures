class StackOverflowError(Exception):
    def __init__(self, limit, message=None):
        super(StackOverflowError, self).__init__()
        self.message = message
        self.limit = limit

    def __str__(self):
        if self.message:
            return f'Stack Overflow Error: Stack has reached limit {self.limit}\n{self.message}'
        else:
            return f'Stack Overflow Error: Stack has reached limit {self.limit}'


class StackUnderflowError(Exception):
    def __init__(self, message=None):
        super(StackUnderflowError, self).__init__()
        self.message = message

    def __str__(self):
        if self.message:
            return f'Stack Underflow Error: {self.message}'
        else:
            return 'Stack Underflow Error: Stack Empty'

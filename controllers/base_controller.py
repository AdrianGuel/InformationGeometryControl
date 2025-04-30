class BaseController:
    def __init__(self, model):
        self.model = model

    def compute_control(self, x_current):
        raise NotImplementedError

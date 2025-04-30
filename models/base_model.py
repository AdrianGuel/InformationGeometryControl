from casadi import SX, Function

class BaseModel:
    def __init__(self):
        self.x = SX.sym("x")
        self.u = SX.sym("u")
        self.f = None

    def define_dynamics(self):
        raise NotImplementedError

    def get_dynamics_function(self) -> Function:
        return self.f

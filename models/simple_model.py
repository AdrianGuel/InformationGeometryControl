from models.base_model import BaseModel
from casadi import SX, Function

class SimpleModel(BaseModel):
    def define_dynamics(self):
        x, u = self.x, self.u
        dx = -x + u
        self.f = Function("f", [x, u], [dx])

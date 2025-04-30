from controllers.base_controller import BaseController
from casadi import SX, vertcat, Function, nlpsol

class MPCController(BaseController):
    def __init__(self, model, horizon=10):
        super().__init__(model)
        self.horizon = horizon
        self.define_problem()

    def define_problem(self):
        N = self.horizon
        x_sym = SX.sym("x0")  # Initial state input
        u_sym = SX.sym("u", N)  # Decision variables: control inputs for all N steps

        X = x_sym
        cost = 0

        for k in range(N):
            u_k = u_sym[k]
            cost += X**2 + u_k**2
            X = X + 0.1 * self.model.get_dynamics_function()(X, u_k)

        nlp = {
            'x': u_sym,
            'p': x_sym,     # Treat x0 as a parameter
            'f': cost
        }

        self.solver = nlpsol("solver", "ipopt", nlp)

    def compute_control(self, x_current):
        sol = self.solver(x0=[0.0]*self.horizon, p=x_current)
        return float(sol['x'][0])  # Return first control input

class Simulator:
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

    def run(self, x0, steps=50, dt=0.1):
        x = x0
        xs = [x]
        us = []

        for _ in range(steps):
            u = self.controller.compute_control(x)
            dx = self.model.get_dynamics_function()(x, u)
            x = float(x + dt * dx)
            xs.append(x)
            us.append(float(u))

        return xs, us

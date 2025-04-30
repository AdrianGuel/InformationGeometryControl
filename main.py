import streamlit as st
import plotly.graph_objects as go

from models.simple_model import SimpleModel
from controllers.mpc_controller import MPCController
from simulators.simulator import Simulator

# Streamlit UI
st.title("1D CasADi Control Simulation")

x0 = st.slider("Initial condition x₀", min_value=-10.0, max_value=10.0, value=5.0)
steps = st.slider("Simulation steps", min_value=10, max_value=200, value=50)
dt = st.number_input("Time step Δt", min_value=0.01, max_value=1.0, value=0.1, step=0.01)
run_sim = st.button("Run Simulation")

if run_sim:
    # Model, controller, simulation
    model = SimpleModel()
    model.define_dynamics()
    controller = MPCController(model)
    sim = Simulator(model, controller)

    results_x, results_u = sim.run(x0=x0, steps=steps, dt=dt)

    # Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=results_x, mode="lines+markers", name="x (state)"))
    fig.add_trace(go.Scatter(y=results_u, mode="lines+markers", name="u (control)", yaxis="y2"))

    fig.update_layout(
        title="State and Control Trajectories",
        xaxis_title="Time Step",
        yaxis=dict(title="State x"),
        yaxis2=dict(title="Control u", overlaying="y", side="right"),
        template="plotly_dark",
        legend=dict(x=0, y=1.1, orientation="h")
    )
    st.plotly_chart(fig, use_container_width=True)

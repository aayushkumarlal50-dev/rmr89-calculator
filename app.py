import streamlit as st

from rmr.constants import (
    JOINT_CONDITIONS, GROUNDWATER_CONDITIONS, 
    ORIENTATION_TUNNELS, ORIENTATION_SLOPES, ORIENTATION_FOUNDATIONS
)
from rmr.calculations import calculate_rmr
from rmr.plotting import create_contribution_bar_chart, create_degradation_pie_chart

# Configure Page
st.set_page_config(page_title="RMR89 Calculator | Geotech Toolkit", layout="wide", page_icon="🪨")

# Main Header
st.title("Rock Mass Rating (RMR89) Calculator")
st.markdown("---")

# ----------------- SIDEBAR INPUTS -----------------
with st.sidebar:
    st.header("Geological Inputs")
    
    st.subheader("Intact Rock Strength")
    ucs_val = st.number_input("UCS (MPa)", min_value=0.0, max_value=500.0, value=150.0, step=1.0)
    
    st.subheader("Drill Core Quality")
    rqd_val = st.number_input("RQD (%)", min_value=0.0, max_value=100.0, value=85.0, step=1.0)
    
    st.subheader("Discontinuity Spacing")
    spacing_val = st.number_input("Spacing (meters)", min_value=0.001, max_value=10.0, value=0.5, step=0.1)
    
    st.subheader("Discontinuity Condition")
    cond_val = st.selectbox("Select Condition", list(JOINT_CONDITIONS.keys()))
    
    st.subheader("Groundwater Condition")
    gw_val = st.selectbox("Select Groundwater", list(GROUNDWATER_CONDITIONS.keys()))
    
    st.markdown("---")
    st.header("Project Configuration")
    excav_type = st.selectbox("Excavation Type", ["Tunnels & Mines", "Slopes", "Foundations"])
    
    # Dynamic orientation options based on excavation type
    if excav_type == "Slopes":
        orient_opts = list(ORIENTATION_SLOPES.keys())
    elif excav_type == "Foundations":
        orient_opts = list(ORIENTATION_FOUNDATIONS.keys())
    else:
        orient_opts = list(ORIENTATION_TUNNELS.keys())
        
    orient_val = st.selectbox("Discontinuity Orientation", orient_opts)

# ----------------- CALCULATION ENGINE -----------------
try:
    results = calculate_rmr(
        ucs=ucs_val,
        rqd=rqd_val,
        spacing=spacing_val,
        condition_str=cond_val,
        groundwater_str=gw_val,
        orientation_str=orient_val,
        excavation_type=excav_type
    )
except Exception as e:
    st.error(f"Calculation Error: {e}")
    st.stop()

# ----------------- DASHBOARD DISPLAY -----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Final RMR", value=results.final_rmr, delta=f"Basic: {results.basic_rmr}")
with col2:
    st.metric("Rock Class", value=f"Class {results.classification.class_number}")
with col3:
    st.metric("Rock Quality", value=results.classification.description)
with col4:
    st.metric("Estimated GSI", value=results.gsi_estimate, help="GSI ≈ RMR89 - 5 (for RMR > 23)")

st.markdown("---")

# ----------------- VISUALIZATIONS -----------------
v_col1, v_col2 = st.columns(2)

with v_col1:
    st.subheader("Parameter Contributions")
    fig_bar = create_contribution_bar_chart(results)
    st.pyplot(fig_bar)

with v_col2:
    st.subheader("Quality Degradation Limits")
    fig_pie = create_degradation_pie_chart(results)
    st.pyplot(fig_pie)

# ----------------- ENGINEERING INTERPRETATION -----------------
st.subheader("Engineering Interpretation & Guidelines")
t_col1, t_col2 = st.columns(2)

with t_col1:
    st.info("**Mohr-Coulomb Parameters (Estimated)**")
    st.write(f"**Cohesion ($c'$):** {results.classification.cohesion_kpa[0]} - {results.classification.cohesion_kpa[1]} kPa")
    st.write(f"**Friction Angle ($\\phi'$):** {results.classification.friction_angle_deg[0]}° - {results.classification.friction_angle_deg[1]}°")
    
    st.warning("**Kinematic/Stability Status**")
    st.write(f"**Typical Stand-up Time:** {results.classification.stand_up_time}")

with t_col2:
    st.success("**Support Recommendations**")
    st.write(results.classification.support_guidelines)
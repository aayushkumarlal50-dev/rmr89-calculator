# Rock Mass Rating (RMR89) Calculator

A production-ready geotechnical engineering application for evaluating rock mass quality using the Bieniawski (1989) Rock Mass Rating system. This tool provides instant empirical estimations for rock strength, stability, and support requirements based on field observations.

---

---

## 1. Project Overview
This application answers a fundamental rock mechanics question: *"How strong is the rock mass?"* 

Designed to integrate with larger slope stability and underground excavation toolkits, this software automates the RMR89 classification process. It translates raw geological data into a standardized point system, applies kinematic orientation penalties, and outputs actionable engineering parameters (Mohr-Coulomb strength, stand-up time, and GSI).

## 2. Engineering Theory & Validation
The classification engine is built strictly upon the **Bieniawski (1989)** standard.

*   **Discrete Rating System:** To prevent arbitrary interpolation errors, this software enforces the exact step-wise boundaries published in the original 1989 literature. For example, Intact Rock Strength (UCS) uses strict categorical thresholds rather than linear interpolation.
*   **Geological Strength Index (GSI):** The application estimates GSI using the universally accepted Hoek et al. (1995) empirical offset formula: `GSI = RMR89 - 5`. This calculation is structurally restricted to execute only when `RMR89 > 23`.
*   **Context-Aware Penalties:** Discontinuity orientation penalties are dynamically mapped to one of three distinct matrices: Tunnels & Mines, Slopes, or Foundations, reflecting the different kinematic dangers of each excavation type.

## 3. Features & Capabilities
*   **Interactive Input Engine:** Real-time processing of UCS, RQD, Discontinuity Spacing, Joint Condition, and Groundwater.
*   **Dynamic Visualizations:** 
    *   *Parameter Contribution Chart:* A bar chart illustrating the positive point distribution driving the rock's strength.
    *   *Quality Degradation Limits:* A donut chart isolating the exact geological parameters penalizing the rock mass.
*   **Automated Design Estimations:** Instant translation of RMR into typical stand-up time windows, internal friction angles ($\phi'$), cohesion ranges ($c'$), and basic support guidelines.

## 4. Software Architecture
The application follows a modular, maintainable structure separating UI from the calculation engine:

```text
rmr_toolkit/
├── app.py                 # Main Streamlit UI and dashboard layout
├── requirements.txt       # Project dependencies
├── rmr/
│   ├── __init__.py
│   ├── constants.py       # Bieniawski reference tables and text definitions
│   ├── ratings.py         # Functions converting raw inputs -> RMR points
│   ├── classification.py  # Mapping Final RMR -> Engineering classes (I-V)
│   ├── calculations.py    # Core engine orchestrating the RMR math
│   └── plotting.py        # Matplotlib visualization generation
└── tests/                 # Pytest suite for boundary and unit testing
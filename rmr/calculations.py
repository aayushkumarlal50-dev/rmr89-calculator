"""
Calculation engine orchestrating the RMR process.
"""
from dataclasses import dataclass
from typing import Optional
from rmr.constants import JOINT_CONDITIONS, GROUNDWATER_CONDITIONS, ORIENTATION_TUNNELS, ORIENTATION_SLOPES, ORIENTATION_FOUNDATIONS
from rmr.ratings import get_ucs_rating, get_rqd_rating, get_spacing_rating
from rmr.classification import classify_rock_mass, RockClassResult

@dataclass
class RMREngineData:
    ucs_rating: int
    rqd_rating: int
    spacing_rating: int
    condition_rating: int
    groundwater_rating: int
    basic_rmr: int
    orientation_adjustment: int
    final_rmr: int
    gsi_estimate: int
    classification: RockClassResult

def calculate_rmr(
    ucs: float,
    rqd: float,
    spacing: float,
    condition_str: str,
    groundwater_str: str,
    orientation_str: str,
    excavation_type: str = "Tunnels & Mines"
) -> RMREngineData:
    """Executes the full RMR89 calculation sequence."""
    
    if condition_str not in JOINT_CONDITIONS:
        raise ValueError(
            f"Unknown condition_str '{condition_str}'. Must be one of: {list(JOINT_CONDITIONS.keys())}"
        )
    if groundwater_str not in GROUNDWATER_CONDITIONS:
        raise ValueError(
            f"Unknown groundwater_str '{groundwater_str}'. Must be one of: {list(GROUNDWATER_CONDITIONS.keys())}"
        )

    r_ucs = get_ucs_rating(ucs)
    r_rqd = get_rqd_rating(rqd)
    r_spacing = get_spacing_rating(spacing)
    r_cond = JOINT_CONDITIONS[condition_str]
    r_gw = GROUNDWATER_CONDITIONS[groundwater_str]
    
    basic_rmr = r_ucs + r_rqd + r_spacing + r_cond + r_gw
    
    # Orientation Penalty based on context
    if excavation_type == "Slopes":
        orientation_table = ORIENTATION_SLOPES
    elif excavation_type == "Foundations":
        orientation_table = ORIENTATION_FOUNDATIONS
    else:
        orientation_table = ORIENTATION_TUNNELS

    if orientation_str not in orientation_table:
        raise ValueError(
            f"Unknown orientation_str '{orientation_str}' for excavation_type '{excavation_type}'. "
            f"Must be one of: {list(orientation_table.keys())}"
        )
    r_orient = orientation_table[orientation_str]
        
    final_rmr = basic_rmr + r_orient
    final_rmr = max(0, min(100, final_rmr)) # Clamp between 0 and 100
    
    # GSI Approximation (Hoek et al., 1995: GSI = RMR89 - 5 for RMR > 23)
    gsi_estimate = max(0, final_rmr - 5) if final_rmr > 23 else final_rmr

    classification = classify_rock_mass(final_rmr)
    
    return RMREngineData(
        ucs_rating=r_ucs,
        rqd_rating=r_rqd,
        spacing_rating=r_spacing,
        condition_rating=r_cond,
        groundwater_rating=r_gw,
        basic_rmr=basic_rmr,
        orientation_adjustment=r_orient,
        final_rmr=final_rmr,
        gsi_estimate=gsi_estimate,
        classification=classification
    )
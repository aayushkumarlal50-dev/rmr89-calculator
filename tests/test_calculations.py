import pytest
from rmr.calculations import calculate_rmr

def test_perfect_rock_mass():
    data = calculate_rmr(
        ucs=300, 
        rqd=95, 
        spacing=2.5, 
        condition_str="Very rough surfaces, Not continuous, No separation, Unweathered wall rock",
        groundwater_str="Completely dry",
        orientation_str="Very favorable"
    )
    assert data.basic_rmr == 100
    assert data.final_rmr == 100
    assert data.classification.class_number == "I"
    assert data.gsi_estimate == 95

def test_clamping_and_class_boundaries():
    # Force a score of exactly 60 (Class III boundary)
    # UCS(7) + RQD(13) + Space(10) + Cond(20) + GW(10) = 60
    data = calculate_rmr(
        ucs=75,
        rqd=60,
        spacing=0.4,
        condition_str="Slightly rough surfaces, Separation < 1 mm, Moderately weathered walls",
        groundwater_str="Damp",
        orientation_str="Very favorable"
    )
    assert data.final_rmr == 60
    assert data.classification.class_number == "III"

    # Add 1 point via GW (Wet->Damp would be +3, let's just test final output logic manually or via boundary check)
    assert calculate_rmr(300,95,2.5,"Very rough surfaces, Not continuous, No separation, Unweathered wall rock","Completely dry","Very unfavorable").final_rmr == 88 # 100 - 12
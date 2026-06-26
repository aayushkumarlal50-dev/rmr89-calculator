"""
Classification logic mapping Final RMR to Engineering properties.
"""
from dataclasses import dataclass
from typing import Tuple

@dataclass
class RockClassResult:
    class_number: str
    description: str
    stand_up_time: str
    cohesion_kpa: Tuple[int, int]
    friction_angle_deg: Tuple[int, int]
    support_guidelines: str

def classify_rock_mass(rmr: int) -> RockClassResult:
    """Classify the rock mass based on Final RMR score."""
    if rmr >= 81:
        return RockClassResult(
            class_number="I",
            description="Very Good Rock",
            stand_up_time="20 years for 15 m span",
            cohesion_kpa=(400, 1000),  # >400 technically, represented as range
            friction_angle_deg=(45, 60), # >45
            support_guidelines="Generally no support required except for occasional spot bolting."
        )
    elif rmr >= 61:
        return RockClassResult(
            class_number="II",
            description="Good Rock",
            stand_up_time="1 year for 10 m span",
            cohesion_kpa=(300, 400),
            friction_angle_deg=(35, 45),
            support_guidelines="Locally rock bolts in crown 3m long, spaced 2.5m with occasional wire mesh."
        )
    elif rmr >= 41:
        return RockClassResult(
            class_number="III",
            description="Fair Rock",
            stand_up_time="1 week for 5 m span",
            cohesion_kpa=(200, 300),
            friction_angle_deg=(25, 35),
            support_guidelines="Systematic bolts 4m long, spaced 1.5-2m in crown and walls with wire mesh. 50-100mm shotcrete in crown."
        )
    elif rmr >= 21:
        return RockClassResult(
            class_number="IV",
            description="Poor Rock",
            stand_up_time="10 hours for 2.5 m span",
            cohesion_kpa=(100, 200),
            friction_angle_deg=(15, 25),
            support_guidelines="Systematic bolts 4-5m long, spaced 1-1.5m. 100-150mm shotcrete in crown, 100mm on walls. Light steel sets."
        )
    else:
        return RockClassResult(
            class_number="V",
            description="Very Poor Rock",
            stand_up_time="30 minutes for 1 m span",
            cohesion_kpa=(0, 100), # <100
            friction_angle_deg=(0, 15), # <15
            support_guidelines="Systematic bolts 5-6m long, spaced 1-1.5m. 150-200mm shotcrete. Medium/heavy steel sets spaced 0.75m."
        )
"""
Core functions mapping raw geological inputs to Bieniawski (1989) RMR ratings.
Strict adherence to discrete step values per the 1989 publication.
"""

def get_ucs_rating(ucs_mpa: float) -> int:
    """Calculate RMR rating for Intact Rock Strength (UCS)."""
    if ucs_mpa > 250:
        return 15
    elif 100 < ucs_mpa <= 250:
        return 12
    elif 50 < ucs_mpa <= 100:
        return 7
    elif 25 < ucs_mpa <= 50:
        return 4
    elif 5 < ucs_mpa <= 25:
        return 2
    elif 1 < ucs_mpa <= 5:
        return 1
    else:
        return 0

def get_rqd_rating(rqd_percent: float) -> int:
    """Calculate RMR rating for Rock Quality Designation (RQD)."""
    if rqd_percent < 0 or rqd_percent > 100:
        raise ValueError("RQD must be between 0 and 100.")
    
    if rqd_percent >= 90:
        return 20
    elif 75 <= rqd_percent < 90:
        return 17
    elif 50 <= rqd_percent < 75:
        return 13
    elif 25 <= rqd_percent < 50:
        return 8
    else:
        return 3

def get_spacing_rating(spacing_m: float) -> int:
    """Calculate RMR rating for Spacing of Discontinuities."""
    if spacing_m > 2.0:
        return 20
    elif 0.6 < spacing_m <= 2.0:
        return 15
    elif 0.2 < spacing_m <= 0.6:
        return 10
    elif 0.06 <= spacing_m <= 0.2:
        return 8
    else:
        return 5
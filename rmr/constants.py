"""
Constants and specific string definitions for the RMR89 system.
"""

JOINT_CONDITIONS = {
    "Very rough surfaces, Not continuous, No separation, Unweathered wall rock": 30,
    "Slightly rough surfaces, Separation < 1 mm, Slightly weathered walls": 25,
    "Slightly rough surfaces, Separation < 1 mm, Highly weathered walls": 20,
    "Slickensided surfaces OR Gouge < 5 mm thick OR Separation 1-5 mm, Continuous": 10,
    "Soft gouge > 5 mm thick OR Separation > 5 mm, Continuous": 0
}

GROUNDWATER_CONDITIONS = {
    "Completely dry": 15,
    "Damp": 10,
    "Wet": 7,
    "Dripping": 4,
    "Flowing": 0
}

# Tunnels & Mines orientation penalties
ORIENTATION_TUNNELS = {
    "Very favorable": 0,
    "Favorable": -2,
    "Fair": -5,
    "Unfavorable": -10,
    "Very unfavorable": -12
}

# Slopes orientation penalties (Included for module compatibility)
ORIENTATION_SLOPES = {
    "Very favorable": 0,
    "Favorable": -5,
    "Fair": -25,
    "Unfavorable": -50,
    "Very unfavorable": -60
}

# Foundations orientation penalties
ORIENTATION_FOUNDATIONS = {
    "Very favorable": 0,
    "Favorable": -2,
    "Fair": -7,
    "Unfavorable": -15,
    "Very unfavorable": -25
}
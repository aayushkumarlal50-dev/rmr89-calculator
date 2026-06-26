"""
Visualization modules utilizing matplotlib for engineering dashboards.
"""
import matplotlib.pyplot as plt
import numpy as np
from rmr.calculations import RMREngineData

def create_contribution_bar_chart(data: RMREngineData) -> plt.Figure:
    """Creates a professional bar chart showing the breakdown of Basic RMR."""
    labels = ['UCS', 'RQD', 'Spacing', 'Condition', 'Groundwater']
    scores = [
        data.ucs_rating, 
        data.rqd_rating, 
        data.spacing_rating, 
        data.condition_rating, 
        data.groundwater_rating
    ]
    max_scores = [15, 20, 20, 30, 15]
    
    fig, ax = plt.subplots(figsize=(8, 4), facecolor='#ffffff')
    
    # Create background bars (Max potential score)
    ax.barh(labels, max_scores, color='#e0e0e0', label='Max Potential')
    # Create foreground bars (Actual score)
    bars = ax.barh(labels, scores, color='#2c5282', label='Actual Score')
    
    ax.set_xlabel('RMR Rating Points')
    ax.set_title('Parameter Contribution to Basic RMR')
    ax.invert_yaxis()  # Read top-to-bottom
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(loc='lower right')
    
    # Annotate values
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{int(width)}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0),
                    textcoords="offset points",
                    ha='left', va='center', fontsize=10, fontweight='bold')
                    
    plt.tight_layout()
    return fig

def create_degradation_pie_chart(data: RMREngineData) -> plt.Figure:
    """Creates a donut chart showing which parameter limits the rock mass quality most."""
    labels = ['UCS Penalty', 'RQD Penalty', 'Spacing Penalty', 'Condition Penalty', 'Groundwater Penalty']
    
    # Calculate how many points were "lost" compared to the max
    penalties = [
        15 - data.ucs_rating,
        20 - data.rqd_rating,
        20 - data.spacing_rating,
        30 - data.condition_rating,
        15 - data.groundwater_rating
    ]
    
    # Filter out 0 penalties
    filtered_labels = [l for l, p in zip(labels, penalties) if p > 0]
    filtered_penalties = [p for p in penalties if p > 0]
    
    fig, ax = plt.subplots(figsize=(6, 6), facecolor='#ffffff')
    if not filtered_penalties:
        ax.text(0.5, 0.5, "Perfect Rock Mass\nNo Penalties", ha='center', va='center', fontsize=14)
        ax.axis('off')
        return fig

    wedges, texts, autotexts = ax.pie(
        filtered_penalties, 
        labels=filtered_labels, 
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.OrRd(np.linspace(0.4, 0.9, len(filtered_penalties)))
    )
    
    # Draw circle for Donut effect
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    
    ax.axis('equal')  
    ax.set_title('Rock Mass Quality Degradation Breakdown')
    plt.tight_layout()
    return fig
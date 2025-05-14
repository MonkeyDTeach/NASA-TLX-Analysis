# task3_poc.py
import pandas as pd
import plotly.express as px

# Load merged data
df = pd.read_csv('mergedNasatlx.csv')

# Create an interactive 3D scatter plot with filters
fig = px.scatter_3d(
    df,
    x='mental_demand',
    y='physical_demand',
    z='frustration',
    color='group',
    symbol='dataset_type',
    title='NASA-TLX: Mental vs Physical Demand vs Frustration',
    labels={
        'mental_demand': 'Mental Demand (0-20)',
        'physical_demand': 'Physical Demand (0-20)',
        'frustration': 'Frustration (0-20)'
    },
    hover_name='name',  # Show clinician name on hover
)

# Add dropdown menu to filter by group
fig.update_layout(
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [{"visible": [True if group == g else False for g in df['group'].unique()]}],
                    "label": group,
                    "method": "update"
                }
                for group in df['group'].unique()
            ],
            "direction": "down",
            "showactive": True,
            "x": 0.1,
            "xanchor": "left",
            "y": 1.1,
            "yanchor": "top"
        }
    ]
)

# Save and show
fig.write_html('poc_3d_interactive.html')
fig.show()
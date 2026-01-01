import plotly.express as px

def apply_plotly_theme():
    px.defaults.template = "plotly_dark"
    px.defaults.color_discrete_sequence = [
        "#6366F1",
        "#22C55E",
        "#F59E0B",
        "#EF4444",
        "#06B6D4"
    ]

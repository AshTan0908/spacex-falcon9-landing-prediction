# Build a Dashboard Application with Plotly Dash
# SpaceX Launch Data

import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the dataset
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Get minimum and maximum payload values
min_payload = spacex_df["Payload Mass (kg)"].min()
max_payload = spacex_df["Payload Mass (kg)"].max()

# Create the Dash application
app = dash.Dash(__name__)

# Application Layout
app.layout = html.Div(
    children=[

        # Dashboard title
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={
                "textAlign": "center",
                "color": "#503D36",
                "font-size": 40
            }
        ),

        # ----------------------------------------------------
        # TASK 1: Launch Site Dropdown
        # ----------------------------------------------------

        html.Div(
            [
                html.Label(
                    "Select a Launch Site:",
                    style={"font-size": "20px"}
                ),

                dcc.Dropdown(
                    id="site-dropdown",

                    options=[
                        {
                            "label": "All Sites",
                            "value": "ALL"
                        }
                    ]
                    +
                    [
                        {
                            "label": site,
                            "value": site
                        }
                        for site in spacex_df["Launch Site"].unique()
                    ],

                    value="ALL",

                    placeholder="Select a Launch Site here",

                    searchable=True
                )
            ],
            style={
                "width": "80%",
                "margin": "auto"
            }
        ),

        html.Br(),

        # ----------------------------------------------------
        # TASK 2: Success Pie Chart
        # ----------------------------------------------------

        html.Div(
            dcc.Graph(
                id="success-pie-chart"
            )
        ),

        html.Br(),

        # ----------------------------------------------------
        # TASK 3: Payload Range Slider
        # ----------------------------------------------------

        html.Div(
            [
                html.Label(
                    "Payload Range (Kg):",
                    style={"font-size": "20px"}
                ),

                dcc.RangeSlider(
                    id="payload-slider",

                    min=0,

                    max=10000,

                    step=1000,

                    marks={
                        0: "0",
                        1000: "1000",
                        2000: "2000",
                        3000: "3000",
                        4000: "4000",
                        5000: "5000",
                        6000: "6000",
                        7000: "7000",
                        8000: "8000",
                        9000: "9000",
                        10000: "10000"
                    },

                    value=[
                        min_payload,
                        max_payload
                    ]
                )
            ],
            style={
                "width": "80%",
                "margin": "auto"
            }
        ),

        html.Br(),

        # ----------------------------------------------------
        # TASK 4: Payload vs Launch Outcome Scatter Plot
        # ----------------------------------------------------

        html.Div(
            dcc.Graph(
                id="success-payload-scatter-chart"
            )
        )
    ]
)


# ============================================================
# TASK 2
# Callback to render the success pie chart
# ============================================================

@app.callback(
    Output(
        component_id="success-pie-chart",
        component_property="figure"
    ),

    Input(
        component_id="site-dropdown",
        component_property="value"
    )
)
def get_pie_chart(entered_site):

    # --------------------------------------------------------
    # All sites selected
    # --------------------------------------------------------

    if entered_site == "ALL":

        # Count successful launches for all sites
        success_count = spacex_df["class"].value_counts().reset_index()

        success_count.columns = ["class", "count"]

        fig = px.pie(
            success_count,
            values="count",
            names="class",
            title="Total Launch Successes"
        )

    # --------------------------------------------------------
    # Specific launch site selected
    # --------------------------------------------------------

    else:

        # Filter the dataframe by selected launch site
        filtered_df = spacex_df[
            spacex_df["Launch Site"] == entered_site
        ]

        # Count success and failure
        success_count = filtered_df["class"].value_counts().reset_index()

        success_count.columns = ["class", "count"]

        fig = px.pie(
            success_count,
            values="count",
            names="class",
            title=f"Launch Successes for {entered_site}"
        )

    return fig


# ============================================================
# TASK 4
# Callback to render the payload scatter chart
# ============================================================

@app.callback(
    Output(
        component_id="success-payload-scatter-chart",
        component_property="figure"
    ),

    [
        Input(
            component_id="site-dropdown",
            component_property="value"
        ),

        Input(
            component_id="payload-slider",
            component_property="value"
        )
    ]
)
def get_scatter_chart(entered_site, payload_range):

    # --------------------------------------------------------
    # Filter according to selected payload range
    # --------------------------------------------------------

    low, high = payload_range

    filtered_df = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= low)
        &
        (spacex_df["Payload Mass (kg)"] <= high)
    ]

    # --------------------------------------------------------
    # If ALL sites are selected
    # --------------------------------------------------------

    if entered_site == "ALL":

        fig = px.scatter(
            filtered_df,

            x="Payload Mass (kg)",

            y="class",

            color="Booster Version Category",

            title="Payload Mass vs. Launch Outcome",

            hover_data=[
                "Launch Site",
                "Booster Version Category"
            ]
        )

    # --------------------------------------------------------
    # If a specific launch site is selected
    # --------------------------------------------------------

    else:

        filtered_df = filtered_df[
            filtered_df["Launch Site"] == entered_site
        ]

        fig = px.scatter(
            filtered_df,

            x="Payload Mass (kg)",

            y="class",

            color="Booster Version Category",

            title=f"Payload Mass vs. Launch Outcome for {entered_site}",

            hover_data=[
                "Launch Site",
                "Booster Version Category"
            ]
        )

    return fig


# ============================================================
# Run the application
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)
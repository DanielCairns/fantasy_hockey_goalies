from dash import html, dcc, dash_table, Input, Output, Dash
import altair as alt
import dash_bootstrap_components as dbc
import pandas as pd

# Read in global data
goalies_df = pd.read_csv('all_goalie_starts.csv')
TEAMS = goalies_df['name'].unique().tolist()
TEAMS.append("ALL TEAMS")
TEAMS.sort()

TEAM_CODES = {
    0:"ALL TEAMS",
    1:"NJD",
    2:"NYI",
    3:"NYR",
    4:"PHI",
    5:"PIT",
    6:"BOS",
    7:"BUF",
    8:"MTL",
    9:"OTT",
    10:"TOR",
    12:"CAR",
    13:"FLA",
    14:"TBL",
    15:"WSH",
    16:"CHI",
    17:"DET",
    18:"NSH",
    19:"STL",
    20:"CGY",
    21:"COL",
    22:"EDM",
    23:"VAN",
    24:"ANA",
    25:"DAL",
    26:"LAK",
    28:"SJS",
    29:"CBJ",
    30:"MIN",
    52:"WPG",
    53:"ARI",
    54:"VGK",
    55:"SEA"
}


# Setup app and layout/frontend
app = Dash(external_stylesheets=[dbc.themes.LUX])

server = app.server

app.layout = dbc.Container([
    html.H1('NHL Goalie Fantasy Point Distribution, 2022-23'),
    dbc.Row([
        dbc.Col([
            html.Label(['Team'], style={'font-weight': 'bold'}),
            dcc.Dropdown(id='team_dd', options=TEAMS, value="ALL TEAMS", multi=False)
        ], md=5),
        dbc.Col([
            html.Label(['Opponent'], style={'font-weight': 'bold'}),
            dcc.Dropdown(id='opp_dd', options=TEAMS, value="ALL TEAMS", multi=False)
        ], md=5),
        dbc.Col([
            html.Label(['Location'], style={'font-weight': 'bold'}),
            dcc.Dropdown(id='loc_dd', options=["All Locations", "Home", "Away"])
        ], md=2)
    ]),
    dbc.Row([
        dbc.Col([
            html.Iframe(id='hist', style={'border-width': '0', 'width': '100%', 'height': '800px'})
            ], md=8),
        dbc.Col([
            dash_table.DataTable(
                id='table',
                page_size=16)
            ], md=4)
    ])
])

# Set up callbacks/backend
@app.callback(Output('hist', 'srcDoc'), Input('team_dd', 'value'), Input('opp_dd', 'value'), Input('loc_dd', 'value'))
def plot_histogram(team, opp, location):
    """
    Update the histogram plot according to the user specified filters.

    Args:
        team (str): Team to include (or ALL TEAMS)
        opp (str): Opponent to include (or ALL TEAMS)
        location (str): One of "All Locations", "Home", or "Away"

    Returns:
        HTML chart
    """

    filtered_df = goalies_df.copy()
    
    # Filter for location Home/Away if specified
    if location == "Home":
        filtered_df = filtered_df.query("isHome == True")
    elif location == "Away":
        filtered_df = filtered_df.query("isHome == False")
        
    # Filter requested team and opponent
    if team != "ALL TEAMS":
        filtered_df = filtered_df[filtered_df['team.name'] == team]
    if opp != "ALL TEAMS":
        filtered_df = filtered_df[filtered_df['opponent.name'] == opp]

    chart_hist = alt.Chart(filtered_df).mark_bar().encode(
        alt.X("FPTS", 
              axis=alt.Axis(title='Fantasy Points'),
              bin=alt.Bin(extent=[-5, 15], step=1)),
        alt.Y("count()",
              axis=alt.Axis(title='Count'))
        ).properties(
            width=700,
            height=500
        ).interactive()
        
    chart_line = alt.Chart(filtered_df).mark_rule(color='red').encode(
        x="mean(FPTS):Q"
    )
    return (chart_hist+chart_line).to_html()

@app.callback(Output('table', 'data'), Input('team_dd', 'value'), Input('opp_dd', 'value'), Input('loc_dd', 'value'))
def update_table(team, opp, location):
    """
    Update the table according to the user specified filters.

    Args:
        team (str): Team to include (or all teams)
        opp (str): Opponent team to include (or all teams)
        location (str): One of "All Locations", "Home", or "Away"

    Returns:
        data to update table with
    """

    filtered_df = goalies_df.copy()
    
    # Filter for location Home/Away if specified
    if location == "Home":
        filtered_df = filtered_df.query("isHome == True")
    elif location == "Away":
        filtered_df = filtered_df.query("isHome == False")
        
    # Filter requested team and opponent
    if team != "ALL TEAMS":
        filtered_df = filtered_df[filtered_df['team.name'] == team]
    if opp != "ALL TEAMS":
        filtered_df = filtered_df[filtered_df['opponent.name'] == opp]
    
    agg_df = filtered_df.groupby(by=["person.fullName", "team.id"]).agg(
        {'stat.gamesStarted':'sum', 'FPTS':'mean'}
    ).reset_index()
    agg_df.columns = ["Name", "Team", "# Starts", "Av. PTS"]
    agg_df.sort_values(by = ["# Starts", "Av. PTS"], ascending=[False, False], inplace=True)
    
    # Clean column values
    agg_df = agg_df.replace({"Team": TEAM_CODES})
    agg_df = agg_df.astype({"# Starts":'int'})
    agg_df["Av. PTS"] = agg_df["Av. PTS"].round(2)   
    
    return agg_df.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)
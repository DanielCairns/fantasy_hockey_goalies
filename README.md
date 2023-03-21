# Fantasy Hockey Goalie Analyzer

This project implements a Python Dash dashboard app to visualize the fantasy performance of NHL goalies during the 2022-23 NHL season.

The dashboard is hosted via Render here: <https://fantasy-hockey-goalies.onrender.com>

## Usage

The dashboard contains a central histogram which highlights the distribution of fantasy points per start of all goalies, as well as the expected value of the distribution. To the right of the histogram is a table listing the individual goalie starts included in the data and the points per game of each goalie.

On start up, the filters are set to include all games played by all teams. There are two main filters on the top. The **Team** filter selects which teams' goalies to include (for example, selecting "VAN" will only include goalies who started games *FOR* the Vancouver Canucks this season). The **Opponent** filter selects which teams the goalies played against (for example, selecting "VAN" will show performances from all goalies who started *AGAINST* the Vancouver Canucks this season).

Notice that selecting the same team for both filters will yield no results, and selecting only a single (different) team for both filters yields only a few games. The recommended approach is to apply only *one* of the **Team** or **Opponent** filters.

Finally, there is a **Location** filter which allows the user to include only games started at Home or on the Road, if desired.

### Fantasy Point Calculation

Fantasy points are calculated per game based on the following conversions:

**3** points per win\
**0.24** points per save\
**3** points per shutout\
**1** point per overtime loss\
**-1** point per goal against\
**-1.5** point per loss

## Data

Raw data retrieved from [NHL.com API](https://statsapi.web.nhl.com/api/v1/teams) on March 12, 2023.

NHL.com API documentation created by Drew Hynes accessible on [gitlab](https://gitlab.com/dword4/nhlapi).

## License

Licensed under the GNU General Public License v3.0.

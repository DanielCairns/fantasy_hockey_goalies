# Proposal

## Motivation and Purpose

My role: Hockey Analytics Consultant

Target audience: Fantasy Hockey Players

Many fantasy hockey leagues allow managers to exchange players on their team with "free agents" who aren't owned by any fantasy teams. A common strategy is to exchange for short-term goalies who are likely to start favourable matchups in the coming week. This dashboard helps managers execute this strategy by identifying which goalie matchups are favourable or unfavourable, and which goalies they should expect to have strong performances in the short-term future.

## Description of the Data

The dataset was pulled from the NHL API and cleaned into a single CSV file. The file contains a row for each game a goalie played in the 2022-23 NHL season between October 1, 2022 and March 12, 2023 (approximately 2,000 rows totals). Each record includes information about the game, such as which team the goalie played for and which team the goalie played against, whether the goalie won or lost, and the goalie's statistical performance (saves, goals against, save percentage, etc.).

## Research Questions and Usage Scenarios

Jeremy is a fantasy hockey manager in a tight playoff game. He wants to add a goalie on Saturday night, and visits this app to identify his best options. He can see the expected fantasy points earned for the average goalie against all teams, and can filter for a specific opponent to see whether that matchup is favourable or not. He can also see which goalies are included in the visualization to check whether there are any differences in goalie quality. After examining different options, Jeremy determines that goalies who face the Chicago Blackhawks have the highest expected points, so he adds the goalie facing the Blackhawks on Saturday to his team.
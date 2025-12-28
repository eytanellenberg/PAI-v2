# Basketball — Calculations Overview (Public-data workflow)

## Unit of analysis
Calculations are conducted at the **possession** level, reconstructed from play-by-play.

For each possession we derive:
- game phase (quarter, clock)
- score differential
- on-court lineup
- terminal event (shot, turnover, foul/FT sequence, end of period)

## Exposure and opportunity (Role)
Player-level exposure and opportunity are summarized over selected time windows (match, segment, rolling):
- minutes played
- on-court possessions
- opportunity proxies: shot attempts, turnovers, free-throw involvement (when available)

Derived role indicators include usage-style proxies expressed per possession.

## Execution and efficiency
Efficiency is computed conditionally on opportunity, including:
- points per possession (or equivalent offensive contribution metric)
- shooting efficiency proxies (based on shot outcomes and shot types when available)
- turnover cost proxies (per possession)

## Context and constraints
Context variables are included to avoid misattribution:
- home/away
- score differential and game phase
- opponent strength proxies
- schedule/congestion proxies when available

## Outcome definition
Rather than raw box-score totals, outcomes reflect a **context-adjusted offensive contribution**
formulated at the possession level to separate opportunity-driven effects from execution effects.

## Attribution
Attribution is performed using a structured, domain-based approach that accounts for
both direct and indirect contributions across:
- availability/exposure
- opportunity/role
- execution/efficiency
- contextual constraints

Implementation details are intentionally abstracted at this stage.

"""
Domain maps group low-level features into coach-readable domains.

Keep this simple and editable. The novelty is not the mapping itself,
but the consistency across sports and the handling of indirect pathways.
"""

BASKET_DOMAIN_MAP = {
    "Availability/Exposure": ["minutes", "poss_on"],
    "Opportunity/Role": ["usage_proxy", "shot_share", "fta_share"],
    "Execution/Efficiency": ["ts_proxy", "efg_proxy", "tov_rate"],
    "Context/Constraints": ["home", "score_diff", "quarter"],
    "Lineup/Environment": ["lineup_strength_proxy", "on_off_proxy"],
}

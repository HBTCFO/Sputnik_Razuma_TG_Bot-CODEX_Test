from enum import StrEnum

class Topic(StrEnum):
    STRESS = "topic_stress"
    PRODUCTIVITY = "topic_productivity"
    RELATIONSHIPS = "topic_relationships"
    OTHER = "topic_other"
    CRISIS = "topic_crisis"

class Tech(StrEnum):
    T478 = "tech_478"
    PMR = "tech_pmr"
    GROUND = "tech_ground"
    JOURNAL = "tech_journal"
    CLOSE = "tech_close"
    WIPE = "wipe_ctx"

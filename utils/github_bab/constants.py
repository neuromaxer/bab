from enum import Enum
from typing import Final


class GithubMilestoneState(Enum):
    OPEN = "open"
    CLOSED = "closed"


BAB_CONTRIBUTOR_USERNAMES: Final[tuple[str, ...]] = (
    "ReznikovRoman",
    "neuromaxer",
    "dzxterity",
)

BAB_BASE_PROJECT_DEFAULT_COLUMN: Final[str] = "To Do"
BAB_BASE_PROJECT_COLUMN_NAMES: Final[tuple[str, ...]] = (
    "In Progress",
    "Waiting",
    "Done",
)
BAB_BASE_PROJECT_DEFAULT_CARD_CONTENT_TYPE: Final[str] = "Issue"

BAB_WEEKS_COUNT: Final[int] = 10

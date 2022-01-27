from __future__ import annotations

import datetime
from dataclasses import dataclass

from github.Milestone import Milestone

from constants import GithubMilestoneState


GithubUsername = str


@dataclass
class GithubMilestone:
    title: str = "Week #{week_id}"
    state: GithubMilestoneState | None = GithubMilestoneState.OPEN.value
    due_on: datetime.date | None = None


@dataclass
class GithubIssue:
    title: str = "{username}-{week_id}"
    body: str | None = ""
    assignee: GithubUsername | None = None
    milestone: Milestone | None = None


@dataclass
class GithubProject:
    name: str = "{username} board"

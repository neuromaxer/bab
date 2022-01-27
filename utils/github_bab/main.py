from __future__ import annotations

import logging
import time
from datetime import datetime, timedelta
from typing import TYPE_CHECKING

from bab_types import GithubIssue, GithubMilestone, GithubProject
from client import bab_repo
from constants import (
    BAB_BASE_PROJECT_COLUMN_NAMES, BAB_BASE_PROJECT_DEFAULT_CARD_CONTENT_TYPE, BAB_BASE_PROJECT_DEFAULT_COLUMN,
    BAB_CONTRIBUTOR_USERNAMES, BAB_WEEKS_COUNT,
)


if TYPE_CHECKING:
    from github.Issue import Issue
    from github.Milestone import Milestone
    from github.ProjectCard import ProjectCard
    from github.ProjectColumn import ProjectColumn


log = logging.getLogger(__name__)


class GithubBabService:

    def __init__(self):
        self.repo = bab_repo

    def _create_milestone(self, milestone_data: GithubMilestone) -> Milestone:
        return self.repo.create_milestone(
            title=milestone_data.title,
            state=milestone_data.state,
            due_on=milestone_data.due_on,
        )

    def _create_issue(self, issue_data: GithubIssue) -> Issue:
        return self.repo.create_issue(
            title=issue_data.title,
            body=issue_data.body,
            assignee=issue_data.assignee,
            milestone=issue_data.milestone,
        )

    def _create_project(self, project_data: GithubProject) -> ProjectColumn:
        project = self.repo.create_project(
            name=project_data.name,
        )
        default_column = project.create_column(name=BAB_BASE_PROJECT_DEFAULT_COLUMN)
        for column_name in BAB_BASE_PROJECT_COLUMN_NAMES:
            project.create_column(name=column_name)
        return default_column

    @staticmethod
    def _create_project_card(column: ProjectColumn, issue_id: int | str) -> ProjectCard:
        return column.create_card(
            content_id=issue_id,
            content_type=BAB_BASE_PROJECT_DEFAULT_CARD_CONTENT_TYPE,
        )

    def _process_user_issues(
        self,
        due_on_date: datetime.date,
        user_project_default_column: ProjectColumn,
        username: str,
        week_id: str | int,
    ) -> None:
        milestone = self._create_milestone(
            milestone_data=GithubMilestone(
                title=f"{username}: Week №{week_id}",
                due_on=due_on_date,
            ),
        )
        issue = self._create_issue(
            issue_data=GithubIssue(
                title=f"BaB Task: {username}-{week_id}",
                body=(
                    f"Finish fundamental lecture №{week_id}, dev lecture №{week_id}, homework №{week_id}"
                ),
                assignee=username,
                milestone=milestone,
            ),
        )
        GithubBabService._create_project_card(
            column=user_project_default_column,
            issue_id=issue.id,
        )

    def process_user(self, username) -> None:
        user_project_default_column = self._create_project(
            project_data=GithubProject(name=f"{username} board"),
        )
        due_on_date = datetime.date(datetime.now())
        log.debug("Create milestones and issues")
        for week_id in range(1, BAB_WEEKS_COUNT + 1):
            due_on_date += timedelta(days=7)
            self._process_user_issues(due_on_date, user_project_default_column, username, week_id)

    def execute(self):
        for username in BAB_CONTRIBUTOR_USERNAMES:
            log.debug(f"Process user: {username}")
            self.process_user(username)
            log.debug(f"Finished processing user: {username}")
            time.sleep(5)
            log.debug("Sleep 5 seconds to avoid hitting the rate limits.")


if __name__ == "__main__":
    bab_service = GithubBabService()
    bab_service.execute()

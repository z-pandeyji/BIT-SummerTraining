import unittest
from pathlib import Path


class AssignmentWorkflowTests(unittest.TestCase):
    def test_workflow_uses_the_trusted_base_validator(self):
        workflow = (
            Path(__file__).parents[1]
            / ".github"
            / "workflows"
            / "validate-assignment-pr.yml"
        ).read_text(encoding="utf-8")

        self.assertIn("pull_request:", workflow)
        self.assertNotIn("pull_request_target:", workflow)
        self.assertIn("permissions:\n  contents: read\n  pull-requests: read", workflow)
        self.assertIn("github.event.pull_request.base.sha", workflow)
        self.assertIn("path: trusted-validator", workflow)
        self.assertIn("gh api --paginate", workflow)
        self.assertIn("trusted-validator/scripts/validate_assignment_pr.py", workflow)

    def test_workflow_compiles_solutions_without_executing_them(self):
        workflow = (
            Path(__file__).parents[1]
            / ".github"
            / "workflows"
            / "validate-assignment-pr.yml"
        ).read_text(encoding="utf-8")

        self.assertIn("python3 -m py_compile", workflow)
        self.assertNotIn('python3 \"$solution\"', workflow)

    def test_workflow_allows_only_the_repository_owner_to_bootstrap_validator(self):
        workflow = (
            Path(__file__).parents[1]
            / ".github"
            / "workflows"
            / "validate-assignment-pr.yml"
        ).read_text(encoding="utf-8")

        self.assertIn("HEAD_REPOSITORY", workflow)
        self.assertIn("REPOSITORY_OWNER", workflow)
        self.assertIn('"${GITHUB_ACTOR}" == "${REPOSITORY_OWNER}"', workflow)
        self.assertIn("submission/scripts/validate_assignment_pr.py", workflow)
        self.assertIn('python3 "${validator}"', workflow)

    def test_workflow_allows_owner_only_non_assignment_maintenance(self):
        workflow = (
            Path(__file__).parents[1]
            / ".github"
            / "workflows"
            / "validate-assignment-pr.yml"
        ).read_text(encoding="utf-8")

        self.assertIn('grep -q "^assignments/"', workflow)
        self.assertIn("Owner-authored maintenance pull request", workflow)
        self.assertIn('"${HEAD_REPOSITORY}" == "${GITHUB_REPOSITORY}"', workflow)
        self.assertIn('"${GITHUB_ACTOR}" == "${REPOSITORY_OWNER}"', workflow)


if __name__ == "__main__":
    unittest.main()

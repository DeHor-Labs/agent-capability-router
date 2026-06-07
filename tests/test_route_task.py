from pathlib import Path
import json
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"


def parse_fixture(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    user_line = next(line for line in text.splitlines() if line.startswith("User: "))
    expected_line = next(line for line in text.splitlines() if line.startswith("Expected route: "))
    return user_line.removeprefix("User: "), expected_line.removeprefix("Expected route: ")


class RouteTaskTests(unittest.TestCase):
    def route(self, task: str) -> dict:
        result = subprocess.run(
            [str(ROOT / "scripts" / "route-task.py"), task],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return json.loads(result.stdout)

    def test_fixtures_classify_expected_primary_routes(self) -> None:
        for fixture in FIXTURES.glob("*.md"):
            with self.subTest(fixture=fixture.name):
                task, expected = parse_fixture(fixture)
                result = self.route(task)
                self.assertEqual(result["primary"], None if expected == "none" else expected)

    def test_external_routes_carry_risk_metadata(self) -> None:
        result = self.route("Which plugin should check the GitHub deployment status?")
        self.assertEqual(result["primary"], "tool-plugin-skill-routing")
        self.assertEqual(result["risk_class"], "authenticated_read")
        self.assertTrue(result["approval_required"])


if __name__ == "__main__":
    unittest.main()

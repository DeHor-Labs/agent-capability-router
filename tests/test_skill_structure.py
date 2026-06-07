from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "agent-capability-router"


class SkillStructureTests(unittest.TestCase):
    def run_script(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [str(ROOT / "scripts" / args[0]), *args[1:]],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )

    def test_validate_skill(self) -> None:
        result = self.run_script("validate-skill.py")
        self.assertIn("OK: skill structure is valid", result.stdout)

    def test_agent_neutrality(self) -> None:
        result = self.run_script("check-agent-neutrality.py")
        self.assertIn("OK: main skill is runtime-neutral", result.stdout)

    def test_install_copy_to_codex_and_claude(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.run_script("install-skill.sh", "--runtime", "both", "--mode", "copy", "--home", tmp, "--confirm")
            codex_skill = Path(tmp) / ".codex" / "skills" / SKILL_NAME / "SKILL.md"
            claude_skill = Path(tmp) / ".claude" / "skills" / SKILL_NAME / "SKILL.md"
            self.assertTrue(codex_skill.is_file())
            self.assertTrue(claude_skill.is_file())

    def test_install_symlink_to_codex(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.run_script(
                "install-skill.sh",
                "--runtime",
                "codex",
                "--mode",
                "symlink",
                "--home",
                tmp,
                "--dev-symlink",
                "--confirm",
            )
            codex_skill = Path(tmp) / ".codex" / "skills" / SKILL_NAME
            self.assertTrue(codex_skill.is_symlink())

    def test_install_requires_runtime_and_confirm(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing_runtime = subprocess.run(
                [str(ROOT / "scripts" / "install-skill.sh"), "--home", tmp, "--confirm"],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.assertNotEqual(missing_runtime.returncode, 0)

            missing_confirm = subprocess.run(
                [str(ROOT / "scripts" / "install-skill.sh"), "--runtime", "codex", "--home", tmp],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.assertNotEqual(missing_confirm.returncode, 0)

    def test_route_task_cli(self) -> None:
        result = self.run_script(
            "route-task.py",
            "Audit all API routes with your team and verify CI findings",
        )
        self.assertIn('"orchestration"', result.stdout)
        self.assertIn('"verification-routing"', result.stdout)


if __name__ == "__main__":
    unittest.main()

from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


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
            self.run_script("install-skill.sh", "--runtime", "both", "--mode", "copy", "--home", tmp)
            codex_skill = Path(tmp) / ".codex" / "skills" / "agent-opportunity-scout" / "SKILL.md"
            claude_skill = Path(tmp) / ".claude" / "skills" / "agent-opportunity-scout" / "SKILL.md"
            self.assertTrue(codex_skill.is_file())
            self.assertTrue(claude_skill.is_file())

    def test_install_symlink_to_codex(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.run_script("install-skill.sh", "--runtime", "codex", "--mode", "symlink", "--home", tmp)
            codex_skill = Path(tmp) / ".codex" / "skills" / "agent-opportunity-scout"
            self.assertTrue(codex_skill.is_symlink())


if __name__ == "__main__":
    unittest.main()

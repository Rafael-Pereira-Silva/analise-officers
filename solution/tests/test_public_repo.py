"""Guarda do repositório público: nenhum texto do projeto pode carregar o contexto original.

Varre os arquivos de texto (`.md`, `.py`, `.js`, `.html`, `.css`) e falha se aparecer um dos termos proibidos.
Ficam de fora `solution/tools/vendor/` (bibliotecas de terceiros) e os dados brutos. Os termos são montados
aos pedaços para que este arquivo não os contenha por extenso.
"""

import re

import pytest

from scorer import config

# Termos proibidos (sem diferenciar maiúsculas), montados aos pedaços.
INSENSITIVE = [
    "gest" + "[aã]o" + r"[\s-]+" + "qua" + "tro",
    "ai" + r"[\s-]+" + "mas" + "ter",
    "g" + "4" + "business",
    "processo " + "seletivo",
    "va" + "ga",
    "candi" + "dat",
    "ban" + "ca",
    "sub" + "miss",
    "chal" + "lenge",
    "b" + "s2",
]
# Esse termo curto só conta como palavra inteira e em maiúsculas: ids de deal do dataset (ex.: "G4F8W039") não valem.
SENSITIVE = [r"\b" + "G" + "4" + r"\b"]

EXTENSIONS = {".md", ".py", ".js", ".html", ".css"}
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", "node_modules"}
RAW_DIR = config.RAW_DIR.resolve()
VENDOR_DIR = (config.SOLUTION_DIR / "tools" / "vendor").resolve()
PROCESSED_DIR = (config.SOLUTION_DIR / "data" / "processed").resolve()

PATTERN = re.compile("|".join(INSENSITIVE), re.IGNORECASE)
PATTERN_CASE = re.compile("|".join(SENSITIVE))


def text_files():
    for path in sorted(config.PROJECT_DIR.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(config.PROJECT_DIR).parts):
            continue
        resolved = path.resolve()
        if VENDOR_DIR in resolved.parents or RAW_DIR in resolved.parents or PROCESSED_DIR in resolved.parents:
            continue
        yield path


def find_terms(text: str) -> list[str]:
    return sorted({m.group(0) for m in PATTERN.finditer(text)} | {m.group(0) for m in PATTERN_CASE.finditer(text)})


def test_no_file_of_the_repository_carries_the_original_context():
    offenders = {}
    for path in text_files():
        found = find_terms(path.read_text(encoding="utf-8", errors="replace"))
        if found:
            offenders[str(path.relative_to(config.PROJECT_DIR))] = found
    report = "\n".join(f"{name}: {terms}" for name, terms in offenders.items())
    assert not offenders, f"termos proibidos em arquivos de texto:\n{report}"


def test_the_guard_scans_the_expected_files():
    names = {p.name for p in text_files()}
    assert {"README.md", "CLAUDE.md", "app.js", "style.css", "index.html", "build.py", "DECISIONS.md"} <= names
    assert "axe.min.js" not in names  # vendor fica de fora


@pytest.mark.parametrize("text", [
    "gest" + "ão qua" + "tro", "AI " + "Master", "ai-" + "master-chal" + "lenge", "g4" + "business.com", "Processo " + "Seletivo",
    "uma va" + "ga", "o candi" + "dato", "a ban" + "ca", "Sub" + "missão", "Chal" + "lenge 003", "o G" + "4 pediu", "Banco B" + "S2", "banco" + "b" + "s2.com.br",
])
def test_the_guard_detects_each_forbidden_term(text):
    assert find_terms(text), text


@pytest.mark.parametrize("text", ["G4F8W039", "JUCNIG4H", "UA8AWDG4", "um lead de alta prioridade"])
def test_the_guard_ignores_deal_ids_and_ordinary_text(text):
    assert find_terms(text) == []

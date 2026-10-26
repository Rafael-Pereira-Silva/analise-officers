"""O README segue a estrutura de projeto e os documentos estão coerentes.

Estrutura (títulos na ordem, resumo executivo curto, aviso e nota obrigatórios) e links relativos que existem.
Os números do README e do MODEL_CARD são conferidos em `test_docs_numbers.py`.
"""

import re

import pytest

from scorer import config, docs

README = config.PROJECT_DIR / "README.md"
MODEL_CARD = config.DOCS_DIR / "MODEL_CARD.md"
PROCESS_LOG = config.PROJECT_DIR / "process-log"
SCREENSHOTS = ["final_inicio_1280.png", "final_inicio_390.png"]
BASE_URL = "https://rafael-pereira-silva.github.io/analise-officers/solution/app/"

NOTICE = (
    "Projeto pessoal de demonstração com dados públicos e fictícios (dataset CRM Sales Predictive Analytics, "
    "Kaggle, CC0). Não é um produto, serviço ou canal do Banco BS2 e não usa dados do banco."
)
NOTE = (
    "Esta versão pública reorganiza a documentação do experimento original; métodos, números, decisões e erros "
    "registrados são os mesmos."
)

TITLES_IN_ORDER = [
    "# Análise Officers — Lead Scorer: priorização de pipeline com frescor do deal",
    "## Resumo executivo",
    "## Experimente",
    "## Como rodar",
    "## Abordagem",
    "## Resultados",
    "## Recomendações",
    "## Limitações",
    "## Como usei IA",
    "### Ferramentas usadas",
    "### Workflow",
    "### Onde a IA errou e como corrigi",
    "### O que eu adicionei que a IA sozinha não faria",
    "## Reaproveitamento em outros contextos",
    "## Evidências",
    "## Sobre o autor",
]
SENTENCE_END = re.compile(r"[.!?](\s|$)")
LINK = re.compile(r"\]\(([^)\s]+)\)")


@pytest.fixture(scope="module")
def text():
    return docs.read_doc(README)


def section(text: str, title: str) -> str:
    """Texto entre o título e o próximo título de qualquer nível (ou separador ---)."""
    start = text.index(f"\n{title}\n") + len(title) + 2
    end = re.search(r"\n(#{1,6} |---\n)", text[start:])
    return text[start : start + end.start()] if end else text[start:]


def test_titles_appear_once_and_in_order(text):
    positions = []
    for title in TITLES_IN_ORDER:
        assert text.count(f"\n{title}\n") + (1 if text.startswith(title + "\n") else 0) == 1, f"título ausente ou repetido: {title}"
        positions.append(text.index(title))
    assert positions == sorted(positions)


def test_separators_between_the_main_sections(text):
    assert text.count("\n---\n") >= 8


def test_notice_and_note_come_right_after_the_title(text):
    head = "\n".join(text.splitlines()[:8])
    assert f"> {NOTICE}" in head
    assert f"> {NOTE}" in head


def test_the_process_log_index_opens_with_the_note():
    first = (PROCESS_LOG / "README.md").read_text(encoding="utf-8").lstrip().splitlines()[0]
    assert first == f"> {NOTE}"


def test_the_bank_is_only_named_in_the_notice_and_in_the_palette_explanation(text):
    for line in text.splitlines():
        if "BS2" in line:
            assert line == f"> {NOTICE}" or "paleta" in line, line[:100]


def test_executive_summary_has_at_most_five_sentences(text):
    summary = section(text, "## Resumo executivo").strip()
    sentences = len(SENTENCE_END.findall(summary))
    assert 3 <= sentences <= 5, f"o resumo tem {sentences} frases"


def test_executive_summary_opens_with_the_finding_and_closes_with_the_recommendation(text):
    summary = section(text, "## Resumo executivo").strip()
    assert "experimento com Claude Code" in summary.split(".")[0]
    assert "frescor" in summary.split(".")[0]
    assert "US$ 3,6 mi" in summary  # a lista Limpe de hoje, com a curva v2 (antes da correção: US$ 3,2 mi)
    assert "depois do backtest" in summary  # a troca de curva é declarada no resumo
    assert summary.rstrip().split(". ")[-1].startswith("Recomendo")


def test_the_scenario_is_declared_as_hypothetical(text):
    intro = "\n".join(text.splitlines()[:8])
    assert "experimento pessoal" in intro and "Claude Code" in intro
    assert "cenário hipotético" in intro


def test_about_the_author_has_linkedin(text):
    about = section(text, "## Sobre o autor")
    assert "https://www.linkedin.com/in/rafael-pereira-30122003-" in about
    assert "Rafael Pereira" in about


def test_try_it_has_the_published_page_and_both_profile_links(text):
    try_it = section(text, "## Experimente")
    assert BASE_URL in try_it
    assert f"{BASE_URL}#perfil=vendedor&nome=Rosalina+Dieter" in try_it
    assert f"{BASE_URL}#perfil=manager&nome=Celia+Rouche" in try_it
    assert "solution/app/index.html" in try_it


def test_added_value_section_is_final_and_ties_to_governance(text):
    added = section(text, "### O que eu adicionei que a IA sozinha não faria")
    assert "[RASCUNHO" not in added  # revisado pelo Rafael no bloco 7
    for needle in ["governança", "não automatizar"]:
        assert needle in added, needle


def test_ai_errors_are_labelled_by_origin(text):
    errors = section(text, "### Onde a IA errou e como corrigi")
    bullets = [b for b in errors.split("\n- ")[1:]]
    assert len(bullets) >= 8
    for bullet in bullets:
        head = bullet.split("\n")[0]
        assert "(fase 0, com Rafael)" in head or "(execução delegada)" in head, head[:80]


def test_evidence_map_exists_and_the_full_chat_export_is_not_shipped():
    for name in ["README.md", "07_revisao-do-rafael.md", "chat-exports/LEIA-ME.md", "10_versao-adaptada.md"]:
        assert (PROCESS_LOG / name).exists(), name
    assert not list((PROCESS_LOG / "chat-exports").glob("sessao-*")), "o export integral não entra nesta versão pública"


def test_tools_table_and_evidence_list_exist(text):
    tools = section(text, "### Ferramentas usadas")
    assert "| Ferramenta | Para que usou |" in tools
    for needle in ["Opus 5.5", "Sonnet", "Haiku", "contexto limpo"]:
        assert needle in tools
    evidence = section(text, "## Evidências")
    assert evidence.count("\n- ") >= 5
    assert "chat-exports" in evidence and "LEIA-ME" in evidence


def test_required_limitations_are_stated(text):
    limits = section(text, "## Limitações")
    for needle in ["16:28 e 19:01", "dulwich", "chat-exports", "experiência, não de segurança"]:
        assert needle in limits, needle


def test_reuse_section_separates_what_travels_from_what_does_not(text):
    reuse = section(text, "## Reaproveitamento em outros contextos")
    for needle in ["validação no tempo", "model card", "não pontuar pessoas", "listas de ação", "visões por perfil",
                   "segregação por papel", "não é reaproveitável", "sintético", "piloto em 2 passos",
                   "histórico real de CRM", "controle"]:
        assert needle.lower() in reuse.lower(), needle


def test_workflow_has_one_item_per_block_from_0_to_6(text):
    flow = section(text, "### Workflow")
    for n in range(7):
        assert re.search(rf"^{n}\. ", flow, re.M), f"falta o item {n}"


def test_setup_has_the_commands(text):
    setup = section(text, "## Como rodar")
    for cmd in ["pip install -r requirements.txt", "python -m pytest", "python -m scorer.build --reference-date 2017-12-31",
                "pip install -r requirements-dev.txt", "python tools/check_app.py --prefix final"]:
        assert cmd in setup, cmd


def test_auto_blocks_of_the_readme_exist(text):
    for name in ["readme-achados", "readme-backtest", "readme-hoje"]:
        assert f"<!-- AUTO:{name} -->" in text and name in docs.BLOCKS
        assert f"<!-- /AUTO:{name} -->" in text


def test_model_card_has_the_required_sections():
    card = docs.read_doc(MODEL_CARD).replace("**", "")
    for needle in ["Propósito e uso pretendido", "Uso NÃO pretendido", "Dados e período", "Desempenho", "Limitações",
                   "Riscos e mitigação", "Quando recalibrar", "Dono e revisão", "<!-- AUTO:mc-desempenho -->",
                   "<!-- AUTO:mc-recalibracao -->", "Limpe significa confirmar"]:
        assert needle in card, needle
    for banned in ["avaliar ou ranquear vendedores", "forecast financeiro", "encerrar deals automaticamente"]:
        assert banned in card.lower().replace("**", "")


def test_readme_and_model_card_are_covered_by_the_number_check():
    names = {p.name for p in config.COVERED_DOCS}
    assert {"README.md", "MODEL_CARD.md"} <= names


def relative_links(text: str) -> list[str]:
    plain = re.sub(r"```.*?```", "", text, flags=re.S)
    found = [m.group(1) for m in LINK.finditer(plain)]
    return [link.split("#")[0] for link in found if not link.startswith(("http://", "https://", "mailto:"))]


@pytest.mark.parametrize("path", [README, MODEL_CARD, PROCESS_LOG / "README.md", PROCESS_LOG / "07_revisao-do-rafael.md",
                                   PROCESS_LOG / "chat-exports" / "LEIA-ME.md"], ids=lambda p: p.name)
def test_relative_links_point_to_existing_files(path):
    base = path.parent
    missing = []
    for link in relative_links(docs.read_doc(path)):
        if link.endswith(tuple(SCREENSHOTS)):
            continue  # os screenshots têm teste próprio (são gerados no fim do bloco 4)
        if link and not (base / link).exists():
            missing.append(link)
    assert not missing, f"links quebrados em {path.name}: {missing}"


@pytest.mark.parametrize("name", SCREENSHOTS)
def test_screenshot_files_linked_by_the_readme_exist(name, text):
    assert f"process-log/screenshots/{name}" in text
    assert (config.PROJECT_DIR / "process-log" / "screenshots" / name).exists(), (
        f"{name} ainda não existe: rode `python tools/check_app.py --prefix final`"
    )

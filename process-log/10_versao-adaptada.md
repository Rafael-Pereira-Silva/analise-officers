# Versão pública: o que mudou e por quê

**Executor:** Claude Sonnet (subagente executor), a pedido do Rafael. **Data:** 26/10/2026.

> Esta versão pública reorganiza a documentação do experimento original; métodos, números, decisões e erros registrados são os mesmos.

## Objetivo

Transformar uma cópia do projeto num repositório público autônomo (`analise-officers`), sem referências ao contexto em que o trabalho nasceu: o enquadramento de entrega, os termos de avaliação externa e os passos de publicação do repositório original. O projeto passa a ser apresentado como o que é: um experimento pessoal para testar o Claude Code num problema real de ponta a ponta, sobre um cenário hipotético de RevOps. O original continua intacto numa pasta separada.

## O que mudou

- **README reescrito** como README de projeto: título, aviso de projeto de demonstração, nota desta versão, resumo executivo (até 5 frases), "Experimente" (página publicada e links por visão), "Como rodar", abordagem, resultados, recomendações, limitações, "Como usei IA", a seção nova "Reaproveitamento em outros contextos", evidências e "Sobre o autor". Os blocos AUTO e todos os números são os mesmos e continuam conferidos por teste.
- **Itens que só faziam sentido no formato de entrega original foram removidos** do README: data de envio, checklist do modelo de README, instruções de publicação do repositório original e a seção sobre o Pages desse repositório.
- **Kit** (`CLAUDE.md`, `PROMPTS.md`, `GUIA.md`, `PROMPT_AUTONOMO.md`, `PROMPT_VISOES_E_DESIGN.md`): o contexto foi trocado (avaliação externa vira "revisor independente"; o cenário vira "experimento"; os passos de publicação do repositório original viram "publicar no repositório"; o caminho da pasta original vira a raiz do repositório).
- **Logs e documentos** (`docs/*.md`, exceto `DESIGN.md`, e `process-log/*.md`, exceto `09_tema-azul.md`): mesma troca de contexto. O avaliador das revisões independentes passou a "revisor independente"; o restante do texto das revisões foi mantido. Nos registros de ferramentas, nomes de pastas e URLs foram generalizados (por exemplo, "pasta do projeto"). A identidade visual da primeira versão (marinho e dourado) passou a ser descrita como substituída pelo tema atual, com remissão a `process-log/09_tema-azul.md`.
- **`plano_execucao_opus.md`** é um artefato gerado: só as referências de contexto foram generalizadas e uma nota no topo diz isso.
- **Código e testes:** a constante de configuração com o nome do contexto original virou `PROJECT_DIR` (`scorer/config.py` e testes). `tests/test_readme.py` foi reescrito para a nova estrutura sem afrouxar: resumo de até 5 frases, aviso e nota presentes, links relativos existentes, comandos de setup, LinkedIn, blocos AUTO, seções do model card. Novo `tests/test_public_repo.py`: teste de guarda que varre os arquivos de texto do repositório e falha se o contexto original reaparecer.
- **Arquivos de projeto:** `LICENSE` (MIT para o código, com a nota de dados CC0 e fontes OFL) e `.gitignore`.
- **Linhas no `DECISIONS.md`** com o marcador "(versão adaptada)".

## O que foi retirado

- `process-log/chat-exports/sessao-orquestracao-claude-code.md`, o export integral da conversa de orquestração. Editar as falas do Rafael nele alteraria a evidência, então o arquivo inteiro não entra nesta versão. O export existe no projeto original. `chat-exports/LEIA-ME.md` foi reescrito para dizer isso, e os links que apontavam para o export foram ajustados.

## Regra de honestidade aplicada

- Nenhum episódio foi inventado nem apagado. Os logs registram o que aconteceu; só o contexto foi trocado.
- Nenhuma motivação foi acrescentada: o texto descreve o trabalho e o método.
- O que é do Rafael continua atribuído a ele: a fase 0, o kit, as mensagens e a revisão da curva.
- A nota acima está no README e no topo de `process-log/README.md`, e o aviso de projeto de demonstração está no topo do README.(ver a seção "Remoção das referências ao banco" no fim)
- Desvios pequenos, declarados: a fase 0 conta que o Claude leu "4 problemas em consideração" e a escolha é descrita como a escolha do problema para o experimento; em `00_bloco-0.md`, a URL e o nome do repositório-base do clone não constam; o texto de saídas literais de ferramentas ("FORA da pasta do projeto: nada") reflete essa generalização.

## Verificação

Rodada com cwd em `solution/`, depois da última edição de texto (ver a seção de resultado no relatório da execução):

- `python -B -m scorer.build --reference-date 2017-12-31`: exit 0 (blocos AUTO sem mudanças).
- `python -B -m scorer.docs --check`: exit 0.
- `python -B -m pytest -p no:cacheprovider`: ver o resultado final abaixo.
- Busca final pelos termos proibidos (os mesmos do teste de guarda), fora de `solution/tools/vendor/` e dos dados brutos: ver o resultado final abaixo.

**Resultado (26/10/2026, última rodada):**

- Build: exit 0.
- `scorer.docs --check`: exit 0.
- Testes: todos os testes do projeto passam, exceto dois, que dependem de arquivos de outro executor que ainda estava trabalhando no tema visual: o teste de guarda aponta `docs/DESIGN.md` (ainda cita a referência visual original) e o teste de links do README aponta `process-log/09_tema-azul.md` (ainda não escrito). Nenhum deles aponta arquivo desta adaptação.
- Busca final pelos termos proibidos: nenhuma ocorrência fora de `docs/DESIGN.md`.

## Verificação final (orquestrador, Claude Opus 5.5)

Depois que o executor do tema terminou, o orquestrador repetiu a verificação do zero na cópia. Primeiro apagou `data.js`, os briefs e os snapshots; depois rodou, com cwd `solution/`:

- `python -m scorer.build --reference-date 2017-12-31`: exit 0.
- `python -m pytest`: 255 testes passando, incluindo o teste de guarda `test_public_repo.py` e o `test_readme.py`. As duas falhas descritas acima foram resolvidas quando o `DESIGN.md` foi reescrito e o log 09 passou a existir.
- `python -m scorer.docs --check`: exit 0.
- `python tools/check_app.py --prefix final` e `python tools/check_views.py`, com axe nos dois temas: os dois passaram.

Buscas no repositório inteiro, fora de vendor e dos dados brutos:
- termos do contexto anterior: nenhuma ocorrência, além da lista de termos dentro do próprio teste de guarda;
- e-mails pessoais: nenhum;
- o nome do banco: removido depois, ver a seção "Remoção das referências ao banco".

## Remoção das referências ao banco

O Rafael pediu que nenhuma menção ao banco que inspirou a paleta ficasse no repositório, porque o público já sabe que o projeto não envolve dados do banco. O que foi feito:

- O aviso do README e o rodapé da página passaram a dizer apenas: "Projeto pessoal de demonstração com dados públicos e fictícios (dataset CRM Sales Predictive Analytics, Kaggle, CC0)."
- O log do tema e a pasta de screenshots do tema, que traziam o nome do banco, viraram `process-log/09_tema-azul.md` e `process-log/screenshots/tema-azul/`. Links e referências (README, `process-log/README.md`, DECISIONS, `design_shots.py`, testes) foram atualizados.
- A origem da paleta não é mais citada: o tema é descrito só como "tema azul" (azul `#0021AF`, Poppins, botões em pílula). A regra de não parecer canal oficial ficou na versão neutra: sem logotipo, sem marca de terceiros, nada que lembre login, e deixar claro que é demonstração.
- `check_aviso_demo` confere o texto novo do rodapé e a ausência do nome do banco na página; `test_readme.py` exige nenhuma menção a ele; `test_public_repo.py` passou a proibir o nome (sem diferenciar maiúsculas), fora de vendor, dados brutos e `data/processed`.
- Os screenshots finais do tema foram regenerados com o rodapé novo.
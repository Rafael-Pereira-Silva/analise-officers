# Guia de execução — Rafael

Roteiro para executar o experimento do Lead Scorer em cerca de 5h30, dividido em 8 blocos. Cada bloco tem um prompt pronto em `PROMPTS.md`.

## Como funciona
- **Claude Code executa.** Você decide nos checkpoints e registra as decisões.
- **O contexto mora em arquivos, não na conversa.** O `CLAUDE.md` guarda as regras e as decisões; `docs/` guarda o conteúdo. Cada bloco começa numa conversa limpa.
- **O process log se monta enquanto você trabalha:** um commit por bloco, `DECISIONS.md`, um `process-log/NN_bloco-N.md` por bloco e um `/export` de cada sessão. Não deixe para reconstruir no final.

## Pré-requisitos (uma vez)
- Conta no GitHub, Git e Python 3.11+ instalados.
- Claude Code instalado e logado.
- Opcional: GitHub CLI (`gh auth login`), que permite ao Claude conferir a página publicada.

## Passo 0 — Montar o projeto (~10 min, manual)
No terminal (PowerShell ou Git Bash):

```bash
# 1. Crie um repositório vazio no GitHub (ex.: analise-officers) e clone
git clone https://github.com/SEU-USUARIO/analise-officers.git
cd analise-officers
```

Depois:
1. Copie **todo o conteúdo desta pasta do kit** (`CLAUDE.md`, `PROMPTS.md`, `GUIA.md`, `docs/`, `process-log/`) para a raiz do repositório.
2. Copie os 4 CSVs (`accounts`, `products`, `sales_teams`, `sales_pipeline`) da sua pasta do Kaggle para `solution/data/raw/`. A licença é CC0, então pode versionar.
3. Abra o Claude Code **na raiz do repositório** e cole o prompt do Bloco 0.

> ⚠️ **Armadilha nº 1:** confira com `git status`, no primeiro commit, que o que você espera entrou (CSVs brutos, `docs/`, `process-log/`) e que nada de ambiente (`.venv`, `__pycache__`) foi junto.

## Ritmo por bloco
1. Abra uma sessão nova (ou rode `/clear`) e cole o prompt do bloco.
2. Nos blocos 3 e 4, use o Plan Mode e tire um print do plano.
3. No checkpoint, **leia de verdade e corrija algo quando fizer sentido.** Cada correção sua é a evidência mais valiosa do log.
4. No fim: `/export` → `process-log/chat-exports/bloco-N.txt` e confira se o commit saiu.

## Onde o seu julgamento entra (o que diferencia de uma entrega de IA sem supervisão)

| Bloco | Sua decisão | Tempo |
|---|---|---|
| 0 Setup | Conferir se os números reproduzem | 10 min |
| 1 Escopo | Responder às 4 perguntas abertas; validar o "fora do escopo" | 40 min |
| 2 Curadoria | Aprovar o tratamento do Q1/2017, dos deals sem conta e dos vendedores sem deals | 1h |
| 3 Scoring | Questionar o backtest e pedir checagem de vazamento; aprovar limiares | 1h30 |
| 4 Produto | Usar a ferramenta como vendedor por 5 min e pedir 3 correções | 1h30 |
| 5 Docs | Reescrever com sua voz "O que eu adicionei" | 45 min |
| 6 Revisão | Decidir quais críticas do revisor independente corrigir | 20 min |
| 7 Publicação | Ativar o GitHub Pages e conferir o link | 15 min |

## Process log — o que juntar
- [ ] **Esta conversa (fase 0):** export ou screenshots das partes em que escolhemos o problema do experimento, achamos o problema do "GTXPro", descobrimos que os atributos não preveem e validamos o frescor. Salve em `process-log/screenshots/fase0-*` ou `chat-exports/`. O resumo escrito já está em `process-log/00_fase0_exploracao.md`.
- [ ] `/export` de cada sessão do Claude Code.
- [ ] Prints dos planos (Plan Mode) dos blocos 3 e 4.
- [ ] Screenshots da ferramenta (gerados no Bloco 4).
- [ ] Histórico do git com 1 commit por bloco ou mais.
- [ ] `DECISIONS.md` preenchido.
- [ ] Opcional: um vídeo de 2 minutos usando a ferramenta como vendedor (Loom). Ajuda quem for rever o trabalho.

## O que já temos de "IA errou / eu corrigi" (use no README)
1. **Join quebrado:** "GTXPro" vs. "GTX Pro" faria o produto mais vendido sumir (1.480 deals). Pego na checagem de integridade.
2. **Métrica inflada:** o AUC por target encoding calculado dentro da própria amostra é otimista. Foi marcado como não confiável, e por isso exigimos backtest temporal.
3. **A primeira ideia de score (win rate por atributos) não funciona:** os dados mostraram efeito quase nulo. Pivotamos para o frescor.
4. **O corte em 138 dias é suspeito** (provável artefato de dado sintético). Decidimos não usá-lo como regra fixa.
5. **O download pelo conector do Kaggle foi bloqueado** pela rede do ambiente. Contornamos usando os arquivos locais, sem burlar o bloqueio.

## Armadilhas
- O GitHub Pages serve a partir da branch; a página fica em `https://SEU-USUARIO.github.io/analise-officers/solution/app/`.
- Use `data.js` em vez de `fetch('data.json')`, porque `fetch` não funciona em duplo-clique (file://).
- Não estoure o tempo polindo o visual.
- Não deixe o Claude escrever "onde a IA errou" de memória: tem que vir dos logs.

## Checklist final (antes de publicar)
- [ ] O link do GitHub Pages abre e funciona no celular.
- [ ] O duplo-clique em `index.html` funciona.
- [ ] `pytest` passa e `python -m scorer.build` regenera tudo do zero.
- [ ] O README segue a estrutura de projeto, com resumo executivo de até 5 frases.
- [ ] `SCORING.md` tem a tabela do backtest com os baselines.
- [ ] `MODEL_CARD.md` tem 1 página.
- [ ] O process log está completo (lista acima).
- [ ] `git status` limpo.

## Se travar
- **O Claude saiu do escopo:** "Pare. Releia CLAUDE.md e SCOPE.md e me diga o que está fora do escopo no que você fez."
- **O backtest não bate os baselines:** aceite e documente. Um resultado negativo explicado vale mais que um número maquiado. Volte ao briefing, seção 6.
- **Estourou o tempo:** corte nesta ordem: modo backtest na interface → brief por vendedor → visual. Nunca corte a validação nem o process log.

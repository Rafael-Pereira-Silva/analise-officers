# Projeto: Lead Scorer — experimento com Claude Code

Memória do projeto para o Claude Code. Leia este arquivo inteiro antes de qualquer tarefa.
Contexto detalhado e números da exploração inicial: `docs/briefing.md`.

## Missão
Construir uma ferramenta que um vendedor abre na segunda de manhã e sabe **onde focar, o que reativar e o que largar** no pipeline. Cada deal precisa vir com uma explicação em linguagem de vendedor. O software tem que rodar com os dados reais do dataset Kaggle "CRM Sales Predictive Analytics".

- **Usuário principal:** vendedor (não técnico), 30 ativos.
- **Usuário secundário:** manager (6), olhando a carteira do time.
- **Patrocinadora:** Head de RevOps. Pediu algo útil e funcionando, não ML perfeito.
- **Revisor independente:** um subagente de contexto limpo avalia a entrega contra critérios de qualidade e aponta o que pareceria uma entrega de IA sem supervisão; ser parecido com essa entrega não basta.

## Decisões já tomadas (não reabrir sem evidência nova; se reabrir, registrar em docs/DECISIONS.md)
1. **Arquitetura:** motor de scoring em Python (pandas, funções puras, pytest) que gera `solution/app/data.js` (`window.LEAD_DATA = {...}`). A interface é uma página estática em HTML, CSS e JS puro, sem build. Ela abre com duplo-clique (sem servidor; por isso data.js e não fetch de JSON) e é publicada no GitHub Pages. **Não usar Streamlit**, porque é o default de uma entrega de IA sem supervisão.
2. **Data de referência ("hoje")** = 2017-12-31, a data máxima do dataset. Ela é um parâmetro, nunca fixada no código.
3. **Tese do score:** o que separa os deals é o **frescor** (idade do deal comparada ao ciclo histórico), não os atributos. O score combina a probabilidade condicionada à idade e ao estágio com o valor do produto. Os atributos (setor, produto, porte da conta) só entram se o backtest temporal mostrar ganho real.
4. **O vendedor não entra como fator de score.** A diferença entre vendedores é compatível com ruído (qui-quadrado p=0,26) e usá-la penalizaria pessoas com base em ruído. O nome pode aparecer como contexto, nunca como penalidade.
5. **Listas de ação:** Foque (vivo e com alto valor esperado), Reative (bom, mas esfriando), Limpe (deal zumbi) e Qualifique (Prospecting, que não tem data).
6. **Validação** sempre fora da amostra e temporal: corte em uma data passada, desfecho posterior. Nunca reportar métrica in-sample como resultado.
7. **Idioma:** a interface e a documentação ficam em português (PT-BR). Nomes de colunas, contas e produtos ficam como no dataset.

## Fatos dos dados (verificados na fase 0, ver docs/briefing.md)
- 8.800 deals: 4.238 Won, 2.473 Lost, 1.589 Engaging e 500 Prospecting. Win rate dos fechados: 63,2%.
- "GTXPro" no pipeline equivale a "GTX Pro" no catálogo (sem corrigir, o join perde 1.480 linhas). O setor "technolgy" deve virar "technology".
- 1.425 deals sem `account`, **todos abertos**. Prospecting não tem `engage_date`.
- 35 vendedores no cadastro, mas só 30 têm deals.
- Produto, setor, região, manager, porte e idade da conta têm win rate entre ~60% e ~65%, sem sinal relevante.
- Nenhum deal fechado teve ciclo maior que 138 dias. 81% dos Engaging já passaram disso na data de referência.
- Snapshot em 30/09/2017: deals abertos com idade de até 30 dias tiveram 50% de vitória depois; acima de 90 dias, 0%.
- O corte duro em 138 dias provavelmente é um **artefato do gerador sintético**. Tratar como "nunca observado", e dizer isso nas limitações.

## Regras de trabalho
- Um bloco por vez (ver `PROMPTS.md`). Ao final de cada bloco: atualizar `docs/DECISIONS.md`, escrever `process-log/NN_bloco-N.md` e fazer um commit `bloco N: <resumo>`.
- `solution/data/raw/` é somente leitura. Toda limpeza acontece em código.
- Todo número citado na documentação ou na interface sai de um script reprodutível. Nada de número digitado à mão.
- Antes de afirmar que algo funciona, rode: testes, build e abertura da página.
- Quando eu (Rafael) corrigir uma decisão sua, registre em `process-log` na seção "Onde a IA errou", com o que você propôs, o que mudou e por quê.
- Pare e peça minha revisão nos checkpoints marcados nos prompts. Não avance de bloco sem confirmação.

## Git e publicação
- O repositório é autônomo: tudo fica na raiz (CLAUDE.md, README.md, docs/, solution/, process-log/).
- Um commit por bloco. Publicar no repositório é decisão do Rafael: não faça push sem ele pedir.

## Estrutura alvo
```
analise-officers/ (raiz do repositório)
├── CLAUDE.md
├── README.md                 ← README de projeto (bloco 5)
├── docs/
│   ├── briefing.md           ← contexto + achados da fase 0
│   ├── SCOPE.md              ← bloco 1
│   ├── DATA_QUALITY.md       ← bloco 2
│   ├── SCORING.md            ← bloco 3 (lógica + validação)
│   ├── MODEL_CARD.md         ← bloco 5
│   └── DECISIONS.md          ← log contínuo de decisões
├── solution/
│   ├── data/raw/             ← CSVs originais (CC0)
│   ├── data/processed/
│   ├── scorer/               ← pacote Python: clean, features, score, explain, validate, build
│   ├── tests/
│   ├── app/                  ← index.html, app.js, style.css, data.js (gerado)
│   ├── briefs/               ← brief de segunda-feira por vendedor (gerado)
│   └── requirements.txt
└── process-log/
    ├── 00_fase0_exploracao.md
    ├── scripts/
    ├── chat-exports/
    └── screenshots/
```

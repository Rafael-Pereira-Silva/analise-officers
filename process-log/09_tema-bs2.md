# 09 — Tema azul (identidade visual nova)

**Executor:** Claude Sonnet (subagente executor).
**Data:** 26/10/2026.

## Objetivo

Trocar a identidade visual da interface (antes marinho e dourado) por uma nova, inspirada em um banco digital brasileiro, sem mexer em estrutura, dados nem lógica. O Lead Scorer continua sendo uma página estática que prioriza deals de CRM e abre por duplo-clique (`file://`).

## Origem da paleta

Valores extraídos dos estilos computados de https://www.bancobs2.com.br em 26/10/2026:

| Valor | Papel no site de referência | Papel aqui |
|---|---|---|
| `#0021AF` | Cabeçalho, botões primários, texto de destaque | Cabeçalho, botão primário, links, foco |
| `#008FF9` | Azul de destaque | Destaque da frase de resumo e barra de progresso, só sobre o bloco escuro |
| `#090E29` | Marinho escuro | Texto, bloco de resumo (claro), fundo do tema escuro |
| `#6EB1DE` | Azul claro | Foco e links no tema escuro |
| `#595450`, `#8D8680`, `#C0B5AC` | Neutros quentes | Texto secundário e lista Limpe, bordas, Limpe no escuro |
| Poppins 700 / 400 / 600 | Títulos / corpo / ênfase | Mesma divisão, auto-hospedada |
| Botão em pílula (30px) | Primário azul, secundário branco | Mesmo formato |

Derivados (não extraídos): `#001A8A`, `#001262` (hover e pressionado do primário) e `#2D55FF` (azul principal clareado, só no tema escuro).

## Regras de não confusão com canal oficial

O site de referência abre com um aviso antifraude, e esta página é pública. Regras aplicadas e verificadas por `check_aviso_demo` (em `tools/check_views.py`, 5 telas × 390 e 1280 px):

- sem logotipo (a marca da barra é só o texto "Lead Scorer"; o losango em CSS da identidade anterior foi removido);
- sem o nome do banco na interface, exceto no rodapé obrigatório;
- nada de login ou abertura de conta: nenhum campo de senha ou e-mail, nenhum botão "Entrar";
- a tela "Quem é você?" ganhou o rótulo "Visão de demonstração" e o texto "Não é um login: não existe conta nem senha, e o nome só filtra o que aparece na tela";
- rodapé visível em todas as telas, fora do `#app` (aparece até sem `data.js`), com o texto exato: "Projeto pessoal de demonstração com dados públicos e fictícios (dataset CRM Sales Predictive Analytics, Kaggle, CC0). Não é um produto, serviço ou canal do Banco BS2.";
- o rótulo do link da visão completa deixou de citar avaliação: "Ver a carteira completa (RevOps)".

## O que mudou

- `solution/app/fonts/`: entram `poppins-latin-{400,600,700}-normal.woff2` e `poppins-LICENSE` (OFL); saem Manrope e Libre Baskerville com as licenças.
- `solution/app/style.css`: tokens reescritos (paleta da marca, semânticos, status), botões em pílula, destaque da frase de resumo em Poppins 700 azul de destaque (antes itálico serifado), `font-synthesis: none`, rodapé de aviso.
- `solution/app/index.html`: `theme-color`, descrição, marca sem losango, texto da entrada, rodapé de aviso (com a linha "Dados de ..." dentro dele, para haver um único `contentinfo`).
- `solution/tools/check_app.py`: pares de contraste reescritos para os tokens novos; a varredura de dígitos do HTML ignora o rodapé de aviso (ele tem "CC0" e o nome do banco), que é conferido à parte.
- `solution/tools/check_views.py`: cor de fundo dos dois temas, checagem de fontes (Poppins 400, 600 e 700, nenhuma outra, destaque em 700 sem itálico) e a checagem nova `check_aviso_demo`.
- `solution/tools/design_shots.py`: grava em `process-log/screenshots/tema-bs2/`.
- `docs/DESIGN.md`: reescrito.
- `solution/app/app.js`: **não foi alterado.**

## Rodadas

Captura: vendedor Rosalina Dieter e manager Celia Rouche × {entrada, aba principal, terceira tela (card aberto com ações para o vendedor; pauta do 1:1 para o manager)} × {390, 1280 px} × {claro, escuro} = 24 imagens por rodada.

| Rodada | Pasta | O que se viu | O que mudou |
|---|---|---|---|
| Antes | `antes/` | Tema marinho e dourado, Manrope e itálico serifado | Linha de base para comparação |
| 1 | `r1/` | Hierarquia boa: cabeçalho azul, bloco de resumo escuro, listas com cor, ícone e rótulo. "Conta não informada" saía em itálico falso (a Poppins não tem itálico). O resumo escuro do tema escuro ficava com o destaque abaixo de 4,5:1. O rodapé não aparecia como região única para leitores de tela. O fundo suave do Limpe no escuro tinha um tom cinza-marrom sem relação com o azul | Itálico removido e `font-synthesis: none`; resumo do escuro escurecido para `#101C60`; `#foot` movido para dentro do rodapé de aviso; fundo do Limpe no escuro para `#262B4D` |
| 2 | `r2/` | Sem corte, sobreposição ou rolagem horizontal. Botões em pílula legíveis nos dois temas, o card tratado e o botão marcado se distinguem do primário. Parece ferramenta de trabalho, não site institucional | Nenhuma correção visual nova. Limite de duas rodadas respeitado |
| Final | `final-vendedor-{390,1280}.png`, `final-manager-{390,1280}.png`, `final-escuro-vendedor-{390,1280}.png`, `final-entrada-{390,1280}.png` | Conjunto final com a página como está no repositório | — |

Observação aceita: na tela de entrada o rodapé fica abaixo da dobra (em 390×844 e em 1280×800), porque a página tem os dois cartões de perfil, o aviso de transparência e as caixas "Como funciona" antes dele. O que está acima da dobra é o rótulo "Visão de demonstração" e a frase "Não é um login".

## Contraste (WCAG AA) e axe

Tabela gerada de `style.css` por `python tools/contrast_table.py` (4,5:1 para texto, 3:1 para gráficos e limites de componente). Todos os pares passam nos dois temas.
| Texto ou elemento | Sobre | Uso | Mínimo | Claro | Escuro | Resultado |
| :--- | :--- | :--- | ---: | ---: | ---: | :--- |
| `text` | `bg` | texto da página | 4,50:1 | 17,45:1 | 18,98:1 | passa |
| `text` | `surface` | texto em cards | 4,50:1 | 18,98:1 | 16,77:1 | passa |
| `text` | `soft` | texto em fundos suaves | 4,50:1 | 16,00:1 | 14,08:1 | passa |
| `muted` | `bg` | texto secundário | 4,50:1 | 6,87:1 | 10,21:1 | passa |
| `muted` | `surface` | texto secundário em cards | 4,50:1 | 7,48:1 | 9,03:1 | passa |
| `muted` | `soft` | texto secundário em fundos suaves e no aviso do rodapé | 4,50:1 | 6,30:1 | 7,58:1 | passa |
| `link` | `bg` | links e botão secundário | 4,50:1 | 10,51:1 | 8,14:1 | passa |
| `link` | `surface` | links e botão secundário em cards | 4,50:1 | 11,43:1 | 7,19:1 | passa |
| `link` | `soft` | botão secundário ao passar o mouse | 4,50:1 | 9,64:1 | 6,04:1 | passa |
| `focus` | `bg` | anel de foco na página | 3,00:1 | 10,51:1 | 8,14:1 | passa |
| `focus` | `surface` | anel de foco em cards | 3,00:1 | 11,43:1 | 7,19:1 | passa |
| `focus-hi` | `bar` | anel de foco no cabeçalho | 3,00:1 | 4,90:1 | 4,90:1 | passa |
| `focus-hi` | `hero` | anel de foco no resumo | 3,00:1 | 8,14:1 | 6,64:1 | passa |
| `control` | `bg` | borda de campos | 3,00:1 | 3,30:1 | 6,28:1 | passa |
| `control` | `surface` | borda de campos | 3,00:1 | 3,59:1 | 5,55:1 | passa |
| `link` | `surface` | borda do botão secundário | 3,00:1 | 11,43:1 | 7,19:1 | passa |
| `primary-ink` | `primary` | texto do botão primário | 4,50:1 | 11,43:1 | 5,45:1 | passa |
| `primary-ink` | `primary-hover` | botão primário ao passar o mouse | 4,50:1 | 13,86:1 | 6,43:1 | passa |
| `primary-ink` | `primary-active` | botão primário pressionado | 4,50:1 | 16,63:1 | 11,43:1 | passa |
| `primary` | `bg` | limite do botão primário na página | 3,00:1 | 10,51:1 | 3,48:1 | passa |
| `primary` | `surface` | limite do botão primário em cards | 3,00:1 | 11,43:1 | 3,08:1 | passa |
| `bar-text` | `bar` | texto do cabeçalho | 4,50:1 | 11,43:1 | 11,43:1 | passa |
| `bar-text` | `bar-field` | campo de data no cabeçalho | 4,50:1 | 13,86:1 | 13,86:1 | passa |
| `bar-line` | `bar` | borda dos botões e do campo no cabeçalho | 3,00:1 | 3,81:1 | 3,81:1 | passa |
| `hero-text` | `hero` | texto do resumo | 4,50:1 | 18,98:1 | 15,47:1 | passa |
| `hero-muted` | `hero` | texto secundário do resumo | 4,50:1 | 10,56:1 | 8,61:1 | passa |
| `hero-accent` | `hero` | palavra de destaque e barra de progresso | 4,50:1 | 5,69:1 | 4,64:1 | passa |
| `inv-text` | `inv-bg` | botão de ação marcado e etiqueta do perfil | 4,50:1 | 18,98:1 | 18,98:1 | passa |
| `note-text` | `note-bg` | faixa do modo teste e avisos | 4,50:1 | 12,38:1 | 11,99:1 | passa |
| `note-line` | `note-bg` | borda dos avisos | 3,00:1 | 4,58:1 | 6,44:1 | passa |
| `bad` | `surface` | alertas em cards | 4,50:1 | 6,54:1 | 8,33:1 | passa |
| `bad` | `bg` | alertas na página | 4,50:1 | 6,01:1 | 9,43:1 | passa |
| `limpe-c` | `border` | barra de higiene sobre a trilha | 3,00:1 | 5,20:1 | 5,27:1 | passa |
| `foque-c` | `surface` | foque: texto em cards | 4,50:1 | 6,51:1 | 9,31:1 | passa |
| `foque-c` | `bg` | foque: texto na página | 4,50:1 | 5,99:1 | 10,53:1 | passa |
| `foque-c` | `foque-t` | foque: texto no fundo suave | 4,50:1 | 5,66:1 | 6,92:1 | passa |
| `text` | `foque-t` | foque: texto principal no fundo suave | 4,50:1 | 16,51:1 | 12,46:1 | passa |
| `muted` | `foque-t` | foque: texto secundário no fundo suave | 4,50:1 | 6,50:1 | 6,71:1 | passa |
| `foque-l` | `surface` | foque: linha gráfica em cards | 3,00:1 | 4,04:1 | 6,74:1 | passa |
| `foque-l` | `bg` | foque: linha gráfica na página | 3,00:1 | 3,71:1 | 7,62:1 | passa |
| `foque-h` | `hero` | foque: número sobre o resumo | 4,50:1 | 10,53:1 | 8,59:1 | passa |
| `reative-c` | `surface` | reative: texto em cards | 4,50:1 | 6,26:1 | 9,63:1 | passa |
| `reative-c` | `bg` | reative: texto na página | 4,50:1 | 5,76:1 | 10,89:1 | passa |
| `reative-c` | `reative-t` | reative: texto no fundo suave | 4,50:1 | 5,38:1 | 8,27:1 | passa |
| `text` | `reative-t` | reative: texto principal no fundo suave | 4,50:1 | 16,29:1 | 14,40:1 | passa |
| `muted` | `reative-t` | reative: texto secundário no fundo suave | 4,50:1 | 6,42:1 | 7,75:1 | passa |
| `reative-l` | `surface` | reative: linha gráfica em cards | 3,00:1 | 3,91:1 | 6,39:1 | passa |
| `reative-l` | `bg` | reative: linha gráfica na página | 3,00:1 | 3,60:1 | 7,24:1 | passa |
| `reative-h` | `hero` | reative: número sobre o resumo | 4,50:1 | 10,89:1 | 8,88:1 | passa |
| `limpe-c` | `surface` | limpe: texto em cards | 4,50:1 | 7,48:1 | 8,34:1 | passa |
| `limpe-c` | `bg` | limpe: texto na página | 4,50:1 | 6,87:1 | 9,44:1 | passa |
| `limpe-c` | `limpe-t` | limpe: texto no fundo suave | 4,50:1 | 6,25:1 | 6,81:1 | passa |
| `text` | `limpe-t` | limpe: texto principal no fundo suave | 4,50:1 | 15,86:1 | 13,68:1 | passa |
| `muted` | `limpe-t` | limpe: texto secundário no fundo suave | 4,50:1 | 6,25:1 | 7,36:1 | passa |
| `limpe-l` | `surface` | limpe: linha gráfica em cards | 3,00:1 | 3,59:1 | 5,48:1 | passa |
| `limpe-l` | `bg` | limpe: linha gráfica na página | 3,00:1 | 3,30:1 | 6,20:1 | passa |
| `limpe-h` | `hero` | limpe: número sobre o resumo | 4,50:1 | 9,44:1 | 7,70:1 | passa |
| `qualifique-c` | `surface` | qualifique: texto em cards | 4,50:1 | 8,47:1 | 7,72:1 | passa |
| `qualifique-c` | `bg` | qualifique: texto na página | 4,50:1 | 7,79:1 | 8,74:1 | passa |
| `qualifique-c` | `qualifique-t` | qualifique: texto no fundo suave | 4,50:1 | 6,97:1 | 6,64:1 | passa |
| `text` | `qualifique-t` | qualifique: texto principal no fundo suave | 4,50:1 | 15,61:1 | 14,42:1 | passa |
| `muted` | `qualifique-t` | qualifique: texto secundário no fundo suave | 4,50:1 | 6,15:1 | 7,76:1 | passa |
| `qualifique-l` | `surface` | qualifique: linha gráfica em cards | 3,00:1 | 5,45:1 | 5,12:1 | passa |
| `qualifique-l` | `bg` | qualifique: linha gráfica na página | 3,00:1 | 5,01:1 | 5,79:1 | passa |
| `qualifique-h` | `hero` | qualifique: número sobre o resumo | 4,50:1 | 8,74:1 | 7,13:1 | passa |

65 pares, nos dois temas. Menor razão entre o medido e o mínimo exigido: claro 1,10x, escuro 1,03x (acima de 1,00x passa).

Axe-core 4.9.1 (`tools/check_views.py`): 40 execuções (10 telas × 1280 e 390 px × claro e escuro), **zero violações serious ou critical e zero de impacto menor** no fim.

## Verificação final

| Comando (cwd = `solution/`) | Resultado |
|---|---|
| `python -B tools/check_app.py --prefix final` | exit 0, 27 de 27 checagens |
| `python -B tools/check_views.py` | exit 0, 12 de 12 checagens (inclui `check_aviso_demo` e o axe) |
| `python -B -m pytest -p no:cacheprovider` | exit 0 (ver o relatório final) |

## Erros reais no caminho

1. **Contraste do tema escuro.** A primeira versão dos tokens reprovou dois pares: texto branco sobre o hover do primário no escuro (4,23:1) e o azul de destaque `#008FF9` sobre o resumo escuro (4,39:1). Corrigidos com o hover `#2549EE` e o resumo `#101C60`.
2. **BOM sem querer.** `Set-Content -Encoding UTF8` do PowerShell 5.1 gravou BOM em CSS, HTML e scripts Python. Notado quando o `ast.parse` reclamou de U+FEFF; BOM removido de todos os arquivos tocados.
3. **Apelido do PowerShell.** Uma função auxiliar chamada `R` colidiu com o apelido de `Invoke-History`, e a primeira rodada de substituições não aplicou nada. Renomeada.
4. **Checagem que nunca acharia nada.** A regex de "nome do banco fora do rodapé" foi escrita com `\\b` dentro de string crua, o que casa uma barra literal. A primeira execução passou por engano; ao corrigir para `\b`, apareceu um falso positivo em "banco de dados" (texto legítimo do aviso de transparência), tratado na própria regex.
5. **Itálico falso.** "Conta não informada" tinha `font-style: italic`, e a Poppins carregada não tem itálico, então o navegador inclinava os glifos. Visto na rodada 1.
6. **Dois `contentinfo`.** Com o rodapé de aviso novo e o `<footer id="foot">` antigo, o axe acusou `landmark-no-duplicate-contentinfo` e `region` (impacto moderado, não bloqueante). O `#foot` virou um `div` dentro do rodapé de aviso.
7. **`text-transform`.** A checagem do rótulo "Visão de demonstração" falhou porque `inner_text` devolve o texto em caixa alta (o rótulo usa `text-transform: uppercase`); passou a comparar em minúsculas.
8. **`data.js` ausente.** Durante a execução do `check_views`, o outro executor estava regerando o `data.js` e o arquivo sumiu por alguns segundos (exit 2, "app/index.html ou app/data.js ausente"). Esperei o arquivo voltar e rodei de novo.
9. **Edição que quebrou o `design_shots.py`.** Uma substituição por índice juntou `]` e `n = 0` na mesma linha. Erro de sintaxe visto na hora e corrigido.
10. **Teste de README.** `test_readme.py::test_relative_links_point_to_existing_files` falhou enquanto este arquivo não existia (o README já aponta para ele). Resolvido por este registro.
# Design — Lead Scorer

Identidade visual do Lead Scorer: uma ferramenta de trabalho em azul, com tom direto, empresarial e confiante. A tabela de contraste abaixo é gerada a partir do `style.css` por `tools/contrast_table.py`. O registro das rodadas visuais está em [`process-log/09_tema-azul.md`](../process-log/09_tema-azul.md).

## 1. Direção

A interface é uma página estática que prioriza deals de CRM. A hierarquia é: **a frase de ação** (o que fazer esta semana) primeiro, **as quatro listas** depois, **o deal** por último. Ela deve parecer uma ferramenta de trabalho (densa, legível, com ações claras) e não um site institucional.

- **Azul principal para ação e marca.** Cabeçalho, botão primário, links, anel de foco e o destaque da frase de resumo. Nunca é cor de status.
- **Status = cor + ícone + rótulo.** Nenhuma lista depende só da cor.
- **Pílulas.** Botões com raio de 30px: primário azul com texto branco, secundário branco com texto e borda azuis.
- **Poppins** auto-hospedada: títulos e números em 700, ênfase em 600, corpo em 400.

## 2. Valores do tema

O tema é azul: azul `#0021AF` para ação e marca, Poppins e botões em pílula. Sem logotipo nem elementos institucionais de terceiros.

| Valor | Descrição | Onde aparece aqui |
|---|---|---|
| `#0021AF` | Fundo do cabeçalho, botões primários, texto de destaque | Cabeçalho, botão primário, links, foco |
| `#008FF9` | Azul de destaque | Palavra de destaque da frase de resumo e barra de progresso (elementos gráficos sobre o bloco escuro) |
| `#090E29` | Marinho escuro | Texto, bloco de resumo no tema claro, fundo do tema escuro |
| `#6EB1DE` | Azul claro | Anel de foco e links no tema escuro, foco sobre o cabeçalho |
| `#FFFFFF` | Branco | Superfícies, texto sobre azul |
| `#595450`, `#8D8680`, `#C0B5AC` | Neutros quentes | Texto secundário e lista Limpe, bordas de campos, Limpe no tema escuro |
| Poppins 700 / 400 / 600 | Títulos / corpo / ênfase | Mesma divisão de pesos |
| Botão em pílula, raio de 30px | Primário azul, secundário branco | Mesmo formato |

Valores derivados: `#001A8A` (hover do primário e campos sobre o cabeçalho), `#001262` (primário pressionado) e `#2D55FF` (o azul principal clareado, só no tema escuro, onde `#0021AF` quase some sobre o marinho).

## 3. Regra: não parecer canal oficial

Esta página é pública, então deve deixar claro que é uma demonstração e não pode se passar por canal de nenhuma instituição. Regras obrigatórias, verificadas por `tools/check_views.py` (`check_aviso_demo`):

1. **Sem logotipo.** A marca da barra é só o texto "Lead Scorer" em Poppins 700. Não há imagem, ícone de marca nem símbolo desenhado em CSS.
2. **Sem marca de terceiros na interface.** O nome da ferramenta continua "Lead Scorer".
3. **Nada que lembre login ou abertura de conta.** Sem campos de senha ou e-mail, sem botões "Entrar" ou "Abrir conta". A tela "Quem é você?" tem o rótulo "Visão de demonstração" e diz que não é um login: o nome só filtra o que aparece na tela.
4. **Rodapé visível em todas as telas**, fora do `#app` (aparece até se o `data.js` não carregar), com este texto exato:

   > Projeto pessoal de demonstração com dados públicos e fictícios (dataset CRM Sales Predictive Analytics, Kaggle, CC0).

5. O rodapé é a única exceção à regra "sem números no HTML" de `tools/check_app.py` (ele contém "CC0"), e o texto exato é conferido por `check_aviso_demo`.

## 4. Tokens (CSS custom properties em `solution/app/style.css`)

### Paleta da marca (igual nos dois temas)

| Token | Valor | Uso |
|---|---|---|
| `--blue-700` | `#0021AF` | Azul principal |
| `--blue-800` | `#001A8A` | Derivado: hover do primário, campos sobre o cabeçalho |
| `--blue-900` | `#001262` | Derivado: primário pressionado |
| `--blue-bright` | `#2D55FF` | Derivado: azul principal clareado (tema escuro) |
| `--sky-500` | `#008FF9` | Azul de destaque (só gráfico e destaque sobre o bloco de resumo) |
| `--sky-300` | `#6EB1DE` | Azul claro (foco e links sobre fundo escuro) |
| `--ink-950` | `#090E29` | Marinho escuro |
| `--warm-700` / `--warm-500` / `--warm-300` | `#595450` / `#8D8680` / `#C0B5AC` | Neutros quentes |

### Semânticos (mudam com o tema)

| Token | Claro | Escuro |
|---|---|---|
| `--bg` | `#F7F5F3` | `#090E29` |
| `--surface` | `#FFFFFF` | `#101947` |
| `--soft` | `#EFEBE7` | `#18236B` |
| `--text` | `#090E29` | `#FFFFFF` |
| `--muted` | `#595450` | `#B6BDDC` |
| `--border` | `#DDD6CF` | `#2A3785` |
| `--control` (borda de campos, 3:1) | `#8D8680` | `#8591CF` |
| `--link` | `#0021AF` | `#6EB1DE` |
| `--focus` | `#0021AF` | `#6EB1DE` |
| `--primary` / `-hover` / `-active` | `#0021AF` / `#001A8A` / `#001262` | `#2D55FF` / `#2549EE` / `#0021AF` |
| `--bar` (cabeçalho) | `#0021AF` | `#0021AF` |
| `--hero` (bloco de resumo) | `#090E29` | `#101C60` |
| `--hero-accent` | `#008FF9` | `#008FF9` |
| `--inv-bg` / `--inv-text` (estado "feito" dos botões) | `#090E29` / `#FFFFFF` | `#FFFFFF` / `#090E29` |
| `--note-bg` / `--note-text` / `--note-line` | `#E3EFF9` / `#0C2B47` / `#2A6FA6` | `#10264A` / `#D6E8F8` / `#6EB1DE` |
| `--bad` | `#B3261E` | `#FF9C94` |

### Status das listas (cor + ícone + rótulo)

Cada lista tem quatro tokens: `-c` (tinta do texto), `-t` (fundo suave), `-l` (linha gráfica, 3:1) e `-h` (variante clara sobre o bloco de resumo). As cores vêm de famílias que combinam com o azul sem se confundir com ele: verde, âmbar, neutro quente e violeta.

| Lista | Significado | Cor (claro: `-c`) | Ícone | Rótulo na tela do manager |
|---|---|---|---|---|
| Foque | vivo, alto valor esperado | verde `#0B6B4D` | alvo | Vivos |
| Reative | bom, mas esfriando | âmbar `#9A4A00` | seta circular | Esfriando |
| Limpe | deal zumbi | neutro quente `#595450` | lixeira | Zumbis |
| Qualifique | Prospecting, sem data | violeta `#5B2FB0` | lupa | Qualifique |

## 5. Contraste (WCAG AA)

Regra: 4,5:1 para texto, 3:1 para elementos gráficos (linhas de status, borda de campos, limite do botão primário, foco). Os dois temas, todos os pares usados. A tabela é gerada do `style.css` por `python tools/contrast_table.py --write`, e `tools/check_app.py` reprova o build se algum par cair abaixo do mínimo.

O `#008FF9` sobre branco dá cerca de 3,3:1 e não passa como texto: por isso ele só aparece sobre o bloco de resumo escuro (5,69:1 no tema claro e 4,64:1 no escuro, onde o resumo foi escurecido para `#101C60` justamente para passar) e como elemento gráfico. Em texto sobre fundo claro, o destaque é `#0021AF`.

<!-- CONTRASTE:inicio -->
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
<!-- CONTRASTE:fim -->

## 6. Tipografia

- `--font-ui: 'Poppins', system-ui, sans-serif`, auto-hospedada em `app/fonts/` (OFL, licença na pasta): 400 (corpo, tabelas), 600 (ênfase, botões, rótulos) e 700 (títulos, números grandes, destaque). Sem itálico e com `font-synthesis: none`, para o navegador nunca inventar um peso.
- **Destaque da frase de resumo** (as palavras "Esta semana", "Seu time"): peso 700 em azul de destaque `#008FF9` sobre o bloco escuro; na tela de entrada, a palavra "você" em 700 no azul principal. Nunca em números ou tabelas.
- `font-variant-numeric: tabular-nums` em valores, scores, contagens e tabelas.
- Escala: 14, 16, 18, 20, 24 e 32px (fluida na frase de ação).

## 7. Espaçamento, raio e sombra

- Espaçamento em múltiplos de 8px (`--s1` = 8px até `--s6` = 48px; 4px só em respiros internos de ícone).
- Raio: 30px em botões (`--r-btn`, pílula), 12px em campos e avisos (`--r-field`), 16px em cards e blocos (`--r-card`).
- Sombras suaves de uma camada (`--shadow`), quase invisíveis no tema escuro, onde a separação vem da borda e da cor da superfície.

## 8. Temas, movimento e foco

- **Claro:** fundo neutro quente muito claro, superfícies brancas, cabeçalho azul principal, bloco de resumo marinho. **Escuro:** fundo marinho `#090E29`, superfícies em azul-noite, cabeçalho azul principal, bloco de resumo em azul mais profundo.
- Segue `prefers-color-scheme` e tem botão de alternância na barra (a escolha fica em `localStorage`, com `try/catch`; sem armazenamento, o tema do sistema vale).
- Transições de 150 a 200ms em cor, borda e sombra. `prefers-reduced-motion: reduce` desliga transições e a contagem animada dos números.
- Foco visível: anel de 3px com deslocamento de 2px (`--focus`: azul principal sobre claro, azul claro sobre escuro; azul claro sobre o cabeçalho e o resumo).

## 9. Layout

- **Vendedor: mobile first.** Uma coluna; cards empilhados; abas em 2×2 no celular e 4 colunas no desktop; no desktop o card vira uma linha (cabeçalho à esquerda, frases à direita).
- **Manager: desktop first.** Tabela "Meu time" larga, ordenável; no celular cada linha vira um cartão com rótulos.
- Alvos de toque de pelo menos 44×44px; sem rolagem horizontal da página.
- O rodapé de aviso fica no fim da página, em todas as telas. Na tela de entrada ele fica abaixo da dobra em 1280×800 e em 390×844; a mensagem "Visão de demonstração, não é um login" está acima da dobra.

## 10. Interatividade com propósito

| O quê | Para quê |
|---|---|
| Card expande com um clique e mostra o "porquê" | Ler a explicação só do deal que importa |
| "Contatei", "Agendei", "Encerrar no CRM" com feedback imediato (botão invertido, selo no card, anúncio por leitor de tela) | Fechar o ciclo da semana; o resumo no topo atualiza na hora; salvo só neste navegador |
| Simulador "E se eu fechar este?" com contagem animada do valor da semana | Ver o impacto de um deal no valor esperado |
| Mapa do time ordenável e clicável; pauta do 1:1 com "Copiar" | Preparar a conversa sem montar planilha |
| Teclado completo: abas com setas, botões nativos, link "pular para o conteúdo", foco movido para o título ao trocar de tela | Acessibilidade |

Nada de animação decorativa sem função.

## 11. Checklist usado em cada rodada

Hierarquia clara em 3 segundos; ação principal óbvia; azul principal só para ação ou marca; status legível sem a cor; nada cortado ou sobreposto; contraste AA; estados vazios úteis; consistência com os tokens; rodapé de aviso presente; "parece uma ferramenta de trabalho, não um site institucional".

## 12. Decisões de design

- Bloco de resumo escuro nos dois temas (âncora visual abaixo do cabeçalho azul; no escuro vira um azul-noite um pouco mais claro que o fundo).
- Estado "feito" dos botões é **invertido** (marinho com texto branco, e o inverso no escuro) com ícone de check, em vez de azul ou verde, para não competir com os status das listas nem com a ação primária.
- Higiene de carteira usa o neutro quente do Limpe e o rótulo "zumbis"; nunca uma escala de bom/ruim, e nunca taxa de vitória por vendedor (decisão 4 do CLAUDE.md).
- Qualifique é violeta e não azul, para o azul continuar exclusivo de ação e marca.

## 13. Ferramentas

- **Contraste:** `python tools/contrast_table.py --write` (pares e mínimos em `check_app.contrast_pairs()`).
- **Acessibilidade:** axe-core 4.9.1 via Playwright (Python) nos dois temas, em 1280 e 390px, em 10 telas (`tools/check_views.py`).
- **Loop visual:** `python tools/design_shots.py --round rN` e `--final`.
- **Lighthouse:** não executado (sem Node nesta máquina).

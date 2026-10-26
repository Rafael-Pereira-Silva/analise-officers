# Fontes auto-hospedadas

Poppins, sob a SIL Open Font License 1.1 (texto completo em `poppins-LICENSE`, nesta pasta). Subconjunto latino, formato woff2, carregadas por `@font-face` em `style.css`. Funcionam em `file://` e no GitHub Pages, sem CDN.

| Arquivo | Peso | Uso |
| --- | --- | --- |
| `poppins-latin-400-normal.woff2` | 400 | Corpo do texto, tabelas, rótulos secundários |
| `poppins-latin-600-normal.woff2` | 600 | Ênfase: botões, rótulos, valores, nomes |
| `poppins-latin-700-normal.woff2` | 700 | Títulos, números grandes e a palavra de destaque da frase de resumo |
| `poppins-LICENSE` | | Licença OFL, obrigatória na redistribuição |

Só estes três pesos são carregados. Qualquer outro peso pedido no CSS seria sintetizado pelo navegador, então o CSS usa apenas 400, 600 e 700. Não há itálico: o destaque editorial é feito com peso 700 e cor, não com fonte serifada.

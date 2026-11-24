# agenti-test

Testovací repozitář pro ukázku napojení AI agentů (Claude Code, GitHub Copilot coding agent, OpenAI Codex) na GitHub.

## Obsah
- `kalkulacka.py` – jednoduchá kalkulačka, na které agenti provádějí změny.

## Funkce kalkulačky
- `secti(a, b)` – vrátí součet `a + b`.
- `odecti(a, b)` – vrátí rozdíl `a - b`.
- `nasob(a, b)` – vrátí součin `a * b`.
- `vydel(a, b)` – vrátí podíl `a / b`; při dělení nulou (`b == 0`) vyhodí `ValueError`.

Ukázku spustíte příkazem `python kalkulacka.py`.

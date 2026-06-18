# PHMN: руководство по визуализациям инцидента

Обновлено: 2026-06-18

Этот документ объясняет, как смотреть и поддерживать визуализации взаимодействий адресов по PHMN incident.

## Самый быстрый публичный просмотр

Откройте готовые файлы в GitHub:

- Русская high-signal инфографика: `graphs/phmn_incident_high_signal_flow_ru.svg`
- Детальный граф: `graphs/phmn_attacker_olim_interaction_graph.svg`
- PNG-версия детального графа: `graphs/phmn_attacker_olim_interaction_graph.png`

## Редактируемые источники

У детального графа есть такие редактируемые источники:

- Mermaid: `graphs/phmn_attacker_olim_interaction_graph.mmd`
- Graphviz DOT: `graphs/phmn_attacker_olim_interaction_graph.dot`
- JSON: `graphs/phmn_attacker_olim_interaction_graph.json`

У high-signal инфографики есть две версии:

- английская SVG: `graphs/phmn_incident_high_signal_flow.svg`
- русская SVG: `graphs/phmn_incident_high_signal_flow_ru.svg`

SVG можно открыть напрямую в браузере или GitHub без дополнительного шага рендера.

## Obsidian view

Откройте папку `entities/phmn-incident/` как Obsidian-style карту доказательств. Начинать лучше отсюда:

- `entities/phmn-incident/README.md`

Каждая страница сущности использует wikilinks для связей между адресами атакера, адресами Olim, доказательствами доступа к серверу, общими контрактами и false-positive controls.

## Как обновлять безопасно

1. Сначала добавьте новое доказательство на страницу сущности.
2. Классифицируйте каждый edge: confirmed incident flow, manual review, common contract, benign context или weak lead.
3. Обновите `PHMN_INCIDENT_FALSE_POSITIVE_REVIEW_RU_2026-06-18.md`, если появился новый false-positive pattern.
4. Обновляйте CSV только если связь влияет на snapshot/distribution review.
5. Пересчитайте `checksums/SHA256SUMS` после изменения публичных файлов.

# PHMN Incident Visualization Guide

Updated: 2026-06-18

This guide explains how to view and maintain the PHMN incident interaction visualizations.

## Fastest Public View

Open the rendered files in GitHub:

- High-signal Russian infographic: `graphs/phmn_incident_high_signal_flow_ru.svg`
- Existing detailed graph: `graphs/phmn_attacker_olim_interaction_graph.svg`
- Existing PNG render: `graphs/phmn_attacker_olim_interaction_graph.png`

## Editable Sources

The detailed graph has these editable sources:

- Mermaid: `graphs/phmn_attacker_olim_interaction_graph.mmd`
- Graphviz DOT: `graphs/phmn_attacker_olim_interaction_graph.dot`
- JSON: `graphs/phmn_attacker_olim_interaction_graph.json`

The new high-signal infographic is hand-authored SVG so it can be opened directly in a browser or GitHub without a rendering step.

## Obsidian View

Open the `entities/phmn-incident/` folder as an Obsidian-style evidence map. Start from:

- `entities/phmn-incident/README.md`

Each entity page uses wikilinks to connect attacker addresses, Olim addresses, server-access evidence, common contracts, and false-positive controls.

## How To Update Safely

1. Add new evidence to an entity page first.
2. Classify each edge as confirmed incident flow, manual review, common contract, benign context, or weak lead.
3. Update `PHMN_INCIDENT_FALSE_POSITIVE_REVIEW_RU_2026-06-18.md` if a new false-positive pattern appears.
4. Update the CSV only when the relation affects snapshot/distribution review.
5. Recalculate `checksums/SHA256SUMS` after changing public files.


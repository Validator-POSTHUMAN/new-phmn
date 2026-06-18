# PHMN Attacker / Olim Interaction Graph - 2026-06-16

This graph is a visual companion to:

- [PHMN_ATTACKER_OLIM_INTERACTION_REVIEW_2026-06-16.md](../reports/PHMN_ATTACKER_OLIM_INTERACTION_REVIEW_2026-06-16.md)
- [attacker_olim_interaction_review_2026-06-16.csv](../adjustments/attacker_olim_interaction_review_2026-06-16.csv)
- [phmn_final_snapshot_address_map.csv](../snapshots/phmn_final_snapshot_address_map.csv)

## Files

- Mermaid source: [phmn_attacker_olim_interaction_graph.mmd](../graphs/phmn_attacker_olim_interaction_graph.mmd)
- DOT source: [phmn_attacker_olim_interaction_graph.dot](../graphs/phmn_attacker_olim_interaction_graph.dot)
- JSON source: [phmn_attacker_olim_interaction_graph.json](../graphs/phmn_attacker_olim_interaction_graph.json)
- SVG render: [phmn_attacker_olim_interaction_graph.svg](../graphs/phmn_attacker_olim_interaction_graph.svg)
- PNG render: [phmn_attacker_olim_interaction_graph.png](../graphs/phmn_attacker_olim_interaction_graph.png)
- High-signal RU infographic: [phmn_incident_high_signal_flow_ru.svg](../graphs/phmn_incident_high_signal_flow_ru.svg)
- False-positive review: [PHMN_INCIDENT_FALSE_POSITIVE_REVIEW_RU_2026-06-18.md](../reports/PHMN_INCIDENT_FALSE_POSITIVE_REVIEW_RU_2026-06-18.md)
- Visualization guide: [PHMN_INCIDENT_VISUALIZATION_GUIDE_RU_2026-06-18.md](../reports/PHMN_INCIDENT_VISUALIZATION_GUIDE_RU_2026-06-18.md)
- Obsidian-style entity map: [entities/phmn-incident/README.md](../entities/phmn-incident/README.md)

## Reading the Graph

- Red / critical edges are confirmed incident flow from the published evidence.
- Dashed yellow edges are leads that need deeper indexed-chain review.
- Green manual-review nodes are snapshot rows that should not be blindly treated as ordinary allocations.
- Grey contract nodes are route/pool/contract addresses, not normal user wallets.
- No-confirmed-link edges are explicitly marked to avoid overstating the evidence.

## Mermaid Preview

~~~mermaid
flowchart LR
  %% Generated from PHMN attacker/Olim interaction review
  minter["Compromised PHMN minter<br/>juno100um...xyyw"]
  att_juno["Attacker Juno<br/>juno1pqard...dea0<br/>15100 PHMN in snapshot"]
  att_cosmos["Attacker Cosmos<br/>cosmos1pqard...wz6n"]
  att_osmo["Attacker Osmosis<br/>osmo1pqard...ajvp"]
  att_neutron["Attacker Neutron<br/>neutron1pqard...qq5"]
  att_noble["Attacker Noble router<br/>noble1pqard...m2za"]
  sol_token["Solana USDC token acct<br/>AhT5Wa...Eer"]
  sol_owner["Solana owner wallet<br/>39CAqA...1HC"]
  sol_caller["Solana CCTP signer<br/>6MxMEe...3Rv"]
  funding_hub["Common funding hub<br/>osmo1m8wg...v83q"]
  secret_root["Secret funding root<br/>secret1h3g...z5k"]
  secret_intermediate["Secret intermediate<br/>secret1j2n...7rn"]
  server["Minter server<br/>payments-2 / valoper"]
  olim_key["OlimJon SSH key<br/>109.75.50.14"]
  unknown_key["Unknown SSH key<br/>153.75.83.51"]
  olim_eltl["Olim eltl snapshot row<br/>juno1eltl...m4u3e<br/>300.009116 PHMN"]
  olim_187["Olim 187 cluster<br/>cosmos/osmo/juno/neutron187<br/>0 PHMN in snapshot"]
  olim_solana["Olim provided Solana<br/>CjHc2h...DNPb"]
  das["POSTHUMAN DAS staking<br/>snapshot attribution"]
  astro_pool["Astroport PHMN/USDC pool<br/>neutron1muu...cwjv<br/>0.000017 PHMN"]
  squid_osmo["Squid / swap-action<br/>Osmosis contract"]
  squid_neutron["Squid / swap-action<br/>Neutron contract"]
  secret_root -.->|"56.102115 SCRT<br/>2026-06-08"| secret_intermediate
  secret_intermediate -.->|"swap/IBC route"| funding_hub
  funding_hub -->|"funded 3.286220 USDC"| att_noble
  att_noble -->|"CCTP 3.115769 USDC"| sol_token
  att_noble -->|"funded gas via OSMO"| att_osmo
  att_noble -->|"funded gas via NTRN"| att_neutron
  att_noble -->|"funded gas via JUNO"| att_juno
  att_juno -->|"1 JUNO gas"| minter
  minter -->|"30000 PHMN"| att_juno
  att_juno -->|"12000 PHMN"| att_osmo
  att_juno -->|"12000 + 3000 PHMN"| att_neutron
  att_neutron -->|"sold 2900 PHMN"| astro_pool
  att_neutron -->|"swap route"| squid_neutron
  att_neutron -->|"returned 12100 PHMN"| att_juno
  att_osmo -->|"sale route"| squid_osmo
  att_osmo -->|"8953.646449 USDC<br/>via Noble/CCTP"| sol_token
  sol_owner -->|"owns"| sol_token
  sol_caller -->|"receive signer"| sol_token
  att_juno -->|"same raw key / snapshot"| att_cosmos
  funding_hub -.->|"funded investigated juno187"| olim_187
  olim_eltl -.->|"DAS active stake<br/>300.009116 PHMN"| das
  olim_key -.->|"logged in during incident"| server
  unknown_key -->|"active during mint/transfer"| server
  server -->|"mint artifacts / scripts"| minter
  olim_187 -.->|"no direct final snapshot PHMN"| att_juno
  olim_solana -.->|"no confirmed link yet"| sol_token
  classDef attacker fill:#ffe1e1,stroke:#b42318,stroke-width:2px,color:#111;
  classDef attackerRoute fill:#fff1e6,stroke:#c2410c,stroke-width:2px,color:#111;
  classDef compromised fill:#ffd6a5,stroke:#9a3412,stroke-width:2px,color:#111;
  classDef lead fill:#fff7cc,stroke:#a16207,stroke-width:2px,color:#111;
  classDef server fill:#e0f2fe,stroke:#0369a1,stroke-width:2px,color:#111;
  classDef unknown fill:#f3e8ff,stroke:#7e22ce,stroke-width:2px,color:#111;
  classDef poi fill:#fef3c7,stroke:#92400e,stroke-width:2px,color:#111;
  classDef manual fill:#dcfce7,stroke:#166534,stroke-width:2px,color:#111;
  classDef contract fill:#e5e7eb,stroke:#374151,stroke-width:2px,color:#111;
  classDef context fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#111;
  class att_juno,att_cosmos,att_osmo,att_neutron,att_noble attacker;
  class sol_token,sol_owner,sol_caller attackerRoute;
  class minter compromised;
  class funding_hub lead;
  class server server;
  class unknown_key unknown;
  class olim_key poi;
  class olim_eltl manual;
  class das,astro_pool,squid_osmo,squid_neutron contract;
  class secret_root,secret_intermediate,olim_187,olim_solana context;
~~~

## Current High-Signal Findings

1. The attacker pqard row is present in the final snapshot with 15100 PHMN and should remain excluded from normal distribution.
2. The Olim eltl row is present in the final snapshot with 300.009116 PHMN via DAS staking attribution and should go through manual review.
3. The Olim 187 cluster is not present in the final snapshot, but remains a contextual lead because the evidence repo notes common funding-hub history with a previously investigated juno187 PHMN/DAS address.
4. The common funding hub osmo1m8wg... is not in the final snapshot, but is a high-priority lead because it funded attacker same-key addresses before the incident.
5. A complete all-snapshot interaction scan still requires an account-history indexer; public RPC/LCD endpoints available in this pass did not provide reliable tx_search event queries.

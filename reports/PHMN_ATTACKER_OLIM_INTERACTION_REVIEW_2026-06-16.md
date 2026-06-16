# PHMN Attacker / Olim Interaction Review — 2026-06-16

This is a first-pass investigation table for the PHMN migration snapshot.

Scope:
- list known attacker addresses across Juno, Cosmos Hub, Osmosis, Neutron, Noble, and Solana;
- list operator-provided Olim addresses and derived Cosmos/Osmosis/Neutron/Juno equivalents;
- identify which relevant addresses are present in the final PHMN snapshot;
- record confirmed interactions from the published evidence repository;
- mark entries that need further investigation before final distribution/quarantine decisions.

Primary sources:
- Final PHMN snapshot: [snapshots/phmn_final_snapshot.csv](../snapshots/phmn_final_snapshot.csv)
- Derived address map: [snapshots/phmn_final_snapshot_address_map.csv](../snapshots/phmn_final_snapshot_address_map.csv)
- Expanded snapshot rows: [snapshots/phmn_final_snapshot_expanded_rows.csv](../snapshots/phmn_final_snapshot_expanded_rows.csv)
- Mint evidence repository: https://github.com/Validator-POSTHUMAN/mint-phmn-evidence
- Attacker address graph: https://github.com/Validator-POSTHUMAN/mint-phmn-evidence/blob/main/artifacts/phmn-attacker-address-links-2026-06-10.md
- Server investigation report: https://github.com/Validator-POSTHUMAN/mint-phmn-evidence/blob/main/artifacts/REPORT.md
- Noble pqard router trace: https://github.com/Validator-POSTHUMAN/mint-phmn-evidence/blob/main/artifacts/phmn-noble-pqard-router-2026-06-10.md
- Osmosis to Solana CCTP route: https://github.com/Validator-POSTHUMAN/mint-phmn-evidence/blob/main/artifacts/phmn-solana-cctp-2026-06-10.md

## Method

The final snapshot already contains Cosmos-equivalent addresses. For this review, every snapshot row was additionally mapped to Juno, Osmosis, and Neutron bech32 forms using the same raw address payload.

Generated map:

- [snapshots/phmn_final_snapshot_address_map.csv](../snapshots/phmn_final_snapshot_address_map.csv)

Important caveat: bech32 conversion only changes the prefix. For 32-byte contract / module / DAO addresses, the converted address is useful for matching, but it does not imply a normal user-controlled wallet on another chain.

## Known attacker addresses

| Role | Network | Address | Evidence / note |
| --- | --- | --- | --- |
| Attacker same raw key | Juno | `juno1pqardc39d558mr58nx5m2wgmy448pv94ehdea0` | Received unauthorized 30000 PHMN from compromised minter; holds 15100 PHMN in final snapshot. |
| Attacker same raw key | Cosmos Hub | `cosmos1pqardc39d558mr58nx5m2wgmy448pv9409wz6n` | Bech32 equivalent of pqard key; final snapshot destination for attacker Juno row. |
| Attacker same raw key | Osmosis | `osmo1pqardc39d558mr58nx5m2wgmy448pv9487ajvp` | Received 12000 PHMN from Juno and later bridged USDC toward Solana. |
| Attacker same raw key | Neutron | `neutron1pqardc39d558mr58nx5m2wgmy448pv94t68qq5` | Received 12000 + 3000 PHMN from Juno; swapped 2900 PHMN to USDC; returned 12100 PHMN to Juno. |
| Attacker same raw key | Noble | `noble1pqardc39d558mr58nx5m2wgmy448pv948xm2za` | Pre-attack router/funding address for gas and CCTP routes. |
| Attacker route | Solana USDC token account | `AhT5WaWAAoMF48nPssaSFEoygCfsq1N2qq7BTUJqEer` | Received USDC through Noble Orbiter / CCTP. |
| Attacker route | Solana owner wallet | `39CAqAK85xu24YbTw7LbqnphG1QqReL4PHkcmTX3v1HC` | Owner of the Solana USDC token account. |
| Attacker route | Solana CCTP signer/caller | `6MxMEeH2MQTjk7Cd4JDbJSnTvtpoKJuv374KpQYKJ3Rv` | Signer/caller for the Solana CCTP receive transaction. |

## Operator-provided Olim addresses and derived equivalents

| Cluster | Network / form | Address | Snapshot status |
| --- | --- | --- | --- |
| Olim eltl | Juno | `juno1eltl6qu6y538vhux3mk3pjpn7redx8najm4u3e` | Present in final snapshot: 300.009116 PHMN, DAS staking active. |
| Olim eltl | Cosmos equivalent | `cosmos1eltl6qu6y538vhux3mk3pjpn7redx8nayfk8k9` | Same snapshot row as above. |
| Olim eltl | Osmosis equivalent | `osmo1eltl6qu6y538vhux3mk3pjpn7redx8navj9hqh` | Derived; not a separate source row in final snapshot. |
| Olim eltl | Neutron equivalent | `neutron1eltl6qu6y538vhux3mk3pjpn7redx8naqkl9vz` | Derived; not a separate source row in final snapshot. |
| Olim 187 | Cosmos | `cosmos187jy6cderlfwwttds33e6cdzntx0z0gh9qrhee` | Not present in final snapshot. |
| Olim 187 | Juno equivalent | `juno187jy6cderlfwwttds33e6cdzntx0z0ghnjqv79` | Not present in final snapshot. Previously investigated as related PHMN/DAS address; final PHMN amount is zero. |
| Olim 187 | Osmosis | `osmo187jy6cderlfwwttds33e6cdzntx0z0ghdms80t` | Not present in final snapshot. |
| Olim 187 | Neutron equivalent | `neutron187jy6cderlfwwttds33e6cdzntx0z0ghpl24r7` | Not present in final snapshot. |
| Olim provided | Solana | `CjHc2hJUxHmYrg9wTttkCekMgQCCa3L3Mhgq8dbrDNPb` | Non-Cosmos address; not part of PHMN snapshot. |

## Snapshot rows requiring attention

| Priority | Snapshot / derived address | Amount | Type | Interaction / reason | Recommended action |
| --- | --- | ---: | --- | --- | --- |
| Critical | `cosmos1pqardc39d558mr58nx5m2wgmy448pv9409wz6n` / `juno1pqardc39d558mr58nx5m2wgmy448pv94ehdea0` | 15100.000000 PHMN | Attacker same-key holder | Confirmed attacker cluster. Received unauthorized PHMN and participated in sale/bridge flow. | Exclude from normal distribution; keep in attacker/excluded bucket. |
| High | `cosmos1eltl6qu6y538vhux3mk3pjpn7redx8nayfk8k9` / `juno1eltl6qu6y538vhux3mk3pjpn7redx8najm4u3e` | 300.009116 PHMN | Operator-provided Olim address | Present in snapshot through DAS staking active attribution. No direct attacker transfer found in local evidence table, but owner is a person of interest in server-access investigation. | Manual review before distribution; decide whether to distribute, quarantine, or handle by governance/legal process. |
| Medium | `cosmos1muu00n0ae5z7kwnjfn98naju9p6vrj4msj35netm2ffjqs5wxyts43f2v0` / `neutron1muu00n0ae5z7kwnjfn98naju9p6vrj4msj35netm2ffjqs5wxyts57cwjv` | 0.000017 PHMN | Astroport PHMN/USDC pool contract | Route contract used in the Neutron PHMN sale path. This is a contract/pool row, not a normal holder. | Treat as contract/LP accounting, not a user allocation; keep audit note. |
| High lead, not in snapshot | `osmo1m8wg4vxkefhs374qxmmqpyusgz289wmulex5qdwpfx7jnrxzer5s9cv83q` | 0 PHMN in final snapshot | Common funding hub | Funded attacker Noble/Juno/Neutron addresses and previously funded investigated `juno187...` PHMN/DAS address. | Continue investigation; no direct distribution action because it is not in snapshot. |
| Context, not in snapshot | `cosmos187jy6cderlfwwttds33e6cdzntx0z0gh9qrhee` / `osmo187jy6cderlfwwttds33e6cdzntx0z0ghdms80t` / `neutron187jy6cderlfwwttds33e6cdzntx0z0ghpl24r7` / `juno187jy6cderlfwwttds33e6cdzntx0z0ghnjqv79` | 0 PHMN in final snapshot | Operator-provided Olim 187 cluster | Evidence notes prior PHMN/DAS activity and common funding hub relation, but final snapshot has no PHMN row for this exact raw-key cluster. | Keep as contextual lead; no snapshot distribution action unless new evidence appears. |
| Context, Solana | `CjHc2hJUxHmYrg9wTttkCekMgQCCa3L3Mhgq8dbrDNPb` | N/A | Operator-provided Solana address | Not a PHMN snapshot address. Needs Solana-side investigation if relevant. | Compare against attacker Solana route addresses `AhT5...`, `39CA...`, `6MxM...` with a Solana indexer. |

## Confirmed interaction table from evidence

| Priority | Time / flow | Source | Destination / counterparty | Network | Snapshot relevance | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Critical | 2026-06-10 09:39 UTC | Compromised minter `juno100umj2mnu0u6ujf37c9a3xfy9gl53hu9ekxyyw` | `juno1pqardc39d558mr58nx5m2wgmy448pv94ehdea0` | Juno | Destination is in final snapshot with 15100 PHMN. | Tx `5AA8C1274E2FC823DCD4DACDC8B951220929D5BA338BFAB57E731CAEBAB737FA`. |
| Critical | 2026-06-10 09:48 UTC | `juno1pqardc39d558mr58nx5m2wgmy448pv94ehdea0` | `osmo1pqardc39d558mr58nx5m2wgmy448pv9487ajvp` | Juno -> Osmosis | Same attacker raw key; Osmosis row itself is not separately counted in final snapshot because remaining PHMN returned/ended on Juno. | Osmosis receive 12000 PHMN, tx `A4207B416F7AB653A0A7B24190D84D51C961285771A0A543D4FFCCBDEA7D5551`. |
| Critical | 2026-06-10 09:50-09:51 UTC | `juno1pqardc39d558mr58nx5m2wgmy448pv94ehdea0` | `neutron1pqardc39d558mr58nx5m2wgmy448pv94t68qq5` | Juno -> Neutron | Same attacker raw key. | Neutron receives 12000 + 3000 PHMN, txs `3430AC...` and `6D0957...`. |
| Critical | 2026-06-10 09:54-09:59 UTC | `neutron1pqardc39d558mr58nx5m2wgmy448pv94t68qq5` | Astroport PHMN/USDC pool `neutron1muu00...` | Neutron | Astroport pool contract appears in final snapshot with dust 0.000017 PHMN. | Three Neutron swap txs listed in attacker graph. |
| Critical | 2026-06-10 10:06 UTC | `osmo1pqardc39d558mr58nx5m2wgmy448pv9487ajvp` | Noble Orbiter / Solana route `AhT5...` owner `39CA...` | Osmosis -> Noble -> Solana | Solana addresses are not PHMN snapshot addresses. | Osmosis tx `0591E90876DF697008C1D68D08534DE2A7991DD4C817CE508953C8C42B73327C`; Solana tx `4DrTnoj...`. |
| High lead | 2026-06-08 pre-attack funding | `osmo1m8wg4vxkefhs374qxmmqpyusgz289wmulex5qdwpfx7jnrxzer5s9cv83q` | Attacker Noble/Juno/Neutron addresses | Osmosis / Noble / Juno / Neutron | Common funding hub is not in final snapshot. | Attacker graph: funded `noble1pqard...`, `juno1pqard...`, `neutron1pqard...`. |
| High lead | Historical context | `osmo1m8wg4vxkefhs374qxmmqpyusgz289wmulex5qdwpfx7jnrxzer5s9cv83q` | Investigated `juno187jy6...` PHMN/DAS address | Osmosis -> Juno | `juno187jy6...` / `cosmos187jy6...` exact cluster is not in final snapshot. | Attacker graph notes common funding hub also funded previously investigated `juno187...` address. |

## Checks attempted for Cosmos / Osmosis / Neutron account-history scan

The request includes checking derived snapshot addresses on Cosmos Hub, Osmosis, and Neutron for interactions with attacker and Olim addresses.

A full scan needs an account-history indexer. Standard public RPC/LCD endpoints available during this pass did not provide reliable indexed transaction search:

| Chain | Endpoint tested | Result |
| --- | --- | --- |
| Cosmos Hub | local RPC `135.181.227.236:26657`, Polkachu RPC | `tx_search` by `transfer.sender` returned RPC 500. |
| Osmosis | local RPC `135.181.232.241:49657`, Polkachu RPC/API, PublicNode REST/RPC | `tx_search` returned RPC 500 or REST 403. |
| Neutron | `rpc-lb.neutron.org`, PublicNode REST/RPC | `tx_search` returned RPC 500 or REST 403. |
| Mintscan public API | unauthenticated account-history patterns | 401/404; no usable account-history endpoint without API access. |

This report therefore records all confirmed interactions from already-published evidence and exact snapshot matching. A complete all-snapshot cross-chain interaction scan should be run with an indexed data provider such as Mintscan API access, Numia, Range, Flipside, BigQuery/SubQuery, or a locally indexed archive.

## Immediate recommendations

1. Keep the pqard attacker row excluded from normal distribution.
2. Put the `juno1eltl...` / `cosmos1eltl...` snapshot row into manual review before final distribution.
3. Treat the Astroport pool row as contract/LP accounting, not as a normal holder.
4. Keep `osmo1m8wg4...` as a high-priority lead even though it has no final PHMN snapshot balance.
5. Run a second pass with a real account-history indexer across all rows in `phmn_final_snapshot_address_map.csv`.

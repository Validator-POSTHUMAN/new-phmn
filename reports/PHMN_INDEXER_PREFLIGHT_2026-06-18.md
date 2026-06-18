# PHMN indexer preflight

Updated: 2026-06-18

This note defines the minimum checks before building a deeper PHMN interaction indexer for Juno, Osmosis, Cosmos Hub, and related routes.

## Goal

The goal is to turn address-interaction review into reproducible data:

- input seed addresses and labels;
- historical transfer and contract interaction rows;
- classified graph edges;
- false-positive controls for common contracts, routers, pools, DAO contracts, and benign community transfers.

## Current seed input

Operator-provided seed addresses are stored in:

- `inputs/phmn_incident_seed_addresses_2026-06-18.csv`

The seed list intentionally separates:

- `manual_review` addresses: Olim-provided or operator-provided addresses that require investigation;
- `common_context` contracts: addresses such as POSTHUMAN DAS that can connect many normal users and must not be treated as attacker evidence by themselves;
- `not_in_phmn_snapshot` cross-chain addresses: useful for routing context, but not direct PHMN distribution rows.

## Known Juno anchor transaction

Confirmed incident transfer:

- hash: `5AA8C1274E2FC823DCD4DACDC8B951220929D5BA338BFAB57E731CAEBAB737FA`
- observed height: `38734241`
- flow: compromised PHMN minter -> attacker Juno `pqard` address
- amount: `30000 PHMN`

This tx is the first endpoint preflight anchor. A usable endpoint should be able to return the transaction by hash. A fully usable historical endpoint should also support event search by sender, recipient, contract, and relevant wasm attributes.

## Endpoint capability checks

Minimum checks per endpoint:

1. `GET /status`
2. `GET /tx?hash=0x<TX_HASH>`
3. `GET /tx_search?query="tx.hash='<TX_HASH>'"`
4. `GET /tx_search?query="transfer.sender='<ADDRESS>'"`
5. `GET /tx_search?query="transfer.recipient='<ADDRESS>'"`
6. `GET /cosmos/tx/v1beta1/txs?events=...` on LCD/REST endpoints

Passing `/tx` by hash is not enough for graph expansion. For deeper investigation, the source must support event search or must be suitable as a block source for SubQuery or another indexer.

## Initial public Juno endpoint observation

Quick test on 2026-06-18:

- `https://juno-rpc.publicnode.com/tx?hash=0x5AA8...` returned the anchor transaction at height `38734241`.
- Public Juno `tx_search` event queries on PublicNode and Polkachu returned HTTP 500 in this environment.
- Public Juno LCD event queries on PublicNode, Polkachu, and `rest.cosmos.directory/juno` returned HTTP 500 in this environment.

Conclusion: public endpoints may be useful for direct tx-hash verification, but the current public endpoints tested are not sufficient as the only source for mass event-search based relationship mapping.

## Preferred next data sources

Use one of:

- archive/indexed RPC with working Tendermint `tx_search`;
- archive LCD/REST with working `/cosmos/tx/v1beta1/txs?events=...`;
- commercial archive endpoint with clear event search support;
- SubQuery Managed Service or local SubQuery with a historical block source.

## Output tables

The deeper indexer should produce:

- `accounts`: address, chain, cluster, label, source, confidence;
- `transfers`: tx_hash, height, timestamp, chain, sender, recipient, denom, amount, contract, memo;
- `contract_interactions`: tx_hash, height, sender, contract, action, funds, wasm attributes;
- `edges`: src, dst, chain, relation, evidence_class, tx_hash, confidence;
- `edge_classification`: confirmed incident flow, server access evidence, manual review, common contract, benign context, weak lead.

## Distribution policy boundary

Indexer output is evidence, not an automatic exclusion rule.

Only confirmed incident flow should directly affect distribution. Common contract edges, DAO/DAS interactions, treasury payments, and benign community transfers must remain contextual unless supported by stronger evidence.

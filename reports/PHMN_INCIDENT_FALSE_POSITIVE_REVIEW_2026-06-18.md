# PHMN Incident False-Positive Review

Updated: 2026-06-18

This note explains how to read the PHMN attacker / Olim interaction evidence without overstating weak or common-contract links.

## Core Rule

A graph edge is not proof by itself.

The review must distinguish:

- direct wallet-to-wallet transfers;
- same raw-key address clusters;
- server-access evidence;
- DEX / pool / router / IBC infrastructure used by many users;
- SubDAO treasury transfers;
- normal community or operator payments;
- unresolved weak leads.

Only direct incident flow and strongly correlated server/on-chain evidence should be treated as high-confidence attacker evidence.

## Strong Evidence

High-confidence attacker evidence currently includes:

- compromised minter `juno100umj2mnu0u6ujf37c9a3xfy9gl53hu9ekxyyw` minted unauthorized PHMN;
- compromised minter sent `30000 PHMN` to attacker Juno address `juno1pqardc39d558mr58nx5m2wgmy448pv94ehdea0`;
- attacker same raw-key cluster moved PHMN through Juno, Osmosis, and Neutron;
- attacker swapped/sold part of PHMN and routed USDC through Noble / CCTP to Solana;
- server evidence shows unknown SSH access active during the mint/transfer window.

## Weak Or Contextual Evidence

These links are useful for investigation, but must not be treated as proof by themselves:

- a shared DEX or swap contract;
- an Osmosis pool module address;
- an Astroport pool contract;
- Squid/swap-action router contracts;
- IBC escrow or channel contracts;
- SubDAO treasury payments;
- a normal PHMN transfer between community members;
- a common funding-hub relation without direct incident-flow confirmation;
- a Solana route/infrastructure overlap through CCTP.

## Known Benign-Control Address

Operator-provided high-activity PHMN sender:

- `juno1e8238v24qccht9mqc2w0r4luq462yxttdl93mj`

This address has sent PHMN to many users, including Olim-related addresses. That interaction must not be interpreted as attacker evidence by itself.

Use this address as a control when testing graph rules: if a rule would mark this address as attacker-related only because it interacted with Olim or a common PHMN contract, the rule is too broad.

## Recommended Edge Classes

- `confirmed_incident_flow`: unauthorized mint, attacker transfer, sale, bridge, same raw-key attacker movement. Distribution impact: exclude or route to incident bucket.
- `server_access_evidence`: SSH/session/log evidence around the incident window. Distribution impact: manual incident evidence, not a token-flow edge.
- `manual_review`: person-of-interest or operator-provided address needing human review. Distribution impact: do not auto-exclude.
- `common_contract`: DEX, pool, router, escrow, IBC, module contract. Distribution impact: never proof alone.
- `benign_context`: known community/operator activity. Distribution impact: explicit non-attacker context.
- `weak_lead`: funding-hub or route relation that may deserve deeper indexer review. Distribution impact: investigate only.

## Practical Review Checklist

- [ ] Is the edge a direct transfer between two user-controlled wallets?
- [ ] Is the edge only a contract/router/pool interaction?
- [ ] Is either endpoint a module, escrow, pool, or public contract?
- [ ] Is the edge part of the confirmed unauthorized mint / sale / bridge flow?
- [ ] Does the address appear in the final PHMN snapshot?
- [ ] Does exclusion depend on this edge alone?
- [ ] Could the same rule falsely flag the benign-control address?
- [ ] Is a real account-history indexer needed before making a decision?

## Current Assessment

The `pqard...` attacker same-key cluster is strong enough to exclude from normal distribution.

The Olim `eltl` snapshot row remains manual-review evidence, not automatic exclusion, because known links include DAS stake context and person-of-interest server/access context rather than a direct confirmed attacker wallet flow.

The `187` cluster and funding-hub relations remain contextual leads. They need deeper account-history indexing before they can be used for any distribution decision.


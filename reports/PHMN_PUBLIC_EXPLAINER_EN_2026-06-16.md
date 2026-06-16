# What Is Happening With PHMN and What the Team Is Doing Next

[Русская версия](PHMN_PUBLIC_EXPLAINER_RU_2026-06-16.md)

This text is written for regular users without a technical background. More detailed technical materials and snapshot files are published in this repository and in the investigation repository.

## Short Version

PHMN had a serious incident: 30,000 PHMN were minted without authorization, and the attacker tried to sell those tokens through liquidity pools.

The team reacted quickly and withdrew liquidity. Based on the current assessment, the attacker managed to sell roughly half of the unauthorized PHMN. The remaining part is still visible on-chain and will be excluded from recovery.

The key point: PHMN is not disappearing. Honest holders should not lose their PHMN because of the attacker's actions. The team is preparing a new PHMN and a 1:1 distribution to old PHMN holders based on the final snapshot.

## Where To Read More

- Main PHMN migration repository:
  https://github.com/Validator-POSTHUMAN/new-phmn
- Final user-attribution snapshot:
  https://github.com/Validator-POSTHUMAN/new-phmn/blob/main/snapshots/phmn_final_snapshot.csv
- Expanded snapshot rows for audit:
  https://github.com/Validator-POSTHUMAN/new-phmn/blob/main/snapshots/phmn_final_snapshot_expanded_rows.csv
- Final snapshot and distribution policy:
  https://github.com/Validator-POSTHUMAN/new-phmn/blob/main/reports/PHMN_MIGRATION_FINAL_SNAPSHOT_POLICY_V2.md
- DAS staking balance expansion:
  https://github.com/Validator-POSTHUMAN/new-phmn/blob/main/reports/PHMN_DAS_STAKING_EXPANSION_2026-06-16.md
- SubDAO treasury reroute:
  https://github.com/Validator-POSTHUMAN/new-phmn/blob/main/reports/PHMN_SUBDAO_REROUTE_RU_2026-06-16.md
- Checksums for published files:
  https://github.com/Validator-POSTHUMAN/new-phmn/blob/main/checksums/SHA256SUMS
- Unauthorized mint investigation materials:
  https://github.com/Validator-POSTHUMAN/mint-phmn-evidence
- Server investigation report:
  https://github.com/Validator-POSTHUMAN/mint-phmn-evidence/blob/main/artifacts/REPORT.md
- Attacker address graph:
  https://github.com/Validator-POSTHUMAN/mint-phmn-evidence/blob/main/artifacts/phmn-attacker-address-links-2026-06-10.md

## What Happened

According to the collected data and the published investigation materials:

https://github.com/Validator-POSTHUMAN/mint-phmn-evidence

a core team participant, Olim, had service access to the PHMN minter infrastructure and either gave minter access to an attacker or acted as the attacker himself.

Through that access, 30,000 PHMN were minted even though they should not have existed. After that, those PHMN were moved and sold through liquidity pools.

The team detected the problem and urgently withdrew liquidity from the pools to stop further selling. That is why the attacker was not able to sell the entire unauthorized amount.

It is important to understand: this was not a failure of the PHMN idea, tokenomics, or community. It was an abuse of service access to the minter. The team treats this as a criminal act; the final legal assessment belongs to competent authorities.

The situation is similar to a company hiring a known security guard with documents and reputation, and then that guard opens the doors to attackers or helps them get inside.

## Why PHMN Is Not Disappearing

PHMN is not just the old contract. PHMN is part of the POSTHUMAN ecosystem: stakedrops, DAS, community participation, long-term distribution, liquidity, treasury, and governance.

The minter incident does not cancel that. It only forces the next stage to happen faster: restore honest balances, remove the influence of attacker-linked addresses, and continue PHMN development through a new governance structure.

The team's plan is simple:

- fix honest balances so honest holders do not lose anything;
- exclude addresses linked to attackers;
- issue a new PHMN and distribute it 1:1 to old PHMN holders;
- create a new POSTHUMAN DAS and give holders time to lock PHMN to receive Voting Power;
- create new liquidity pools with PHMN paired against BTC and USDC.

## What Has Already Been Done

The team has already done several important things.

Liquidity was withdrawn from the main pools to stop further damage.

BTC that was in the BTC/PHMN pair on Osmosis has already been sent to the new Liquidity SubDAO treasury. PHMN from that pair is still on the old POSTHUMAN core team Ledger address:

`osmo1hyjhy0tp6geral2g9vj9nyteglf8t5q4pqwre8`

That address holds 12,661.70 PHMN. These tokens are not lost. They will be accounted for in the migration and in future liquidity.

Liquidity was also withdrawn from Astroport: 6,415 USDC and 14,652.885449 PHMN. The USDC is already in the new Liquidity SubDAO, while the PHMN remains on the old Liquidity SubDAO treasury and will also be accounted for.

The new Liquidity SubDAO currently holds 16,727 USDC:

- 10,290 USDC - 20% of POSTHUMAN revenue intended for PHMN buybacks;
- 20 USDC - from the old Osmosis Liquidity SubDAO;
- 6,415 USDC - from Astroport liquidity.

The new Liquidity SubDAO also holds 0.08908914 BTC withdrawn from Osmosis liquidity.

## What Happens Next

The near-term plan:

1. Finalize the PHMN holder snapshot.
2. Exclude addresses linked to attackers.
3. Issue the new PHMN.
4. Distribute the new PHMN 1:1 to old PHMN holders.
5. Create the new POSTHUMAN DAS.
6. Open a one-week period when holders can lock PHMN and receive Voting Power.
7. One week after the new PHMN distribution, restore liquidity in PHMN/BTC and PHMN/USDC pairs.

After the final snapshot, old PHMN should no longer affect the right to receive new PHMN. This prevents the attacker from continuing to move unauthorized tokens and interfering with recovery.

## What This Means For Regular Holders

If you honestly held PHMN, you do not need to panic.

The team is working so that honest holders receive the new PHMN 1:1. In other words, for every honestly accounted old PHMN, the holder should receive one new PHMN.

If you locked PHMN in POSTHUMAN DAS, you have even less reason to worry: those balances are visible and will be accounted for. New PHMN will be distributed unlocked, so every holder can decide what to do next.

After the new PHMN distribution, a one-week locking period will open in the new DAS. Holders who lock PHMN will receive Voting Power and will be able to participate in governance.

One week after the new PHMN distribution, the team plans to restore liquidity: new pools will be created with PHMN paired against BTC and USDC, and PHMN trading will resume.

The main point is simple: honest holders are not being left alone with this problem. The team itself is one of the largest PHMN holders and is highly interested in PHMN recovery and development.

## PHMN Is Not Stopping and Continues To Develop

The incident does not stop PHMN. On the contrary, it accelerates the transition to the next stage.

POSTHUMAN continues to develop the ecosystem: validating new networks not only inside Cosmos but also beyond it, developing AI tools, working with fund delegations, and expanding PHMN's role inside the community.

Liquidity SubDAO will continue directing part of POSTHUMAN revenue toward PHMN buybacks. But the approach will change: instead of scheduled buybacks that could create expectations and price manipulation, the buyback model will become more adaptive under Liquidity SubDAO responsibility.

PHMN keeps a strong foundation:

- the team continues working;
- holders will be accounted for through the snapshot;
- DAS and Voting Power will be restored;
- liquidity will return;
- POSTHUMAN revenue will continue supporting PHMN;
- the community will have more real governance over future decisions.

Situations like this are unpleasant. But they often become a trigger for activity, better processes, and faster development.

## What the Community Will Decide

After PHMN recovery and the launch of the new DAS, the community will need to make important decisions.

1. Vote on tokenomics changes.
2. Decide whether PHMN should remain in Cosmos or move to EVM.
3. Choose the network for restoring NFT avatars as AI agents: EVM or NEAR.
4. Decide what to do with PHMN bought back by Liquidity SubDAO: distribute it, burn it, or use another governance-approved model.

This is an important part of recovery. The team is not only bringing liquidity back. The team is restoring decentralized governance and giving the community the ability to define the next stage of PHMN development.

## Key Point

The team is not "restarting PHMN from zero" and is not asking users to forget old balances.

The team is fixing the old state, separating honest holders from attacker-linked addresses, and preparing the new PHMN so that the token's history can continue without the effects of the unauthorized mint.

PHMN continues. Liquidity will be restored. Governance will be restored. And the community will be able to make the key decisions about PHMN's future.


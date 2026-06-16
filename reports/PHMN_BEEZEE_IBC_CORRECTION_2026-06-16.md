# PHMN BeeZee IBC Correction - 2026-06-16

## Summary

A small amount of old PHMN is present on BeeZee through Osmosis -> BeeZee IBC.

This is not additional PHMN supply. It is the same PHMN that was previously
visible in the corrected snapshot as an Osmosis IBC escrow balance.

Correct accounting action:

- remove the Osmosis transfer/channel-340 escrow row from user-facing ownership;
- replace it with the three BeeZee PHMN holder rows;
- keep the corrected total unchanged.

## Verified BeeZee State

BeeZee chain:

`beezee-1`

BeeZee PHMN denom:

`ibc/12C0B8B561AFCFDA3C73DEE0F7F84AA2B860D48493C27E8E81A5D14724FAB08B`

Denom trace on BeeZee:

`transfer/channel-0/transfer/channel-169/cw20:juno1rws84uz7969aaa7pej303udhlkt3j9ca0l3egpcae98jwak9quzq8szn2l`

BeeZee transfer/channel-0 counterparty:

`Osmosis transfer/channel-340`

BeeZee PHMN total supply:

`0.904878 PHMN`

BeeZee PHMN holders:

- `bze1z3mkcr2jz424w6m49frgjmy9uhlrx69phqwg3l` - `0.587395 PHMN`
- `bze18mhtjwczlzqqgvw84uz8lrdv4hqule3jp8allp` - `0.310000 PHMN`
- `bze1aeqpudy590y4s02mk0dmgmyfe9crlnlzlz5n0l` - `0.007483 PHMN`

## Osmosis Escrow Link

Osmosis channel:

`transfer/channel-340`

Counterparty:

`BeeZee transfer/channel-0`

Osmosis ICS20 escrow address for transfer/channel-340:

`osmo1k67mnu27xfsdnzzh8rsh078qvstsdu0cfwzp0z`

The escrow derivation for transfer/channel-340 matches this address, and its
PHMN balance is exactly:

`0.904878 PHMN`

Therefore the Osmosis row is not an end user holder. It is the escrow backing
the BeeZee voucher supply.

## Corrected Snapshot Impact

Previous corrected canonical ownership total:

`121822.000000 PHMN`

Updated canonical ownership total with BeeZee end holders:

`121822.000000 PHMN`

Total change:

`0.000000 PHMN`

Recipient mapping change:

- before: `0.904878 PHMN` was assigned to Osmosis escrow address `osmo1k67mnu27xfsdnzzh8rsh078qvstsdu0cfwzp0z`;
- after: `0.904878 PHMN` is assigned to the three BeeZee holder addresses.

## Updated Files

- `canonical_ownership_current_with_beezee.csv`
- `canonical_ownership_current_with_beezee.json`
- `beezee_phmn_owners.csv`
- `beezee_phmn_owners.json`
- `beezee_multihop_reconciliation.csv`
- `beezee_multihop_reconciliation.json`
- `summary_beezee_corrected.json`

## Plain-Language Meaning

The BeeZee DEX balance does not increase the total PHMN amount.

It only shows that a very small part of PHMN moved one more hop:

`Juno -> Osmosis -> BeeZee`

For migration, that PHMN should go to the BeeZee holders, not to the Osmosis
escrow address that temporarily holds the backing voucher balance.

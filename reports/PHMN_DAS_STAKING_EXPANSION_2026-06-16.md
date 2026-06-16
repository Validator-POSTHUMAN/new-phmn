# PHMN DAS Staking Expansion

Date: 2026-06-16

This update expands the POSTHUMAN DAS staking contract row into user-level
ownership rows.

## Reason

The previous public snapshots/phmn_final_snapshot.csv included the DAS
staking contract as one aggregate holder:

53919.085804 PHMN

That accounting was supply-correct, but it was confusing for users whose PHMN
was staked or unbonding through the DAS staking contract. Their personal row
showed only direct wallet PHMN, while the staked or pending-claim PHMN was
held by the staking contract.

## Change

The public snapshots/phmn_final_snapshot.csv is now a user-attribution
snapshot. For each Cosmos-equivalent address it shows:

- direct or IBC-voucher PHMN;
- active DAS staked PHMN;
- pending DAS unstaking / claim PHMN;
- total PHMN attributed to that address.

Audit files:

- snapshots/phmn_final_snapshot_expanded_rows.csv - source rows after
  replacing the DAS staking aggregate row with staking/claim rows.
- adjustments/das_staking_breakdown.csv - only the DAS staking expansion rows.

## DAS Staking Accounting

- Staking contract:
  juno1jktfdt5g2d0fguvy8r8pl4gly7wps8phkwy08z6upc4nazkumrwq7lj0vn
- Aggregate row replaced:
  53919.085804 PHMN
- Active staked:
  50656.015662 PHMN
- Pending claims from raw contract claims state:
  3263.060141 PHMN
- Unattributed residual left on the staking contract:
  0.010001 PHMN

The residual is not assigned to a user because it is not present in active
stake or raw claims state. It remains visible as a residual row on the
staking contract.

## Supply Check

- Previous corrected total:
  121822.000000 PHMN
- New user-attribution total:
  121822.000000 PHMN

The total did not change. Only ownership attribution changed.

## Example

Address:

juno1zwtv7pplzh7m3t4m2zel8c0q78qsyptv8eqnk6

Updated attribution:

- Direct PHMN:
  3.536226 PHMN
- DAS pending claim:
  194.479048 PHMN
- Total:
  198.015274 PHMN


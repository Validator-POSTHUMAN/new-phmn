# Liquidity SubDAO: Pool Creation and PHMN Buyback

## Context

Liquidity SubDAO acts simultaneously in two roles:

1. **Liquidity Provider** — creates a PHMN/USDC pool on Osmosis DEX, seeding both sides
2. **PHMN Buyer** — uses additional USDC to buy back PHMN from the same pool

Pool parameters and buyback volume are calibrated to achieve the target asset ratio
in the pool after the operation completes.

---

## Input Data

| Parameter | Value |
|-----------|-------|
| PHMN in pool (initial) | 27,313 |
| USDC in pool (initial) | 11,624 |
| Swap fee | 0% |
| USDC for PHMN buyback | 11,526 |
| Pool type | Balancer 50/50 |
| AMM model | Constant Product: `x · y = k` |

---

## Buyback Calculation

### Model: Constant Product AMM (x · y = k)

An Osmosis Balancer pool with equal weights (50/50) uses the formula:

```
x · y = k
```

where `x` — PHMN amount, `y` — USDC amount, `k` — invariant constant.

### Step 1: Pool constant before the swap

```
k = PHMN_initial × USDC_initial
k = 27,313 × 11,624
k = 317,486,312
```

### Step 2: New USDC balance after buyer deposits

```
USDC_after = USDC_initial + USDC_swap_in
USDC_after = 11,624 + 11,526 = 23,150
```

### Step 3: New PHMN balance (from invariant preservation)

```
PHMN_after = k / USDC_after
PHMN_after = 317,486,312 / 23,150
PHMN_after ≈ 13,714.3115
```

### Step 4: PHMN amount received by the buyer

```
PHMN_received = PHMN_initial − PHMN_after
PHMN_received = 27,313 − 13,714.3115
PHMN_received ≈ 13,598.6885
```

---

## Pool State: Before and After

| Metric | Before Buyback | After Buyback | Δ |
|--------|---------------|---------------|---|
| PHMN in pool | 27,313 | 13,714.31 | −13,598.69 |
| USDC in pool | 11,624 | 23,150 | +11,526 |
| Constant k | 317,486,312 | 317,486,312 | 0 |
| PHMN price (USDC) | 0.4256 | 1.6880 | +296.6% |

---

## Liquidity SubDAO Fund Flow Summary

### Deposited into pool (liquidity provision)

| Asset | Amount |
|-------|--------|
| PHMN | 27,313 |
| USDC | 11,624 |

### PHMN buyback (swap)

| Asset | Amount |
|-------|--------|
| USDC spent | 11,526 |
| PHMN received | 13,598.69 |

### Net result

| Item | PHMN | USDC |
|------|------|------|
| Deposited into pool | −27,313 | −11,624 |
| Spent on buyback | — | −11,526 |
| Received from buyback | +13,598.69 | — |
| **Net result** | **−13,714.31** | **−23,150** |

> After the operation, Liquidity SubDAO holds the pool's LP tokens,
> representing the remaining **13,714.31 PHMN** and **23,150 USDC** in the pool.
>
> The bought-back 13,598.69 PHMN are sent to the Liquidity SubDAO treasury.

---

## Economic Rationale

### Objectives

The operation aims to address the consequences of the **unauthorized mint of excess
PHMN**. Specific objectives:

1. **Minimize losses for PHMN holders** — buying back excess supply from the market
   reduces sell pressure and restores token equilibrium.

2. **Prevent MEV attacks** — executing the buyback through a proprietary liquidity pool
   eliminates the possibility of frontrunning and sandwich attacks by bots, which are
   inevitable with large market orders in public pools.

3. **Protect against bot and script speculation** — the controlled environment of a
   proprietary pool prevents automated systems from extracting value at the expense
   of PHMN holders.

4. **Protect PHMN holder interests** — all actions are performed by Liquidity SubDAO
   in accordance with the mandate received from PHMN governance.

### Mechanics

1. **Controlled liquidity pool creation** — Liquidity SubDAO solely seeds the pool,
   ensuring full control over parameters and eliminating external influence during
   the buyback phase.

2. **Large-volume buyback** (11,526 USDC — nearly equal to the entire USDC in the pool)
   enables removal of a significant amount of PHMN from circulation in a single
   transaction, without slippage benefiting third parties.

3. **Post-buyback pool ratio** (13,714 PHMN / 23,150 USDC) establishes a new
   PHMN market price of ≈ 1.69 USDC on Osmosis DEX.

### Future Use of Bought-Back PHMN

The bought-back **13,598.69 PHMN** are sent to the **Liquidity SubDAO treasury**
and will be used **exclusively** for:

- Creating new liquidity pools with PHMN
- Any other decisions voted on by PHMN holders who lock their tokens in
  **POSTHUMAN DAS**

---

## Why Swap Fee = 0

Liquidity SubDAO is the **sole liquidity provider** in the pool
(holds 100% of LP tokens). In Osmosis, as in other AMMs, swap fees are
distributed among LP token holders proportionally to their share.

Since all LP tokens belong to Liquidity SubDAO:

- **Any swap fee paid during the swap is immediately returned to the same
  Liquidity SubDAO** as fee revenue accrued to the LP position.
- For a sole LP, the fee is effectively moving funds from one pocket to another,
  with no impact on the net balance.

Therefore, for calculation purposes, the **swap fee is effectively 0 at any
nominal value**, and the `x·y = k` formula is applied without adjustments.

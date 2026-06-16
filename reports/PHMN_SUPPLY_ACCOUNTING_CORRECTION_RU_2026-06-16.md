# PHMN supply accounting correction — 2026-06-16

## Короткий вывод

Да, в предыдущем отчёте была ошибка учёта.

Я сложил:

- Juno CW20 holder state;
- Osmosis IBC voucher holders;
- Neutron IBC voucher holders.

Так делать нельзя, потому что PHMN — это CW20 на Juno. Когда PHMN уходит через IBC, исходные CW20 tokens на Juno не сжигаются. Они лежат в Juno ICS20 escrow contract, а на Osmosis/Neutron появляются voucher tokens.

Поэтому сумма `157146.920311 PHMN` была double-counted cross-chain holder view, а не реальный supply.

Реальный minted supply сейчас:

`121822.000000 PHMN`

Cap в контракте:

`131072.000000 PHMN`

Оставшаяся mint capacity:

`9250.000000 PHMN`

То есть supply не превышает cap.

## Проверка контракта

Juno PHMN contract:

`juno1rws84uz7969aaa7pej303udhlkt3j9ca0l3egpcae98jwak9quzq8szn2l`

Smart query `token_info`:

- total_supply: `121822000000`
- decimals: `6`
- total_supply PHMN: `121822.000000`

Smart query `minter`:

- minter: `juno100umj2mnu0u6ujf37c9a3xfy9gl53hu9ekxyyw`
- cap: `131072000000`
- cap PHMN: `131072.000000`

## Где появилась ошибка

В Juno holder snapshot есть два больших contract holder rows:

- `juno1v4887y83d6g28puzvt8cl0f3cdhd3y6y9mpysnsp3k8krdm7l6jqgm0rkn`
  - label: `ICS20 contract`
  - amount: `20927.290666 PHMN`
  - это backing escrow для Osmosis PHMN vouchers
- `juno1vw6l0gjwju73chh0nqc097347r7ucdx7vshm38qp25xr36wckhqsepcmsd`
  - label: `ICS20 Neutron`
  - amount: `14758.684333 PHMN`
  - это backing escrow для Neutron PHMN vouchers

Эти amounts уже входят в Juno total supply. Если сверху добавить Osmosis/Neutron voucher holders, получится double count.

Проверка совпадения:

- Juno Osmosis escrow: `20927.290666 PHMN`
- Osmosis PHMN bank supply: `20927.290666 PHMN`
- Juno Neutron escrow: `14758.684333 PHMN`
- Neutron PHMN bank supply: `14758.684333 PHMN`

## Правильная модель

Для supply:

`real PHMN supply = Juno CW20 total_supply = 121822.000000 PHMN`

Для distribution ownership:

1. Берём Juno holders.
2. Исключаем Juno ICS20 escrow contract rows.
3. Вместо них учитываем actual holders на Osmosis и Neutron.
4. Для Osmosis остаётся caveat: denom-owner rows ниже bank supply на `361.054688 PHMN`. В corrected file это вынесено отдельной unresolved accounting-gap строкой.

Corrected canonical ownership с gap сходится к реальному supply:

`121822.000000 PHMN`

## Что это меняет в предыдущих выводах

Предыдущая сумма `157146.920311 PHMN` не должна использоваться как supply или final allocation total.

Она полезна только как техническая сумма raw rows из трёх источников, но она double-counted и не подходит для публичного accounting.

Правильная верхняя сумма для нового PHMN distribution должна исходить из:

`121822.000000 PHMN`

Дальше поверх неё применяются:

- attacker exclusions/quarantine;
- compromised minter policy;
- SubDAO treasury reroute adjustment;
- contract / LP / DAO / escrow reconciliation;
- unresolved Osmosis denom-owner gap handling.

## Files

Output directory:

`data/phmn-snapshots/2026-06-16-supply-correction/`

Files:

- `summary_corrected.json` — corrected supply summary.
- `escrow_reconciliation.csv` — Juno escrow vs destination bank supply.
- `canonical_ownership_current.csv` — ownership-oriented snapshot: Juno non-escrow holders + destination voucher holders + Osmosis unresolved gap.
- `SHA256SUMS` — checksums.

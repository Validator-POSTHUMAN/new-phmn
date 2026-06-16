# PHMN BeeZee IBC Correction - 2026-06-16

## Кратко

Небольшое количество старого PHMN находится на BeeZee через IBC-маршрут Osmosis -> BeeZee.

Это не дополнительный PHMN supply. Это тот же PHMN, который в исправленном снапшоте раньше был виден как Osmosis IBC escrow balance.

Правильное accounting action:

- убрать Osmosis transfer/channel-340 escrow row из user-facing ownership;
- заменить его на три BeeZee PHMN holder rows;
- оставить общий corrected total без изменений.

## Проверенное состояние BeeZee

BeeZee chain:

`beezee-1`

BeeZee PHMN denom:

`ibc/12C0B8B561AFCFDA3C73DEE0F7F84AA2B860D48493C27E8E81A5D14724FAB08B`

Denom trace на BeeZee:

`transfer/channel-0/transfer/channel-169/cw20:juno1rws84uz7969aaa7pej303udhlkt3j9ca0l3egpcae98jwak9quzq8szn2l`

Counterparty для BeeZee transfer/channel-0:

`Osmosis transfer/channel-340`

BeeZee PHMN total supply:

`0.904878 PHMN`

BeeZee PHMN holders:

- `bze1z3mkcr2jz424w6m49frgjmy9uhlrx69phqwg3l` - `0.587395 PHMN`
- `bze18mhtjwczlzqqgvw84uz8lrdv4hqule3jp8allp` - `0.310000 PHMN`
- `bze1aeqpudy590y4s02mk0dmgmyfe9crlnlzlz5n0l` - `0.007483 PHMN`

## Связь с Osmosis escrow

Osmosis channel:

`transfer/channel-340`

Counterparty:

`BeeZee transfer/channel-0`

Osmosis ICS20 escrow address для transfer/channel-340:

`osmo1k67mnu27xfsdnzzh8rsh078qvstsdu0cfwzp0z`

Escrow derivation для transfer/channel-340 совпадает с этим адресом. Его PHMN balance точно равен:

`0.904878 PHMN`

Значит Osmosis row не является конечным user holder. Это escrow, который обеспечивает BeeZee voucher supply.

## Влияние на corrected snapshot

Предыдущий corrected canonical ownership total:

`121822.000000 PHMN`

Updated canonical ownership total с end holders:

`121822.000000 PHMN`

Изменение total:

`0.000000 PHMN`

Изменение recipient mapping:

- раньше `0.904878 PHMN` были привязаны к Osmosis escrow address `osmo1k67mnu27xfsdnzzh8rsh078qvstsdu0cfwzp0z`;
- теперь `0.904878 PHMN` привязаны к трём verified end-holder addresses.

## Простыми словами

BeeZee DEX balance не увеличивает общий PHMN amount.

Он только показывает, что очень маленькая часть PHMN прошла ещё один IBC-hop:

`Juno -> Osmosis -> BeeZee`

Для миграции этот PHMN должен попасть к конечным holders, а не к Osmosis escrow address, который временно держит backing voucher balance.


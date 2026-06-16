# PHMN SubDAO treasury reroute adjustment — 2026-06-16

## Короткий вывод

Создан отдельный adjustment layer для финального PHMN distribution snapshot.

Смысл: PHMN, который в старом snapshot лежит на treasury адресах старых SubDAO, не должен отправляться обратно на старые treasury addresses при выпуске нового PHMN. Эти amounts должны быть перенаправлены на новые DAO treasury addresses на Cosmos Hub.

Это не меняет исторический holder snapshot. Это отдельный слой правил поверх snapshot для финального распределения нового PHMN.

## Новые SubDAO treasury destinations

### Strategic SubDAO New

DAO:
https://daodao.zone/dao/cosmos146s5j3t7gh2g37ywm47dp8avhesu2htvjjaxq7z55e7xj0rq0k8q5qnjjy

Treasury addresses:

- Cosmos: `cosmos146s5j3t7gh2g37ywm47dp8avhesu2htvjjaxq7z55e7xj0rq0k8q5qnjjy`
- Juno: `juno1tuk72phdvmv4e0fz38mmvg5syrvtsnqelkj54ym7pqzfg2379lysdsayk2`
- Osmosis: `osmo1wj0hxnk3x0fwl2yqfxtus8sasa5her0enxc39mjvtjwlpn3wa2nszyphdd`

### Liquidity SubDAO New

DAO:
https://daodao.zone/dao/cosmos1pu90e2gm2kq9lvheqzrh0tl9dw5aqg6v5gr9jug2eqdel0vzuxkqvg72nn

Treasury addresses:

- Cosmos: `cosmos1pu90e2gm2kq9lvheqzrh0tl9dw5aqg6v5gr9jug2eqdel0vzuxkqvg72nn`
- Juno: `juno1zm2cze0fcqstwfurgmjkwhu8cgvt6y7an33qu3k0p8g7mlp3l5rs0ez8ql`
- Osmosis: `osmo13r98mdfg3f0xzvk40y6q7whm8lx9793ge2td45fadezgls9zjjzsjfrgnl`

## Reroute totals from the 2026-06-16 PHMN snapshot

Source snapshot:
`data/phmn-snapshots/2026-06-16-current-final-check/combined_current.json`

### To Liquidity SubDAO New

Old treasury rows found:

- `juno16rd66nkhuc2qvzarqs28z0l6gk50qy5w0jdwk2xygtkjz5kclu9qlsyxl4` — `3056.690993 PHMN`
- `neutron1prefwzgnqm0yp579027gt6hl0vlh3ywqt30weknvcgev4r7v0wqqrhl7ry` — `14652.885449 PHMN`

Total to reroute to Liquidity SubDAO New:

`17709.576442 PHMN`

Destination:

`cosmos1pu90e2gm2kq9lvheqzrh0tl9dw5aqg6v5gr9jug2eqdel0vzuxkqvg72nn`

### To Strategic SubDAO New

Old treasury rows found: `15`

Total to reroute to Strategic SubDAO New:

`3276.387140 PHMN`

Destination:

`cosmos146s5j3t7gh2g37ywm47dp8avhesu2htvjjaxq7z55e7xj0rq0k8q5qnjjy`

## Grand total

Total PHMN covered by this SubDAO reroute adjustment:

`20985.963582 PHMN`

Found rows: `17`

Not found rows: `0`

## How to apply this to final distribution

When building the final new PHMN distribution file:

1. Keep the original old-chain source rows for auditability.
2. Mark these old treasury rows as rerouted.
3. Do not send new PHMN to the old snapshot-derived destination for those rows.
4. Send the exact amounts to the new Cosmos treasury destination:
   - old Liquidity SubDAO treasury rows -> `cosmos1pu90e2gm2kq9lvheqzrh0tl9dw5aqg6v5gr9jug2eqdel0vzuxkqvg72nn`
   - other old SubDAO treasury rows -> `cosmos146s5j3t7gh2g37ywm47dp8avhesu2htvjjaxq7z55e7xj0rq0k8q5qnjjy`
5. Preserve the old address, old chain, source amount, and reroute destination in the final CSV.

## Files

- `subdao_reroute_adjustments.csv` — row-level adjustment file.
- `subdao_reroute_adjustments.json` — machine-readable adjustment file.
- `summary.json` — totals and destination metadata.
- `SHA256SUMS` — checksums.

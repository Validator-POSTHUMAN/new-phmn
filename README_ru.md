# Миграция PHMN: финальный снапшот и правила распределения

[English version](README.md)

Публичное объяснение простым языком:

- [Что происходит с PHMN и что команда делает дальше](reports/PHMN_PUBLIC_EXPLAINER_RU_2026-06-16.md)
- [English version](reports/PHMN_PUBLIC_EXPLAINER_EN_2026-06-16.md)

## Кратко

POSTHUMAN готовит миграцию старого PHMN в новый PHMN на Cosmos Hub через TokenFactory.

У нового PHMN будет такой же максимальный supply, как у старого токена:

`131,072 PHMN`

Перед созданием и распределением нового токена мы публикуем финальный снапшот владения старым PHMN. Этот снапшот будет базой для распределения нового PHMN.

После публикации снапшота любые переводы старого PHMN не будут влиять на распределение нового PHMN. Если баланс старого PHMN изменится после публикации, для миграции это изменение будет проигнорировано.

## Почему мы это делаем

В старом PHMN-контракте на Juno был скомпрометирован minter. Из-за этого произошёл неавторизованный mint.

Чтобы защитить держателей PHMN и сделать будущий governance безопаснее, POSTHUMAN переносит PHMN в новый TokenFactory-токен на Cosmos Hub.

Новая схема устроена так:

- пользователи получают новый PHMN по финальному опубликованному снапшоту;
- incident-related адреса не получают новый PHMN как обычные держатели;
- treasury-балансы SubDAO переводятся на новые treasury-адреса SubDAO;
- весь нераспределённый и резервный PHMN контролируется новым Strategic SubDAO;
- крупные объёмы PHMN не смогут попасть на рынок без governance proposal и approval SubDAO.

## Правило финального снапшота

Финальный migration snapshot учитывает старые PHMN-балансы во всех проверенных сетях и IBC-локациях, где существует старый PHMN.

Снапшот исправлен с учётом IBC accounting.

Это важно, потому что старый PHMN — это CW20-токен на Juno. Когда PHMN уходит через IBC в другие сети, оригинальные CW20-токены остаются заблокированы в Juno IBC escrow contracts, а на destination chain появляются voucher tokens.

Поэтому нельзя просто сложить raw balances из разных сетей. Так один и тот же PHMN будет посчитан дважды.

Исправленная модель учёта:

1. Считаем обычных Juno holders.
2. Исключаем Juno IBC escrow contract balances.
3. Считаем реальные destination-chain PHMN voucher holders.
4. Для multi-hop IBC считаем финальную holder-chain, если она проверена.
5. Неразрешённые accounting gaps оставляем в quarantine до ручной проверки.

Исправленный old PHMN supply:

`121,822 PHMN`

Финальная multi-hop IBC проверка разрешила `0.904878 PHMN`, которые раньше были привязаны к промежуточному channel escrow address. Это не меняет общий corrected total. Меняется только финальная карта получателей: escrow row заменён на проверенные end-holder rows.

Старый contract cap:

`131,072 PHMN`

Незаминченная ёмкость старого токена:

`9,250 PHMN`

## Что происходит после публикации

После публикации финального снапшота:

- переводы старого PHMN после публикации не учитываются;
- покупки или продажи старого PHMN после публикации не меняют распределение нового PHMN;
- финальное распределение использует опубликованный snapshot и correction rules;
- любые дальнейшие движения старого PHMN не имеют значения для миграции.

Это защищает пользователей от last-minute balance manipulation и даёт всем понятную публичную точку отсчёта.

## Исключённые и quarantined балансы

Некоторые балансы не будут распределены на старый snapshot address.

Сюда входят:

- подтверждённый attacker address cluster;
- compromised minter address, если команда отдельно не опубликует другое решение;
- адреса и связанные clusters, исключённые по результатам incident investigation;
- unresolved accounting rows, которые пока нельзя безопасно сопоставить с пользователем.

Подтверждённый attacker cluster сейчас держит:

`15,100 PHMN`

Compromised minter address сейчас держит:

`2,032.149313 PHMN`

Эти балансы не будут считаться обычными user allocations.

Excluded и quarantined PHMN останутся под DAO-controlled handling, а не будут отправлены incident-related или неясным адресам.

## Перенаправление SubDAO treasury

Часть старого PHMN принадлежит POSTHUMAN SubDAO treasuries.

Эти балансы видны в снапшоте, но они не должны быть отправлены обратно на старые treasury-адреса. Они будут перенаправлены на новые treasury-адреса SubDAO.

### New Strategic SubDAO

DAO:

https://daodao.zone/dao/cosmos146s5j3t7gh2g37ywm47dp8avhesu2htvjjaxq7z55e7xj0rq0k8q5qnjjy

New Cosmos treasury:

`cosmos146s5j3t7gh2g37ywm47dp8avhesu2htvjjaxq7z55e7xj0rq0k8q5qnjjy`

Old SubDAO treasury balances, redirected to Strategic SubDAO New:

`3,276.387140 PHMN`

### New Liquidity SubDAO

DAO:

https://daodao.zone/dao/cosmos1pu90e2gm2kq9lvheqzrh0tl9dw5aqg6v5gr9jug2eqdel0vzuxkqvg72nn

New Cosmos treasury:

`cosmos1pu90e2gm2kq9lvheqzrh0tl9dw5aqg6v5gr9jug2eqdel0vzuxkqvg72nn`

Old Liquidity SubDAO treasury balances, redirected to Liquidity SubDAO New:

`17,709.576442 PHMN`

Эти reroutes не меняют общий PHMN supply. Они меняют только destination address для treasury-owned PHMN в новом распределении.

## План минта нового токена

Новый PHMN на Cosmos Hub будет создан с тем же максимальным supply, что и старый PHMN:

`131,072 PHMN`

POSTHUMAN планирует сразу создать полный объём.

Дальше:

- eligible snapshot amount будет распределён пользователям и treasury destinations по опубликованным правилам;
- excluded или quarantined balances не будут отправлены excluded addresses;
- весь оставшийся PHMN будет отправлен в новый Strategic SubDAO treasury.

Strategic SubDAO будет отвечать за будущие PHMN allocations, например stake-drops и reserves.

Цель: никакой крупный объём PHMN не сможет выйти на рынок без governance proposal и multisig approval. Intended control policy: минимум 3 из 5 signers.

## Что нужно делать пользователям

На этом этапе обычным пользователям не нужно двигать старый PHMN.

Главное правило:

Не рассчитывайте, что переводы старого PHMN после публикации финального снапшота повлияют на распределение.

Если вы переведёте старый PHMN после публикации снапшота, распределение нового PHMN всё равно будет использовать ваш баланс из опубликованного снапшота.

## Опубликованные файлы

Актуальные migration accounting artifacts:

- Snapshot CSV: [snapshots/phmn_final_snapshot.csv](snapshots/phmn_final_snapshot.csv)
- Expanded source rows: [snapshots/phmn_final_snapshot_expanded_rows.csv](snapshots/phmn_final_snapshot_expanded_rows.csv)
- DAS staking breakdown: [adjustments/das_staking_breakdown.csv](adjustments/das_staking_breakdown.csv)
- SubDAO reroute adjustment: [adjustments/subdao_reroute_adjustments.csv](adjustments/subdao_reroute_adjustments.csv)
- BeeZee IBC reconciliation: [adjustments/beezee_multihop_reconciliation.csv](adjustments/beezee_multihop_reconciliation.csv)
- Snapshot address map: [snapshots/phmn_final_snapshot_address_map.csv](snapshots/phmn_final_snapshot_address_map.csv)
- Attacker/Olim interaction review: [reports/PHMN_ATTACKER_OLIM_INTERACTION_REVIEW_2026-06-16.md](reports/PHMN_ATTACKER_OLIM_INTERACTION_REVIEW_2026-06-16.md)
- Attacker/Olim interaction CSV: [adjustments/attacker_olim_interaction_review_2026-06-16.csv](adjustments/attacker_olim_interaction_review_2026-06-16.csv)
- Public explainer RU: [reports/PHMN_PUBLIC_EXPLAINER_RU_2026-06-16.md](reports/PHMN_PUBLIC_EXPLAINER_RU_2026-06-16.md)
- Public explainer EN: [reports/PHMN_PUBLIC_EXPLAINER_EN_2026-06-16.md](reports/PHMN_PUBLIC_EXPLAINER_EN_2026-06-16.md)
- Reports: [reports/](reports/)
- Checksums: [checksums/SHA256SUMS](checksums/SHA256SUMS)

### Финальный ownership snapshot

[`phmn_final_snapshot.csv`](snapshots/phmn_final_snapshot.csv)

Это user-attribution snapshot по всем проверенным сетям. Он показывает direct/IBC-voucher PHMN, active DAS stake, pending DAS claim и итоговый total PHMN для каждого Cosmos-equivalent адреса.

Он исключает double-counting Juno IBC escrow, учитывает проверенные multi-hop IBC balances, раскрывает DAS staking contract в user-level строки и сходится к:

`121,822 PHMN`

SHA-256:

`ddf01379371c848512a96565559debd369a3dfba8ab6a0a5ab3dbdd75f4004b5`

DAS staking expansion заменил старую aggregate строку staking contract на user-level active stake и pending-claim строки. Общий supply не изменился.

Audit files:

- [`phmn_final_snapshot_expanded_rows.csv`](snapshots/phmn_final_snapshot_expanded_rows.csv)
- [`das_staking_breakdown.csv`](adjustments/das_staking_breakdown.csv)
- [`PHMN_DAS_STAKING_EXPANSION_2026-06-16.md`](reports/PHMN_DAS_STAKING_EXPANSION_2026-06-16.md)

### Supply accounting correction report

[`PHMN_SUPPLY_ACCOUNTING_CORRECTION_RU_2026-06-16.md`](reports/PHMN_SUPPLY_ACCOUNTING_CORRECTION_RU_2026-06-16.md)

### BeeZee IBC correction report

[`PHMN_BEEZEE_IBC_CORRECTION_RU_2026-06-16.md`](reports/PHMN_BEEZEE_IBC_CORRECTION_RU_2026-06-16.md)

### SubDAO reroute adjustment

[`subdao_reroute_adjustments.csv`](adjustments/subdao_reroute_adjustments.csv)

## Простыми словами

- Мы сделали финальный снапшот старых PHMN-балансов.
- Мы исправили IBC accounting, чтобы один и тот же PHMN не считался дважды.
- Переводы после публикации не влияют на миграцию.
- Attacker и incident-related addresses не получат новый PHMN как обычные holders.
- PHMN, принадлежащий SubDAO treasuries, будет отправлен в новые SubDAO treasuries.
- Новый токен сохранит прежний лимит supply.
- Оставшийся PHMN reserve будет контролироваться новым Strategic SubDAO.

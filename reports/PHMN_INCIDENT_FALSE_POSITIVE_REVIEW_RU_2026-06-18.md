# PHMN: проверка ложных связей

Обновлено: 2026-06-18

Этот документ объясняет, как читать доказательства по взаимодействиям адресов атакера, Олима и других адресов, не преувеличивая слабые связи и связи через общие контракты.

## Главное правило

Сам факт ребра в графе не является доказательством.

При проверке нужно разделять:

- прямые переводы между пользовательскими кошельками;
- кластеры адресов с одним raw key;
- доказательства по доступу к серверу;
- DEX / pool / router / IBC инфраструктуру, которой пользуются многие;
- переводы из treasury SubDAO;
- обычные community или operator payments;
- слабые следы, которые пока не доказаны.

Только прямой поток инцидента и сильно коррелирующие серверные/on-chain доказательства должны считаться доказательствами атакера с высокой уверенностью.

## Сильные доказательства

Сейчас к доказательствам атакера с высокой уверенностью относятся:

- скомпрометированный minter `juno100umj2mnu0u6ujf37c9a3xfy9gl53hu9ekxyyw` выпустил неавторизованный PHMN;
- скомпрометированный minter отправил `30000 PHMN` на Juno-адрес атакера `juno1pqardc39d558mr58nx5m2wgmy448pv94ehdea0`;
- кластер атакера с одним raw key двигал PHMN через Juno, Osmosis и Neutron;
- атакер обменял/продал часть PHMN и вывел USDC через Noble / CCTP в Solana;
- серверные доказательства показывают неизвестный SSH-доступ во время окна mint/transfer.

## Слабые или контекстные связи

Эти связи полезны для расследования, но сами по себе не являются доказательством:

- общий DEX или swap contract;
- Osmosis pool module address;
- Astroport pool contract;
- Squid/swap-action router contracts;
- IBC escrow или channel contracts;
- SubDAO treasury payments;
- обычный PHMN transfer между участниками сообщества;
- связь через общий funding hub без прямого подтверждения потока инцидента;
- пересечение маршрута через Solana CCTP инфраструктуру.

## Известный benign-control адрес

Адрес активного отправителя PHMN, предоставленный оператором:

- `juno1e8238v24qccht9mqc2w0r4luq462yxttdl93mj`

Этот адрес отправлял PHMN многим пользователям, включая адреса, связанные с Olim. Такое взаимодействие не должно интерпретироваться как доказательство связи с атакером само по себе.

Используйте этот адрес как контрольный пример: если правило помечает его как связанный с атакером только потому, что он взаимодействовал с Olim или общим PHMN contract, правило слишком широкое.

## Рекомендуемые классы рёбер

- `confirmed_incident_flow`: неавторизованный mint, перевод атакера, продажа, bridge, движение атакера с тем же raw key. Влияние на distribution: исключить или отправить в incident bucket.
- `server_access_evidence`: SSH/session/log доказательства вокруг окна инцидента. Влияние на distribution: ручное доказательство инцидента, не token-flow edge.
- `manual_review`: person-of-interest или адрес, предоставленный оператором, требующий ручной проверки. Влияние на distribution: не исключать автоматически.
- `common_contract`: DEX, pool, router, escrow, IBC, module contract. Влияние на distribution: никогда не является доказательством само по себе.
- `benign_context`: известная активность сообщества или оператора. Влияние на distribution: явный контекст, не связанный с атакером.
- `weak_lead`: funding-hub или route relation, требующий более глубокой проверки через indexer. Влияние на distribution: только расследовать.

## Практический чеклист проверки

- [ ] Это прямой transfer между двумя user-controlled wallets?
- [ ] Или это только взаимодействие с contract/router/pool?
- [ ] Является ли один из endpoint module, escrow, pool или public contract?
- [ ] Является ли edge частью подтверждённого unauthorized mint / sale / bridge flow?
- [ ] Присутствует ли адрес в final PHMN snapshot?
- [ ] Зависит ли exclusion только от этого edge?
- [ ] Может ли это же правило ложно пометить benign-control address?
- [ ] Нужен ли реальный account-history indexer перед решением?

## Текущая оценка

`pqard...` кластер атакера с тем же raw key достаточно подтверждён для исключения из normal distribution.

Olim `eltl` snapshot row остаётся доказательством для ручной проверки, а не automatic exclusion, потому что известные links включают DAS stake context и person-of-interest server/access context, но не прямой confirmed attacker wallet flow.

`187` cluster и funding-hub relations остаются контекстными следами. Для использования в distribution decision им нужен более глубокий account-history indexing.

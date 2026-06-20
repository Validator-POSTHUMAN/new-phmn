# PHMN: старые адреса, которые не получают новый PHMN

Дата: 2026-06-20

Этот реестр перечисляет старые адреса, на которых есть старый PHMN, но новый PHMN напрямую на эти адреса или на механически пересчитанные `cosmos...` адреса отправляться не должен. Для каждой строки указано почему и куда сумма попадает в corrected broadcast/handling.

## Итог

- Строк: 66
- Сумма старого PHMN в этих строках: 51463.381079 PHMN
- Strategic SubDAO recipient: `cosmos146s5j3t7gh2g37ywm47dp8avhesu2htvjjaxq7z55e7xj0rq0k8q5qnjjy`
- Прямая отправка на старый или механически пересчитанный Cosmos-адрес: **нет** для всех строк.

## По статусам

- `excluded_incident`: 2 строк, 17132.149313 PHMN
- `excluded_olim_operator_confirmed`: 1 строк, 300.009116 PHMN
- `quarantined_contract_or_module_account`: 44 строк, 326.324751 PHMN
- `quarantined_unresolved_accounting_gap`: 1 строк, 57.230100 PHMN
- `rerouted_to_subdao`: 18 строк, 33647.667799 PHMN

## Куда направляется

- `specific_subdao_treasury`: 3 строк, 30371.280659 PHMN
- `strategic_subdao_treasury`: 18 строк, 20708.545569 PHMN
- `strategic_subdao_unresolved_accounting_gap_handling`: 1 строк, 57.230100 PHMN
- `strategic_subdao_unresolved_contract_holder_handling`: 44 строк, 326.324751 PHMN

## Файлы

- `phmn_old_addresses_not_receiving_new_phmn_register.csv` - чистый публичный реестр.
- `phmn_old_addresses_not_receiving_new_phmn_register.json` - тот же реестр в JSON.
- `phmn_old_addresses_not_receiving_new_phmn_register_summary.json` - totals/statuses для проверки.

#!/usr/bin/env bash
# Capture real CRUD request/response evidence from a running Accounts API.
set -euo pipefail

API_URL="${API_URL:-http://localhost:8080}"
OUT_DIR="${OUT_DIR:-.}"
mkdir -p "$OUT_DIR"

payload='{"name":"Nur Evidence","email":"nur.evidence@example.com","address":"Astana, Kazakhstan","phone_number":"+77000000000"}'
create_cmd="curl -sS -X POST '$API_URL/accounts' -H 'Content-Type: application/json' -d '$payload'"
create_response="$(curl -sS -X POST "$API_URL/accounts" -H 'Content-Type: application/json' -d "$payload")"
printf '$ %s\n%s\n' "$create_cmd" "$create_response" > "$OUT_DIR/rest-create-done"
account_id="$(printf '%s' "$create_response" | python -c 'import json,sys; print(json.load(sys.stdin)["id"])')"

list_cmd="curl -sS '$API_URL/accounts'"
list_response="$(curl -sS "$API_URL/accounts")"
printf '$ %s\n%s\n' "$list_cmd" "$list_response" > "$OUT_DIR/rest-list-done"

read_cmd="curl -sS '$API_URL/accounts/$account_id'"
read_response="$(curl -sS "$API_URL/accounts/$account_id")"
printf '$ %s\n%s\n' "$read_cmd" "$read_response" > "$OUT_DIR/rest-read-done"

update_payload='{"name":"Nur Evidence Updated","email":"nur.evidence@example.com","address":"Astana, Kazakhstan","phone_number":"+77000000000"}'
update_cmd="curl -sS -X PUT '$API_URL/accounts/$account_id' -H 'Content-Type: application/json' -d '$update_payload'"
update_response="$(curl -sS -X PUT "$API_URL/accounts/$account_id" -H 'Content-Type: application/json' -d "$update_payload")"
printf '$ %s\n%s\n' "$update_cmd" "$update_response" > "$OUT_DIR/rest-update-done"

delete_cmd="curl -sS -X DELETE '$API_URL/accounts/$account_id' -w 'HTTP %{http_code}\n'"
delete_response="$(curl -sS -X DELETE "$API_URL/accounts/$account_id" -w 'HTTP %{http_code}\n')"
printf '$ %s\n%s\n' "$delete_cmd" "$delete_response" > "$OUT_DIR/rest-delete-done"

echo "Created evidence files in $OUT_DIR:"
printf '%s\n' rest-create-done rest-list-done rest-read-done rest-update-done rest-delete-done

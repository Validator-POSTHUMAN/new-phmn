#!/usr/bin/env python3
"""Preflight public Cosmos endpoints for PHMN incident indexer work."""

from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass


ANCHOR_TX = "5AA8C1274E2FC823DCD4DACDC8B951220929D5BA338BFAB57E731CAEBAB737FA"
MINTER = "juno100umj2mnu0u6ujf37c9a3xfy9gl53hu9ekxyyw"
ATTACKER_JUNO = "juno1pqardc39d558mr58nx5m2wgmy448pv94ehdea0"


@dataclass(frozen=True)
class Endpoint:
    chain: str
    kind: str
    url: str


ENDPOINTS = [
    Endpoint("juno", "rpc", "https://juno-rpc.publicnode.com"),
    Endpoint("juno", "rpc", "https://juno-rpc.polkachu.com"),
    Endpoint("juno", "lcd", "https://juno-rest.publicnode.com"),
    Endpoint("juno", "lcd", "https://juno-api.polkachu.com"),
    Endpoint("juno", "lcd", "https://rest.cosmos.directory/juno"),
]


def fetch_json(url: str, timeout: int = 12) -> tuple[int | None, object | str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "POSTHUMAN-PHMN-indexer-preflight/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read(300_000)
            status = response.status
    except Exception as exc:  # noqa: BLE001 - preflight should keep scanning.
        return None, f"{type(exc).__name__}: {exc}"

    try:
        return status, json.loads(body)
    except json.JSONDecodeError:
        return status, body[:200].decode("utf-8", "replace")


def rpc_checks(endpoint: Endpoint) -> list[tuple[str, int | None, str]]:
    checks = [
        ("status", "/status"),
        ("tx_by_hash", f"/tx?hash=0x{ANCHOR_TX}"),
        (
            "tx_search_hash",
            "/tx_search?query=" + urllib.parse.quote(f"tx.hash='{ANCHOR_TX}'") + "&prove=false",
        ),
        (
            "tx_search_sender",
            "/tx_search?query=" + urllib.parse.quote(f"transfer.sender='{MINTER}'") + "&prove=false&per_page=2",
        ),
        (
            "tx_search_recipient",
            "/tx_search?query="
            + urllib.parse.quote(f"transfer.recipient='{ATTACKER_JUNO}'")
            + "&prove=false&per_page=2",
        ),
    ]
    results = []
    for name, path in checks:
        status, payload = fetch_json(endpoint.url + path)
        results.append((name, status, summarize_payload(payload)))
    return results


def lcd_checks(endpoint: Endpoint) -> list[tuple[str, int | None, str]]:
    events = [
        ("lcd_tx_hash", f"tx.hash='{ANCHOR_TX}'"),
        ("lcd_sender", f"transfer.sender='{MINTER}'"),
        ("lcd_recipient", f"transfer.recipient='{ATTACKER_JUNO}'"),
    ]
    results = []
    for name, event in events:
        query = urllib.parse.urlencode(
            {"events": event, "pagination.limit": "2", "order_by": "ORDER_BY_DESC"}
        )
        status, payload = fetch_json(endpoint.url + "/cosmos/tx/v1beta1/txs?" + query)
        results.append((name, status, summarize_payload(payload)))
    return results


def summarize_payload(payload: object | str) -> str:
    if isinstance(payload, str):
        return payload[:180]
    if not isinstance(payload, dict):
        return type(payload).__name__

    if payload.get("error"):
        return "error=" + json.dumps(payload["error"], ensure_ascii=False)[:180]

    result = payload.get("result")
    if isinstance(result, dict):
        if "sync_info" in result:
            sync = result.get("sync_info") or {}
            return f"height={sync.get('latest_block_height')} catching_up={sync.get('catching_up')}"
        if "tx" in result:
            return f"tx height={result.get('height')}"
        if "txs" in result:
            return f"txs={len(result.get('txs') or [])} total={result.get('total_count')}"

    if "txs" in payload:
        pagination = payload.get("pagination") or {}
        return f"txs={len(payload.get('txs') or [])} total={pagination.get('total')}"

    return json.dumps(payload, ensure_ascii=False)[:180]


def main() -> int:
    for endpoint in ENDPOINTS:
        print(f"## {endpoint.chain} {endpoint.kind} {endpoint.url}")
        checks = rpc_checks(endpoint) if endpoint.kind == "rpc" else lcd_checks(endpoint)
        for name, status, summary in checks:
            print(f"{name}\t{status or 'ERR'}\t{summary}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())

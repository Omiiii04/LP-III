"""Generate a deterministic demo wallet identifier without handling real private keys.

Use MetaMask for an actual wallet; never put a seed phrase or private key in source code.
"""
from __future__ import annotations

import argparse
import hashlib


def demo_address(label: str) -> str:
    if not label:
        raise ValueError("label must not be empty")
    return "0x" + hashlib.sha256(label.encode("utf-8")).hexdigest()[-40:]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("label", nargs="?", default="SPPU-LP-III-demo")
    args = parser.parse_args()
    print("Demo public identifier:", demo_address(args.label))
    print("For real transactions create/import the wallet only in MetaMask.")


if __name__ == "__main__":
    main()

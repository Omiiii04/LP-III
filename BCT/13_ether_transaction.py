"""Offline MetaMask/Ether transaction arithmetic for practical demonstration."""
from __future__ import annotations

import argparse


def transaction_summary(amount_eth: float, gas_limit: int, gas_price_gwei: float) -> dict[str, float]:
    if amount_eth < 0 or gas_limit <= 0 or gas_price_gwei < 0:
        raise ValueError("amount and gas price must be non-negative; gas limit must be positive")
    fee_eth = gas_limit * gas_price_gwei / 1_000_000_000
    return {"amount_eth": amount_eth, "gas_fee_eth": fee_eth, "total_debit_eth": amount_eth + fee_eth}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--amount", type=float, default=0.01)
    parser.add_argument("--gas-limit", type=int, default=21000)
    parser.add_argument("--gas-price-gwei", type=float, default=20)
    args = parser.parse_args()
    print(transaction_summary(args.amount, args.gas_limit, args.gas_price_gwei))


if __name__ == "__main__":
    main()

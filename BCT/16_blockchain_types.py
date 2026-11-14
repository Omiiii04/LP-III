"""Compare blockchain types and print representative real-world use cases."""
from dataclasses import dataclass


@dataclass(frozen=True)
class BlockchainType:
    name: str
    access: str
    control: str
    use_cases: tuple[str, ...]


TYPES = (
    BlockchainType("Public", "permissionless", "decentralized", ("digital currency", "public smart contracts")),
    BlockchainType("Private", "permissioned", "single organization", ("internal audit", "asset management")),
    BlockchainType("Hybrid", "mixed", "organization plus public visibility", ("healthcare", "real estate")),
    BlockchainType("Consortium", "permissioned members", "multiple organizations", ("banking", "supply chain")),
)


if __name__ == "__main__":
    for blockchain in TYPES:
        print(f"{blockchain.name}: {blockchain.access}; {blockchain.control}; {', '.join(blockchain.use_cases)}")

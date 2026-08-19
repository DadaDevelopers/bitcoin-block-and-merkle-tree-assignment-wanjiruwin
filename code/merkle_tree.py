import hashlib


# Four transaction IDs from Bitcoin Block #100,000
txids = [
    "8c14f0db3df150123e6f3dbbf30f8b955a8249b62ac1d1ff16284aefa3d06d87",
    "fff2525b8931402dd09222c50775608f75787bd2b87e56995a7bdd30f79702c4",
    "6359f0868171b1d194cbee1af2f16ea598ae8fad666d9b012c8ed2b79a236ec4",
    "e9a66845e05d5abc0ad04ec80f774a7e585c6e8db975962d069a522137b80c1d",
]

EXPECTED_ROOT = (
    "f3e94742aca4b5ef85488dc37c06c3282295ffec960994b2c0d5ac2a25a95766"
)


def double_sha256(data):
    """Perform SHA-256 twice."""
    return hashlib.sha256(
        hashlib.sha256(data).digest()
    ).digest()


def calculate_merkle_root(txids):
    """Calculate and display each level of the Bitcoin Merkle tree."""

    # Convert displayed TXIDs to the byte order used during hashing.
    hashes = [bytes.fromhex(txid)[::-1] for txid in txids]

    print("LEVEL 0 - TRANSACTION HASHES")
    for i, txid in enumerate(txids):
        print(f"TX {chr(65 + i)}: {txid}")

    print("\nLEVEL 1 - INTERMEDIATE HASHES")

    new_level = []

    for i in range(0, len(hashes), 2):
        left = hashes[i]
        right = hashes[i + 1]

        parent = double_sha256(left + right)
        new_level.append(parent)

        print(
            f"Hash {chr(65 + i)}{chr(65 + i + 1)}: "
            f"{parent[::-1].hex()}"
        )

    hashes = new_level

    print("\nLEVEL 2 - MERKLE ROOT")

    root = double_sha256(hashes[0] + hashes[1])

    print(f"Merkle Root: {root[::-1].hex()}")

    return root[::-1].hex()


merkle_root = calculate_merkle_root(txids)

print("\nEXPECTED MERKLE ROOT")
print(EXPECTED_ROOT)

print("\nVERIFICATION")

if merkle_root == EXPECTED_ROOT:
    print("SUCCESS: The calculated Merkle root matches Block #100,000!")
else:
    print("ERROR: The calculated Merkle root does not match.")
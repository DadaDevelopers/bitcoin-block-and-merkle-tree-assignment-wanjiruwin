# Task 2: Merkle Tree Construction

## Overview

For this task, I constructed a Merkle tree using the four real transaction hashes from Bitcoin Block #100,000.

The purpose was to demonstrate how individual transaction hashes are combined and hashed to produce a single Merkle root.

Bitcoin uses double SHA-256 when calculating the parent hashes in a Merkle tree.

## Transaction Hashes

The four transactions in Block #100,000 are:

| Transaction | Transaction Hash |
|---|---|
| TX A | `8c14f0db3df150123e6f3dbbf30f8b955a8249b62ac1d1ff16284aefa3d06d87` |
| TX B | `fff2525b8931402dd09222c50775608f75787bd2b87e56995a7bdd30f79702c4` |
| TX C | `6359f0868171b1d194cbee1af2f16ea598ae8fad666d9b012c8ed2b79a236ec4` |
| TX D | `e9a66845e05d5abc0ad04ec80f774a7e585c6e8db975962d069a522137b80c1d` |

## Merkle Tree Structure

```text
                              Merkle Root
                                   |
                          Double SHA-256
                                   |
                    +--------------+--------------+
                    |                             |
                  Hash AB                       Hash CD
                    |                             |
              Double SHA-256               Double SHA-256
                 /       \                     /       \
                /         \                   /         \
              TX A       TX B               TX C       TX D
# Bitcoin Block Inspection — Block #100,000

## Block Inspection Results

| Field | Value |
|---|---|
| **Block Height** | 100,000 |
| **Block Hash** | `000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506` |
| **Previous Block Hash** | `000000000002d01c1fccc21636b607dfd930d31d01c3a62104612a1719011250` |
| **Merkle Root** | `f3e94742aca4b5ef85488dc37c06c3282295ffec960994b2c0d5ac2a25a95766` |
| **Number of Transactions** | 4 |
| **Timestamp** | 2010-12-29 11:57:43 UTC |

## What I Found

### Block Height

The block height is the position of a block in the Bitcoin blockchain. The block inspected for this assignment is **Block #100,000**.

### Block Hash

The block hash is:

`000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506`

The block hash acts as a unique identifier for the block. It is calculated from information contained in the block header.

### Previous Block Hash

The previous block hash is:

`000000000002d01c1fccc21636b607dfd930d31d01c3a62104612a1719011250`

This hash links Block #100,000 to Block #99,999. Each Bitcoin block contains the hash of the previous block, creating the blockchain.

### Merkle Root

The Merkle root is:

`f3e94742aca4b5ef85488dc37c06c3282295ffec960994b2c0d5ac2a25a95766`

The Merkle root is a single hash that represents the transactions included in the block. It is calculated using a Merkle tree.

### Number of Transactions

Block #100,000 contains **4 transactions**. These transactions will be used in Task 2 to construct and verify the Merkle tree.

### Timestamp

The timestamp recorded for Block #100,000 is:

**2010-12-29 11:57:43 UTC**

## Conclusion

Block #100,000 demonstrates how Bitcoin blocks contain information that identifies the block, links it to the previous block, and summarizes its transactions using a Merkle root.
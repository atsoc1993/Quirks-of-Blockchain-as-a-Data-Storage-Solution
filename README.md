# Quirks-of-Blockchain-as-a-Data-Storage-Solution
This repository reviews the pros and cons of an experiment in using blockchain as a data storage solution

# Concept
On average, current options for data storage solutions on average charge $0.00001 to $0.0001 per byte.
An Algorand transaction costs 1,000 microAlgo, which is 1/1,000,000th of an Algo.
At current price, Algorand is $0.27, meaning 1 microAlgo is equivalent to $0.00000027
The maximum capacity of data that can be passed into an application call is 3,584 bytes, and at minimum an application call requires 1,000 microAlgo, meaning each byte stored on-chain costs 0.28 microAlgo (0.2790178571428571)
The current cost per byte using Algorand as a data storage solution would be $0.0000000754
This is roughly 133x to 1,326x cheaper than traditional data storage solutions, and all data is immutable once stored, and does not incur a reccuring cost to the user.

# Workflow 
- A user would deploy their own dedicated smart contract, that has a method to accept data as an application argument.
- Assertions are made that only the user may submit transactions
- An arbitrary amount of data would be broken into chunks of 3226 bytes per application call
- Labeling could be done in any number of ways, but generally we would have byte prefix' for the file name, round start, and round end, as well as byte-labeling for file start transaction and file end transaction
- Transactions are submitted for each chunk to the application, and the full data can be can be retrieved in chunks and reconstructed at any time by indexing application-call type transactions to the user's dedicated smart contract's application ID.

# Storage Per Transaction
- The maximum application argument size is 2048 bytes; subtracting the bytes needed for the method argument, this allows us 2042 bytes of storage
- The maximum note field size is 1024 bytes
- ~~The maximum foreign accounts reference size is 4 addresses, each at 32 bytes long~~
- ~~The maximum foreign assets reference size is 8, with a maximum total references set to 8, allowing 4 foreign asset references, each at 8 bytes long~~
- The maximum box reference size is 8, with a max key size of 64 bytes, a total of 512 bytes

Total Bytes per Transaction: 2048 + 1024 + 512 = 3,584 bytes

# Pros 
- Immutable Storage
- Cheaper per byte cost
- One-time payment for storage
- Decentralized, not authority-dependant for future access
- Data can be encrypted using curve25519 keys, converted from native ed25519 keys used by accounts for signing on Algorand

# Cons
- Relay nodes and Indexers are affected as they store the full state of the chain, using blockchain as a data storage solution causes bloat across all hosts— which technically increases the shared storage by several folds.
- Indexer access is required to inquire for data, although there are free tiers of access available depending on the amount of data API limits may be exceeded
- There is no current ed25519 to curve25519 key conversion support from current wallet providers, and the user would either need to encrypt their own data or allow us to have a custodial escrow account to encrypt their data for them


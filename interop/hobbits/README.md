# Initial Interop

For the initial client interop, clients will utilize a simplified networking implementation and wire protocol. For more information please review the hobbits specification [here](https://github.com/deltap2p/hobbits).

### Prereqs

- targeting the frozen spec (v0.8)
- all clients must pass reference tests
- all clients must pass [hobbits integration tests](./integration-tests.md)
- all wire protocol implementations must pass [hobbits conformance tests](./conformance-tests.md)

## Stage One: Coordinated Start

Clients simulate a coordinated genesis event and gossip blocks/attestations for each slot.  This stage demonstrates the ability of clients to finalize the chain starting from `Eth2Genesis`.

### Prereqs

- Ability to read in the N number of deposits required to trigger the `is_genesis_trigger` function
- Ability to gossip blocks and attestations
- Static peering
- TCP transport
- [Minimal Constants](https://github.com/ethereum/eth2.0-specs/tree/master/configs/constant_presets)

### Procedure

For the initial round: 
1. Clients will pair off in teams of two.
2. `is_genesis_trigger` will be triggered on startup
3. Once the clients can finalize the chain, then they pick another client pair to interop with.  

Repeat (1) & (2) until all clients are talking.

>**Round 1:** 2 nodes (one per client) with 16 validators/client  
>**Round 2:** 4 nodes (one per client) with 8 validators/client  
>**Round 3:** 8 nodes (one per client) with 4 validators/client

### Goal

Clients can declare success at each round after 3 epochs where:
- Epoch 2 is justified
- Epoch 1 is finalized

Stretch goal is for clients to run ~15 minutes without error and continual finalization.

## Stage Two: Join & Sync

Clients join an existing short-lived testnet and sync.  This stage demonstrates the clients' ability to successfully join an existing network.

### Prereqs

- RPC methods implemented so that a new client can sync to an existing testnet.
- Standup a short-lived heterogeneous testnet 
- Static peering
- TCP transport

### Procedure

For the initial round: 
1. Clients will pair off in teams of two  
2. Clients A & B create a testnet
3. A adds another node to sync from scratch
4. B adds another node to sync from scratch

> Note: The additional nodes will not have validators

Repeat steps (1) thru (3) until all clients are talking.

>**Round 1:** 2 nodes (one per client) with 16 validators/client
>**Round 2:** 4 nodes (one per client) with 8 validators/client
>**Round 3:** 8 nodes (one per client) with 4 validators/client

### Goal

Clients can declare success when they are able to sync to the existing testnet chain and stay in sync for 3 epochs where:
- Epoch 2 is justified
- Epoch 1 is finalized

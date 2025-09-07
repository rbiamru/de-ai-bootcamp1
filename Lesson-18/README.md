# Lesson 18: Blockchain Data Structures and Advanced Concepts

This lesson explores the fundamental data structures used in blockchain systems, along with advanced concepts like oracles, verifiable computation, and decentralized storage solutions. Understanding these components is crucial for building robust decentralized AI applications.

## Prerequisites

- Proficiency in using a shell/terminal/console/bash on your device
  - Familiarity with basic commands such as `cd`, `ls`, and `mkdir`
  - Ability to execute packages, scripts, and commands on your device
- Node.js installed on your device
  - [Node.js](https://nodejs.org/en/download/)
- Familiarity with Solidity programming
  - [Solidity Documentation](https://docs.soliditylang.org/)

## Review of Lesson 17

- Web3 fundamentals
- Smart contract development
- EVM architecture
- Token creation and deployment

## Blockchain Data Structures

For the EVM and all Smart Contracts running on it, the data should be entirely present either inside the **Blockchain Storage** or in the **Transaction Data**.

### Blockchain Storage

- **Block Structure**:
  - Header components
  - Transaction root
  - State root
  - Receipt root

- **Contract Storage**:
  - Storage slots and mapping ([Solidity Storage Layout](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html))
  - State variables ([State Variables](https://docs.soliditylang.org/en/latest/structure-of-a-contract.html#state-variables))
  - Persistent data structures ([Data Location](https://docs.soliditylang.org/en/latest/types.html#data-location))
  - Key-value storage ([Mappings](https://docs.soliditylang.org/en/latest/types.html#mapping-types))
  - Storage layout patterns ([Layout of State Variables in Storage](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html))

- **Transaction Properties**:
  - Input data encoding ([ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html))
  - Receipt logs ([Events and Logs](https://docs.soliditylang.org/en/latest/contracts.html#events))
  - Transaction finality ([Blocks](https://docs.soliditylang.org/en/latest/introduction-to-smart-contracts.html#blocks))
  - Reversion handling ([Error Handling](https://docs.soliditylang.org/en/latest/control-structures.html#error-handling))
  - Event emission ([Events](https://docs.soliditylang.org/en/latest/contracts.html#events))

### Development Tools

- **Hardhat**:
  - [Hardhat](https://hardhat.org/) is a development environment for Ethereum software
  - Features include:
    - Built-in smart contract compilation
    - Network management for deployment
    - Testing framework for automated testing
    - Console debugging capabilities
    - Task automation and scripting

## Hands-on Experience

- Practical exercise:
  - Exercise 1: Implement a simple [Storage Contract](./exercises/00-Storage-Contract.md) and test it using the development tools from Hardhat

## Oracles and External Data

But what happens when we need data that isn't on the blockchain? That's where oracles come in. Think of oracles as bridges between the blockchain and the real world. They help us bring external data onto the blockchain in a secure and reliable way.

Let's explore how oracles work. When your smart contract needs data from outside the blockchain, it sends a request to an oracle network. The network's nodes gather the data, verify it, and send it back to your contract. This is crucial for AI applications that need real-world data to make decisions.

- Oracle Networks
  - Understanding [Oracles](https://ethereum.org/en/developers/docs/oracles/)
  - Oracle networks provide external data feeds
  - Decentralization vs Quick Resolution vs Accuracy
  - Examples:
    - [Chainlink Documentation](https://docs.chain.link/)
    - [Band Protocol](https://docs.bandchain.org/)
    - [UMA Protocol](https://docs.uma.xyz/)
    - [API3](https://docs.api3.org/)
    - [Tellor](https://docs.tellor.io/)

- Oracle Implementation
  - Smart contract interfaces for data requests
  - Data validation and verification mechanisms
  - Error handling and fallback strategies

## Verifiable Computation

Zero-knowledge proofs enable verification of information without revealing the underlying data. This technology is particularly valuable for AI applications that need to verify model outputs while maintaining privacy of training data and model parameters.

- Zero-Knowledge Proofs
  - Understanding [zk-rollups](https://ethereum.org/en/developers/docs/scaling/zk-rollups/)
  - Proof systems and circuit compilation
  - Privacy preservation and scalability solutions
  - Examples:
    - [Zero Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/)
    - [StarkNet](https://starknet.io/docs/)
    - [Scroll](https://docs.scroll.io/)

- Applications
  - Privacy-preserving AI model verification
  - Identity verification without data exposure
  - Compliance proof for sensitive data

Trusted Execution Environments (TEEs) provide hardware-level security for sensitive computations. These secure enclaves ensure that code and data remain protected even when running on untrusted systems.

- TEE Integration
  - Understanding [Intel SGX](https://www.intel.com/content/www/us/en/developer/tools/software-guard-extensions/overview.html) and [TDX](https://www.canarybit.eu/intel-sgx-vs-tdx-what-is-the-difference/)
  - [ARM TrustZone](https://www.arm.com/technologies/trustzone-for-cortex-m) implementation
  - Secure enclaves and remote attestation
  - Examples:
    - [Confidential Computing](https://confidentialcomputing.io/)
    - [TEE Security](https://www.intel.com/content/www/us/en/security/software-guard-extensions.html)
    - [Oasis Network](https://docs.oasis.dev/general/)
    - [Secret Network](https://docs.scrt.network/)
    - [Phala Network](https://www.phala.network/docs/)

- Applications
  - Confidential computing for AI models
  - Secure oracles and private smart contracts
  - Secure key management and data protection

## Decentralized Storage

### IPFS Architecture

Many of the limitations of blockchain for data storage are inherent for the security needed for archiving consensus over the state of the blocks all across the network. The [IPFS](https://docs.ipfs.tech/) implementation differs from normal blockchains by removing the need for all nodes to store all the data, implementing a P2P network of storage providers that can share blocks of bytes between each other in a secure and decentralized way.

- **Components**:
  - Content addressing
  - DHT networking
  - BitSwap protocol
  - Pinning services

- **Integration**:
  - File upload/download
  - Content persistence
  - Gateway access
  - DNSLink

### Filecoin Integration

While the IPFS can handle all needs for communication, discovery and file sharing inside the protocol itself, it doesn't solve the incentivization aspect on itself. We can't expect storage providers to store and serve files for long time, incurring costs for hosting and network, without any kind of financial compensation.
For guaranteeing the longevity of file availability on these P2P networks, some sort of Data Availability solution needs to be implemented on top to incentivize correct behavior from all parts.
The [Filecoin](https://docs.filecoin.io/) network is one of many solutions that can provide this economic incentives on top of the file hosting and sharing operations.

- **Storage Markets**:
  - Deal making
  - Proof of Replication
  - Proof of Spacetime
  - Storage providers

- **Smart Contract Integration**:
  - Storage deals
  - Data retrieval
  - Payment channels
  - Verification

## Introduction to Smart Contracts for AI Systems

The integration of AI systems with blockchain technology is creating new possibilities for decentralized intelligence. Here are some notable projects in this space:

### Web3 and AI Tooling Projects

- **Coinbase's AgentKit**
  - [AgentKit Repository](https://github.com/coinbase/agentkit)
  - Open-source framework for building AI agents that can interact with Web3
  - Enables agents to perform on-chain actions and interact with smart contracts
  - Provides tools for wallet management and transaction handling

- **Fetch.ai**
  - [Fetch.ai Documentation](https://docs.fetch.ai/)
  - First open network for AI agents
  - Enables autonomous economic agents for DeFi and data services
  - Provides AI-powered infrastructure for smart autonomous services

- **Ocean Protocol**
  - [Ocean Protocol Documentation](https://docs.oceanprotocol.com/)
  - Decentralized data exchange protocol for AI
  - Enables data monetization and sharing while preserving privacy
  - Provides marketplace for AI data and models

- **OpSec Network**
  - [OpSec Documentation](https://docs.opsec.computer/)
  - Layer-1 blockchain with AI-driven consensus
  - Provides decentralized cloud computing and storage solutions
  - Features RDP for remote server access and GPU hosting

- **ORA Protocol**
  - [ORA Website](https://ora.io)
  - Decentralized oracle network specifically designed for AI models
  - Enables verifiable AI computations on-chain
  - Provides infrastructure for AI model marketplaces

- **Venice AI**
  - [Venice Protocol](https://docs.venice.ai/welcome/about-venice)
  - Framework for decentralized AI model training and deployment
  - Uses [VVV](https://venice.ai/blog/introducing-the-venice-token-vvv) token paying for decentralized AI inference

- **OORT**
  - [OORT Protocol](https://www.oortech.com/)
  - Decentralized infrastructure for AI computation
  - Provides distributed computing resources for AI workloads
  - Enables efficient resource allocation and scaling

- **ElizaOS**
  - [ElizaOS Framework](https://www.elizaos.ai/)
  - Operating system for developing and running decentralized AI agents
  - Provides infrastructure for AI agent deployment and management
  - Supports cross-chain agent operations

- **0G Protocol**
  - [0G Website](https://0g.ai/)
  - First decentralized AI operating system and Layer 1 ecosystem
  - Designed for scalable AI and web3 applications
  - Provides infrastructure for AI model deployment and inference

- **Thirdweb Nebula** [Documentation](https://portal.thirdweb.com/nebula):
  - Tooling for interacting with blockchain reasoning models
  - Integrated autonomous transaction capabilities for assistants and AI agents
  - Real-time access for blockchain data augmented generation capabilities

- **Olas Network**:
  - [Olas Website](https://olas.network/)
  - Framework for co-owning and monetizing AI agents
  - Decentralized agent economies and marketplaces
  - Key components:
    - Pearl "Agent App Store" for deploying agents
    - Mech Marketplace for agent-to-agent services
    - Developer rewards and staking mechanisms
    - Multi-chain protocol coordination
  - Supports both sovereign (local/cloud) and decentralized agents

### Integration Patterns

The integration of AI systems with blockchain technology requires careful consideration of various patterns to ensure secure, efficient, and scalable operations. These patterns address key aspects of AI model deployment, computation verification, data management, and economic incentives.

1. **Model Registry**
   - Storage of model metadata on-chain
   - Verification of model authenticity
   - Access control and licensing
   - Version tracking

2. **Computation Verification**
   - Proof of computation
   - Result validation
   - Resource usage tracking
   - Reward distribution

3. **Data Management**
   - Training data access control
   - Privacy-preserving computation
   - Data marketplace integration
   - Quality assurance mechanisms

4. **Token Economics**
   - Incentive design
   - Staking mechanisms
   - Slashing conditions
   - Reward distribution

5. **Message Routing**
   - Content-based routing for AI model requests
   - Dynamic routing based on model capabilities
   - Load balancing across compute nodes

6. **Service Integration**
   - AI model service discovery
   - Service negotiation and contracts
   - Distributed business processes

7. **Data Sharing/Replication**
   - Model state synchronization
   - Training data distribution
   - Result aggregation

These are some of the common patterns that can be used to build robust and secure AI applications on blockchain networks.

## Next Steps

- Introduction to Smart Contracts for AI Systems
- Exploring Verifiable AI and Transparency in Model Outputs
- Implementing AI Applications with Blockchain-Backed Data Verification

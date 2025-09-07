# Lesson 19: Verifiable AI and Decentralized AI Protocols

This lesson explores the intersection of AI and blockchain technology, focusing on verifiable AI systems and the emerging landscape of decentralized AI protocols. We'll examine how blockchain technology can enhance AI transparency, accountability, and decentralization.

## Prerequisites

- Proficiency in using a shell/terminal/console/bash on your device
  - Familiarity with basic commands such as `cd`, `ls`, and `mkdir`
  - Ability to execute packages, scripts, and commands on your device
- Node.js installed on your device
  - [Node.js](https://nodejs.org/en/download/)
- Understanding of basic AI concepts and blockchain technology
- Familiarity with smart contracts and Web3 development
- Basic knowledge of cryptographic principles

## Review of Lesson 18

- Smart contract development
- Blockchain data structures
- Oracle integration
- Decentralized storage solutions
- Integration Patterns

## Verifiable AI Systems

- Transparent and accountable AI systems
  - Proof of model
  - Proof of computation
  - Proof of result
    - Locking the `seed` parameter when doing sampling
- Incentives for honest/reliable behavior
- Community coordination tools
- This can be applied both to the operation of these AI systems as well for the governance of the development/execution of these systems

### The Foundation of Trust

At its core, verifiable AI is about building trust through transparency. Think of it like having a digital notary for your AI system - every decision, every prediction, and every computation can be verified independently. This isn't just about checking results; it's about creating an entire ecosystem where AI systems can be audited, validated, and trusted.

The key pillars that make this possible are:

- **Model Verification**: Like having a fingerprint for your AI model, ensuring it hasn't been tampered with
- **Input/Output Validation**: Guaranteeing that the data going in and coming out is exactly what we expect
- **Computation Proof Systems**: Mathematical guarantees that the AI performed its calculations correctly
- **Transparency Mechanisms**: Clear windows into how decisions are made

### Building Trust Through Technology

The magic happens through several sophisticated verification methods:

1. **Zero-Knowledge Proofs for AI**: Imagine proving that your AI made a correct decision without revealing the actual decision or the data it used. This is what zero-knowledge proofs enable - privacy-preserving verification.

2. **Formal Verification**: Like having a mathematical proof that your AI system will behave correctly under all circumstances. This is particularly crucial for safety-critical applications.

3. **Model Attestation**: A way to certify that your AI model hasn't been modified or compromised, similar to having a digital seal of authenticity.

4. **Reproducibility Frameworks**: Ensuring that AI results can be independently verified and reproduced, building confidence in the system's reliability.

### Where Blockchain Meets AI

The blockchain becomes our trust layer, providing two main approaches to verification:

#### On-chain Verification

Think of this as having a smart contract that acts as a judge for your AI system. It can:

- Verify model checkpoints
- Validate inputs and outputs
- Process and validate proofs
- Maintain an immutable record of all verifications

#### Off-chain Verification

Sometimes we need more powerful tools than what's available on-chain. This is where off-chain verification comes in:

- Trusted Execution Environments (TEEs): Secure hardware that guarantees computation integrity
- Distributed verification networks: Multiple parties working together to verify results
- Proof aggregation systems: Combining multiple proofs into a single, verifiable result
- Challenge-response protocols: Interactive verification methods that ensure system honesty

### Making AI Transparent

Transparency isn't just about seeing what's inside the black box - it's about understanding and verifying every aspect of the AI system:

#### Model Transparency

- Version control and tracking: Every change to the model is recorded and verifiable
- Parameter verification: Ensuring model parameters haven't been tampered with
- Training data provenance: Tracking where the training data came from
- Audit trails: Complete history of all operations and decisions

#### Output Verification

- Result validation: Confirming that outputs meet expected criteria
- Confidence scoring: Understanding how sure the AI is about its decisions
- Bias detection: Identifying and preventing unfair or discriminatory outputs
- Performance metrics: Measuring and verifying system accuracy and reliability

## Decentralized AI Protocols

The convergence of AI and blockchain technology has given birth to a new generation of protocols that are revolutionizing how we develop, deploy, and monetize AI systems. Let's explore how these protocols are reshaping the AI landscape by leveraging the power of Web3.

### Major Protocols Overview

- [Ocean Protocol](https://docs.oceanprotocol.com/) is pioneering a new way to handle AI data through blockchain technology
  - decentralized marketplace where data becomes a valuable asset that can be traded, shared, and monetized while maintaining privacy and control
  - According to their [latest updates](https://blog.oceanprotocol.com/fetch-ai-ocean-protocol-and-singularitynet-unite-to-create-artificial-superintelligence-alliance-0768d608ecfa), their [Ocean Predictoor](https://docs.predictoor.ai/) product has achieved over $800M in monthly volume, demonstrating significant market adoption

- [SingularityNET](https://singularitynet.io/) is building a decentralized network where AI services can be created, shared, and monetized
  - Founded by Dr. Ben Goertzel, known as the "Father of AGI", it's like an "App Store for AI" but with blockchain-powered governance and economics
  - Also part of the [Artificial Superintelligence Alliance](https://superintelligence.io/)

- [Fetch.ai](https://fetch.ai/) is pushing the boundaries of what's possible by creating autonomous AI agents that can interact with blockchain networks
  - AI systems with the ability to make economic decisions and execute transactions independently
  - Also part of the [Artificial Superintelligence Alliance](https://superintelligence.io/)

- [Internet Computer Protocol](https://internetcomputer.org/what-is-the-ic) (ICP) is bringing AI computation directly to the blockchain, creating a new paradigm for verifiable AI execution
  - ICP network is orchestrated by permissionless decentralized governance and is hosted on sovereign hardware devices run by independent parties

- [Akash Network](https://docs.akash.network/) is revolutionizing how we deploy AI workloads by creating a decentralized marketplace for computing resources
  - Open network that facilitates the secure and efficient buying and selling of computing resources
    - It's like an "Airbnb/Uber for AI computing power"

Each of these protocols represents a different approach to combining AI with blockchain technology, creating new possibilities for:

- Decentralized AI development and deployment
- Fair and transparent AI service monetization
- Privacy-preserving AI training and inference
- Autonomous AI systems with economic agency
- Verifiable AI computation on the blockchain

## ORA Protocol

As an example of the applications of verifiable AI by leveraging Web3 technologies, let's explore the [ORA Protocol](https://ora.io/) for some practical examples of combinations of these technologies.

- [ORA Protocol](https://docs.ora.io/doc/introduction/about-ora) is a decentralized protocol providing chain-agnostic infrastructure that bridges the gap between AI and blockchain
- The base of the ORA Protocol is the use of [Onchain AI Oracles](https://www.ora.io/app/opml/) to safely execute AI inference off-chain while providing verifiable results onchain

### Optimistic ML

- The [opML paper](https://arxiv.org/abs/2401.17555)
- Open-source framework for verifying ML inference onchain
- Similar to optimistic rollups
- Example [opML powered AI](https://www.ora.io/app/opml/openlm)

### Resilient Model Services (RMS)

- [RMS (Resilient Model Services)](https://docs.ora.io/doc/resilient-model-services-rms/overview) is an AI service designed to provide computation for all scenarios
  - It ensurer resilient (stable, reliable, fault tolerant, and secure) AI computation
  - Powered by opML
- AI API service that integrates seamlessly with existing AI frameworks
- Replace your existing AI API provider with RMS API Key and point it to the RMS endpoint

### Initial Model Offerings

- Model Ownership ([ERC-7641 Intrinsic RevShare Token](https://ethereum-magicians.org/t/erc-7641-intrinsic-revshare-token/18999)) + Inference Asset (eg. [ERC-7007 Verifiable AI-Generated Content Token](https://github.com/AIGC-NFT/ERCs/blob/master/ERCS/erc-7007.md))
- IMO launches an ERC-20 token (more specifically, ERC-7641 Intrinsic RevShare Token) of any AI model to capture its long-term value
- Anyone who purchases the token becomes one of the owners of this AI model
- Token holders share revenue of the IMO AI model
- The [IMO launch blog post](https://mirror.xyz/orablog.eth/xYMD27tN23ppbKCluB9faytF_W6M1hKXTuKcfkm3D50) and the [first IMO implementation](https://mirror.xyz/orablog.eth/GSjMm-qC4WWsduGqCISSvA1IxicJbyRDES_bl7-Tt2o)

### Perpetual Agents

- The [opAgent](https://mirror.xyz/orablog.eth/sEFCQVmERNDIsiPDs2LUnU-__SdLmKERpCKcEP7hO08) use case
  - Agents running without relying on a centralized provider
  - Token economic incentives for hosting the agent
- Lifecycle
  - Genesis Transaction: The initial creation transaction that establishes the agent's existence on the blockchain
  - Asset Binding: Permanent linkage of digital assets to the agent through smart contracts
    -Identity Formation: Creation of a unique, immutable identity that cannot be replicated or falsified
  - Autonomous Initialization: Self-bootstrapping process that establishes initial operating parameters

### Tokenized AI Generated Content (AIGC)

- The [ERC-7007 standard](https://eips.ethereum.org/EIPS/eip-7007)
- [ERC-721](https://eips.ethereum.org/EIPS/eip-721) extension
- Verifiable AIGC tokens using ZK and opML
- Verifiable "AI Creativity" with the [7007 Protocol](https://www.7007.ai/)

### Running AI Text Generation Tasks with Decentralized AI Model Inferences

- The [OAO repository](https://github.com/ora-io/OAO)
- Implementing the `IAIOracle.sol` interface
- Building smart contracts [with ORA's AI Oracle](https://docs.ora.io/doc/ai-oracle/ai-oracle/build-with-ai-oracle)
- Handling the [Callback gas limit estimation](https://docs.ora.io/doc/ai-oracle/ai-oracle/callback-gas-limit-estimation) for each model ID
- [Reference list](https://docs.ora.io/doc/ai-oracle/ai-oracle/references) for models and addresses for different networks

## Hands-on Experience

- Practical exercise:
  - Exercise 1: [Invoking an Onchain AI Oracle](./exercises/00-Decentralized-Inference.md) from a smart contract to execute a provable inference

## Decentralized AI Inference

- Most AI inference providers we used required credit card payments or similar subscription or usage-based payments
- Some providers are starting to support crypto payments
  - Often these payments are converted to fiat currency by the provider to fund their corporate operations
- The approach of Decentralized AI Inference is to provide a way to execute AI inference off-chain while providing verifiable results onchain, while handling all the payments through cryptocurrencies and ensuring the proper incentives for the providers
  - Tokens as payment medium
  - Tokens as security mechanism (incentives and penalties)
  - Tokens as a governance mechanism

### Venice AI Platform

- One example of a Decentralized AI Inference platform is the [Venice Protocol](https://docs.venice.ai/)
  - Privacy-preserving computation
  - Uncensored models
  - Decentralized inference infrastructure
  - Token economics ([VVV](https://venice.ai/blog/introducing-the-venice-token-vvv))

- Practical exercise:
  - Exercise 2: Implementing a privacy-preserving chatbot using the [Venice API](https://docs.venice.ai/welcome/about-venice)

## Next Steps

- Implementing AI Applications with Blockchain-Backed Data Verification
- Integrating Decentralized Identity (DID) for User Authentication in AI Apps
- Leveraging Blockchain for Storing and Verifying AI Outputs
- Weekend project

# Lesson 22: Decentralized AI Agents

In this lesson, we will explore how to build AI agents using open-source tools and leverage Large Language Models (LLMs) to power the reasoning process behind agent task execution.

We will also examine how AI Agents can be integrated into Retrieval-Augmented Generation (RAG) pipelines to automate decision-making about information retrieval from various indexes and its application to the generation task at hand.

By the end of this lesson, we will begin our introduction to the subject of decentralized AI agents by leveraging a set of dev tooling for connecting our agents to Web3 wallets.

## Prerequisites

- Proficiency in using a shell/terminal/console/bash on your device
  - Familiarity with basic commands like `cd`, `ls`, and `mkdir`
  - Ability to execute packages, scripts, and commands on your device
- Installation of Python tools on your device
  - [Python](https://www.python.org/downloads/)
  - [Pip](https://pip.pypa.io/en/stable/installation/)
- Proficiency in using `python` and `pip` commands
  - Documentation: [Python](https://docs.python.org/3/)
  - Documentation: [Pip](https://pip.pypa.io/en/stable/)
- Proficiency in using `venv` to create and manage virtual environments
  - Documentation: [Python venv](https://docs.python.org/3/library/venv.html)
- Installation of Node.js on your device
  - [Node.js](https://nodejs.org/en/download/)
- Proficiency in using `npm` and `npx` commands
  - Documentation: [npm](https://docs.npmjs.com/)
  - Documentation: [npx](https://www.npmjs.com/package/npx)
- Proficiency in using `npm install` and managing the `node_modules` folder
  - Documentation: [npm install](https://docs.npmjs.com/cli/v10/commands/npm-install)
- Installation of `git` CLI on your device
  - [Git](https://git-scm.com/downloads)
- Proficiency in using `git` commands to clone repositories
  - Documentation: [Git](https://git-scm.com/doc)
- A free account on [LlamaCloud](https://cloud.llamaindex.ai/) with an active [API key](https://cloud.llamaindex.ai/api-key)
- An account at [OpenAI Platform](https://platform.openai.com/)
  - To run API Commands on the platform, set up [billing](https://platform.openai.com/account/billing/overview) and add at least **5 USD** credits to your account

## Review of Lesson 21

- AI Agents
- Task planning
- Goals
- Types of agents
- Applications and examples
- Setting up an AI agent

## Building a Simple AI Agent Program

- Defining tools
- Using a Query Engine for processing tasks
- Implementing Query Transformations
- Task planning
- Handling steps
- Evaluating goals

- Practical exercises
  - Exercise 1: Implementing a [Simple AI Agent](./exercises/00-Simple-AI-Agent-With-LlamaIndex.md) using the [Agent Tools](https://docs.llamaindex.ai/en/stable/use_cases/agents/) from [LlamaIndex](https://llamaindex.ai)
  - Exercise 2: Implementing a [Structured Planning AI Agent](./exercises/01-Structured-Planning-AI-Agent.md) using the [Structured Planner](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/)

## Agentic RAG

- Retrieval Agents
  - File search functions
  - Web search functions
  - Chunking data
  - Embeddings
  - Vector search
- Integrating Query Engines into Agent tasks
- Multi-tool invocation
- Implementing Query Transformations
  - Decision-making for information retrieval
- Multi-step queries

- Practical exercise:
  - Exercise 3: Implementing an [Agentic RAG](./exercises/02-Agentic-RAG.md) AI using the [Query Engine Tool](https://docs.llamaindex.ai/en/stable/understanding/agent/rag_agent/) for passing documents to the agent

## Monetizing AI Agents with Tokens

AI Agents can be designed to handle monetary transactions using digital tokens, which are often implemented on blockchain networks. This capability opens up new possibilities for creating autonomous economic systems to incentivize AI-driven services.

### Decentralized AI Agents tools

- Building AI Agents with token enabled functions
- Managing wallets and transactions
- Building smart contracts
- Deploying decentralized AI Agents

### Popular Web3 Agent Frameworks and Tools

- ElizaOS [Documentation](https://eliza.how/docs/intro/):
  - Proposed to be the [first open-source web3-friendly Agentic framework](https://arxiv.org/abs/2501.06781v1)
  - Open-source TypeScript framework for building autonomous AI agents
  - Built-in Web3 capabilities through plugins
  - Supports multi-agent architectures and cross-platform interactions
  - Provides a [robust architecture](https://eliza.how/docs#system-architecture) for building complex web3-enabled agents

- Coinbase AgentKit [Documentation](https://github.com/coinbase/agentkit):
  - Framework for building crypto-native AI agents
  - Native integration with [Coinbase products](https://www.coinbase.com/products)

- Fleek [Documentation](https://fleek.xyz/):
  - Web3 native platform for building and deploying AI agents
    - Hosting secure agents in [TEEs](https://fleek.xyz/guides/understanding-tees-and-sgx-fleek/)
  - Quick deployments of secure [AI Agents](https://fleek.xyz/docs/ai-agents/)
  - Can also be used for [hosing](https://fleek.xyz/docs/platform/hosting/) static websites and applications
    - [Decentralized storage](https://fleek.xyz/docs/platform/storage/) leveraging [IPFS](https://ipfs.io/), [Arweave](https://www.arweave.org/), and [Filecoin](https://filecoin.io/)
  - Can be used for running [Verified and Confidential Compute](https://fleek.xyz/docs/platform/fleek-machines/)
    - Quick deployment of lightweight TEE VMs with docker support

- Olas [Agents SDK](https://docs.olas.network/olas-sdk/)
  - Olas is a protocol for building [autonomous services](https://docs.olas.network/open-autonomy/) running multi-agent-systems (MAS) and offering enhanced on-chain functionalities
  - [Agent Services](https://docs.olas.network/open-autonomy/get_started/what_is_an_agent_service/#architecture) are registered into [On-Chain Registries](https://docs.olas.network/protocol/#components) in the form of NFTs
    - These registries provide the primitives needed to combine components into agents, agents into autonomous services, and to operate and secure such autonomous services
  - Olas protocol Tokenomics defines an economic model that uses the OLAS token as a coordination mechanism to accomplish three main objectives:
    - Enable the pairing of capital and code in a permissionless manner
    - Create a flywheel that attracts increasingly more value and provides truly-decentralized autonomous services, owned by a DAO, operated by ecosystem actors, and coded by the ecosystem developers
    - Incentivize software composability

- Fetch.ai [AI Agents Framework](https://fetch.ai/docs/guides/agents/quickstart)
  - The [uAgents Framework](https://fetch.ai/docs/guides/agents/getting-started/whats-an-agent) is a lightweight library designed to facilitate the development of decentralized Agents
  - Agents in a multi-agent system can communicate with any, and all agents in the system to solve problems, execute tasks and transact
  - Agents can use the [FET token](https://fetch.ai/docs/guides/agents/getting-started/fet-token-for-agents), which was created to facilitate payments in an Agentic ecosystem
    - Micro payments to one agent to another which traditional currencies would not support
    - FET tokens are used for agent Almanac registration, and wider contract interactions
  - The deployed agents can be registered in the [Almanac](https://fetch.ai/docs/references/contracts/uagents-almanac/almanac-overview) contract to become part of an [Agentverse](https://agentverse.ai/), where they can be connected through the [Agentverse Marketplace](https://fetch.ai/docs/guides/agentverse/creating-agentverse-agents/agent-explorer)

- Phala Network [Documentation](https://docs.phala.network/)
  - Phala Network provides a decentralized infrastructure for AI agents with a focus on privacy and security through Trusted Execution Environments (TEEs)
  - The platform enables the deployment of autonomous AI agents like [Eliza](https://docs.phala.network/phala-cloud/launch-an-eliza-agent) without requiring coding knowledge
  - Phala's [Agent Wars](https://phala.network/agent-wars-shaping-the-future-of-ai-and-web3-with-tokenization) initiative explores tokenization of AI agents, creating economic models for agent creation and improvement
  - The platform uses a tokenomics system where:
    - Agent ownership is managed through a staking-based DAO governance model
    - Agent creators and contributors can benefit from agent improvements
    - One-time payment for agent creation covers hosting costs, eliminating ongoing charges
  - Phala's infrastructure allows for secure deployment of AI agents in TEEs, ensuring privacy and security for sensitive operations
  - The platform supports integration with various LLM providers and external services, making it versatile for different agent applications

- Galadriel [Documentation](https://docs.galadriel.com/overview)
  - [Sentience SDK](https://github.com/galadriel-ai/sentience) enables developers to build autonomous, fully on-chain verifiable AI agents
  - The SDK [verifies agent's LLM inferences](https://docs.galadriel.com/for-agents-developers/verify-signatures) (thoughts, actions, output) with a simple developer experience, eliminating the need to understand underlying cryptographic primitives of TEEs
  - Supports all [OpenAI models](https://docs.galadriel.com/for-agents-developers/models) out of the box, including fine-tuned models, making it compatible with any existing AI agent framework
  - Leverages a [Trusted Execution Environment (TEE) architecture](https://docs.galadriel.com/for-agents-developers/how-tee-works) to securely execute LLM API calls, ensuring verifiability through cryptographic attestations
  - Each [attestation is easily verifiable](https://docs.galadriel.com/for-agents-developers/verify-attestation) for transparency and integrity, allowing third parties to verify the provenance and authenticity of requests and outputs
  - Provides logging functionality to retrieve and display verified inferences, making it easy to implement proof terminals

## Next Steps

- Building Blockchain-Enabled Autonomous AI Agents
- Developing AI Agents with Tokenized Incentive Structures
- Implementing custom function calling capabilities to AI agents
- Deploying Onchain AI Agents on decentralized hosting providers

# Lesson 23: Building Blockchain-Enabled AI Agents

In this lesson, we will explore how to build autonomous AI agents that can interact with blockchain networks, handle tokenized transactions, and execute smart contract functions. We'll learn how to integrate Web3 capabilities into our AI agents and deploy them on decentralized infrastructure.

## Prerequisites

- Proficiency in using a shell/terminal/console/bash on your device
  - Familiarity with basic commands like `cd`, `ls`, and `mkdir`
  - Ability to execute packages, scripts, and commands on your device
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
- A free account at [Coinbase Developer Platform Portal](https://portal.cdp.coinbase.com/access/api)
- An account at [OpenAI Platform](https://platform.openai.com/)
  - To run API Commands on the platform, set up [billing](https://platform.openai.com/account/billing/overview) and add at least **5 USD** credits to your account

## Review of Lesson 22

- AI Agents fundamentals
- Task planning and execution
- RAG integration with agents
- Decentralized AI agents

## Building Blockchain-Enabled Autonomous AI Agents

- Getting started with [AgentKit](https://www.coinbase.com/en-us/developer-platform/discover/launches/introducing-agentkit)
- The [AgentKit](https://docs.cdp.coinbase.com/agentkit/docs/welcome) is a development kit with many building blocks for implementing onchain agents
  - Compatible with other tools, like [LangChain](https://www.langchain.com/), [ElizaOS](https://eliza.how/) and [Vercel AI SDK](https://sdk.vercel.ai/docs/introduction)
  - Many pre-configured tools for wallet and onchain interactions
  - Composable frameworks and extensions
  - Compatible with many wallet providers using the [Wallet API from Coinbase Developer Platform](https://docs.cdp.coinbase.com/wallet-api/docs/welcome)
  - Composable with many [Action Providers](https://docs.cdp.coinbase.com/agentkit/docs/architecture-overview#4-action-providers)
  - Compatible with [Model Context Protocol (MCP)](https://docs.cdp.coinbase.com/agentkit/docs/model-context-protocol)
- Create your first onchain agent with [AgentKit CLI](https://www.npmjs.com/package/create-onchain-agent)
  - Multiple project templates
    - Next.js template for web applications
    - MCP template for Model Context Protocol servers
  - Component generators for existing projects
  - Guided setup with interactive prompts
  - Support for multiple AI frameworks
  - Support for multiple blockchain networks
  - Flexible wallet provider options
  - Automated environment setup

### Getting started with AgentKit

- Creating a project using the [AgentKit CLI](https://www.npmjs.com/package/create-onchain-agent)
- Configuring the necessary environment variables
- Experimenting with onchain actions

- Practical exercises:
  - Exercise 1: Configure and run the [Replit Template for OpenAI Agents SDK with AgentKit](./exercises/00-agentkit-replit-template.md)
  - Exercise 2: [Create a new agent](./exercises/01-agentkit-project.md) using the [AgentKit CLI](https://docs.cdpmjs.com/package/create-onchain-agent)

## Developing AI Agents with Tokenized Incentive Structures

- Reading onchain information inside the agent flow
- Token-gating features
- Guarding agents against Jail-Break exploits
- Implementing approval control flows

## Implementing Custom Function Calling Capabilities

- Adding [custom capabilities](https://docs.cdp.coinbase.com/agentkit/docs/agent-actions#creating-an-action-provider)
- Adding [LangChain Tools integrations](https://docs.cdp.coinbase.com/agentkit/docs/integrate-langchain-tools)

- Practical exercise:
  - Exercise 3: Implement LangChain Tools for [Generating Images with Dall-E](./exercises/02-langchain-tools.md)

## Deploying Decentralized Onchain AI Agents

- Hosting AI Agents
- The problems of "centralized decentralization"
- Denial of Service due centralized hosting
- The concept of [Perpetual AI Agents](https://x.com/OraProtocol/status/1879323919381069864)
- Verifying [Proof of Machinehood](https://blog.ata.network/verifiability-as-the-missing-piece-for-ai-agents-in-web3-504839dca893)

### Deploying an AI Agent to the Agentverse

- Hosting agents in the [Fetch.ai Agentverse](https://fetch.ai/docs/concepts/agent-services/agentverse-intro)
  - Agents can be either [Self Hosted](https://fetch.ai/docs/guides/agents/getting-started/create-a-uagent) or deployed to the [Agentverse](https://fetch.ai/docs/guides/agentverse/creating-agentverse-agents/creating-a-hosted-agent)
- Invoking agents from the Agentverse [Marketplace](https://agentverse.ai/marketplace)

- Practical exercise:
  - Exercise 4: [Deploy a simple AI Agent to the Agentverse](./exercises/03-deploy-decentralized-agent.md)

## Next Steps

- Overview of Decentralized Marketplaces for AI Models and Services
- Exploring Federated Learning for Decentralized AI
- Final project

# Lesson 16: Implementing RAG Tools

OpenAI Assistants can leverage the extensive capabilities of the OpenAI infrastructure for efficient processing of functions like File Search, while abstracting away the complexity of underlying algorithms. However, these benefits come at a cost, similar to the situations we studied when replacing cloud-based LLM inference with locally hosted LLM inference.

In this lesson, we will explore the fundamentals of RAG-based inference by implementing a comprehensive RAG pipeline within a chat application using [LlamaIndex](https://www.llamaindex.ai/) TypeScript libraries.

In the end, we will also explore the Model Context Protocol (MCP) and how it can be used to integrate RAG pipelines with our AI applications.

## Prerequisites

- Proficiency in using a shell/terminal/console/bash on your device
  - Familiarity with basic commands such as `cd`, `ls`, and `mkdir`
  - Ability to execute packages, scripts, and commands on your device
- Node.js installed on your device
  - [Node.js](https://nodejs.org/en/download/)
- Proficiency with `npm` and `npx` commands
  - Documentation: [npm](https://docs.npmjs.com/)
  - Documentation: [npx](https://www.npmjs.com/package/npx)
- Understanding of `npm install` and managing the `node_modules` folder
  - Documentation: [npm install](https://docs.npmjs.com/cli/v10/commands/npm-install)
- Git CLI installed on your device
  - [Git](https://git-scm.com/downloads)
- Proficiency with `git` commands for cloning repositories
  - Documentation: [Git](https://git-scm.com/doc)
- Basic knowledge of JavaScript programming language syntax
  - [JavaScript official tutorial](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
  - [Learn X in Y minutes](https://learnxinyminutes.com/docs/javascript/)
- Basic knowledge of TypeScript programming language syntax
  - [TypeScript official tutorial](https://www.typescriptlang.org/docs/)
  - [Learn X in Y minutes](https://learnxinyminutes.com/docs/typescript/)
- Creation of an account at [OpenAI Platform](https://platform.openai.com/)
  - To run the RAG Commands on the platform, set up [billing](https://platform.openai.com/account/billing/overview) and add at least **5 USD** credits to your account

## Review of Lesson 15

- Retrieval Augmented Generation (RAG)
- Integrating OpenAI Assistants with RAG
- Developing a chat application using OpenAI Assistants
- Implementing RAG in the chat application
- Vercel SDK Quickstart Template for Assistants

## Retrieval-Augmented Generation (RAG) Tools

- Web search capabilities
- File content search
- Video content analysis
- PDF document and book reading
- Windows-specific tool: NVIDIA [Chat with RTX](https://www.nvidia.com/en-us/ai-on-rtx/chatrtx/)
- Python package example: [Haystack](https://haystack.deepset.ai/)
- Multi-language tool (Python and TypeScript): [LlamaIndex](https://www.llamaindex.ai/)
- Enterprise-grade RAG solution: [LangChain](https://www.langchain.com/retrieval)
- Cloud-native RAG solution: [Pinecone](https://www.pinecone.io/solutions/rag/)
- RAG-powered Research Assistant from Google: [NotebookLM](https://notebooklm.google/)

## Implementing a RAG Pipeline

- **Key components of a RAG pipeline**:

  - Document loader: Imports documents from various sources (e.g., PDFs, web pages, databases)
  - Text splitter: Divides documents into manageable chunks for processing
  - Text embedding model: Converts text chunks into numerical vectors
  - Vector store: Stores and indexes embedded text chunks for efficient retrieval
  - Retriever: Identifies relevant text chunks based on a query
  - Language model: Generates responses using retrieved information and the query

- **Implementation steps**:

  1. Load and preprocess documents
  2. Split documents into chunks
  3. Create embeddings for text chunks
  4. Store embeddings in a vector database
  5. Implement the retrieval mechanism
  6. Integrate with a language model for generation

- **Practical considerations**:

  - Optimal chunk size and overlap
    - Avoid splitting words and embedding-critical fragments
    - Maximize size for fitting context-critical parts without chunking, while still keeping the context window in mind
  - Cleaning the dataset
    - Lowering cases
    - Merging spaces
    - Trimming whitespace
    - Cleaning punctuation
    - Flattening special characters
    - Converting numbers to words (ordinal or cardinal when appropriate)
    - Removing meaningless words (e.g., "the", "a", "an", "is") in some cases
    - Lemmatizing words to their reduced form
    - Wiping specific POS (Part of Speech) such as adverbs or interjections in some cases
    - Summarizing paragraphs or segments before chunking
  - Embedding model selection
    - Choosing an embedding model that is appropriate for the type of data and the desired similarity search
  - Vector store scalability
    - [Storing and indexing embeddings efficiently](https://www.pinecone.io/learn/vector-database/)
    - Query processing
    - [K-Nearest Neighbors (KNN) search](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
    - Filtering
      - Weights and medians
      - Keyword search
      - Semantic search
  - Retrieval strategies
    - [Similarity search](https://www.pinecone.io/learn/vector-similarity/)
    - [Semantic search](https://www.sbert.net/examples/applications/semantic-search/README.html)
    - [Hybrid search](https://www.pinecone.io/learn/hybrid-search-intro/)
  - Prompt engineering for effective utilization of retrieved context

- **Advanced RAG techniques**:
  - Multi-document RAG
  - Hierarchical RAG
  - Iterative refinement
  - Agentic RAG

## Constructing a RAG Pipeline with LlamaIndex

- LlamaIndex [Python package](https://docs.llamaindex.ai/en/stable/)
- LlamaIndex [TypeScript package](https://ts.llamaindex.ai/)
- The [TypeScript Playground](https://github.com/run-llama/ts-playground) example project
- Essential [concepts](https://ts.llamaindex.ai/docs/llamaindex/tutorials/rag/concepts)
- Integrating LlamaIndex into a Next.js application

- Practical exercise:
  - Exercise 1: [Build a RAG pipeline](./exercises/00-RAG-With-LlamaIndex.md) using the [LlamaIndex TypeScript Toolset](https://ts.llamaindex.ai/) for chunking uploaded files and generating text based on their content

## Model Context Protocol (MCP)

- The [Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) is an open protocol introduced by [Anthropic](https://www.anthropic.com/news/model-context-protocol) that standardizes how applications provide context to LLMs
  - Acts like a "USB-C port" for AI applications - providing a standardized way to connect AI models to different data sources and tools
  - Helps build agents and complex workflows on top of LLMs by enabling integration with data and tools
- Implementing MCP with AI Applications can add modularity and flexibility for handling context for AI Inferences
  - Pre-built integrations that LLMs can directly plug into
  - Flexibility to switch between LLM providers and vendors
  - Standardized communication between AI models and external tools/data
  - Growing ecosystem of compatible servers and clients
- In the next lessons, we will see about *AI Agents*
  - When studying the subject of *function calling*, we are going to see how MCPs are especially useful for agentic workflows
- Find a list of Model Context Protocol servers in [this open source repository list](https://github.com/modelcontextprotocol/servers)

- Practical exercise:
  - Exercise 2: Implement a simple [Fetch MCP Server](./exercises/01-Fetch-MCP-Server.md) and test it using the  [MCP Inspector](https://github.com/modelcontextprotocol/inspector) tool in your local machine

## Weekend Project

To consolidate this week's learning, complete the following project:

1. Create a GitHub repository for your project
2. Add all group members as collaborators
3. Create a README.md file with a comprehensive project description
4. Use the **LlamaIndex TypeScript Toolset** as a foundation or develop a new application from scratch using Next.js
5. Design a page with a single input field for `.txt` file uploads
   - Users should upload a book or similar content with characters and settings
6. Implement a button to **extract characters** from the uploaded file
7. Develop a RAG pipeline to extract characters from the uploaded file
   - Each character should have a name, description, and personality
8. Add a text area below the button to display the results
9. Convert the output from the AI into an array of objects and present it in a table format
   - (optional) Use [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) to make it easier to process the textual responses in the pages
10. Integrate the `story-telling-app` features to enable users to create new stories using imported characters, reusing their descriptions and personalities inside the stories being generated by the AI
11. Submit your project through the designated submission form

> Locate your group in the [Discord](https://discord.gg/encodeclub) AI Bootcamp Channel
> > If you cannot find your group, please contact the program manager via Discord or email

## Next Steps

- Introduction to Web3 and Smart Contracts
- Implementing Smart Contracts with Solidity
- Introduction to the Ethereum Virtual Machine (EVM)
- Decentralized Computing for AI Applications

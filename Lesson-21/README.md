# Lesson 21: Introduction to AI Agents

In the past weeks, we explored how Large Language Models (LLMs) can generate textual responses to user prompts. These models can follow instructions and call functions while fulfilling user requests. However, after generating an answer, the process typically ends, and the model remains dormant until the next prompt arrives.

Today, we'll delve into the concept of AI Agents, which can continuously run and invoke functions until a specific condition or stop trigger is met. Beyond merely generating textual answers, AI Agents can be assigned tasks and/or goals to accomplish. They attempt to discover the optimal approach to achieve desired results by utilizing LLMs and other AI resources to guide the process.

We'll explore how these AI Agents differ from simple programmed scripts and how the inference process used to generate textual answers can also guide the "thought" process of these agents.

## Prerequisites

- Proficiency in using a shell/terminal/console/bash on your device
  - Familiarity with basic commands like `cd`, `ls`, and `mkdir`
  - Ability to execute packages, scripts, and commands on your device
- Python tools installed on your device
  - [Python](https://www.python.org/downloads/)
  - [Pip](https://pip.pypa.io/en/stable/installation/)
- Proficiency with `python` and `pip` commands
  - Documentation: [Python](https://docs.python.org/3/)
  - Documentation: [Pip](https://pip.pypa.io/en/stable/)
- Familiarity with `venv` for creating and managing virtual environments
  - Documentation: [Python venv](https://docs.python.org/3/library/venv.html)
- Node.js installed on your device
  - [Node.js](https://nodejs.org/en/download/)
- Proficiency with `npm` and `npx` commands
  - Documentation: [npm](https://docs.npmjs.com/)
  - Documentation: [npx](https://www.npmjs.com/package/npx)
- Understanding of `npm install` and managing the `node_modules` folder
  - Documentation: [npm install](https://docs.npmjs.com/cli/v10/commands/npm-install)
- Git CLI installed on your device
  - [Git](https://git-scm.com/downloads)
- Proficiency with `git` commands for repository cloning
  - Documentation: [Git](https://git-scm.com/doc)

## Review of Lesson 20

- Weekend project
- Blockchain-Backed Data Verification
- User Authentication in AI Apps
- Storing and Verifying AI Outputs

## AI Agents

### Overview

- The common "SaaS" business model
  - Using applications to provide services
    - Automation of repetitive or mundane tasks
    - Reducing human intervention
    - Increasing efficiency
    - Reducing costs
    - Improving accuracy
    - Increasing speed
    - Providing 24/7 availability
    - Scaling effortlessly
    - Ability to work on multiple tasks simultaneously
    - Reduced bias in decision-making processes (when properly designed)
  - Human in the loop with backoffice applications, if needed
- AI Agents for _replacing_/enhancing SaaS applications
  - General purpose AI Agents
  - No specific knowledge of the task domain
  - LLM as the core component for "reasoning"
  - Can be enhanced with tools and plugins to perform specific tasks
  - Multilingual support

### Architecture of AI Agents

- The AI Agent "reasoning" process
  - **Differs from static programs** built with coded scripts and well-defined methods
  - AI Agents attempt to "figure out" the best approach to achieve desired results using LLMs and other AI resources
  - A conventional program relies on scripted logic to respond to user input, while an AI Agent uses LLMs to determine the optimal course of action
  - LLM limitations also apply to AI Agents' "reasoning" process:
    - Struggle with complex tasks requiring extensive information processing
    - Difficulty with tasks demanding specificity and accuracy due to potential hallucinations or mistakes
    - Challenges with tasks requiring creativity, as they may struggle to generate original ideas beyond training data
  - AI Agents can be assigned tasks and/or goals, and they strive to discover the best method to achieve desired outcomes using LLMs and other AI resources
- Agent Functions
  - **Core components** of an AI Agent
  - Can be considered the "brain" of an AI Agent
  - Triggered by users or other functions when fulfilling a prompt
- Agent programs
  - Provide infrastructure for hosting and managing agent function invocations and fulfillments
  - Offer an interface to interact with agent functions by:
    - Initiating processes
    - Defining and managing goals
    - Monitoring the agent's progress and status
    - Orchestrating the agent's execution
    - Handling agent's failures and errors
    - Providing feedback and information to the user
  - **Context/state management** is crucial for the agent's execution:
    - Allows tracking of the agent's progress and status
    - Provides necessary information to agent functions
    - Manages all data that needs to be handled/carried between different function invocations
    - Essential because LLMs cannot independently maintain the agent's state between function calls
  - **Performance management** is a significant role of the agent program:
    - Inference operations can be computationally intensive, especially with larger models
    - Ensures each step is executed efficiently to deliver expected results
    - Optimizes task execution to balance performance and accuracy

## Types of Agents

- **Single-step Agents**
  - Perform a single task or action
  - No extended "reasoning" or planning beyond the task at hand
  - Executes the task in a single code block or textual output
  - Example: [CodeAgent](https://huggingface.co/docs/transformers/en/agents#code-agent)
- **Reactive Agents**
  - Most basic type, capable of responding only to direct user input
  - No extended "reasoning" or planning beyond answering user input
  - Example: [ReactCodeAgent](https://huggingface.co/docs/transformers/en/agents#react-agents)
- **Reflective Agents**
  - Simple reflex agents
    - Operate based on predefined rules and immediate data
    - Limited to reacting within given event-condition-action rules
    - Precise and efficient but unable to handle undefined situations
  - Model-based reflex agents
    - More sophisticated decision-making mechanism
    - Utilize Large Language Models (LLMs) to infer probable outcomes based on current state and goals
    - Attempt to evaluate consequences of action paths before determining task execution order
    - Leverage available data to construct an "emulated model of the world" for decision support
  - Example: [Operator](https://openai.com/index/introducing-operator/)
- **Rule-based Agents**
  - AI agents with more robust "reasoning" capabilities
  - Analyze environmental data and compare approaches to achieve desired outcomes
  - Goal-based agents aim to select the most efficient path
  - Agent program employs Natural Language Processing (NLP) for "reasoning" based on available information and goals
  - Example: [Goal-based Agent](https://docs.crewai.com/concepts/agents)
- **Hierarchical Agents**
  - Comprise multiple AI entities organized in a layered structure
  - Top-tier agents decompose complex objectives into manageable subtasks, which are then assigned to lower-level agents
  - Each individual agent functions autonomously and reports progress to its overseeing agent
    - Lower-tier agents can be simpler implementations, such as reactive or reflective agents
  - Higher-level agents consolidate outcomes and coordinate the efforts of their subordinates to ensure overall goal achievement
  - Example: [CrewAI](https://docs.crewai.com/concepts/crews)

## Building Agents on top of OpenAI Features  

- OpenAI Assistants features (review)
  - [Code Interpreter](https://platform.openai.com/docs/assistants/tools/code-interpreter)
  - [File Search](https://platform.openai.com/docs/assistants/tools/file-search)
    - [Vector Stores](https://platform.openai.com/docs/assistants/tools/file-search/vector-stores)
  - [Function Calling](https://platform.openai.com/docs/assistants/tools/function-calling)
    - [Function Call Workflow](https://platform.openai.com/docs/guides/function-calling)
    - Using [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs/introduction) for [Function Calling](https://platform.openai.com/docs/guides/function-calling/function-calling-with-structured-outputs)
- Building Agents with OpenAI Tools using [LangChain](https://python.langchain.com/v0.1/docs/modules/agents/agent_types/openai_tools/)
- Building Agents with OpenAI features using [LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent/)

## Automation Process

- Goals
  - Agent Programs are designed to receive specific instructions to scope one or more measurable goals that govern the agent's execution
    - These goals determine the **task planning** process, where the agent composes a set of actions it "believes" necessary to achieve the desired results, according to how the NLP models can "reason" about concepts related to the passed goals and the agent's training to trigger each programmed function
    - The model's training allows linking actionable tasks to specific concepts or sets of concepts contained in the output of an inference operation from a prompt
  - Each goal is defined as a desirable outcome that the agent can "understand" sufficiently to evaluate at any given moment whether that goal has been achieved
- Information acquisition
  - The agent must gather information from various sources to achieve the desired results, and the agent program must provide the necessary tools for this purpose
  - In some cases, all required information is already accessible to the Agent Program, simplifying the process to selecting available information from the source and passing it to subsequent tasks
  - In other instances, when information is not readily available, the agent may need to trigger intermediary tasks for function invocations before proceeding with the main task initially chosen to progress towards the desired goal
  - These tasks could include:
    - Using the `web_search` function to search for information on the web
    - Employing the `file_search` function to search for information in local files
    - Utilizing the `vector_search` function to search for information in the vector database
- Implementing tasks
  - When the agent program determines that the goal has not yet been achieved but sufficient data exists to execute the next task, it methodically implements the next task by invoking the agent functions programmed to handle the task with the provided data
  - Upon task completion, the program removes it from the list of planned tasks and proceeds to the next task until the goal is achieved
  - If the agent exhausts its task list, the program can be configured to either devise an alternative task plan or halt, report progress to the user, and terminate execution
- "Reasoning"
  - The "reasoning" process in AI agents typically follows a decision flow with nodes and edges:
    - Nodes represent agents and tools:
      - Agent nodes: Different types of agents (e.g., reactive, reflective, rule-based) that process information and make decisions
      - Tool nodes: Functions or APIs that agents can use to gather information or perform actions
    - Edges represent conditions and checks:
      - Condition edges: Logical conditions that determine which path the decision process should take
      - Check edges: Validation steps to ensure the output of a node meets certain criteria before proceeding
  - The decision process flow involves traversing nodes and edges while updating the execution state of the agent program at each step
    - The agent program must provide a mechanism to update the agent program's state at each step, enabling it to track the agent's progress and status, and supply necessary information to agent functions
  - This flow of actions between nodes and edges forms a **graph**
    - The graph can be evaluated before execution to estimate possible paths
    - This evaluation helps optimize the agent's goal by:
      - Filtering out paths that don't lead to goal achievement
      - Eliminating paths that are significantly longer than shorter alternatives
  - The process of **routing** choices between nodes and edges forms the **decision process** of the agent
    - Since LLMs cannot truly "reason" about how to draw these routes based on available information in the state and goal criteria, the "emulated reasoning" process involves passing available node choices to the LLM and then running a completion task to generate probable outputs

## Examples of AI Agents

- [LangChain](https://www.langchain.com/agents): AI Agent Solution from LangChain
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT): Open-source tool for building AI Agents
- [GPT Engineer](https://github.com/gpt-engineer-org/gpt-engineer): Open-source software for writing code from natural language descriptions
- [AgentGPT](https://agentgpt.reworkd.ai/): Web-based AI agent creation platform
- [BabyAGI](https://github.com/yoheinakajima/babyagi): One of the first task management systems using AI
- [ChatDev](https://github.com/OpenBMB/ChatDev): Virtual software company for AI-driven development
- [Crew AI](https://www.crewai.com/): AI Agent Framework for multi-agent automation
- [Agentverse](https://agentverse.ai/): A platform for building, running, and managing AI agents
- [Jarvis](https://github.com/microsoft/JARVIS): An AI Agent developed by Microsoft that can _figure out_ what models from Hugging Face to use for given tasks planned by the Agent to answer the prompts
- [AI Agents List](https://github.com/e2b-dev/awesome-ai-agents): A list of AI Agents maintained by [E2B](https://e2b.dev/) developers

## Setting up an AI Agent

- Installing necessary tools
- Configuring the environment
- Creating the agent program
- Building agent functions
- Integrating the agent with the agent program
- Testing the agent

- Practical exercise:
  - Exercise 01: Implementing a [Simple AI Agent](./exercises/00-Simple-AI-Agent.md) to experiment with AI Agents using the [BabyAGI](https://github.com/yoheinakajima/babyagi) sample project

## Using Functions to Enhance "Reasoning"

- How to [teach reasoning](https://openai.com/index/learning-to-reason-with-llms/) on top of non-reasoning text-generation processes
  - OpenAI [o1](https://openai.com/index/introducing-openai-o1-preview/) example
- Automating the Chain of Thought prompt generation with agents
  - Amazon Web Services [Auto-CoT](https://arxiv.org/pdf/2210.03493) example
- Variations for Chain of Thought
  - [Tree of Thoughts](https://github.com/princeton-nlp/tree-of-thought-llm) (ToT)
  - [Graph of Thoughts](https://github.com/spcl/graph-of-thoughts) (GoT)
  - [Algorithm of Thoughts](https://github.com/kyegomez/Algorithm-Of-Thoughts) (AoT)

## Next Steps

- Utilizing RAG pipelines with Agents
- Managing agent information context
- Goals and tasks
- Constructing an Agentic RAG
- Introduction to computer vision

# Implementing LangChain Tools

The AgentKit Action Providers allows for easy integration with external tools, like LangChain actions.

## Steps

1. Open the project created in the previous exercise:

   ```bash
   cd onchain-agent
   code .
   ```

2. Install the necessary dependencies:

   ```bash
   npm install @langchain/openai
   ```

3. Import Required Modules

   - Open the `app/api/agent/create-agent.ts` file
   - Modify the import from `@langchain/openai` to include the `DallEAPIWrapper`

   ```typescript
   import { ChatOpenAI, DallEAPIWrapper } from "@langchain/openai";
   ```

4. Update Agent Initialization

   - Keep editing the `app/api/agent/create-agent.ts` file
   - Locate the line that initializes the `tools` constant inside the `createAgent` function

   ```typescript
   const tools = await getLangChainTools(agentkit);
   ```

   - Add the `DallEAPIWrapper` to the `tools` array

   ```typescript
    const dallETool = new DallEAPIWrapper({
      n: 1,
      model: "dall-e-3",
      apiKey: process.env.OPENAI_API_KEY,
    });
    tools.push(dallETool);
   ```

5. Run the project

   - Start the development server

   ```bash
   npm run dev
   ```

   - Access the application at <http://localhost:3000>

6. Test the agent

   - Ask the agent to generate an image of a pizza

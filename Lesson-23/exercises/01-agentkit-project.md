# Creating an Onchain Agent with AgentKit

Create a simple onchain agent that can check token balances using the AgentKit CLI tool.

## Steps

1. Create a new project:

   ```bash
   npm create onchain-agent@latest -y
   ```

   Choose:
   - Project name: `onchain-agent`
   - AI Framework: `Langchain`
   - Network family: `Ethereum Virtual Machine (EVM)`
   - Network type: `Testnet`
   - Network: `Base Sepolia`
   - Wallet Provider: `CDP`

2. Install dependencies:

   ```bash
   cd onchain-agent
   npm install
   ```

3. Configure the environment variables:

   - Edit the `.env.local` file with your own values

   ```text
   OPENAI_API_KEY=
   CDP_API_KEY_NAME=
   CDP_API_KEY_PRIVATE_KEY=
   ```

4. Test the project:

   ```bash
   npm run dev
   ```

   - Access the application at <http://localhost:3000>

5. Test your agent:
   - Ask about the balance of a token
   - Send tokens to another wallet
   - Deploy a smart contract

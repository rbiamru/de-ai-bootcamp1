# Creating and Deploying an ERC20 Token

1. Visit the OpenZeppelin Wizard at [wizard.openzeppelin.com](https://wizard.openzeppelin.com)

2. Configure your token
   - Select "ERC20" from the contract type
   - Choose the following features:
     - Mintable
     - Burnable
     - Pausable
   - Set your token details:
     - Name: `Your Token Name`
     - Symbol: `YTN`
     - Decimals: `18`
     - Initial Supply: `1000000`

3. Copy the generated contract code

4. Open Remix IDE at [remix.ethereum.org](https://remix.ethereum.org)

5. Create a new file
   - Click the "Create New File" button
   - Name it "MyToken.sol"
   - Paste the contract code from OpenZeppelin

6. Compile the contract
   - Click the "Solidity Compiler" tab
   - Keep the recommended compiler version
   - Click "Compile MyToken.sol"

7. Deploy the contract
   - Click the "Deploy & Run Transactions" tab
   - Select "Injected Provider - MetaMask" as the environment
   - Make sure you're on Sepolia testnet
   - Copy your address and paste it into the "Recipient" and "Initial Owner" fields
   - Click "Deploy"
   - Confirm the transaction in MetaMask

8. Interact with your deployed contract
   - After deployment, you'll see your contract's functions
   - Try these operations:
     - Mint tokens to your address
     - Transfer tokens to another address
     - Check balances
     - Burn some tokens
     - Pause and unpause the contract

9. View your contract on Etherscan
   - Copy your contract address
   - Visit [Sepolia Etherscan](https://sepolia.etherscan.io)
   - Search for your contract address
   - View the contract's transactions and interactions

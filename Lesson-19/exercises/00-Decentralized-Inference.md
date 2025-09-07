# Exercise 1: Experimenting with the OAO Sample Prompt Contract Implementation

1. Open the [OAO repository](https://github.com/ora-io/OAO) in [Remix IDE](https://remix.ethereum.org/)
   - Click on the hamburger menu for the `WORKSPACES` section
   - Select the `Clone` option
   - Pase the URL of the repository in the `Repository URL` field
      - URL: <https://github.com/ora-io/OAO>
2. Open the `Prompt.sol` file in the `contracts` folder and compile it
3. Go for the `Deploy & run transactions` tab and select the `injected provider` environment
4. Make sure that your wallet is connected to the `sepolia` network
5. Go for the the `At Address` button, paste the example `Prompt` contract address (`0xe75af5294f4CB4a8423ef8260595a54298c7a2FB` for the `sepolia` network), and then click on the `At Address` button
6. Scroll down to the `Deployed Contracts` section and click on the `Prompt` contract
7. Click on the `estimateFee` function and set the model ID to `11`
8. Copy the returned value and set it as the transaction value (in wei)
   - Scroll up to see the `VALUE` field, and make sure that the dropdown is set to `Wei`
9. Click on the `calculateAIResult` function and set the model ID to `11` and the prompt text to `"What is the capital of France?"`
10. Click on the red `Transact` button and confirm the popup on your wallet to execute the transaction
11. Wait for the transaction to be confirmed
    - It might take a little while until the callback is executed and the result is available
12. When the callback is executed, the result is stored in the storage of the `Prompt` contract
    - The `prompt` function can be called to retrieve the result, by passing the model ID and prompt text again
13. Try this process with a different prompt, for example: `"How to make a perfect chocolate cake?"`

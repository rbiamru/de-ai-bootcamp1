# Connecting to OpenAI API with GPT4All

1. Open the GPT4All application on your computer

2. Open the `Models` tab

3. Click on the `Add Model` button

4. Search for the `OpenAI-Compatible API Model`

   - Input your OpenAI API key in the `$API_Key` field
     - You can find this in the `API Keys` section of your OpenAI account
     - If you have this key set up in your environment, you can copy it from there too
     - If you don't have one:
       - Go to the [OpenAI website](https://platform.openai.com)
       - Sign up for an account or log in if you already have one
       - Navigate to the API section and create a new API key
       - Copy the API key (make sure to save it securely, as you won't be able to see it again)
   - Input the OpenAI API base URL in the `$API_Base` field
     - The default is <https://api.openai.com/v1>
   - Input the model name in the `$Model` field
     - For example `gpt-4o` or `gpt-4o-mini`

5. You should now see an option to select OpenAI models alongside the local models

6. Try a simple prompt to test the connection:
   "What are the main differences between GPT-3 and GPT-4?"

7. Observe the response and note any differences in quality or speed compared to local models

8. Experiment with different OpenAI models if available

9. Compare the results of the same prompt using both local and OpenAI models:
   "Explain the concept of neural networks in simple terms."

10. Try a more specialized prompt that might benefit from OpenAI's broader knowledge:
    "What are the latest advancements in fusion energy research?"

11. Explore the capabilities of the OpenAI connection:

    - Code generation: "Write a Python function to calculate the Fibonacci sequence."
    - Language translation: "Translate 'Hello, how are you?' into French, Spanish, and Japanese."
    - Creative writing: "Write a short poem about the intersection of technology and nature."

12. Consider the trade-offs between using local models and the OpenAI API:
    - Speed of responses
    - Quality and accuracy of outputs
    - Privacy considerations
    - Bias and censorship
    - Costs (OpenAI API usage is metered)

> Remember to be mindful of your API usage, as OpenAI charges based on the number of tokens processed. Always review and follow OpenAI's usage policies and guidelines when using their API.

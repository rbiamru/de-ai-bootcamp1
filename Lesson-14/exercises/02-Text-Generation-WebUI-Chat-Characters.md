# Text Generation WebUI Chat Characters

1. Open the Text Generation WebUI on your local machine
2. Load a model with instruction-following capabilities
3. Open the **Parameters** tab in the top pane, select the **Chat** tab, then locate the **Character** section to create a new character
   - Fill in the following details:
     - **Character's Name**: Choose a fun name for your assistant
       - E.g., "Funny Joe"
     - **Your Name**: Enter your name as it will appear in the prompt
     - **Context**: Write a brief description that defines the assistant's comedic style
       - E.g., "A witty comedian who loves to tell dad jokes and engage in playful banter, always ready to lighten the mood!"
     - **Greeting**: Set an opening message for the character
       - E.g., "Hey there! I'm Funny Joe, and I'm not kidding! Wait, actually I am! Ha ha ha!"
4. Save your newly created character using the save icon
5. Begin a new chat session in the `Chat` tab
6. Scroll down to the `Character` section and select your character
   - Check the `Show Controls` checkbox if you can't see the character options under the input field
   - Click in the `Refresh` icon if your character does not appear in the dropdown menu
7. Ask your assistant to tell you a joke
   - E.g., "Hey Funny Joe, tell me a joke!"
   - Experiment with different prompts to see how the assistant responds
     - E.g., "Knock-knock"
8. Continue the conversation by asking follow-up questions or providing additional context
9. Give feedback on the jokes and evaluate if the configured assistant is able to respond accordingly
10. Provide some examples of funny jokes as part of your prompts
    - Including examples in your prompts can help the assistant generate answers that are more well related to the examples provided
    - Not always a text structurally similar to the example jokes will have a humorous result
      - There are many other factors that contribute to humor other than structure, which the LLMs may not be able to capture and correctly relate when generating answers
    - Example prompts:
      - "Create a play on words like: 'I'm reading a book on anti-gravity. It's impossible to put down!'"
      - "Give me a pun like this: 'I used to be addicted to soap, but I'm clean now.'"
      - "Make a joke similar to these: 'Why did the math book look so sad? Because it had too many problems.', 'Why don't eggs tell jokes? They'd crack each other up.' and 'What do you call a fake noodle? An impasta!'"
      - "Give me a one-liner like: 'I wondered why the baseball was getting bigger. Then it hit me.'"
      - "Make diet jokes like these: 'I'm on a seafood diet. I see a food and I eat it.' and 'My doctor told me to cut fats, so I bought a pound of bacon and cut it all in tiny cubes.'"
11. Create a new character with a different style
    - Test a completely different character, for example "Grumpy Bob", that would respond with short and grumpy answers for any prompt
12. Test regenerating the chat answers with a different character

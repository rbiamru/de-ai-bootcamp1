# Building a RAG Pipeline with LlamaIndex using Create-Llama

In this exercise, we'll build a RAG (Retrieval Augmented Generation) application using LlamaIndex and the `create-llama` tool, which provides a full-featured starter template.

1. Create a new LlamaIndex application

   ```bash
   npx create-llama@latest
   ```

   When prompted, choose the following options:
   - Project name: `rag-app`
   - What app do you want to build: `Agentic RAG`
   - What language do you want to use: `Typescript (NextJS)`
   - Do you want to use LlamaCloud services: `No`
   - Please provide your OpenAI API key: Paste your OpenAI API key (`sk-proj-...`)
     - If you have it configured in your machine's environment variables, you can leave it blank
   - How would you like to proceed: pick the `Just generate code` option
     - We will install the dependencies and run the app in the next steps

2. Navigate to the project directory and install dependencies

   ```bash
   cd rag-app
   npm install
   ```

3. Set up your environment variables

   - Tweak the keys and configurations for this project in the `.env` file

4. Run the development server

   ```bash
   npm run dev
   ```

5. Open the application in your browser

   - Navigate to <http://localhost:3000>
   - You'll see a modern interface with file upload capabilities and chat functionality

6. Test the RAG features

   - Click on the "Upload files" button
   - Upload the [Shrek.txt](../examples/Shrek.txt) file
   - Wait for the file to be processed and indexed
   - Use the chat interface to ask questions about the content
   - Try queries like:
     - "List the name, description, and personality of every character"
     - "What happens at the beginning of the story?"
     - "Describe Lord Farquaad's character"

7. Explore the code structure

   ```bash
   code .
   ```

   Key files and directories to examine:
   - `/app`: Contains the main application code
   - `/app/api`: Backend API routes
   - `/app/page.tsx`: Main page component with the chat wrappers
   - `/app/components`: React components
   - `app/components/chat-section.tsx`: Main component for the chat interface
     - Modify the page inside or around the `ChatSectionUI` component to change the chat interface
   - `/app/components/ui`: Atomic components for the UI elements in the chat

8. Understanding the RAG Pipeline

   The application uses several key components:
   - File processing and chunking
   - Vector embeddings generation
   - Similarity search
   - LLM-based response generation

9. Customization (Optional)

   You can customize various aspects of the application:
   - Adjust the chunk size in the configuration
   - Modify the prompt templates
   - Customize the UI components

10. Best Practices

    - Keep your API keys secure in the `.env` file
    - Monitor your API usage
    - Document your changes and commit them often to keep track of your progress and to avoid losing much of your work in case of unexpected issues

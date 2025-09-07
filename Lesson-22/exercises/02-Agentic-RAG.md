# Implementing an Agentic RAG with LlamaIndex

1. Set up the environment

   - Skip this step if you have already set up the environment

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Setup LlamaIndex

   - Skip this step if you have already set up the environment

   ```bash
   pip install llama-index
   ```

3. Create an [API key](https://cloud.llamaindex.ai/api-key) for LlamaCloud

4. Set the API key in your environment

   ```bash
   export LLAMA_CLOUD_API_KEY="<your API key>"
   ```

   - Replace `<your API key>` with your actual API key from LlamaCloud

   - For Windows, use one of the following commands:

     ```bash
     # If using a command prompt, use the following command:
     setx LLAMA_CLOUD_API_KEY "<your API key>"

     # If using PowerShell, use the following command:
     $env:LLAMA_CLOUD_API_KEY = "<your API key>"
     ```

5. Create a python file

   ```bash
   touch agentic-rag.py
   ```

6. Open the file in VSCode

   ```bash
   code agentic-rag.py
   ```

7. Download a sample document

   - For example, download the [Zork I Manual](https://infodoc.plover.net/manuals/zork1.pdf)
     - Place the file in the same directory as the python file

8. Add the needed imports

   ```python
   from llama_index.core import VectorStoreIndex, Settings
   from llama_index.core.tools import QueryEngineTool
   from llama_index.core.agent import ReActAgent
   from llama_parse import LlamaParse
   from llama_index.llms.openai import OpenAI
   ```

9. Set the model settings

   ```python
   Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0)
   ```

10. Define the Query Engine

    ```python
    documents = LlamaParse(result_type="markdown").load_data(
        "./<file>.pdf"
    )
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    ```

    - Replace `<file>.pdf` with the name of the file you downloaded
      - For example: `zork1.pdf`
    - You can test the query engine with the following command:

      ```python
      response = query_engine.query(
          "<your question>"
      )

      print(response)
      ```

      - Replace `<your question>` with the question you want to ask
        - For example: `What is the concept of interactive fiction?`

11. Define and configure the Query Engine Tool

    ```python
    query_tool = QueryEngineTool.from_defaults(
        query_engine,
        name="<name>",
        description="<description>",
    )
    ```

    - The name of the tool should represent the most probable word to be linked with the tool when the agent is asked to perform a task
    - Replace `<name>` with the name of the tool
      - For example: `Zork`
    - Replace `<description>` with the description of the tool
      - For example: `A RAG engine with the Game Manual for Zork I: The Great Underground Empire.`

12. Define an agent to use the tool

    ```python
    agent = ReActAgent.from_tools(
        [query_tool], verbose=True
    )
    ```

13. Test the RAG agent

    ```python
    agent.chat("<your question>")
    ```

    - Replace `<your question>` with the question you want to ask
      - For example: `How to play Zork I?` or `Explain a step by step on how to beat the first level of Zork I.`

14. Run the agent

    ```bash
    python agentic-rag.py
    ```

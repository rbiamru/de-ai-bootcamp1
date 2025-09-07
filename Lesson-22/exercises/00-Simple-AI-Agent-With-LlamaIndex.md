# Implementing a Simple AI Agent with LlamaIndex

1. Set up the environment

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Setup LlamaIndex

   ```bash
   pip install llama-index
   ```

3. Create a python file

   ```bash
   touch agent.py
   ```

4. Open the file in VSCode

   ```bash
   code agent.py
   ```

5. Add the needed imports

   ```python
   from llama_index.core.tools import FunctionTool
   from llama_index.llms.openai import OpenAI
   from llama_index.core.agent import ReActAgent
   ```

6. Define the function

   ```python
   def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b
   ```

7. Define and configure the agent

   ```python
   multiply_tool = FunctionTool.from_defaults(fn=multiply)
   llm = OpenAI(model="gpt-4o-mini")
   agent = ReActAgent.from_tools([multiply_tool], llm=llm, verbose=True)
   ```

8. Test the agent

   ```python
   agent.chat("What is 123 * (1 + 2 + 3)?")
   ```

9. Run the agent

   ```bash
   python agent.py
   ```

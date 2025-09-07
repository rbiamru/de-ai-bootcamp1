# Implementing a Structured Planning AI Agent with LlamaIndex

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

3. Create a python file

   ```bash
   touch worker.py
   ```

4. Open the file in VSCode

   ```bash
   code worker.py
   ```

5. Add the needed imports

   ```python
   from llama_index.core.tools import FunctionTool
   from llama_index.llms.openai import OpenAI
   from llama_index.core.agent import (
       StructuredPlannerAgent,
       FunctionCallingAgentWorker,
   )
   ```

6. Define the function

   ```python
   def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b
   ```

7. Define and configure the worker agent

   ```python
   multiply_tool = FunctionTool.from_defaults(fn=multiply)
   llm = OpenAI(model="gpt-4o-mini")
   worker = FunctionCallingAgentWorker.from_tools([multiply_tool], llm=llm, verbose=True)
   worker_agent = StructuredPlannerAgent(worker, [multiply_tool], verbose=True)
   ```

8. Test the worker agent

   ```python
   worker_agent.chat("Solve the equation x = 123 * (x + 2y + 3)")
   ```

9. Run the agent

   ```bash
   python worker.py
   ```

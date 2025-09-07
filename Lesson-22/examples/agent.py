from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent


def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)
llm = OpenAI(model="gpt-4o-mini")
agent = ReActAgent.from_tools([multiply_tool], llm=llm, verbose=True)

agent.chat("What is 123 * (1 + 2 + 3)?")

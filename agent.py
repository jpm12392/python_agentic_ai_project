from llm import call_llm
from tools import calculator, search

TOOLS = {
    "calculator": calculator,
    "search": search
}

class Agent:
    def __init__(self):
        self.memory = []

    def decide(self, goal: str) -> str:
        prompt = f"""
You are an AI agent.

Goal: {goal}

Decide which tool to use:
- calculator (for math)
- search (for information)

Respond ONLY in this format:
TOOL:<tool_name>
INPUT:<tool_input>
"""
        return call_llm(prompt)

    def act(self, decision: str) -> str:
        lines = decision.split("\n")
        tool_name = lines[0].replace("TOOL:", "").strip()
        tool_input = lines[1].replace("INPUT:", "").strip()

        tool = TOOLS.get(tool_name)
        if not tool:
            return "Unknown tool selected."

        result = tool(tool_input)
        self.memory.append((tool_name, tool_input, result))
        return result

    def run(self, goal: str) -> str:
        decision = self.decide(goal)
        return self.act(decision)

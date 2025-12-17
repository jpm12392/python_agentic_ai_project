from agent import Agent

agent = Agent()

while True:
    goal = input("\nEnter your goal (or 'exit'): ")
    if goal.lower() == "exit":
        break

    result = agent.run(goal)
    print("Agent Output:", result)

from agents.planner import planner_agent
from agents.executor import executor_agent

task = "Find trending GitHub repositories and weather in Mumbai"

plan = planner_agent(task)

print("PLAN:")
print(plan)

result = executor_agent(plan)

print("\nEXECUTION RESULT:")
print(result)

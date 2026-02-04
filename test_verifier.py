from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.verifier import verifier_agent

task = "Find trending GitHub repositories and weather in Mumbai"

plan = planner_agent(task)

execution_result = executor_agent(plan)

final_answer = verifier_agent(task, execution_result)

print("\nFINAL OUTPUT:\n")
print(final_answer)

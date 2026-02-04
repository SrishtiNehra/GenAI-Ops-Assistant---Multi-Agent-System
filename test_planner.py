from agents.planner import planner_agent

task = "Find trending GitHub repositories and weather in Mumbai"

plan = planner_agent(task)

print(plan)

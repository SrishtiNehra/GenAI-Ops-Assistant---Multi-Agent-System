import json
import re
from llm.llm_client import call_llm


def extract_json(text):
    """
    Extract JSON object from LLM output safely
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group()
    return None


def planner_agent(user_task: str):
    """
    Converts user task into JSON execution plan
    """

    prompt = f"""
You are a Planner Agent.

Convert the following user request into a STRICT JSON execution plan.

User Request:
{user_task}

IMPORTANT RULES:
- Output ONLY raw JSON
- Do NOT add explanation
- Do NOT add markdown
- Do NOT add text outside JSON
- JSON must start with {{ and end with }}

Use tools: github, weather

Output format:

{{
  "steps": [
    {{"tool": "github", "action": "get_repos", "params": {{"location": "CITY"}}}},
    {{"tool": "weather", "action": "get_weather", "params": {{"location": "CITY"}}}}
  ]
}}
"""

    response = call_llm(prompt)

    cleaned_json = extract_json(response)

    if not cleaned_json:
        raise ValueError("Planner could not generate valid JSON")

    plan = json.loads(cleaned_json)

    return plan

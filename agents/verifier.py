from llm.llm_client import call_llm


def verifier_agent(user_task: str, execution_result: dict):
    """
    Verifies output and formats final response
    """

    prompt = f"""
You are a Verifier Agent.

User Request:
{user_task}

Execution Result:
{execution_result}

Tasks:
- Check if all required information is present
- Format the output nicely for user
- Return clear readable final answer
"""

    final_output = call_llm(prompt)

    return final_output

from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.verifier import verifier_agent

app = FastAPI()


class TaskRequest(BaseModel):
    task: str


@app.post("/run")
def run_ai_ops(task_request: TaskRequest):

    task = task_request.task

    plan = planner_agent(task)

    execution_result = executor_agent(plan)

    final_answer = verifier_agent(task, execution_result)

    return {
        "task": task,
        "plan": plan,
        "result": execution_result,
        "final_answer": final_answer
    }

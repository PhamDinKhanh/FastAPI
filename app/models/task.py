from pydantic import BaseModel


class TaskModel(BaseModel):
    id: int
    summary: str
    description: str
    status: str
    priority: str

    def __init__(id, summary, description, status, priority):
        self.id= id
        self.summary = summary
        self.description = description
        self.status = status
        self.priority = priority
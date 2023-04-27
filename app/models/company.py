from pydantic import BaseModel


class CompanyModel(BaseModel):
    id: int
    name: str
    description: str
    mode: str
    rating: str

    def __init__(id, name, description, mode, rating):
        self.id = id
        self.name = name
        self.description = description
        self.mode = mode
        self.rating = rating
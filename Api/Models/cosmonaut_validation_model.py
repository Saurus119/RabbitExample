from pydantic import BaseModel, constr

class Cosmonaut(BaseModel):
    name: constr(max_length=100)
    
    def __str__(self) -> str:
        return f"Cosmounamt(name={self.name})"
    
from pydantic import BaseModel, Field


class Test:
    id: str = ""
    is_done: bool = False
    num: int = Field(default=0)


result = hasattr(Test, "num")
attr = dir(Test)

print(result)
print(attr)

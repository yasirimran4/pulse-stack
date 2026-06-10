from typing import Annotated
from pydantic import Field ,BaseModel , AnyUrl

class CreateMonitorRequest(BaseModel):
    name : Annotated[str,Field(...,min_length=3,max_length=100,description="Name of the Monitor")]
    url : Annotated[AnyUrl,Field(...,description="URl of the Website")]
    interval_time = Annotated[int,Field(...,ge=1)] # Interval time should be greater than one








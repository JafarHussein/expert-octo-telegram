from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4
from typing import Optional

# This is the blueprint of how every user should look like
class UserBluePrint(BaseModel):
    user_id:UUID=Field(default_factory=uuid4)
    first_name:str
    last_name:str
    email:str
    password:str
    username:Optional[str]
    
# This is the class that is going to be used to validate users
class UserLogin(BaseModel):
    username:str
    email:Optional[str]
    password:str
    
# This is the response that the api is going to retur once it sends back a response

class UserResponse(BaseModel):
    username:str
    email:str
    created_at:datetime
    
# This is the category create blueprint

class CategoryCreate(BaseModel):
    category_id:UUID=Field(default_factory=uuid4)
    category_name:str
    category_monthly_spend_limit:int
    created_at:datetime
    
class CategoryUpdate(BaseModel):
    category_name:Optional[str]=None
    monthly_spend_limit:Optional[int]=None
    
class CategoryResponse(BaseModel):
    id:UUID
    user_id:UUID=Field(default_factory=uuid4)
    category_name:str
    monthly_spend_limit:int
    
class ExpenseCreate(BaseModel):
    category_id:UUID=Field(default_factory=uuid4)
    amount:float=Field(gt=0)
    description:str
    transaction_date:datetime
    created_at:datetime
    updated_at:datetime | None
    
# Now lets create the summaries needed


    


    
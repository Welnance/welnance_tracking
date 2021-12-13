from datetime import datetime
from pydantic import BaseModel
import pytz
class Socials(BaseModel):
   
    Facebook : int
    Twitter : int
    CMC : int
    Date : datetime 
    Info : str
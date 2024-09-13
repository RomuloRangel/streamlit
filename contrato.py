from pydantic import BaseModel, EmailStr, validate_call, PositiveFloat, PositiveInt 
from datetime import datetime
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "ZapFlow com Gemini"
    produto2 = "ZapFlow com ChatGPT"
    produto3 = "ZapFlow com Lhama 3.0"


class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

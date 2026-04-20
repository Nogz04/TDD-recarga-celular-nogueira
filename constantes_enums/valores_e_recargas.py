from decimal import Decimal
from enum import Enum

class ValoresErecargas(Enum):
    
    VALOR_EM_REAIS_MINIMO = Decimal("20.00")
    VALOR_GB_BONUS = int(20)
    VALOR_EM_REAIS_GATILHO_BONUS = Decimal("50.00")
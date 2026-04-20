from decimal import Decimal
from enum import Enum

class ValoresErecargas(Enum):
    """
    Classe que armazena as constantes de valores de recarga mínimos, bônus e gatilho de bônus.
    """

    VALOR_EM_REAIS_MINIMO = Decimal("20.00") # Valor em R$ de recarga mínima.
    VALOR_GB_BONUS = int(20) # Valor de bônus em GB quando elegível.
    VALOR_EM_REAIS_GATILHO_BONUS = Decimal("50.00") # Valor em R$ de gatilho do bônus, quando atingir esse valor ou >, ativa o bônus.

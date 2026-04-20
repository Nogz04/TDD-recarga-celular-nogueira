from enum import Enum
from constantes_enums.valores_e_recargas import ValoresErecargas

class MensagensErro(Enum):
    VALOR_MINIMO_RECARGA = f"Valor minimo de recarga é R$ {ValoresErecargas.VALOR_EM_REAIS_MINIMO.value}"
    VALOR_QUEBRADO = "Valor da recarga deve ser inteiro"
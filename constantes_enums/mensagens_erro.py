from enum import Enum
from constantes_enums.valores_e_recargas import ValoresErecargas

class MensagensErro(Enum):
    """
    Classe que armazena as mensagens de erro que serão usadas no sistema.
    """ 

    VALOR_MINIMO_RECARGA = f"Valor minimo de recarga é R$ {ValoresErecargas.VALOR_EM_REAIS_MINIMO.value}"
    VALOR_QUEBRADO = "Valor da recarga deve ser inteiro"
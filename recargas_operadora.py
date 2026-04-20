from decimal import Decimal
from constantes_enums.mensagens_erro import MensagensErro
from constantes_enums.valores_e_recargas import ValoresErecargas

class GerenciadorRecarga:
    """
    Classe que gerencia as recargas de celular.
    """

    def __init__(self):
        self._saldo_total_gb = 0

    @property
    def saldo_total_gb(self) -> int: #É uma função que com o @property vira uma variável que pode ser usada para acessar ou retornar o saldo total de GB
        return self._saldo_total_gb

    def efetuar_recarga(self, valor_pago: Decimal) -> int:
        
        self._validar_valor_recarga(valor_pago) # Verifica a recarga, se quebrar ja para aqui

        self._verifica_valor_quebrado(valor_pago)

        gb_base = int(valor_pago) # Se não quebrar ele vai atribuir os GB conforme o valor pago, ja que R$1,00 = 1GB

        bonus_gb = self._verifica_elegibilidade_bonus_de_gb(valor_pago)
        saldo_gb_recarga_mais_bonus = gb_base + bonus_gb

        self._saldo_total_gb += saldo_gb_recarga_mais_bonus

        return self._saldo_total_gb


    def _validar_valor_recarga(self, valor_pago: Decimal):
        if valor_pago < ValoresErecargas.VALOR_EM_REAIS_MINIMO.value:
            raise Exception(MensagensErro.VALOR_MINIMO_RECARGA.value.replace(".", ","))

    def _verifica_elegibilidade_bonus_de_gb(self, valor_pago: Decimal):
        if valor_pago >= ValoresErecargas.VALOR_EM_REAIS_GATILHO_BONUS.value:
            return ValoresErecargas.VALOR_GB_BONUS.value
        return 0
        
    def _verifica_valor_quebrado(self, valor_pago: Decimal):
        if valor_pago % 1 != 0:
            raise Exception(MensagensErro.VALOR_QUEBRADO.value)
class GerenciadorRecarga:

    # CONTANTES

    _VALOR_EM_REAIS_MINIMO = 20.00 # Valor mínimo em reais para efetuar a recarga
    _VALOR_GB_BONUS = 20 # Valor de bônus que será adicionado quando tiver elegibilidade de bônus
    _VALOR_EM_REAIS_GATILHO_BONUS = 50.00 # Valor que ativa o gatilho de elegibilidade de bônus


    def __init__(self):
        self._saldo_total_gb = 0

    @property
    def saldo_total_gb(self) -> int: #É uma função que com o @property vira uma variável que pode ser usada para acessar ou retornar o saldo total de GB
        return self._saldo_total_gb

    def efetuar_recarga(self, valor_pago: float) -> int: #A função de recarga recebe o valor pago em float e retorna os GB (int)
        
        self._validar_valor_recarga(valor_pago) # Verifica a recarga, se quebrar ja para aqui

        gb_base = int(valor_pago) # Se não quebrar ele vai atribuir os GB conforme o valor pago, ja que R$1,00 = 1GB

        bonus_gb = self._verifica_elegibilidade_bonus_de_gb(valor_pago)
        saldo_gb_recarga_mais_bonus = gb_base + bonus_gb

        self._saldo_total_gb += saldo_gb_recarga_mais_bonus

        return self._saldo_total_gb


    def _validar_valor_recarga(self, valor_pago: float):
        if valor_pago < 20.00:
            raise Exception(f"Valor minimo de recarga é R$ {self._VALOR_EM_REAIS_MINIMO:.2f}".replace(".", ","))

    def _verifica_elegibilidade_bonus_de_gb(self, valor_pago: float):
        if valor_pago >= self._VALOR_EM_REAIS_GATILHO_BONUS:
            return self._VALOR_GB_BONUS
        return 0
        

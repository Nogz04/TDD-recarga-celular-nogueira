from unittest import TestCase
from recargas_operadora import GerenciadorRecarga

class TestGerenciadorRecarga(TestCase):

    def test_nao_aceita_recarga_abaixo_de_vinte_reais(self):
        gerenciador = GerenciadorRecarga()

        # Avisa que irá testar a execução de uma função abaixo que é para dar erro 
        with self.assertRaises(Exception) as context:
            gerenciador.efetuar_recarga(10.00) # Essa aqui é a função, ela tenta fazer uma recarga de R$10,00, que não é permitida pelas regras de negócio

        self.assertTrue("Valor minimo de recarga é R$ 20,00" in str(context.exception)) # Aqui ele lança um erro que é comparado com o erro que bate na função, se bater com o erro, significa que esse teste passou.


    def test_recarga_de_valor_retorna_o_mesmo_valor_em_gb(self):
    
        gerenciador = GerenciadorRecarga()
        resultado = gerenciador.efetuar_recarga(20.00)
        
        self.assertEqual(20, resultado)


    def test_recarga_com_elegibilidade_de_bonus(self):

        gerenciador = GerenciadorRecarga()
        resultado = gerenciador.efetuar_recarga(50.00)

        self.assertEqual(70, resultado)

    def test_saldo_acumulado_recarga_sem_bonus(self):

        gerenciador = GerenciadorRecarga()
        resultado = gerenciador.efetuar_recarga(20.00)
        resultado = gerenciador.efetuar_recarga(20.00)

        self.assertEqual(40, resultado)

    def test_saldo_acumulado_recarga_elegivel_com_bonus(self):

        gerenciador = GerenciadorRecarga()
        resultado = gerenciador.efetuar_recarga(50.00)
        resultado = gerenciador.efetuar_recarga(50.00)

        self.assertEqual(140, resultado)

    def test_saldo_acumulado_recarga_elegivel_de_bonus_e_sem_bonus(self):

        gerenciador = GerenciadorRecarga()
        resultado = gerenciador.efetuar_recarga(50.00)
        resultado = gerenciador.efetuar_recarga(20.00)

        self.assertEqual(90, resultado)

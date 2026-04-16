from unittest import TestCase
from recargas_operadora import GerenciadorRecarga

class TestGerenciadorRecarga(TestCase):

    def test_nao_aceita_recarga_abaixo_de_vinte_reais(self):
        gerenciador = GerenciadorRecarga()

        with self.assertRaises(Exception) as context:
            gerenciador.efetuar_recarga(10.00)

        self.assertTrue("Valor minimo de recarga é R$ 20,00" in str(context.exception))


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
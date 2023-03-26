from Conta import Conta
from Conta_corrente import Conta_corrente
from Conta_poupanca import Conta_poupanca

#Teste conta corrente (alteração de valores, deposito, saque)
conta1 = Conta_corrente(id_conta=1, saldo_conta=100000, limite=1000)

conta1.id
conta1.saldo
conta1.limite

conta1.id=3
conta1.saldo=100000
conta1.limite=3000

conta1.id
conta1.saldo
conta1.limite

conta1.depositar(20000)
conta1.saldo

conta1.sacar(3000000)

#Teste conta poupança (deposito, valor de rendimento após determinado tempo)
conta2 = Conta_poupanca(id_conta=2, saldo_conta=1000, taxaDeRendimentoPoupanca=100)

conta2.id
conta2.saldo
conta2.taxa_rendimento_poupanca

conta2.id=4
conta2.saldo=10000

conta2.id
conta2.saldo
conta2.taxa_rendimento_poupanca

conta2.depositar(20000)
conta2.saldo

conta2.Valor_rendimento_por_tempo(1,0,0,0,0,0)
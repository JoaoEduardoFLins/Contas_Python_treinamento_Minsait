from Conta import Conta

class Conta_corrente(Conta):
    def __init__(self, id_conta, saldo_conta, limite):
        super().__init__(id_conta, saldo_conta)
        self._limite = limite

    #get do limite da conta
    @property
    def limite(self):
        print(f"O limite de cheque especial da conta é: R${self._limite}")
        print("------------------------------------------------------------")

    #set do limite da conta
    @limite.setter
    def limite(self, valor_limite):
        self._limite = valor_limite
    
    #Função de depositar
    def depositar(self, valor_deposito):
        self._saldo_conta += valor_deposito
        print(f"Deposito no valor de R${valor_deposito} feito com sucesso")
        print("------------------------------------------------------------")

    #Função de sacar, com erro se valor de saque maior que o saldo na conta
    def sacar(self,valor_saque):
        try:
            self._saldo_conta=(self._saldo_conta+self._limite)-valor_saque
            if self._saldo_conta<0:
                raise ValueError
            else:
                print(f"Foi sacado: R${valor_saque}")
                print(f"O saldo em conta atual é: R${self._saldo_conta}")
                print(f"O seu limite de cheque especial atual é: R${self._limite}")
                print("------------------------------------------------------------")
        
        except ValueError:
            print("O valor de saque é maior que o saldo em conta somado do valor limite do cheque especial, não é possível realizar a operação")
            print("------------------------------------------------------------")

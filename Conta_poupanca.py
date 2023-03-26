from Conta import Conta

class Conta_poupanca(Conta):
    def __init__(self, id_conta, saldo_conta, taxaDeRendimentoPoupanca):
        super().__init__(id_conta, saldo_conta)
        self._taxaDeRendimentoPoupanca = taxaDeRendimentoPoupanca

    #Get da taxa de rendimento da conta
    @property
    def taxa_rendimento_poupanca(self):
        print(f"A taxa de rendimento (a.a.) da conta é: {self._taxaDeRendimentoPoupanca}")
        print("------------------------------------------------------------")

    #Set da taxa de rendimento da conta
    @taxa_rendimento_poupanca.setter
    def limite(self, taxa_rendimento_poupanca):
        self._taxaDeRendimentoPoupanca = taxa_rendimento_poupanca

    #Função de depositar
    def depositar(self, valor_deposito):
        self._saldo_conta += valor_deposito
        print(f"Deposito no valor de R${valor_deposito} feito com sucesso")
        print("------------------------------------------------------------")

    #Função de sacar, com erro se valor de saque maior que o saldo na conta
    def sacar(self,valor_saque):
        try:
            self._saldo_conta-=valor_saque
            if self._saldo_conta<0:
                raise ValueError
            else:
                print(f"Foi sacado R${valor_saque}")
                print(f"O saldo em conta atual é: R${self._saldo_conta}")
                print("--------------------------------------------------------")

        except ValueError:
            print("O valor de saque é maior que o saldo em conta, não é possível realizar a operação")
            print("------------------------------------------------------------- ")

    #Função de calcular o rendimento em determinado tempo, separar os valores do tempo de rendimento desejado por virgula
    def Valor_rendimento_por_tempo(self, anos, meses, dias, horas, minutos, segundos):
        #transformação do tempo para segundos
        tempo_total =  (((((anos*12)*30)*24)*60)*60)
        tempo_total += ((((meses*30)*24)*60)*60)
        tempo_total += (((dias*24)*60)*60)
        tempo_total += ((horas*60)*60)
        tempo_total += (minutos*60)
        tempo_total += segundos

        #calculo do rendimento por segundo
        self._taxaDeRendimentoPoupanca= ((((((self._taxaDeRendimentoPoupanca/100)/12)/30)/24)/60)/60)

        #calculo do rendimento por segundo pelo tempo total em segundos
        rendimento = (self._taxaDeRendimentoPoupanca*self._saldo_conta)*tempo_total

        #Apresentação dos valores após os cálculos de rendimento
        print(f"O rendimento total no tempo {anos} anos, {meses} meses, {dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos, foi igual a: R${rendimento:.2f}")
        print("------------------------------------------------------------")

        self._saldo_conta+=rendimento
        print(f"O saldo ficou em R${self._saldo_conta:.2f}")
        print("------------------------------------------------------------")
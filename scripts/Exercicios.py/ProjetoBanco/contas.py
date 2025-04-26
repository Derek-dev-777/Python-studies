from abc import ABC, abstractmethod

class MyRepr:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f"{class_name}({class_dict})"
        return class_repr 

class Conta(ABC, MyRepr):

    def __init__(self, agencia, numero_conta):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo_corrente = 0
        self.saldo_poupança = 0
        self.divida = 0

    @abstractmethod
    def sacar(self, valor_do_saque, agencia):
       pass
        
    @abstractmethod
    def depositar(self, valor_do_deposito, agencia):
        pass
        

class ContaCorrente(Conta):
        
    def sacar(self, valor_do_saque, agencia):
        if agencia == self.agencia:
            saldo_na_conta = self.saldo_corrente

            if  saldo_na_conta >= valor_do_saque:
                self.saldo_corrente -= valor_do_saque
                return self.saldo_corrente
            elif saldo_na_conta < valor_do_saque:
                print(f"Você tem apenas {self.saldo_corrente}")
                raise ValueError("Saldo insuficiente para saque")
        else:
            raise ValueError("Voce não tem conta nessa agencia bancaria")
        
    def depositar(self, valor_do_deposito, agencia):
        if agencia == self.agencia:
            saldo_na_conta = self.saldo_corrente
            valor_pos_deposito = valor_do_deposito + saldo_na_conta
            self.saldo_corrente = valor_pos_deposito
            return self.saldo_corrente
        else:
            raise ValueError("Voce não tem conta nessa agencia bancaria")


class ContaPoupança(Conta):

    
    def sacar(self, valor_do_saque, agencia):
        if agencia == self.agencia:
            saldo_na_conta = self.saldo_poupança
            if saldo_na_conta >= valor_do_saque:
                saldo_na_conta -= valor_do_saque
                return saldo_na_conta
            
            elif saldo_na_conta < valor_do_saque:
                print(f"Você tem apenas {saldo_na_conta}")
                raise ValueError("Saldo insuficiente para saque.")
        else:
            raise ValueError("Você não tem conta nessa agência bancária.")
        
    def depositar(self, valor_do_deposito, agencia):
        if agencia == self.agencia:
            saldo_na_conta = self.saldo_poupança
            valor_pos_deposito = valor_do_deposito + saldo_na_conta
            self.saldo_poupança = valor_pos_deposito
            return self.saldo_poupança
        else:
            raise ValueError("Voce não tem conta nessa agencia bancaria")


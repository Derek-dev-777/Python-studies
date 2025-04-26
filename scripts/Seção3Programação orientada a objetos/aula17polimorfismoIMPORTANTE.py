# ->  significa = tal função deve RETORNAR o tipo que colocou ex: -> bool ( deve retornar boolean )

from abc import ABC, abstractmethod

class Notificacao(ABC):

    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool: 
        print("e mail:   enviando", self.mensagem)
        return True
    
class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool: 
        print("SMS: enviando", self.mensagem)
        return False

def notificar(notificacao: Notificacao): # aqui você consegue atribuir todos os metodos da classe, para ser usada
    
    notificacao_enviada  = notificacao.enviar()  # dentro da função

    if notificacao_enviada:
        print("notificação enviada")
    else:
        print("notificação nao enviada")

notificação_sms = NotificacaoSMS("Testando sms")
notificação_Email = NotificacaoEmail("Testando email")

notificar(notificação_sms)
notificar(notificação_Email)
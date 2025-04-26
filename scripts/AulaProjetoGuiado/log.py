from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt" # usando a pathlib, cria o caminho do meu arquivo e o arquivo junto


class Log:

    def _log(self, msg):
        raise NotImplementedError ("Implemente o metodo log") # demonstra que não se deve usar essa função
    
    def log_error(self, msg):
        return self._log(f"error {msg}")
    
    def log_success(self, msg):
        return self._log(f"Success {msg}")
    

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f"{msg} ({self.__class__.__name__})"
        with open (LOG_FILE, "w") as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write("\n")

# o codigo escrevemos aqui para que nao afete o programa principal, depois que tudo for testado, ai sim cola
# no nosso modulo main, uma especie de colete aprova de erros kkkk
if __name__ == "__main__": 
    l = LogFileMixin()
    l.log_success("QUalquer coisa")
    print(LOG_FILE)
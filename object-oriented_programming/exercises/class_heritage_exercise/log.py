class Log:
    def _log(self, msg):
        raise NotImplementedError("Implemente Log Method")
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')

class LogFileMixin(Log): #Take a look! This "Mixin" is to another classes can be use its methods/attributes
    def _log(self, msg): #It's a signature of the method, and don't change it if you overlap in another class
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == "__main__":   
    l = LogPrintMixin()
    l.log_error("qualquer coisa")
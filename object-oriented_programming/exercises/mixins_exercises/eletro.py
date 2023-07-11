from log import LogPrintMixin, LogFileMixin

class Eletronic:
    def __init__(self, name):
        self._name = name
        self._status = False #It's turn on
    
    def turn_on(self):
        if not self._status:
            self._status = True
    
    def turn_off(self):
        if self._status:
            self._status = False
    

class Smarthphone(Eletronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()

        if self._status:
            msg = f'{self._name} is turn on.'
            self.log_sucess(msg)

    def turn_off(self):
        super().turn_off()

        if not self._status:
            msg = f'{self._name} is turn off.'
            self.log_error(msg)

        

            

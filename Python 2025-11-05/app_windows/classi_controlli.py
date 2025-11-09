class controllo():
    def __init__(self, obj):
        self.obj = obj

    def controllo_dato(self, tipo_controllo):

        if self.obj.strip() == '':
            return False

        if tipo_controllo == 'STR':
            var1 = 'ABCDEFGHIJKLAMNOPQRSTUVWYZ'

        elif tipo_controllo == 'NUMB':
            var1 = '0123456789'
        elif tipo_controllo == 'STR_NUMB':
            var1 = 'ABCDEFGHIJKLAMNOPQRSTUVWYZ0123456789'           

        for i in range(len(self.obj)):
            if self.obj[i].upper() not in var1:

    def ctrl_numb(self):
        pass
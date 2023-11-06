class pago:
    

   
    def __init__(self):
       
        self.valor_por_hora=10000

    def monto(self,tiempo):
        
        resultado=tiempo*self.valor_por_hora 
        return resultado
      

    def visualizar(self,tiempo):
        monto_a_pagar=self.monto(tiempo)
        return monto_a_pagar

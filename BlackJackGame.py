#!/usr/bin/env python3

class Player:
    def __init__(self, jugador):
        self.jugador = jugador
        self.manos = []
        self.dinero = 100

    def agregar_dinero(self, cantidad):
        self.dinero += cantidad
        return
    
    def puede_apostar(self, cantidad):
        self.dinero >= cantidad
        return
    
    def retirar_dinero(self, cantidad):
        if self.dinero >= cantidad:
            self.dinero -= cantidad
        else:
            return 
        
    def iniciar_ronda(self):
        self.manos = []
        return
    
    def agregar_mano(self, mano_nueva):
        self.manos += mano_nueva
        return
        
    def recibir_carta(self, mano_actual, carta):
        mano_actual += carta
        return
    
    def obtener_manos(self):
        self.manos()
        return 
                


jugador = Player("jugador")






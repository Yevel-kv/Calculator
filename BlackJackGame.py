#!/usr/bin/env python3

class Card:
    def __init__(self, rango, palo):
        self.rango = rango
        self.palo = palo
    @property
    def valor(self):
        if self.rango.isdigit():
            return int(self.rango)
        elif self.rango in ("J", "Q", "K"):
            return 10
        elif self.rango == "A":
            return 11

    def __str__(self):
        return f"{self.rango}{self.palo}"
    
class Shoe:
    def __init__(self):
        self.cartas = []
        self._genera_cartas()
        self.barajar = False
        self.corte = (int)
    
    NUM_MAZOS = 8
    PALOS = ("♠", "♥", "♦", "♣")
    RANGOS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def _genera_cartas(self):   
        self.cartas.clear()
        for Shoe.NUM_MAZOS


        
        
            
        
        
    def repartir(self, carta):
        if carta in self.cartas:
            self.cartas.pop()
        else:
            return ValueError
        



    def cartas_restantes(self):

    
    def llego_al_corte(self):




class Hand:
    def __init__(self):
        self.cartas = []
        self.bet = 0
        self.activa = True
        self.double = False
    
    def agregar_carta(self, carta):
        self.cartas.append(carta)
        return
    
    def calcular_valor(self):
        total = 0
        contador_ases = 0
        for carta in self.cartas:
            total += carta.valor
            if carta == "A":
                contador_ases += 1
        while total > 21 and contador_ases > 0:
                total -= 10
                contador_ases -= 1
        return total        

    def esta_busted(self):
        if self.calcular_valor > 21:
            return True
        else:
            return False
    
    def es_blackjack(self):
        if len(self.cartas) == 2:
            self.calcular_valor() == 21

    def puede_split(self):
        if len(self.cartas) == 2:
            print("ambas cartas tiene el mismo valor, No esta definida esta funcion")

    def puede_doblar(self):
        if len(self.cartas) == 2:
            
            self.double == False


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






import time

# Find the nth digit of the infinite integer sequence:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
# EXAMPLE:
# Input: 11
# Output: 0
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 
# is a 0, which is part of the number 10.

class Solution:
    # FUERZA BRUTA: _> Complejidad > O(n) _> TIME EXCEEDED 
    # Esta primera implementación por fuerza bruta funciona, pero es muy lenta.
    # Sobrepasa el límite de tiempo. Básicamente lo que hacemos es mantener dos 
    # contadores, uno para el número de dígito y otro para el número entero actual
    # que estamos analizando. Solo incrementamos el numero entero cuando hayamos
    # analizado todos sus digitos con el contador anterior. 
     
    def findNthDigit(self, n):
        nint = 0
        nth = 0

        nextChange = 9
        actualIntSize = 1

        while 1:
            # Update nint counter:
            nint += 1

            # Update nextChange and actualIntSize if needed:
            if nint > nextChange:
                nextChange = nextChange + 9*(10**actualIntSize)
                actualIntSize += 1

            # Iterate inside each int number to find the solution:
            for intCounter in range(actualIntSize):
                # Update nth counter:
                nth += 1

                if nth == n:
                    return str(nint)[intCounter]
    
    
    # OPTIMIZACION: _> Complejidad = O(n) _> TIME EXCEEDED 
    # La idea puede ser intentar calcular matemáticamente cuantos números
    # enteros completos (con todos sus digitos) entra antes de alcanzar 
    # el valor de n y solamente analizar el último. 
    def optimizedFindNthDigit (self, n):

        nint = 0
        nth = 0

        nextChange = 9
        actualIntSize = 1

        while 1:
            nint += 1

            if nint > nextChange:
                nextChange = nextChange + 9*(10**actualIntSize)
                actualIntSize += 1

            nth += actualIntSize
            if nth > n:
                return str(nint)[n-(nth-actualIntSize)]
            elif nth == n:
                return n
                    
# Respuesta: La idea es ir avanznado sobre los valores de n
n = 3
solution = Solution()

start_time = time.time()
print(solution.findNthDigit(n))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(solution.optimizedFindNthDigit(n))
print("--- %s seconds ---" % (time.time() - start_time))

print("Act 9 clase humano")
print("Miguel Rios Mat: 22308051281094")

# zon de class
class Humano1094:
    # Zona de atributos dentro de la clase
    edad=0
    Genero=""
    estatura=0
    fecha_nacimiento=""
    Color_pelo=""
    peso=0



    # Zona funcicones dentro de la clase
    def bailar1094(self,n):
        print(f" {n} Esta Bailando!")
    
    def correr1094(self,n):
        print(f" {n} Esta Corriendo!")

    def comer1094(self,n):
        print(f" {n} Esta Comiendo!")

    def jugar1094(self,n):
        print(f" {n} Esta Jugando!")


    def caminar1094(self,n):
        print(f" {n} Esta Caminando!")
    
    def musica1094(self,n):
        print(f" {n} Esta Escuchando Musica!")
# Zona de creacion de objetos
Miguel=Humano1094()
Ricardo=Humano1094()
# Zona de usando objetos
print("----Resultados para Miguel----")
Miguel.edad=17
Miguel.Genero="Masculino"
Miguel.estatura=1.98
Miguel.fecha_nacimiento="27 De Junio 2007"
Miguel.Color_pelo="Negro"
Miguel.peso="90kg"
print(f" Edad : {Miguel.edad}")
print(f" Edad : {Miguel.Genero}")
print(f" Edad : {Miguel.estatura}")
print(f" Edad : {Miguel.fecha_nacimiento}")
print(f" Edad : {Miguel.Color_pelo}")
print(f" Edad : {Miguel.peso}")

Miguel.bailar1094("Miguel")
Miguel.correr1094("Miguel")
Miguel.comer1094("Miguel")
Miguel.caminar1094("Miguel")
Miguel.musica1094("Miguel")


print("----Resultado para Ricardo----")
Ricardo.edad=20
Ricardo.Genero="Masculino"
Ricardo.estatura=1.85
Ricardo.fecha_nacimiento="13 de noviembre de 2003"
Ricardo.Color_pelo="Cafe"
Ricardo.peso="70kg"
print(f"Edad : {Ricardo.edad}")
print(f" Edad : {Ricardo.Genero}")
print(f" Edad : {Ricardo.estatura}")
print(f" Edad : {Ricardo.fecha_nacimiento}")
print(f" Edad : {Ricardo.Color_pelo}")
print(f" Edad : {Ricardo.peso}")
Ricardo.bailar1094("Ricardo")
Ricardo.correr1094("Ricardo")
Ricardo.comer1094("Ricardo")
Ricardo.caminar1094("Ricardo")
Ricardo.musica1094("Ricardo")
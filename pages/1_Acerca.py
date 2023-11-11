import streamlit as st

# Estilo del título
st.title("Acerca del equipo de trabajo")

# Sección para Juan Esteban Rendón Torres
st.header("Juan Esteban Rendón Torres.")

class JovenProgramador:
    def __init__(self, edad):
        self.edad = edad
        self.pasion = "programación"
        self.dedicacion = True
        self.mente_inquisitiva = True
        self.amor_resolver_problemas = True

    def mostrar_informacion(self):
        return f"Este joven de {self.edad} años destaca por su pasión y dedicación hacia el mundo de la {self.pasion}. Con una mente inquisitiva y un amor innato por resolver problemas, se sumerge en el fascinante universo del código con entusiasmo y curiosidad. Su rostro ilumina cuando habla de algoritmos, lenguajes de programación y proyectos desafiantes."

# Crear una instancia del joven programador
joven_programador = JovenProgramador(18)

# Obtener el texto
texto_acercade_joven = joven_programador.mostrar_informacion()

# Mostrar el texto del joven programador en Streamlit
st.write(texto_acercade_joven)

# Sección para Diego Alexander Alvarez
st.header("Diego Alexander Alvarez")

class IndividuoMaduro:
    def __init__(self, edad):
        self.edad = edad
        self.determinacion = True
        self.enfoque_centrado = True
        self.experiencia = True
        self.seriedad = True
        self.proposito = True

    def mostrar_informacion(self):
        return f"Este individuo de {self.edad} años se embarca en el estudio de la programación con una determinación madura y un enfoque centrado. Su expresión, marcada por líneas de experiencia y determinación, refleja una combinación de seriedad y propósito. Viste de manera práctica y funcional, priorizando la comodidad sobre las tendencias de moda, sugiriendo una mentalidad más orientada hacia sus objetivos académicos que hacia la estética."

# Crear una instancia del individuo maduro
individuo_maduro = IndividuoMaduro(36)

# Obtener el texto
texto_acercade_maduro = individuo_maduro.mostrar_informacion()

# Mostrar el texto del individuo maduro en Streamlit
st.write(texto_acercade_maduro)

# Sección para Juan David Cano
st.header("Juan David Cano")

class JovenEnLasSombras:
    def __init__(self, edad):
        self.edad = edad
        self.seriedad_trascendental = True
        self.conexion_fuerzas_ocultas = True
        self.poseido_entendimiento_terrenal = True

    def mostrar_informacion(self):
        return f"Este joven de {self.edad} años se sumerge en las sombras del mundo de la programación con una seriedad que trasciende lo convencional. Su expresión, más allá de ser reflexiva, sugiere una conexión más profunda con fuerzas ocultas. Su mirada, en lugar de revelar determinación, refleja un conocimiento más allá de lo común, como si estuviera poseído por un entendimiento más allá de lo terrenal."

# Crear una instancia del joven en las sombras
joven_en_las_sombras = JovenEnLasSombras(18)

# Obtener el texto
texto_acercade_sombras = joven_en_las_sombras.mostrar_informacion()

# Mostrar el texto del joven en las sombras en Streamlit
st.write(texto_acercade_sombras)

# Sección para Vanesa Garcia
st.header("Vanesa Garcia")

class JovenEnergetica:
    def __init__(self, edad):
        self.edad = edad
        self.energia_vibrante = True
        self.entusiasmo_determinacion = True
        self.brillo_ojos_curiosidad = True
        self.confianza_valentia = True

    def mostrar_informacion(self):
        return f"Esta joven de {self.edad} años irradia una energía vibrante mientras se sumerge en el fascinante mundo de la programación. Su expresión refleja una mezcla de entusiasmo y determinación, con ojos brillantes que revelan la chispa de su curiosidad y pasión por el código. A pesar de su juventud, lleva consigo una confianza evidente, derivada de su habilidad para enfrentar desafíos técnicos con valentía."

# Crear una instancia de la joven energética
joven_energetica = JovenEnergetica(18)

# Obtener el texto
texto_acercade_energetica = joven_energetica.mostrar_informacion()

# Mostrar el texto de la joven energética en Streamlit
st.write(texto_acercade_energetica)

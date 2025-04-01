#importamos tres funciones dentro de la carpeta src
from funciones import calcular_puntos, determinar_mvp, mostrar_ranking

# Datos de las rondas (estan indicadas en el enunciado)
#Rondas es una lista de diccionarios, donde cada diccionario representa una ronda
rondas = [
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
        'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
        'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
        'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
        'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
    }
]

jugadores = {}  #Diccionario que se ira actualizando en cada ronda con las estadisticas de cada jugador

for i, ronda in enumerate(rondas, start=1): #en cada iteracion, i sera el numero de la ronda y ronda sera el diccionario de la ronda
    print(f"\n🔹 Ronda {i}:")
    for jugador, stats in ronda.items():        #el for recorre cada jugador y sus estadisticas dentro de la ronda

        if jugador not in jugadores:            #si el jugador no esta dentro de los jugadores, lo agrega con valor cero
            jugadores[jugador] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'puntos': 0}
        # Sumar estadísticas
        jugadores[jugador]['kills'] += stats['kills']
        jugadores[jugador]['assists'] += stats['assists']
        jugadores[jugador]['deaths'] += 1 if stats['deaths'] else 0
        jugadores[jugador]['puntos'] += calcular_puntos(stats)

    # Determinar MVP de la ronda
    mvp = determinar_mvp(ronda)
    jugadores[mvp]['mvp'] += 1  # Aumentar su contador de MVPs
    
    print(f"🏅 Mejor jugador de la ronda: {mvp}")
    

    # Mostrar ranking actual
    mostrar_ranking(jugadores)


# Mostrar ranking final
print("\n🏆 RANKING FINAL 🏆")
mostrar_ranking(jugadores)   
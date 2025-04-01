def calcular_puntos(jugador):
    """Calcula el puntaje total del jugador basado en kills, asistencias y muertes."""
    return jugador['kills'] * 3 + jugador['assists'] * 1 - (1 if jugador['deaths'] else 0)

def determinar_mvp(ronda):
    """Devuelve el jugador con mayor puntaje en la ronda."""
    return max(ronda, key=lambda j: calcular_puntos(ronda[j]))

def mostrar_ranking(jugadores):
    """Imprime el ranking ordenado por puntos totales."""
    jugadores_ordenados = sorted(jugadores.items(), key=lambda x: x[1]['puntos'], reverse=True)
    print("\n🏆 Ranking:")
    print(f"{'Jugador':<10} {'Kills':<6} {'Asist.':<6} {'Muertes':<7} {'MVPs':<5} {'Puntos'}")
    print("-" * 50)
    for nombre, datos in jugadores_ordenados:
        print(f"{nombre:<10} {datos['kills']:<6} {datos['assists']:<6} {datos['deaths']:<7} {datos['mvp']:<5} {datos['puntos']}")
"""
Task 3: Route Verification (Перевірка маршруту)
Перевірити, чи є маршрут коректним у графі.
Маршрут коректний, якщо кожен перехід існує у множині допустимих переходів.
"""

def verify_route(route, edges, rooms):
    """
    Перевіряє, чи є маршрут коректним.
    
    Args:
        route: список аудиторій у порядку відвідування
        edges: множина допустимих переходів (кортежі (from, to))
        rooms: множина допустимих аудиторій
    
    Returns:
        True, якщо маршрут коректний; False - інакше
    """
    if not route or len(route) == 0:
        return False
    
    # Перевіряємо, що всі аудиторії існують
    for room in route:
        if room not in rooms:
            return False
    
    # Перевіряємо, що кожен перехід існує
    for i in range(len(route) - 1):
        from_room = route[i]
        to_room = route[i + 1]
        
        if (from_room, to_room) not in edges:
            return False
    
    return True

def solve_task3():
    """Перевіряє кілька маршрутів"""
    
    rooms = {"A", "B", "C", "D", "E"}
    edges = {
        ("A", "B"), ("B", "A"),
        ("A", "C"), ("C", "A"),
        ("B", "D"), ("D", "B"),
        ("C", "D"), ("D", "C"),
        ("D", "E"), ("E", "D")
    }
    
    # Тестові маршрути
    test_routes = [
        ["A", "B", "D", "C", "A"],      # Valid
        ["A", "C", "D", "E", "D", "B"],  # Valid
        ["A", "B", "C"],                 # Invalid: no edge B->C
        ["A", "C", "D", "E", "B"],       # Invalid: no edge E->B
        ["A", "B", "D", "C", "A", "B"],  # Valid
        ["B", "D", "E"]                  # Valid: B->D, D->E exist
    ]
    
    results = []
    for route in test_routes:
        is_valid = verify_route(route, edges, rooms)
        results.append((route, is_valid))
    
    return results, edges

def main():
    print("=" * 50)
    print("Завдання 3: Перевірка маршруту")
    print("=" * 50)
    print()
    
    results, edges = solve_task3()
    
    print("Граф аудиторій:")
    print(f"Аудиторії: {{'A', 'B', 'C', 'D', 'E'}}")
    print("Допустимі переходи:")
    for from_room, to_room in sorted(edges):
        print(f"  {from_room} → {to_room}")
    print()
    
    print("Перевірка маршрутів:")
    print("-" * 50)
    
    for i, (route, is_valid) in enumerate(results, 1):
        status = "✓ VALID" if is_valid else "✗ INVALID"
        route_str = " → ".join(route)
        print(f"{i}. {route_str}")
        print(f"   {status}")
    
    print()

if __name__ == '__main__':
    main()

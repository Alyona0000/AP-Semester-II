"""
Task 2: Team Selection (Підбір команди)
Знайти найменшу команду, яка покриває всі необхідні навички.
"""

from itertools import combinations

def solve_task2():
    """Знаходить найменшу команду з необхідними навичками"""
    
    candidates = [
        {"name": "Anna", "skills": {"python", "sql"}},
        {"name": "Bohdan", "skills": {"excel", "sql"}},
        {"name": "Iryna", "skills": {"python", "statistics"}},
        {"name": "Maksym", "skills": {"excel", "presentation"}},
        {"name": "Olha", "skills": {"statistics", "sql"}}
    ]
    
    required_skills = {"python", "sql", "statistics", "excel"}
    
    best_team = None
    min_size = float('inf')
    
    # Перебираємо всі можливі групи кандидатів
    for team_size in range(1, len(candidates) + 1):
        for team_combination in combinations(candidates, team_size):
            # Збираємо навички всієї команди
            team_skills = set()
            for candidate in team_combination:
                team_skills.update(candidate["skills"])
            
            # Перевіряємо, чи покриваємо всі необхідні навички
            if required_skills.issubset(team_skills):
                if team_size < min_size:
                    min_size = team_size
                    best_team = team_combination
        
        # Якщо вже знайшли команду цього розміру, не шукаємо більші
        if best_team is not None and team_size >= min_size:
            break
    
    return best_team, required_skills

def main():
    print("=" * 50)
    print("Завдання 2: Підбір команди")
    print("=" * 50)
    print()
    
    team, required_skills = solve_task2()
    
    print(f"Необхідні навички: {required_skills}")
    print(f"Мінімальний розмір команди: {len(team)}")
    print(f"Склад команди: {[member['name'] for member in team]}")
    
    # Обчислюємо сумарний набір навичок
    team_skills = set()
    for member in team:
        team_skills.update(member["skills"])
    
    print(f"Сумарний набір навичок команди: {team_skills}")
    print()
    
    # Деталі кожного члена команди
    print("Деталі членів команди:")
    for member in team:
        print(f"  - {member['name']}: {member['skills']}")
    
    print()

if __name__ == '__main__':
    main()

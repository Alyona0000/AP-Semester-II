"""
Task 1: Class Schedule (Розклад пар)
Розмістити 3 предмети (Python, Math, Statistics) по 5 часових слотів
з обмеженнями:
- Python не може бути у слоті 1
- Math не може стояти одразу після Statistics
"""

from itertools import combinations

def is_valid_schedule(schedule):
    """
    Перевіряє, чи розклад задовольняє всім умовам.
    schedule: список кортежів [(subject, slot), ...]
    """
    # Розпакування розкладу
    subject_to_slot = {subj: slot for subj, slot in schedule}
    
    # Умова 1: Python не може бути у слоті 1
    if subject_to_slot.get('Python') == 1:
        return False
    
    # Умова 2: Math не може стояти одразу після Statistics
    if (subject_to_slot.get('Statistics') is not None and 
        subject_to_slot.get('Math') is not None):
        if subject_to_slot['Statistics'] + 1 == subject_to_slot['Math']:
            return False
    
    return True

def solve_task1():
    """Знаходить усі допустимі розклади"""
    subjects = ['Python', 'Math', 'Statistics']
    slots = [1, 2, 3, 4, 5]
    valid_schedules = []
    
    # Вибираємо 3 різні слоти з 5 можливих
    for selected_slots in combinations(slots, 3):
        # Генеруємо всі перестановки предметів для цих слотів
        from itertools import permutations
        for subject_perm in permutations(subjects):
            schedule = list(zip(subject_perm, selected_slots))
            if is_valid_schedule(schedule):
                valid_schedules.append(schedule)
    
    return valid_schedules

def main():
    print("=" * 50)
    print("Завдання 1: Розклад пар")
    print("=" * 50)
    print()
    
    valid_schedules = solve_task1()
    
    print(f"Усього допустимих розкладів: {len(valid_schedules)}")
    print()
    print("Перші 10 коректних варіантів:")
    print("-" * 50)
    
    for i, schedule in enumerate(valid_schedules[:10], 1):
        schedule_dict = {subj: slot for subj, slot in schedule}
        print(f"{i:2d}. Python:slot{schedule_dict['Python']}  "
              f"Math:slot{schedule_dict['Math']}  "
              f"Statistics:slot{schedule_dict['Statistics']}")
    
    print()

if __name__ == '__main__':
    main()

"""
Main script - runs all 4 tasks
"""

import task1
import task2
import task3
import task4

def main():
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  AP Semester II - Homework 5: Algorithmic Problems".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\n")
    
    # Task 1
    task1.main()
    
    input("Press Enter to continue to Task 2...")
    print("\n")
    
    # Task 2
    task2.main()
    
    input("Press Enter to continue to Task 3...")
    print("\n")
    
    # Task 3
    task3.main()
    
    input("Press Enter to continue to Task 4...")
    print("\n")
    
    # Task 4
    task4.main()
    
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  All tasks completed!".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\n")

if __name__ == '__main__':
    main()

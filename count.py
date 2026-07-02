#!/usr/bin/env python3
"""
A program that counts up to 100 and then counts down.

This script demonstrates basic loop functionality by:
1. Counting up sequentially from 1 to 100
2. Counting down sequentially from 100 back to 1
"""

def main():
    """Main function to execute the counting operations.
    
    Prints numbers counting up from 1 to 100, then counts down from 100 to 1.
    Displays a separator between the two sequences.
    """
    # Count up from 1 to 100 (inclusive)
    print("Counting up to 100...")
    for i in range(1, 101):
        print(i)
    
    # Count down from 100 to 1 (inclusive)
    print("\nCounting down from 100...")
    for i in range(100, 0, -1):
        print(i)
    
    print("\nDone!")

if __name__ == "__main__":
    main()

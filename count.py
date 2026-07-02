#!/usr/bin/env python3
"""
A program that counts up to 150 and then counts down.

This script demonstrates basic loop functionality by:
1. Counting up sequentially from 1 to 150
2. Counting down sequentially from 150 back to 1
"""

def main():
    """Main function to execute the counting operations.
    
    Prints numbers counting up from 1 to 150, then counts down from 150 to 1.
    Displays a separator between the two sequences.
    """
    # Count up from 1 to 150 (inclusive)
    print("Counting up to 150...")
    for i in range(1, 151):
        print(i)
    
    # Count down from 150 to 1 (inclusive)
    print("\nCounting down from 150...")
    for i in range(150, 0, -1):
        print(i)
    
    print("\nDone!")

if __name__ == "__main__":
    main()

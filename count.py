#!/usr/bin/env python3
"""
A program that counts up to 1000 and then counts down.
"""

def main():
    # Count up to 1000
    print("Counting up to 1000...")
    for i in range(1, 1002):
        print(i)
    
    # Count down from 1000
    print("\nCounting down from 1000...")
    for i in range(1001, 0, -1):
        print(i)
    
    print("\nDone!")

if __name__ == "__main__":
    main()

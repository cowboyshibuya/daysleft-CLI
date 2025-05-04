#!/usr/bin/env python3
import datetime
import argparse
import os

def calculate_time_remaining(birthdate_str, target):
    # Parse the birthdate
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    
    # Calculate 85th birthday
    eighty_fifth_birthday = birthdate.replace(year=birthdate.year + target)
    
    # Get current time
    now = datetime.datetime.now()
    
    # Calculate time difference
    time_diff = eighty_fifth_birthday - now
    
    # If already past 85, display 0
    if time_diff.total_seconds() < 0:
        return "You are already 85 or older!"
    
    # Calculate days, hours, and minutes
    days = time_diff.days
    hours = time_diff.seconds // 3600
    minutes = (time_diff.seconds % 3600) // 60
    
    # Calculate percentage of life completed (assuming 85 years lifespan)
    total_lifespan_days = target * 365.25  # Accounting for leap years
    days_lived = (now - birthdate).days
    percentage_completed = (days_lived / total_lifespan_days) * 100
    
    return {
        "days": days,
        "hours": hours, 
        "minutes": minutes,
        "percentage": percentage_completed
    }

def display_countdown(birthdate, target):
    # Clear the terminal
    os.system('clear')
    
    # Get terminal width
    terminal_width = os.get_terminal_size().columns
    
    # Calculate time remaining
    result = calculate_time_remaining(birthdate, target)
    
    if isinstance(result, str):
        # Handle the case when already 85 or older
        print("\n" + "=" * terminal_width)
        print(result.center(terminal_width))
        print("=" * terminal_width + "\n")
        return
    
    # Create border
    border = "=" * terminal_width
    
    # Print header
    print("\n" + border)
    print(f"TIME REMAINING UNTIL YOU TURN {target}".center(terminal_width))
    print(border)
    
    # Print time remaining
    print("\n")
    print(f"Days: {result['days']}".center(terminal_width))
    print(f"Hours: {result['hours']}".center(terminal_width))
    print(f"Minutes: {result['minutes']}".center(terminal_width))
    print("\n")
    
    # Create progress bar
    progress_width = terminal_width - 10  # Leave some margin
    percentage = result['percentage']
    completed_width = int((percentage / 100) * progress_width)
    progress_bar = "[" + "#" * completed_width + "-" * (progress_width - completed_width) + "]"
    
    # Print progress bar
    print("Life Journey Progress:".center(terminal_width))
    print(progress_bar.center(terminal_width))
    print(f"{percentage:.1f}% complete".center(terminal_width))
    print("\n")
    
    # Print footer
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    print(border)
    print(f"Today is {current_date}".center(terminal_width))
    print("Each day is a gift. Make the most of your time!".center(terminal_width))
    print(border + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser( 
        description="Show time remaining until specified age."
    )
    parser.add_argument( 
        "birthdate",
        help="Your birthdate in YYYY-MM-DD format"
    )
    parser.add_argument( 
        "target", 
        type=int,
        help="Target age (e.g., 85)"
    )
    args = parser.parse_args()
    display_countdown(args.birthdate, args.target)
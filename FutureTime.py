#FutureTime.py
#Name: Collin Frederick
#Date: 2/02/2025
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main(): 
  now = datetime.datetime.now()
  currentHour = now.hour -6
  currentMinute = now.minute

  hours_to_add = int(input("Enter the number of hours to add: "))
  minutes_to_add = int(input("Enter the number of minutes to add: "))

  total_minutes = currentMinute + minutes_to_add
  additional_hours = total_minutes // 60 
  remaining_minutes = total_minutes % 60 

  total_hours = currentHour + hours_to_add + additional_hours
  remaining_hours = total_hours % 12 

  future_time = f"{remaining_hours:02d}:{remaining_minutes:02d}"

  print(f"The future time is: {future_time}")


if __name__ == '__main__':
  main()

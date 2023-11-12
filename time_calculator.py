"""
The add_time function takes a 12-hour clock start time, adds a specified duration, 
and optionally considers a starting day. It returns the resulting time, 
including the day of the week and information about additional days if applicable.
"""


def add_time(start_time, duration, start_day=None):
    """
    Adds a duration to a given start time in 12-hour clock format.

    Args:
        start_time (str): The start time in the format 'hh:mm AM/PM'.
        duration (str): The duration to add in the format 'hh:mm'.
        start_day (str, optional): The starting day of the week (case insensitive).

    Returns:
        str: The resulting time and day (if provided), with information about additional days.

    Examples:
        >>> add_time("3:00 PM", "3:10")
        '6:10 PM'

        >>> add_time("11:30 AM", "2:32", "Monday")
        '2:02 PM, Monday'

        >>> add_time("11:43 AM", "00:20")
        '12:03 PM'

        >>> add_time("10:10 PM", "3:30")
        '1:40 AM (next day)'

        >>> add_time("11:43 PM", "24:20", "tueSday")
        '12:03 AM, Thursday (2 days later)'

        >>> add_time("6:30 PM", "205:12")
        '7:42 AM (9 days later)'
    """

    # Parse start time
    start_time_parts = start_time.split()
    start_hour, start_minute = map(int, start_time_parts[0].split(":"))
    period = start_time_parts[1].upper()

    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Convert start time to 24-hour format
    if period == "PM":
        start_hour += 12

    # Calculate total minutes
    total_minutes = (
        start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    )

    # Calculate new time and days
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60
    new_period = "AM" if new_hour < 12 else "PM"
    days_later = total_minutes // (24 * 60)

    # Adjust for 12-hour clock format
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    # Determine the day of the week
    if start_day:
        days_of_week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        start_day_index = days_of_week.index(start_day.capitalize())
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]

    # Format the result
    result = f"{new_hour}:{new_minute:02d} {new_period}"
    if start_day:
        result += f", {new_day}"
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result

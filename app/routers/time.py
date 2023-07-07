from fastapi import APIRouter
import datetime

router = APIRouter()



# Helper functions
def days_since_start():
    """
    Get the amount of days that have passed since the initial start date

    Returns:
        int: number of days from the initial starting day
    """

    # Hard coded start day
    start_day = datetime.datetime(2023, 7, 1)
    current_time = datetime.datetime.utcnow()
    return (current_time - start_day).days

def time_until_tomorrow():
    """
    Get the amount of time before the next day (in UTC)

    Returns:
        datetime.timedelta: time delta of the amount of time until the next day
    """
    current_time = datetime.datetime.utcnow()
    # Calculate time until next day
    tomorrow_date = current_time + datetime.timedelta(days=1)

    return datetime.datetime.combine(tomorrow_date, datetime.time.min) - current_time

# Routes
@router.get("/time")
async def time():
    """
    Get current day and time until next day. All time is calculated and presented in UTC

    Returns:
        JSON:
            days_since: number of days from the initial starting day
            time_until: time (in seconds) until the next day

    """

    return {'currentDay':days_since_start(), 'timeUntil':time_until_tomorrow()}

# 

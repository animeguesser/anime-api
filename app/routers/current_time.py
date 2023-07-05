from fastapi import APIRouter
import datetime

router = APIRouter()

@router.get("/time")
async def time():
    """
    Get current day and time until next day. All time is calculated and presented in UTC

    Returns:
        JSON:
            days_since: number of days from the initial starting day
            time_until: time until the next day

    """

    # Hard coded start day
    start_day = datetime.datetime(2023, 7, 1)

    # Calculate time until next day
    current_time = datetime.datetime.now()
    tomorrow_date = current_time + datetime.timedelta(days=1)
    time_until_tomorrow = datetime.datetime.combine(tomorrow_date, datetime.time.min) - current_time

    # Calculate number of days between now and starting day
    delta_between_days = current_time - start_day

    return {'days_since':delta_between_days.days, 'time_until':time_until_tomorrow}

import datetime
import json

# Helper functions
def days_since_start():
    """
    Get the amount of days that have passed since the initial start date

    Returns:
        int: number of days from the initial starting day
    """

    # Hard coded start day
    start_day = datetime.datetime(2023, 7, 1)

    # Get current UTC time
    current_time = datetime.datetime.utcnow()

    return (current_time - start_day).days

def time_until_tomorrow():
    """
    Get the amount of time before the next day (in UTC)

    Returns:
        datetime.timedelta: time delta of the amount of time until the next day
    """

    # Get current UTC time
    current_time = datetime.datetime.utcnow()
    
    # Calculate time until next day
    tomorrow_date = current_time + datetime.timedelta(days=1)

    return datetime.datetime.combine(tomorrow_date, datetime.time.min) - current_time

def lambda_handler(event, context):

    # Return time
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'currentDay':days_since_start(), 
            'timeUntil':time_until_tomorrow().seconds
            })
    }
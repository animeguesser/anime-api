# For testing
import json

# Helper function
def return_bad():
    """
    Returns a message stating it was a bad request

    Returns:
        JSON:
            statusCode: 400,
            headers: Content-Type text/plain
            body: 400: Bad request
    """
    return {
        'statusCode': 400,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': '400: Bad request'
    }

# Routes
def lambda_handler(event, context):
    """
    Perform a search through the list of anime and try to match items with approximate names in it's titles

    Returns:
        JSON:
            titles: the titles of animes
    """

    # Ensure there's something in the body
    if not event['body']:
        return return_bad()
    
    # Load the query
    query = json.loads(event['body'])
    search_item = query['query']

    # Ensure that the query is at least 3 characters
    if len(search_item) < 3 or len(search_item) > 15:
        return return_bad()
        
    # For testing, open file directly and load it
    f = open('./parsed-anime-list-mini.json')
    data = json.load(f)

    # Keep track of titles that are possible
    anime_list = {"titles": []}

    # Cycle through list to find an include
    for item in data:
        if search_item.lower() in item['title'].lower():
            anime_list['titles'].append(item['title'])

    # Return the list of animes
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(anime_list)
    }

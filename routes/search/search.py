import json
from rapidfuzz import fuzz
from operator import itemgetter

# Helper functions
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
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, PUT, GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With',
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
    
    # Preflight cors issue
    if event['httpMethod'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*'
            } 
        }

    # Ensure there's something in the body
    if not event['body']:
        return return_bad()
    
    # Load the query
    query = json.loads(event['body'])

    try:
        search_item = query['query']
    except KeyError:
        return return_bad()

    # Ensure that the query is at least 3 characters
    if len(search_item) < 3 or len(search_item) > 15:
        return return_bad()
    
    # Log msg
    print(f'Search query: {search_item}')
        
    # Open file directly and load it
    f = open('./parsed-anime-list-mini.json')
    data = json.load(f)

    # Keep track of titles and scores that are possible
    anime_score_list = []

    # Cycle through list parsed list
    for item in data:

        # Perform a fuzzy search and get a score back
        fuzzy_search = fuzz.ratio(search_item.lower(), item['title'].lower())

        # Check if the search item is in the title
        in_title = search_item.lower() in item['title'].lower()

        # If the query is in the title or has a high fuzzy search score
        if in_title or fuzzy_search > 65:

            # If the query is in the title, give it a higher score
            if in_title:
                
                # If the query is the same as the title, give it the highest score
                if search_item.lower() == item['title'].lower():
                    anime_score_list.append({'title': item['title'], 'score': 200})
                else:
                    anime_score_list.append({'title': item['title'], 'score': 100})

            # Else, give it the fuzzy search score
            else:
                anime_score_list.append({'title': item['title'], 'score': fuzzy_search})
        
        # Check the synonymns if it's not in the title or a fuzzy search isn't matched
        else:
            for synonym in item['synonyms']:
                
                # Perform a fuzzy search for each synonym and get a score back
                fuzzy_search = fuzz.ratio(search_item.lower(), synonym.lower())

                # Check if the search item is in the synonym
                in_synonym = search_item.lower() in synonym.lower()

                # If the query is in the synonym or has a high fuzzy search score
                if in_synonym or fuzzy_search > 65:

                    # If the query is in the synonym, give it a higher score
                    if in_synonym:

                        # If the query is the same as the synonym, give it the highest score
                        if search_item.lower() == synonym.lower():
                            anime_score_list.append({'title': f'{item["title"]} [{synonym}]', 'score': 200})
                        else:
                            anime_score_list.append({'title': f'{item["title"]} [{synonym}]', 'score': 100})
                        break
                    
                    # Else, give it the fuzzy search score
                    else:
                        anime_score_list.append({'title': f'{item["title"]} [{synonym}]', 'score': fuzzy_search})
                        break

    # Sort possible anime titles by score
    anime_score_list = sorted(anime_score_list, key=itemgetter('score'), reverse=True)

    # Final list of only titles
    anime_list = {'titles': []}
    for anime in anime_score_list:
        anime_list['titles'].append(anime['title'])

    # Log msg
    print(f'Return list: {anime_list}')

    # Return the list of animes
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST',
            'Content-Type': 'application/json'
        },
        'body': json.dumps(anime_list)
    }

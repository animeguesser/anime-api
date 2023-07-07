# For testing
import json

# Routes
def lambda_handler(event, context):
    """
    Perform a search through the list of anime and try to match items with approximate names in it's titles

    Returns:
        JSON:
            titles: the titles of animes
    """

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            '':''
            })
    }

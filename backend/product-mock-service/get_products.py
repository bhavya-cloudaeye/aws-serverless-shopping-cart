import json
import os
from itertools import groupby
from aws_lambda_powertools import Logger, Tracer

logger = Logger()
tracer = Tracer()

with open('product_list.json', 'r') as product_list:
    product_list = json.load(product_list)

HEADERS = {
    "Access-Control-Allow-Origin": os.environ.get("ALLOWED_ORIGIN"),
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
}

# define a fuction for key
def key_func(k):
    return k.get('category','')

@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
    Return list of all products.
    """
    logger.info("Fetching product list")
    logger.info(f"Total items avaiable in shop : {len(product_list)}")
  
    # sort INFO data by 'company' key.
    product_list_sorted = sorted(product_list, key=key_func)
    
    logger.info(f"Listing items per category : ")
    for key, value in groupby(product_list_sorted, key_func):
        value = list(value)
        logger.info(f"Category : {key} , Items available : {len(value)}")

    return {
        "statusCode": 200,
        "headers": HEADERS,
        "body": json.dumps({"products": product_list}),
    }

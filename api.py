import requests
import config
import logger

url = config.api_endpoint

def send(data):
    logger.info(f"POST {url}: {data}")
    requests.post(
        url,
        auth=(config.username, config.password),
        json=data
    )

import os
import click
import requests
from pprint import pprint

# Local imports 
from util import *


@click.command()
@click.option("--config", type=str, default="config.json", help="path to the config file")
def run(config):

    huoju_cfg = load_config(get_config_or_default(config))['huoju']

    host = huoju_cfg['https']
    group = huoju_cfg['group']
    apikey = huoju_cfg['apikey']
    secret = huoju_cfg['secret']

    ts = utc_timestamp()
    headers = make_auth_headers(ts, "info", apikey, secret)
    url = f"{host}/{ROUTE_PREFIX}/info"

    print(f"Using url: {url}")

    res = requests.get(url, headers=headers)
    pprint(parse_response(res))


if __name__ == "__main__":
    run()

import os
import click
import requests
from pprint import pprint

# Local imports 
from util import *


@click.command()
@click.option("--account", type=click.Choice(['cash']), default="cash")
@click.option("--symbol", type=str, default=None)
@click.option("--n", type=int, default=None)
@click.option("--executed-only/--no-executed-only", default=False)
@click.option("--config", type=str, default="config.json", help="path to the config file")
@click.option("--verbose/--no-verbose", default=False)
def run(account, symbol, n, executed_only, config, verbose):

    huoju_cfg = load_config(get_config_or_default(config))['huoju']

    host = huoju_cfg['https']
    group = huoju_cfg['group']
    apikey = huoju_cfg['apikey']
    secret = huoju_cfg['secret']

    ts = utc_timestamp()
    headers = make_auth_headers(ts, "order/hist/current", apikey, secret)
    url = f"{host}/{group}/{ROUTE_PREFIX}/{account}/order/hist/current"
    
    params = dict(symbol=symbol, n=n, executedOnly=executed_only)

    if verbose:
        print(f"Using url: {url}")
        print(f"params: {params}")

    res = requests.get(url, headers=headers, params=params)
    pprint(parse_response(res))


if __name__ == "__main__":
    run()

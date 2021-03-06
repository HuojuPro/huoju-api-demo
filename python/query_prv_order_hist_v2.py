import click
import requests
from pprint import pprint
import time
# Local imports
from util import *


@click.command()
@click.option("--account", type=click.Choice(['cash']), default="cash")
@click.option("--symbol", type=str)
@click.option("--start_time", type=int, default=None)
@click.option("--end_time", type=int, default=None)
@click.option("--seq_num", type=int, default=None)  #
@click.option("--limit", type=int, default=None)
@click.option("--config", type=str, default="config.json", help="path to the config file")
@click.option("--verbose/--no-verbose", default=False)
def run(account, symbol, start_time, end_time, seq_num, limit, config, verbose):
    huoju_cfg = load_config(get_config_or_default(config))['huoju']

    host = huoju_cfg['https']
    group = huoju_cfg['group']
    apikey = huoju_cfg['apikey']
    secret = huoju_cfg['secret']

    url = f"{host}/{group}/{ROUTE_PREFIX_V2}/order/hist"
    
    ts = utc_timestamp()
    headers = make_auth_headers(ts, "order/hist", apikey, secret)
    params = dict(
        account = account,
        symbol = symbol,
        startTime = start_time,
        endTime = end_time,
        seqNum = seq_num,
        limit = limit,
    )

    if verbose:
        print(f"url: {url}")
        print(f"params: {params}")

    res = requests.get(url, headers=headers, params=params)
    pprint(parse_response(res))


if __name__ == "__main__":
    run()


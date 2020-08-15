import click
import requests
from pprint import pprint
from util import *
# from util.auth import *

@click.command()
@click.option("--page", type=int, default=1, help='')
@click.option("--pagesize", type=int, default=100, help="")
@click.option("--tx-type", type=str, default="withdrawal", help="")
@click.option("--startts", type=int, default=None, help="")
@click.option("--endts", type=int, default=None, help="")
@click.option("--asset", type=str, default="USDT", help="")
@click.option("--config", type=str, default="config.json", help="path to the config file")
@click.option("--verbose/--no-verbose", default=False)
def run(page, pagesize, tx_type, startts, endts, asset, config, verbose):
    huoju_cfg = load_config(config)['huoju']

    host   = huoju_cfg['https']
    group  = huoju_cfg['group']
    apikey = huoju_cfg['apikey']
    secret = huoju_cfg['secret']

    ts = utc_timestamp()
    headers = make_auth_headers(ts, "wallet/transactions", apikey, secret)
    url = f"{host}/api/pro/v1/wallet/transactions"

    params = dict(
        page = page,
        pageSize = pagesize,
        txType = tx_type,
        startTs = startts,
        endTs = endts,
        asset = asset
    )

    if verbose: 
        print(f"URL: {url}")
        print(f"Params: {params}")

    res = requests.get(url, headers=headers, params = params)
    pprint(parse_response(res))

if __name__ == "__main__":
    run()


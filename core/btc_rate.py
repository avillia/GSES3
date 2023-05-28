from requests import get


PUBLIC_BTC_RATE_API = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=uah"


def fetch_btc_rate() -> float:
    response = _make_response_to_external_service()
    exchange_rate = _extract_rate_from(response)
    return exchange_rate


def _make_response_to_external_service() -> dict:
    return get(PUBLIC_BTC_RATE_API).json()


def _extract_rate_from(response: dict) -> float:
    return float(response["bitcoin"]["uah"])

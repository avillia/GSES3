from asyncio import gather
from typing import Protocol

from api.db import retrieve_all_emails

from core.btc_rate import fetch_btc_rate


class Letter(Protocol):
    """
    Ascribing this as a protocol since different mailing backends
    mostly likely will share the same attributes as content, to,
    from, cc, topic etc, but will have different letter instances
    under the hood to work with.
    """


async def mail_every_user_in_db():
    current_btc_rate = fetch_btc_rate()
    subscribed_users = retrieve_all_emails()
    letter = generate_letter_for(current_btc_rate)
    await send_emails(subscribed_users, letter)


def generate_letter_for(current_btc_rate: float) -> Letter:
    return ...


async def send_emails(subscribed_users: list[str], letter: Letter):
    tasks = [send_email(user, letter) for user in subscribed_users]
    await gather(*tasks)


async def send_email(user, letter):
    """
    Honestly, have no time to properly implement this.
    Ideally, this must be a coroutine that either uses smtp module
    within python internal libraries to send the e-mail from
    pre-setup mailing server, or access external mailing service.
    """


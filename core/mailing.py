from core.btc_rate import fetch_btc_rate


def mail_every_user_in_db():
    current_btc_rate = fetch_btc_rate()
    subscribed_users = retrieve_all_emails()
    letter = generate_letter_for(current_btc_rate)
    send_emails(subscribed_users, letter)


def retrieve_all_emails() -> list[str]:
    return ...


def generate_letter_for(current_btc_rate: float):
    return ...


def send_emails(subscribed_users: list[str], letter):
    pass

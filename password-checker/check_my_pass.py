import requests
import hashlib
import sys
from pathlib import Path


def request_api_data(query):
    url = f'https://api.pwnedpasswords.com/range/{query}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the API and try again!')
    return res


def get_passwords_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwend_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chart, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_chart)
    return get_passwords_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwend_api_check(password)
        if count:
            print(
                f'{password} was found {count} times... you should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'Done!'


if __name__ == '__main__':
    passwords = Path('passwords.txt').read_text().splitlines()
    sys.exit(main(passwords))

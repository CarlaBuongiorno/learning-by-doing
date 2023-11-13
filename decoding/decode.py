from urllib.parse import unquote
from base64 import urlsafe_b64decode
import argparse


def main():
    args = get_encoded_text()
    decoded_text = decode_text(args)
    print(decoded_text)


def get_encoded_text():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=['url', 'b64', 'jwt'], help="A choice of three actions for decoding encoded text")
    parser.add_argument("encoded_text", help="The encoded text to be decoded")
    parser.add_argument("jwt_split_on", nargs='?', type=int, default=2, choices=[1, 2], help="Specify which part of a jwt token to be decoded (optional)")
    return parser.parse_args()


def decode_text(args):
    encoding_actions =  {'url': decode_url_encoding, 'b64': decode_base64, 'jwt': decode_jwt}
    return encoding_actions[args.action](args)


# url_encoding
def decode_url_encoding(args):
    return unquote(args.encoded_text)


# base64
def decode_base64(args):
    padded_payload = args.encoded_text + ('=' * (-len(args.encoded_text) % 4))
    return urlsafe_b64decode(padded_payload).decode()


# jwt
def decode_jwt(args):
    args.encoded_text = args.encoded_text.split('.')[args.jwt_split_on-1]
    return decode_base64(args)


if __name__ == '__main__':
    main()
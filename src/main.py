#!/usr/bin/env python3
'''
Script to check for price movements of desired stocks and sent a price notification
'''

import argparse


def main():
    '''Main entrypoint for the script'''
    parser = argparse.ArgumentParser(
        description='Check stocks for price movements',
        epilog='example usage: ./main.py -e johndoe@gmail.com -t 10 FUJHY AAPL TXN'
    )
    parser.add_argument(
        '-e', '--email',
        type=str,
        help='Email to send notification to'
    )
    parser.add_argument(
        '-t', '--threshold',
        type=int,
        help='Percentage threshold of when to trigger a notification'
    )
    parser.add_argument(
        'tickers',
        metavar='TICKERS',
        type=str,
        nargs='+',
        help='List of stock tickers to check'
    )
    parser.parse_args()

if __name__ == '__main__':
    main()

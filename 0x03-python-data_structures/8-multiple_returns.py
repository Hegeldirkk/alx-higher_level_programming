#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_sent = sentence[0] if length > 0 else None
    return (length, first_sent)
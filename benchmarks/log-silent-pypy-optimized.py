#!/usr/bin/env -S pypy3 -O

# -*- coding: utf-8 -*-

"""

Benchmark performance for logging a large amount of messages that are not being output to terminal.
As an example, the log level is set to 0 which will exclude debug level messages.

This benchmark will ran in optimized mode using pypy.

"""

## Import timeit
from timeit import timeit

## Import logging modules
from gbe0_log import Logger
import logging as log

## Set up logger
Logger(verbosity = 0)

## Functions to test
def __log_debug_fstring() -> None:
    """ Log a message at debug level 1000 times

    The message will be output using a fstring.
    """
    for i in range(1000):
        log.debug(f'Logging message {i}')

def __log_debug_format() -> None:
    """ Log a message at debug level 1000 times

    The message will be output using a the format function.
    """
    for i in range(1000):
        log.debug('Logging message {i}'.format(i = i))

def __log_debug_percent() -> None:
    """ Log a message at debug level 1000 times

    The message will be output using the % operator.
    """
    for i in range(1000):
        log.debug('Logging message %s' % i)

def __log_debug_string() -> None:
    """ Log a message at debug level 1000 times

    The log message will simply be the loop number.
    """
    for i in range(1000):
        log.debug(i)

fstring = timeit(__log_debug_fstring, number = 1000)
format = timeit(__log_debug_format, number = 1000)
percent = timeit(__log_debug_percent, number = 1000)
string = timeit(__log_debug_string, number = 1000)

print('Results:')
print(f'\t- fstring: {fstring}')
print(f'\t- format: {format}')
print(f'\t- percent: {percent}')
print(f'\t- string: {percent}')
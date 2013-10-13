#!/usr/bin/env python
# vim: set expandtab:

"""

License: GPL V2 See LICENSE file
Author: Jim Richardson
email: weaselkeeper@gmail.com

"""
PROJECTNAME = 'someproject'
import os
import sys
from ConfigParser import SafeConfigParser
import logging

# Example conditional import.
try:
    from pymongo import Connection
except ImportError as err:
    print 'Failed import of pymmongo, system says %s' % err
    sys.exit(1)


""" Setup logging """
logging.basicConfig(level=logging.WARN,
                    format='%(asctime)s %(levelname)s - %(message)s',
                    datefmt='%y.%m.%d %H:%M:%S')

# Setup logging to console.
console = logging.StreamHandler(sys.stderr)
console.setLevel(logging.WARN)
logging.getLogger(PROJECTNAME).addHandler(console)
log = logging.getLogger(PROJECTNAME)


def run(_args, _config):
    """ Do, whatever it is, we do. """
    log.debug((_args, _config))


def get_options():
    """ Parse the command line options"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Someproject does something')
    parser.add_argument('-n', '--dry-run', action='store_true',
        help='Dry run, do not actually perform action', default=False)
    parser.add_argument('-d', '--debug', action='store_true',
        help='Enable debugging during execution.', default=None)
    parser.add_argument('-r', '--readable', action='store_true', default=False,
        help='Display output in human readable formant (as opposed to json).')
    parser.add_argument('-c', '--config', action='store', default=None,
        help='Specify a path to an alternate config file')

    _args = parser.parse_args()
    _args.usage = PROJECTNAME + ".py [options]"

    return _args


def get_config(args):
    """ Now parse the config file.  Get any and all info from config file."""
    parser = SafeConfigParser()
    configuration = {}
    configfile = os.path.join('/etc', PROJECTNAME, PROJECTNAME +'.conf')
    if args.config:
        config = args.config
    else:
        if os.path.isfile(configfile):
            config = configfile
        else:
            log.warn('No config file found at %s' % configfile)
            sys.exit(1)

    parser.read(config)

    try:
        configuration['SOMEOPTION'] = args.SOMEOPTION
    except:
        configuration['SOMEOPTION'] = parser.get('CONFIGSECTION', 'SOMEOPTION')

    log.warn('Doing things with %s' % configuration['SOMEOPTION'])
    return configuration



# Here we start if called directly (the usual case.)
if __name__ == "__main__":
    """This is where we will begin when called from CLI. No need for argparse
    unless being called interactively, so import it here"""
    args = get_options()

    if args.debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.WARN)

    # Override config file location if present as option
    if args.config:
        config = args.config

    parsed_config = get_config(args)

    # and now we can do, whatever it is, we do.
    run(args, parsed_config)

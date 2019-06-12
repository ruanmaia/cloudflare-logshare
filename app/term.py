#### LIBRARIES IMPORT
import sys
import arrow
import click
import json

from app import cli

# IMPORT PONY ORM STATEMENTS
from pony.orm import *

#### CRAWLER GROUP COMMANDS
@cli.command('run')
@click.option(
    '--from', '_from', 
    required=True, type=click.Choice(('local', 's3', 'http-api')), 
    help='The type of data source'
)
@click.option(
    '--objects-folder',
    required=True,
    help='The path to find the log files'
)
@click.option(
    '--to', 'to', 
    required=True, type=click.Choice(('local', 's3', 'mysql', 'postgresql', 'csv', 'json', 'txt', 'elastic-search', 'http-api')), 
    help='The type of destination'
)
def run(_from, objects_folder, to): 
    print(_from)
    print(objects_folder)
    print(to)
#### LIBRARIES IMPORT
import os
import logging
import click
import yaml

#### BASIC APP CONFIGURATIONS
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
APP_VERSION = '1.0.0'

with open(BASE_PATH + '/../config.yml') as r:
    config = yaml.safe_load(r.read())

#### DATABASE CONFIGURATION
from pony.orm import Database

# db = Database()
# db.bind(**config['pony_orm'])

#### DEFAULT CLI GROUP
@click.group()
def cli(): pass

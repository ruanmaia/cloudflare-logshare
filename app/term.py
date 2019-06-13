#### LIBRARIES IMPORT
import sys
import arrow
import click
import json
import shutil
import os

from pathlib import Path
from tqdm import tqdm

from app import cli, config

# IMPORT PONY ORM STATEMENTS
from pony.orm import *

#### CLI COMMANDS
@cli.command('run')
def run(): 
    
    for input_file in tqdm(Path(config['source']['path']).glob('**/*.log.gz')):
        
        output_file = str(input_file).replace(config['source']['path'], '').lstrip('/')
        output_file = Path('/'.join((config['destination']['path'], output_file)))

        os.makedirs(output_file.parent, exist_ok=True)
        shutil.copyfile(str(input_file), str(output_file))

        os.system('gunzip -fq {}'.format(str(output_file)))
        adjusted_output = str(output_file.parent) + '/' + str(output_file.stem)
        lines = open(adjusted_output).readlines()

        # print(adjusted_output)

        with open(adjusted_output, 'w') as f:

            for line in lines:
                data = json.loads(line)
                line = '{} {} {} {} {}'.format(
                    data['EdgeStartTimestamp'],
                    data['ClientIP'], 
                    data['ClientRequestHost'], 
                    data['ClientRequestMethod'], 
                    data['ClientRequestURI']
                )
                # print(line)
                f.write(line + "\n")

        # exit(0)
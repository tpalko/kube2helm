#!/usr/bin/python

import yaml
import click
import os
from datetime import datetime

class Converter(object):

    yaml_source = None 

    def __init__(self, *args, **kwargs):
        for k in kwargs:
            self.__setattr__(k, kwargs[k])
    
    def run(self):
        content = None 
        with open(self.yaml_source, 'r') as f:
            content = f.read()
        if not content:
            return 
        y = yaml.load(content)
        objs = y['objects']
        if len(objs) == 0:
            return 
        #templates_folder = os.path.join("processed", datetime.strftime(datetime.now(), "%Y%m%d_%H%M%S"))
        chart_name = os.path.basename(self.yaml_source).split(".")[0]
        templates_folder = os.path.join("charts", chart_name, "templates")
        #os.makedirs(templates_folder)
        for o in objs:
            kind = o['kind']
            name = o['metadata']['name']
            with open(os.path.join(templates_folder, "%s_%s.yml" %(kind, name)), 'w') as o_file:
                o_file.write(yaml.dump(o))


@click.command()
@click.option('--yaml-source', '-f', 'yaml_source', required=True, help='The YAML file')
def main(yaml_source):
    c = Converter(yaml_source=yaml_source)
    c.run()

if __name__ == "__main__":
    main()

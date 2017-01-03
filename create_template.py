'''
This script can be used to quickly print a command for pushing a new template to ES cluster

Usage:-
    python create_template.py --index logstash-2016.12.23 --name=logs --pattern logstash-\* > push_template.sh
'''
import requests
import sys
import argparse
import logging
import json


logger = logging.getLogger(__file__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(filename)s:%(lineno)s %(levelname)s:%(message)s')


class IndexNotFound(Exception):
    pass


def parse_args():
    '''
    Parses command-line arguments
    '''
    parser = argparse.ArgumentParser(description='Create templates from a live index')
    parser.add_argument('--index', dest='index', required=True, help='Index that is used for fetching the mapping')
    parser.add_argument('--name', dest='name', required=True, help='Name of template. REST resource where PUT request is sent')
    parser.add_argument('--pattern', dest='pattern', required=True, help='This pattern decides what all indices will have that mapping')
    args = parser.parse_args()
    return args


def get_mapping(index_name):
    '''
    Gets current mapping for an index
    '''
    try:
        mapping = requests.get("http://localhost:9200/{0}/_mapping".format(index_name)).json()[index_name]['mappings']
    except KeyError:
        raise IndexNotFound("get_mapping: Index Not Found")
    return mapping


def main():
    args = parse_args()

    # Get current mapping
    mapping = None
    try:
        mapping = get_mapping(args.index)
    except:
        logging.exception("Error getting mapping for index, index not found")
        sys.exit(1)

    index_template = {
        "template": args.pattern,
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": mapping
    }

    print "curl localhost:9200/_template/{0} -d '\n{1}'".format(args.name, json.dumps(index_template, indent=2))


if __name__ == '__main__':
    main()

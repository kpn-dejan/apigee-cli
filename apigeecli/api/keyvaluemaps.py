#!/usr/bin/env python
"""https://apidocs.apigee.com/api-services/content/environment-keyvalue-maps"""

import requests
import json

from apigeecli import APIGEE_ADMIN_API_URL
from apigeecli.util import authorization

def create_keyvaluemap_in_an_environment(args):
    uri = '{}/v1/organizations/{}/environments/{}/keyvaluemaps'.format(
        APIGEE_ADMIN_API_URL, args.org, args.environment, args.name
    )
    hdrs = authorization.set_header({'Accept': 'application/json', 'Content-Type': 'application/json'}, args)
    body = json.loads(args.body)
    resp = requests.post(uri, headers=hdrs, json=body)
    resp.raise_for_status()
    # print(resp.status_code)
    return resp

def delete_keyvaluemap_from_an_environment(args):
    uri = '{}/v1/organizations/{}/environments/{}/keyvaluemaps/{}'.format(
        APIGEE_ADMIN_API_URL, args.org, args.environment, args.name
    )
    hdrs = authorization.set_header({'Accept': 'application/json'}, args)
    resp = requests.delete(uri, headers=hdrs)
    resp.raise_for_status()
    # print(resp.status_code)
    return resp

def get_keyvaluemap_in_an_environment(args):
    uri = '{}/v1/organizations/{}/environments/{}/keyvaluemaps/{}'.format(
        APIGEE_ADMIN_API_URL, args.org, args.environment, args.name
    )
    hdrs = authorization.set_header({'Accept': 'application/json'}, args)
    resp = requests.get(uri, headers=hdrs)
    resp.raise_for_status()
    # print(resp.status_code)
    return resp

def list_keyvaluemaps_in_an_environment(args):
    uri = '{}/v1/organizations/{}/environments/{}/keyvaluemaps'.format(
        APIGEE_ADMIN_API_URL, args.org, args.environment
    )
    hdrs = authorization.set_header({'Accept': 'application/json'}, args)
    resp = requests.get(uri, headers=hdrs)
    resp.raise_for_status()
    # print(resp.status_code)
    return resp

def update_an_entry_in_an_environment_scoped_kvm(args):
    uri = '{}/v1/organizations/{}/environments/{}/keyvaluemaps/{}/entries/{}'.format(
        APIGEE_ADMIN_API_URL, args.org, args.environment, args.name, args.entry_name
    )
    hdrs = authorization.set_header({'Accept': 'application/json', 'Content-Type': 'application/json'}, args)
    body = {
      'name' : args.entry_name,
      'value' : args.updated_value
    }
    resp = requests.post(uri, headers=hdrs, json=body)
    resp.raise_for_status()
    # print(resp.status_code)
    return resp

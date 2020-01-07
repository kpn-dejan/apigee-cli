#!/usr/bin/env python
"""https://apidocs.apigee.com/api/caches"""

import json
import requests

from apigee import APIGEE_ADMIN_API_URL
from apigee.abstract.api.caches import ICaches, CachesSerializer
from apigee.util import authorization

class Caches(ICaches):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clear_all_cache_entries(self, environment):
        uri = '{0}/v1/organizations/{1}/environments/{2}/caches/{3}/entries?action=clear' \
            .format(APIGEE_ADMIN_API_URL,
                    self._org_name,
                    environment,
                    self._cache_name)
        hdrs = authorization.set_header({'Accept': 'application/json',
                                         'Content-Type': 'application/octet-stream'},
                                        self._auth)
        resp = requests.post(uri, headers=hdrs)
        resp.raise_for_status()
        # print(resp.status_code)
        return resp

    def clear_a_cache_entry(self, environment, entry):
        uri = '{0}/v1/organizations/{1}/environments/{2}/caches/{3}/entries/{4}?action=clear' \
            .format(APIGEE_ADMIN_API_URL,
                    self._org_name,
                    environment,
                    self._cache_name,
                    entry)
        hdrs = authorization.set_header({'Accept': 'application/json',
                                         'Content-Type': 'application/octet-stream'},
                                        self._auth)
        resp = requests.post(uri, headers=hdrs)
        resp.raise_for_status()
        # print(resp.status_code)
        return resp

    def create_a_cache_in_an_environment(self, environment, request_body):
        uri = '{0}/v1/organizations/{1}/environments/{2}/caches?name={3}' \
            .format(APIGEE_ADMIN_API_URL,
                    self._org_name,
                    environment,
                    self._cache_name)
        hdrs = authorization.set_header({'Accept': 'application/json',
                                         'Content-Type': 'application/json'},
                                        self._auth)
        body = json.loads(request_body)
        resp = requests.post(uri, headers=hdrs, json=body)
        resp.raise_for_status()
        # print(resp.status_code)
        return resp
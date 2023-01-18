#!/usr/bin/env python3

"""
This script provides some stats about about nginx logs stored in MongoDB
"""

import pymongo


if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    log_stats = '{} logs\nMethods:'.format(nginx.count_documents({}))
    methods = [
               'GET',
               'POST',
               'PUT',
               'PATCH',
               'DELETE'
               ]
    for i in range(5):
        log_stats += '\n\tmethod {}: {}'.format(methods[i],
                                                nginx.count_documents({
                                                    "method": methods[i]
                                                    }))
    log_stats += '\n{} status check'.format(nginx.count_documents({
                                                        "$and": [
                                                            {"method": "GET"},
                                                            {"path": "/status"}
                                                        ]
                                                    }))
    print(log_stats)

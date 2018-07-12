# -*- coding: utf-8 -*-
# plugin_rally.py
import json
import logging
import os
LOG = logging.getLogger(__name__)


def start(requestdict):
    try:
        from rally import api as rally_api
    except ImportError:
        rally_api = None

    try:
        from rally.cli.commands import task as rally_task
    except ImportError:
        rally_task = None

    if rally_api is None or rally_task is None:
        LOG.warning('Failed to import Rally')

    else:
        temp_dict = json.loads(requestdict)
        key = temp_dict.keys()
        if not temp_dict['syntaxcheck']:
            key.remove('syntaxcheck')
            file_path = './' + key[0] + '.json'
            with open(file_path, 'w') as make_file:
                json.dump(temp_dict[key[0]], make_file)

            rally_task.TaskCommands().start(rally_api.API(),
                                            file_path,
                                            tags=['Vitrage', key[0]])
            os.remove(file_path)

        else:
            key.remove('syntaxcheck')
            file_path = './' + key[0] + '.json'
            with open(file_path, 'w') as make_file:
                json.dump(temp_dict[key[0]], make_file)
            rally_task.TaskCommands().validate(rally_api.API(), file_path)

            os.remove(file_path)
# -*- coding: utf-8 -*-
# plugin_rally.py

import json
import logging
import os

LOG = logging.getLogger(__name__)


def start(requestdict):
    """Starts Rally testing.

    Args:
        requestdict: A dictionary that is used to execute the Rally testing.

    Returns:
        None.
    """
    LOG.debug("plugin_rally.py start()")
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
        LOG.warning(requestdict)
        temp_dict = json.loads(requestdict)
        key = temp_dict.keys()
        # if not temp_dict['syntaxcheck']:
        #     key.remove('syntaxcheck')
        file_path = './' + key[0] + '.json'
        LOG.warning(file_path)
        with open(file_path, 'w') as make_file:
            json.dump(temp_dict, make_file)

        rally_task.TaskCommands().start(rally_api.API(),
                                        file_path,
                                        tags=['Vitrage', key[0]])
        os.remove(file_path)

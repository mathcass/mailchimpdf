from __future__ import print_function

import sys

import pandas as pd
import six
import slumber

from mailchimpdf import util as mcutil


def get_list(list_id):
    """Returns a pandas.DataFrame of the given MailChimp list

    Args:
        list_id (int|string): the desired list_id

    Returns:
        pandas.DataFrame if successful, None otherwise
    """
    list_data = get_mailchimp_list(list_id)
    list_df = list_data_to_df(list_data)
    return list_df


def get_mailchimp_list(list_id):
    """Returns a list of MailChimp subscribers given the list_id

    Args:
        list_id (int|string): the desired list_id

    Returns:
        list if dict if successful, [] otherwise
    """
    # retrieve first set of subscribers, loop thru cursor, extend and then
    # return
    apikey = mcutil.get_mailchimp_apikey()
    endpoint = mcutil.get_mailchimp_endpoint(apikey)
    api = slumber.API(endpoint, auth=('', apikey))
    list_method = api.lists(list_id)

    BATCH_SIZE = 1000
    members = []
    apiargs = {'count': BATCH_SIZE}
    batch = list_method.members.get(**apiargs)
    members.extend(batch['members'])

    while batch:
        apiargs.setdefault('offset', 0)
        apiargs['offset'] += BATCH_SIZE
        batch = list_method.members.get(**apiargs)['members']
        members.extend(batch)

    return members


def list_data_to_df(list_data):
    """Turns a list of MailChimp subscribers into a pandas.DataFrame

    Args:
        list_data (list): list of dicts of MailChimp subscribers

    Returns:
        pandas.DataFrame if successful, None otherwise
    """
    # We generally don't have to modify much to make this work. We should
    # ensure that we massage some of the column data into a consistent format
    df = pd.DataFrame(list_data)
    df.drop(labels='_links', axis=1, inplace=True)  # No need for REST helpers

    field_names = ['merge_fields', 'interests', 'location',
                   'stats']
    dfs = [df]
    for field_name in field_names:
        if field_name in df.columns:
            dfs.append(dict_series_to_df(df[field_name]))
            df.drop(labels=field_name, axis=1, inplace=True)

    return pd.concat(dfs, axis=1)


def dict_series_to_df(dict_series):
    """Turns a series of dictionaries into a DataFrame with keys as columns and
    values as rows

    Args:
        dict_series (pandas.Series): Series of dictionaries

    Returns:
        pandas.DataFrame if successful, None otherwise

    """
    fields = {}
    IDX = 'index'
    for (i, item) in dict_series.iteritems():
        fields.setdefault(IDX, [])
        fields[IDX].append(i)

        for (k, v) in six.iteritems(item):
            fields.setdefault(k, [])
            fields[k].append(v)

    return pd.DataFrame(fields).set_index(IDX)


def main():
    args = list(sys.argv)
    list_id = args[1]  # First argument is list id
    print(get_list(list_id))


if __name__ == '__main__':
    main()

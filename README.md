# MailChimp DataFrames

## About

[MailChimp](http://mailchimp.com/) subscriber lists have a natural translation
onto spreadsheets and other data structures. It's also fairly easy to pull data
via their [REST API](http://developer.mailchimp.com/). 

This package provides a set of tools to make it easier to map a MailChimp list
onto a Pandas [DataFrame](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) object for analysis. 

## Usage 

This package has been tested with Python 2.7 only. 

The base usage is fairly simple. You'll need a MailChimp
[API key](https://admin.mailchimp.com/account/api-key-popup) to get started.
Once you have that, drop it into a `~/.mailchimprc` file in your home directory.
Next,
[go grab the id](http://kb.mailchimp.com/lists/managing-subscribers/find-your-list-id)
of a list you're interested in.

    from mailchimpdf.list import get_list
    get_list(<list_id>)

Additionally, there's also a simple command-line script for quick inspection: 

    mailchimpdf-list <list_id>

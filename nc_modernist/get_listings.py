#!/usr/bin/env python
"""Show the latest results from NC Modernist listings."""

from datetime import date, timedelta
from apiclient.discovery import build  # pylint: disable=import-error
import attr
import click


@attr.s
class Listing(object):
    """Class that contains listing attributes."""

    added = attr.ib()
    price = attr.ib()
    address = attr.ib()
    url = attr.ib()


@click.command()
@click.option('--days', '-d',
              default=3,
              help='Show listings posted in the past x days.')
@click.argument('key',
                envvar='GOOGLE_API_KEY')
def search(key, days):
    """Search the fusion table."""
    today = date.today()
    # Search this amount of past days
    dlt = timedelta(days=days)
    table_id = '1qkrH6LkYzH-hAb1mbk8Fq4SbOkaJG5Y2QDekTFI'
    service = build('fusiontables', 'v2', developerKey=key)

    try:
        # Run the query
        results = service.query().sql(
            sql="SELECT 'Date Posted', Price, Address, 'Link/Comments' FROM {id} \
                 WHERE 'Date Posted'>='{day}' \
                 ORDER BY 'Date Posted' \
                 DESC".format(id=table_id,
                              day=(today-dlt).strftime('%m/%d/%y'))).execute()

        total = len(results['rows'])
        print('Found {} total results for the last {} day(s)'.format(total,
                                                                     days))

        # Create a Listing object for each search result
        listings = []
        for result in results['rows']:
            listings.append(Listing(*result))

        for listing in listings:
            click.echo(
                """Added on: {added}
Price: ${price}
Address: {address}
URL: {url}
""".format(**attr.asdict(listing)))
    except KeyError:
        print('No results for the past {} day(s).'.format(days))


if __name__ == "__main__":
    search()  # pylint: disable=no-value-for-parameter

## View the latest listings from NC Modernist

[NC Modernist](http://www.ncmodernist.org/forsale.html) maintains a [Google Fusion Table](https://www.google.com/fusiontables/DataSource?docid=1qkrH6LkYzH-hAb1mbk8Fq4SbOkaJG5Y2QDekTFI) of modern homes for sale in North Carolina. This is used to return listings in the past number of specified days.

### Usage

Install prerequisites:
```
pip install -r requirements.txt
```

Run the script:
```
> python get_listings.py -d 3
Found 3 total results for the last 3 day(s)
Added on: 8/31/18
Price: $250000
Address: 1903 Colonial Avenue Greensboro NC
URL: https://www.realtor.com/realestateandhomes-detail/1903-Colonial-Ave_Greensboro_NC_27408_M60522-82888

Added on: 8/31/18
Price: $885000
Address: 1020 Highland Woods Road Chapel Hill NC
URL: ps://www.realtor.com/realestateandhomes-detail/1020-Highland-Woods-Rd_Chapel-Hill_NC_27517_M68863-54508

Added on: 8/28/18
Price: $449900
Address: 3500 Craig Avenue Charlotte NC
URL: https://www.realtor.com/realestateandhomes-detail/3500-Craig-Ave_Charlotte_NC_28211_M66240-96584
```

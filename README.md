## Information:
The information in JSON Files which the crawler gets from various websites is organized like this:
##### 1. List of places which host a horse-racing event
##### 2. In that list there's information about each place and the events at the said place
##### 3. Each event has from 6 to 9 races
##### 4. Each race has it's runners(horses/jockeys) Usually 9 of them and it's own information
##### 5. Each horse has it's own list of information, includes nicking stats.
That should be it.

## JSON Structure:

``` 
[
    {
        "date": "28",
        "name": "\nBelmont Park\n",
        "url": "http://www.equibase.com/static/entry/RaceCardIndexBEL042818USA-EQB.html",
        "races": [
            {
                "Race: ": "Race 1",
                "URL": "http://www.equibase.com/static/entry\\BEL042818USA1-EQB.html",
                "Purse": "$80,000",
                "Race Type": "AllowanceOptionalClaiming",
                "Distance": "7 Furlongs",
                "Surface": "Turf",
                "Starters": "8",
                "Est. Post": "1:30 PM",
                "Horses": [
                    {
                        "P#": "2",
                        "PP": "2",
                        "Name": "Annie Rocks",
                        "Claim": "$62,500",
                        "Jockey": "P   Fragoso",
                        "Wgt": "120",
                        "Trainer": "C F Martin",
                        "M/L": "6/1",
                        "Info": [
                            {
                                "sire": "SIRE of : A. P. Warrior",
                                "name": "A. P. Warrior",
                                "foals": "247",
                                "starters": "203,82",
                                "winners": "163,66",
                                "BW (%)": "8,3",
                                "earnings": "10948495",
                                "ael": "1.01"
                            },
                           
                                "sire": "BROODMARE SIRE of : Five Star Day",
                                "name": "Five Star Day",
                                "mares": "93",
                                "foals": "279",
                                "starters": "173,62",
                                "winners": "125,45",
                                "BW (%)": "11,4",
                                "earnings": "8003219",
                                "ael": "1.04"
                            },
                            {
                                "sire": "Nicking Stats for mares by Five Star Day when bred to A. P. Warrior",
                                "mares": "1",
                                "foals": "1",
                                "starters": "1,100",
                                "winners": "1,100",
                                "BW (%)": "0,0",
                                "earnings": "264005",
                                "ael": "3.64"
                            }
                        ],
                        "uuid": "633e5662-0ccd-4a0e-bfc8-ec6ad30c2a01"
                    },
                    ```


<a className="gh-badge" href="https://datahub.io/core/fips-10-4"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

List of FIPS (Federal Information Processing Standards) region codes.

## Data

FIPS publication 10-4: COUNTRIES, DEPENDENCIES, AREAS OF SPECIAL SOVEREIGNTY, AND THEIR PRINCIPAL ADMINISTRATIVE DIVISIONS

Comes from [efele.net](http://efele.net/maps/fips-10/data/)  
 
Source url: http://efele.net/maps/fips-10/data/fips-414.txt  
Output csv file: `data/data.csv`

### Data format

```
region code,region division,region name
AA00,country,ARUBA
AC00,country,ANTIGUA AND BARBUDA
AC01,dependency,Barbuda
AC03,parish,Saint George
```

* `region_code` - FIPS 10-4 code
* `region_division` - division name for the given country
* `region_name` - name of the region
 
## Preparation
 
If you want to update this data, you will need git and python3 installed to run processing script.

``` bash
git clone https://github.com/datasets/administrative-codes-FIPS-10-4.git
cd administrative-codes-FIPS-10-4
python3 scripts/process.py
```

## license

Author:
eric.muller at efele.net

*To the extent possible under law, Eric Muller has waived all copyright and related or neighboring rights to this page. This work is published from the United States.
Note that this does not affect the rights other persons may have in those files. I am not qualified to determine whether such rights exist.*

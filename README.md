# Data Collection

This is a repository for high-quality, transparent data collection. 

# Getting github

If not familiar with Github, it is *the* gold standard version control system which manages all versioning and makes the history tracking of versioning transparent. 

* [Install git](https://git-scm.com/).
* Try this [tutorial](https://guides.github.com/activities/hello-world/). In particular, learn how to create a pull request. [Here is an example of a pull request](https://github.com/apache/hadoop/pull/2437). 

# Organization

## Directory organization
The repository is organized as such: 

* `/data/` - Root data directory
* `/data/<state>` - State-level data, e.g., `/WI`
* `/data/<state>/<county>` - County-level data, e.g., `/WI/Milwaukee`
* `/scripts` - Various helper example scripts (advanced)

## Data grouping

Data within the state + county folders are **organized by granularity.** That is, ward-level data for Milwaukee might be stored in `/data/WI/Milwaukee/ward` whereas hypothetical district-level data would be stored in `/data/WI/Milwaukee/district`. 

Each data folder has 2 files:

* `csv` - A single CSV file containing all the data for that folder. 
* `README.md` - A README that shows each row of data and how it was determined. See `/WI/Milwaukee/ward/README.md` as an example. 

# Data collection guidelines

* **Descriptive headers** - All row headers are in [`snake_case`](https://en.wikipedia.org/wiki/Snake_case) . Row headers should be descriptive, because their name will be extracted automatically. For instance, `ballots_cast` will convert to "Ballots Cast."
* **Indicate dates** - Indicate dates the data was originally collected where possible. For example, for a ward's population that was tabulated in 2018, use `ward_population_2018`. 
* **Prefer raw numbers over ratios or other derivative calculations** - E.g., instead of entering `percent_population_minors_2019` to indicate a percentage of a ward's population, use `number_of_minors_2019`. 

# PR guidelines

For adding new columns or new sets of data, we recommend the following guidelines: 
* **Document data source** - All PRs must document exactly how the data source was collected. 

* **Archive link** - If the data source was collected from a hyperlink, *always* include a link to its archive. Example of an archiving site: [archive.is](http://archive.is) 
* **Update the README.md** Include *all* of the following information: 
	* *Row type* - Is the row type numeric or text? What possible values does it have? 
	* *Row description* - A description of the row, be as specific as possible. 

**PRs that add new data should not be approved until all guidelines are met!**



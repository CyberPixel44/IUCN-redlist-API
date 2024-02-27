# IUCN Species Data Retrieval Script

This Python script allows users to retrieve biological data about species from the IUCN (International Union for Conservation of Nature) Red List. By interacting with the IUCN API, users can obtain information based on different search criteria such as country, category, or specific species.

## Prerequisites

Before using the script, ensure that you have a valid API token from IUCN. Insert your token in the script where specified:

```python
locu_api = '?token=<INSERT_YOUR_TOKEN_id_HERE>'
```
You can get your personal API [here](https://apiv3.iucnredlist.org/api/v3/token)

## Usage

1. Run the script in a Python environment.

```bash
python iucn_species_data.py
```

2. Select the type of search you want to perform: Country, Category, or Species.

3. Follow the prompts to provide additional information based on your selected search type.

4. View the retrieved biological data for the specified species or criteria.

## Options

- **Country**: Retrieve species data based on a specific country.
- **Category**: Retrieve species data based on a specific conservation category.
- **Species**: Retrieve detailed information about a specific species.

## Example

```bash
Options: Country, Category, Species
Type The Option: Country
Type country code: US
-----------------------------------------------
LC Canis lupus
LC Ursus americanus
...
-----------------------------------------------
```

Feel free to explore and analyze data for conservation research or other purposes using this script. Remember to respect the terms of use for the IUCN API.
Learn more about the API [here](https://apiv3.iucnredlist.org/api/v3/docs)

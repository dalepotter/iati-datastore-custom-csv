# Generating a custom CSV from the IATI Datastore

This python script shows a process to generate a CSV file with custom data from the [IATI Datastore](http://datastore.iatistandard.org).


## Usage

### Installation

```
# Clone the code
git clone https://github.com/dalepotter/iati-datastore-custom-csv.git

# Create and activate a virtual environment
virtualenv pyenv
source pyenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Getting raw IATI data

Use [wget](http://www.computerhope.com/unix/wget.htm) to download some data from the [IATI Datastore](http://datastore.iatistandard.org).

In this case, all IATI data relating to Somalia can be downloaded and saved to `somalia.xml` using:

```
wget http://datastore.iatistandard.org/api/1/access/activity.csv?recipient-country=SO&stream=True --output-document somalia.xml
```

### Generating a CSV

```
python tocsv.py
```

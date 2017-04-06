import csv
from lxml import etree
import math

tree = etree.parse("somalia.xml")

def first_elem(list):
	if len(list) > 0:
		return list[0]
	else:
		return None

with open('somalia-IATI.csv', 'w', newline='') as csvfile:
	csv_writer = csv.writer(csvfile, delimiter=',')
	csv_writer.writerow([
		'iati-identifier',

		'reporting-org/@ref',
		'reporting-org/@secondary-reporter',

		'title',
		'description',

		'recipient-country',
		'activity-status',

		'sector/@vocabulary',
		'sector/@code',
		'sector/@percentage',

		'location/@ref',
		'location/location-id',
		'location/location-id/@vocabulary',

		'location/name',
		'location/description',
		'location/point/pos',
		'location/exactness/@code',
		'location/location-class/@code'
		])

	for activity in tree.find('iati-activities').findall('iati-activity'):

		# get IATI major version
		ns = etree.FunctionNamespace("http://datastore.iatistandard.org/ns")
		ns.prefix = "iati-extra"
		major_version = math.floor(float(activity.xpath('@iati-extra:version')[0]))

		# import pdb;pdb.set_trace()

		row = [
			first_elem(activity.xpath('iati-identifier/text()')),

			first_elem(activity.xpath('reporting-org/@ref')),
			first_elem(activity.xpath('reporting-org/@secondary-reporter')),

			first_elem(activity.xpath('title/text()') if major_version == 1
				else activity.xpath('title/narrative/text()')),
			first_elem(activity.xpath('description/text()') if major_version == 1
				else activity.xpath('description/narrative/text()')),

			first_elem(activity.xpath('recipient-country/@code')),
			first_elem(activity.xpath('activity-status/@code')),

			';'.join(activity.xpath('sector/@vocabulary')),
			';'.join(activity.xpath('sector/@code')),
			';'.join(activity.xpath('sector/@percentage')),

			first_elem(activity.xpath('location/@ref')),
			first_elem(activity.xpath('location/location-id/@code')),
			first_elem(activity.xpath('location/location-id/@vocabulary')),

			first_elem(activity.xpath('location/name/text()') if major_version == 1
				else activity.xpath('location/name/narrative/text()')),
			first_elem(activity.xpath('location/description/text()') if major_version == 1
				else activity.xpath('location/description/narrative/text()')),

			first_elem(activity.xpath('location/point/pos/text()')),
			first_elem(activity.xpath('location/exactness/@code')),
			first_elem(activity.xpath('location/location-class/@code'))
		]

		# Write row, but add NULL if nothing contained at the field
		csv_writer.writerow([output if bool(output) else 'NULL' for output in row])

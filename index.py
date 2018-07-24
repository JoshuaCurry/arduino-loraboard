import json
import pprint

with open('package_loraboard_index.json', 'r') as file:
    data = json.load(file)


toInsert = {}

toInsert['boards'] = []
toInsert['boards'].append({'name': 'LoRaBoard M0'})

toInsert['architecture'] = 'samd'
toInsert['name'] = 'LoRaBoard M0 Boards'
toInsert['category'] = 'test'

toInsert['version'] = input('board version? ')
toInsert['archiveFileName'] = input('bzip filename? ')
toInsert['checksum'] = input('bzip checksum? ')

toInsert['help'] = {'online': 'https://forums.localhost'}

toInsert['url'] = input('bzip url? ')

toInsert['size'] = input('bzip filesize? ')

toInsert['toolsDependencies'] = []

tool1 = {"name": "arm-none-eabi-gcc", "packager": "arduino", "version": "4.8.3-2014q1"}
tool2 = {"name": "bossac", "packager": "arduino", "version": "1.6.1-arduino"}
tool3 = {"name": "openocd", "packager": "arduino", "version": "0.9.0-arduino"}
tool4 = {"name": "CMSIS", "packager": "arduino", "version": "4.0.0-atmel"}

toInsert['toolsDependencies'].append(tool1)
toInsert['toolsDependencies'].append(tool2)
toInsert['toolsDependencies'].append(tool3)
toInsert['toolsDependencies'].append(tool4)

pprint.pprint(toInsert)

data['packages'][0]['platforms'].append(toInsert)

with open('package_loraboard_index.json', 'w') as file:
    json.dump(data, file, indent="\t")

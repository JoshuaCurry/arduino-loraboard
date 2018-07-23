#!/bin/bash

rm loraboard-1.0.0.tar.bz2
tar -jcvf loraboard-1.0.0.tar.bz2 loraboard/

a=$(openssl dgst -sha256 loraboard-1.0.0.tar.bz2 | cut -d ' ' -f 2)

sed -i.bak "s/\"SHA-256:.*\"/\"SHA-256:$a\"/g" package_loraboard_index.json

rm package_loraboard_index.json.bak

echo -e "\nDone - Ready for git\n"

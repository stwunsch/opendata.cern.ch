#!/bin/bash

docker exec -i -t opendatacernch_web_1 cernopendata fixtures records --mode insert-or-replace \
    -f /code/cernopendata/modules/fixtures/data/records/cms-tools-nanoaod-outreach-dimuon-spectrum.json \
    -f /code/cernopendata/modules/fixtures/data/records/cms-tools-nanoaod-outreach-higgstautau.json \
    -f /code/cernopendata/modules/fixtures/data/records/cms-derived-nanoaod-outreach-higgstautau.json \
    -f /code/cernopendata/modules/fixtures/data/records/cms-derived-nanoaod-outreach-DoubleMuParked.json \

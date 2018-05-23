#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A krvjezivot.celeryapp worker -l INFO

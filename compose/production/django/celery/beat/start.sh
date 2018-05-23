#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A krvjezivot.celeryapp beat -l INFO

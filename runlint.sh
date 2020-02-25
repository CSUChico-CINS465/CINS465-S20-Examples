#!/bin/bash

pylint --load-plugins pylint_django --disable=missing-docstring ./mysite/mysite
pylint --load-plugins pylint_django --disable=missing-docstring ./mysite/myapp
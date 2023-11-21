#!/bin/bash
pg_restore -U admin -Fc -C -d online_python_school < ../tmp/db.pgsql
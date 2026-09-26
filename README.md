# ora-csv-loader

[![tests](https://github.com/raoulmunet/ora-csv-loader/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-csv-loader/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Inspect a CSV file and generate starter Oracle loading artifacts.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ CREATE TABLE and SQL*Loader output |
> | Oracle Database 23ai | ✅ CREATE TABLE and SQL*Loader output |
> | Oracle AI Database 26ai | ✅ CREATE TABLE and SQL*Loader output |
>
> Generated artifacts intentionally use conservative syntax shared by all three releases.

## Features

- samples CSV values;
- infers `NUMBER`, `DATE`, `TIMESTAMP` or `VARCHAR2(n)`;
- generates `CREATE TABLE`;
- generates a SQL*Loader control file;
- keeps inference visible so you can review before loading.

## Usage

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-csv-loader.git"

ora-csv-loader examples/customers.csv --table STG_CUSTOMERS
ora-csv-loader examples/customers.csv --table STG_CUSTOMERS --format ctl
```

## Example

For:

```csv
customer_id,name,created_date
1,Ana,2026-01-01
2,Mihai,2026-01-02
```

the tool proposes:

```sql
CREATE TABLE STG_CUSTOMERS (
  CUSTOMER_ID NUMBER,
  NAME VARCHAR2(...),
  CREATED_DATE DATE
);
```

## Important

Type inference is a convenience, not schema truth. Sampled files can hide later values that require wider strings or different numeric precision.

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.

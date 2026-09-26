# ora-csv-loader

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

## License

MIT.

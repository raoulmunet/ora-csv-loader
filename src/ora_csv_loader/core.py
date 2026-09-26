from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
import csv,re
from pathlib import Path

@dataclass(frozen=True)
class ColumnGuess:
    name:str
    datatype:str

def _is_number(v:str)->bool:
    try: float(v); return True
    except ValueError: return False

def _is_date(v:str)->bool:
    try: datetime.strptime(v,"%Y-%m-%d"); return True
    except ValueError: return False

def _is_timestamp(v:str)->bool:
    try: datetime.fromisoformat(v); return "T" in v or " " in v
    except ValueError: return False

def infer_columns(path:str|Path,sample_rows:int=1000)->list[ColumnGuess]:
    with open(path,newline="",encoding="utf-8-sig") as f:
        reader=csv.DictReader(f)
        values={h:[] for h in (reader.fieldnames or [])}
        for i,row in enumerate(reader):
            if i>=sample_rows: break
            for h in values:
                v=(row.get(h) or "").strip()
                if v!="": values[h].append(v)
    guesses=[]
    for h,vals in values.items():
        name=re.sub(r"\W+","_",h.strip()).strip("_").upper() or "COLUMN"
        if vals and all(_is_number(v) for v in vals): dtype="NUMBER"
        elif vals and all(_is_date(v) for v in vals): dtype="DATE"
        elif vals and all(_is_timestamp(v) for v in vals): dtype="TIMESTAMP"
        else:
            maxlen=max([len(v) for v in vals] or [1])
            size=min(max(maxlen*2,32),4000)
            dtype=f"VARCHAR2({size})"
        guesses.append(ColumnGuess(name,dtype))
    return guesses

def render_ddl(table:str,cols:list[ColumnGuess])->str:
    body=",\n".join(f"  {c.name} {c.datatype}" for c in cols)
    return f"CREATE TABLE {table.upper()} (\n{body}\n);"

def render_ctl(table:str,csv_name:str,cols:list[ColumnGuess])->str:
    fields=[]
    for c in cols:
        if c.datatype=="DATE": fields.append(f'  {c.name} DATE "YYYY-MM-DD"')
        elif c.datatype=="TIMESTAMP": fields.append(f'  {c.name} TIMESTAMP "YYYY-MM-DD HH24:MI:SS"')
        else: fields.append(f"  {c.name}")
    return "\n".join([
        "LOAD DATA",
        f"INFILE '{csv_name}'",
        f"INTO TABLE {table.upper()}",
        "APPEND",
        "FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"'",
        "TRAILING NULLCOLS",
        "(",
        ",\n".join(fields),
        ")"
    ])

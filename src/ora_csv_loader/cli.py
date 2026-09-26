from __future__ import annotations
import argparse
from pathlib import Path
from .core import infer_columns,render_ctl,render_ddl

def main(argv=None):
    p=argparse.ArgumentParser(description="Generate Oracle CSV loading artifacts.")
    p.add_argument("source")
    p.add_argument("--table",required=True)
    p.add_argument("--format",choices=("ddl","ctl"),default="ddl")
    p.add_argument("--sample-rows",type=int,default=1000)
    a=p.parse_args(argv)
    cols=infer_columns(a.source,a.sample_rows)
    print(render_ddl(a.table,cols) if a.format=="ddl" else render_ctl(a.table,Path(a.source).name,cols))
    return 0
if __name__=="__main__": raise SystemExit(main())

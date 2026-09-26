from pathlib import Path
from ora_csv_loader import infer_columns,render_ddl

def test_inference(tmp_path:Path):
    p=tmp_path/"x.csv"
    p.write_text("id,name,d\n1,Ana,2026-01-01\n2,Mihai,2026-01-02\n",encoding="utf-8")
    cols=infer_columns(p)
    assert cols[0].datatype=="NUMBER"
    assert cols[2].datatype=="DATE"
    assert "CREATE TABLE STG_X" in render_ddl("stg_x",cols)

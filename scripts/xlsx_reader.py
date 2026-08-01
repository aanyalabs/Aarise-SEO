"""Minimal stdlib-only .xlsx reader (no openpyxl/pandas available on this machine)."""
import zipfile
from xml.etree import ElementTree as ET

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
RNS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
COL_RE = __import__("re").compile(r"([A-Z]+)(\d+)")


def col_to_idx(col):
    idx = 0
    for ch in col:
        idx = idx * 26 + (ord(ch) - ord("A") + 1)
    return idx - 1


def load_workbook(path):
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        root = ET.fromstring(z.read("xl/sharedStrings.xml"))
        for si in root.iter(NS + "si"):
            shared.append("".join(t.text or "" for t in si.iter(NS + "t")))

    wb = ET.fromstring(z.read("xl/workbook.xml"))
    sheets = [(s.get("name"), s.get(RNS + "id")) for s in wb.iter(NS + "sheet")]

    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    rel_map = {r.get("Id"): r.get("Target") for r in rels}

    sheet_files = {}
    for name, rid in sheets:
        target = rel_map[rid]
        if not target.startswith("xl/"):
            target = "xl/" + target
        sheet_files[name] = target

    return z, shared, sheet_files


def read_sheet(z, shared, path):
    root = ET.fromstring(z.read(path))
    rows_out = []
    for row in root.iter(NS + "row"):
        cells = {}
        maxcol = 0
        for c in row.iter(NS + "c"):
            ref = c.get("r")
            m = COL_RE.match(ref)
            col_letters = m.group(1)
            ci = col_to_idx(col_letters)
            maxcol = max(maxcol, ci)
            v = c.find(NS + "v")
            val = None if v is None else v.text
            if c.get("t") == "s" and val is not None:
                val = shared[int(val)]
            cells[ci] = val
        rowlist = [cells.get(i) for i in range(maxcol + 1)]
        rows_out.append(rowlist)
    return rows_out


def get_sheet_rows(xlsx_path, sheet_name):
    z, shared, sheet_files = load_workbook(xlsx_path)
    if sheet_name not in sheet_files:
        raise KeyError(f"Sheet {sheet_name!r} not found. Available: {list(sheet_files.keys())}")
    return read_sheet(z, shared, sheet_files[sheet_name])


def list_sheets(xlsx_path):
    _, _, sheet_files = load_workbook(xlsx_path)
    return list(sheet_files.keys())

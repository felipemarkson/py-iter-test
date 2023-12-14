import os
import sys
import shutil
from pathlib import Path

shutil.rmtree("results", ignore_errors=True)
TIMES = 1000


def run_test(result_name, value):
    os.makedirs(Path("results", result_name))
    path_for = Path("results", result_name, "for.csv")
    path_reduce = Path("results", result_name, "reduce.csv")
    path_lcomp = Path("results", result_name, "lcomp.csv")
    os.system(f"{sys.executable} pyitertst.py {value} {TIMES} for > {path_for}")
    os.system(f"{sys.executable} pyitertst.py {value} {TIMES} reduce > {path_reduce}")
    os.system(f"{sys.executable} pyitertst.py {value} {TIMES} lcomp > {path_lcomp}")


run_test("result_1e2", 100)
run_test("result_1e3", 1_000)
run_test("result_1e6", 1_000_000)
import sys
import iter_test as it


MODES = {
    "for": it.run_for,
    "reduce": it.run_reduce,
    "lcomp": it.run_list_comprehension
}

def print_usage():
    usage = """ pyitertst - Testing ways to iterate over a list
    pyitertst.py <size> <times> {for | reduce | lcomp}"""
    print(usage, file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print_usage()
        print("Three argument should be provided.", file=sys.stderr)
        exit(1)

    n_itens = 0
    n_times = 0

    try:
        n_itens = int(sys.argv[1])
        n_times = int(sys.argv[2])
    except ValueError:
        print_usage()
        print("The first two arguments must be an intergers", file=sys.stderr)
        exit(1)
    if n_itens < 1 or n_times < 1:
        print_usage()
        print("The first two arguments must be greater than zero", file=sys.stderr)
        exit(1)

    func = MODES["for"]
    try:
        func = MODES[sys.argv[3]]
    except KeyError:
        print_usage()
        print("Unknow mode", file=sys.stderr)
        exit(1)

    items = it.get_items(n_itens)
    it.warm_things(items)

    for _ in range(n_times):
        print(func(items))

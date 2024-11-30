import pandas as pd

def example_table():
    data = [
        ['a', 'A,C', '-',   'A', 'N',   '-'],
        ['b', 'B',   'A,B', 'N', 'B,C', '-'],
        ['c', '-',   'N',   'C', '-',   '-']
    ]
    columns = ['F', 'S', 'A', 'B', 'C', 'N']
    table = pd.DataFrame(data, columns=columns)
    return table
#Таблица
import pandas as pd
from tabulate import tabulate
#Латиница
from string import ascii_lowercase, ascii_uppercase
#Граф
import networkx as nx
import matplotlib.pyplot as plt
#Регулярки
import re

def generate_undetermined_grammar_sheet(nonterminals_count, terminals_count):
    #Первая строка - F, S, нетерминалы
    field_names = (
            ["F"] +
            ["S"] +
            [nonterminal for nonterminal in ascii_uppercase[:nonterminals_count] if nonterminal not in {"F", "S", "N"}]
    )
    table = pd.DataFrame(columns=field_names)

    #Первая колонка - терминалы, остальные ячейки - пустые строки
    for i in range(terminals_count):
        row = (
            [ascii_lowercase[i]] +
            ["" for _ in range(len(field_names) - 1)]
        )
        table.loc[i] = row

    #Вывод: незаполненная таблица
    print("Ваша незаполненная таблица:")
    print(format_table(table), end="\n\n")

    #Ручной ввод грамматики в таблицу
    for lin in range(terminals_count):
        for col in range(1, nonterminals_count + 2):
            table.iloc[lin, col] = "INPUT"
            print(format_table(table.iloc[[lin]]))

            user_input = input("Введите заместо 'INPUT': ")
            while not re.match(r"^[A-Z](,[A-Z])*$" , user_input):
                print("Неверный ввод!")
                user_input = input("Введите заместо 'INPUT': ")
            table.iloc[lin, col] = user_input

    #Добавим столбец N после ввода грамматики
    table["N"] = "-"
    return table

def put_undetermined_units(table=pd.DataFrame()):
    units = {} # Словарь неопределённостей: ключ - переменная, значение - неопределённости
    for lin in range(table.shape[0]):
        for col in range(1, table.shape[1]):
            str_cell = "".join(table.iloc[lin, col])
            if len(str_cell) > 1:
                table.iloc[lin, col] = (str(table.columns[col]) +
                                        str(table.iloc[lin, 0]) +
                                        "_" +
                                        table.iloc[lin, col]) # Заполняем ячейку переменной из неопределённостей
                units[table.iloc[lin, col]] = str_cell.split(",")
    return table, units

def create_and_add_helpers(table=pd.DataFrame(), units=dict):
    if units is None:
        units = {}

    for key in units.keys():
        table[key] = "-"

    for key, value in units.items():
        for i in range(len(units[key])):
            terminal = units[key][i]
            units[key][i] = terminal + "h"

            helper = units[key][i]
            if helper not in table.columns:
                table[helper] = "N"

            non_terminal = terminal.lower()
            table.loc[table['F'] == non_terminal, helper] = terminal
            table.loc[table['F'] == non_terminal, key] = helper

    table.pop("N")
    table["N"] = "-"

    return table, units

def draw_graph(table=pd.DataFrame()):
    #Создаём граф и заполняем его вершинами названий колонок (кроме "F")
    column_names_list = table.columns.to_list()[1:]
    grammar_graph = nx.DiGraph()
    grammar_graph.add_nodes_from(column_names_list)

    for i in range(table.shape[0]):
        for j in range(1, table.shape[1]):
            source = table.iloc[i, j]
            if source == "-":
                continue
            else:
                grammar_graph.add_edge(table.columns[j], table.iloc[i, j], type=table.iloc[i, 0])

    #Рисуем граф в MatPlotLib
    pos = nx.spring_layout(grammar_graph)
    nx.draw(grammar_graph,
            pos,
            with_labels=True,
            node_color='lightblue',
            node_size=1000,
            font_size=10)
    edge_labels = nx.get_edge_attributes(grammar_graph, 'type')
    nx.draw_networkx_edge_labels(grammar_graph, pos, edge_labels=edge_labels)
    plt.show()

def format_table(table):
    #Формирование любого вида таблицы (даже строки) с "шапкой"
    return tabulate(table, headers="keys", tablefmt="grid")

def format_dict(d):
    # Форматируем вывод
    formatted_output = []
    for key, values in d.items():
        formatted_output.append(f"{key} = ({', '.join(values)})")
    return "\n".join(formatted_output)

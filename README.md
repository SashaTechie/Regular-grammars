Grammar and Automata Project

This project involves working with grammars and automata, providing tools to manipulate context-free grammars, visualize grammar transformations, and perform grammar-based calculations. It includes functionality to create and manipulate grammar tables, generate undetermined grammar sheets, and visualize grammar transformations using graphs.

Project Overview

The main components of the project include:

GrammarRework.py: Contains functions for manipulating and working with grammars, including generating grammar tables, adding helper variables, and creating graph representations of grammars.
Example.py: Provides an example grammar table for demonstration purposes.
2.py: The main program file with an interactive menu that allows the user to either:
Perform a calculation with an example grammar (Option 1).
Input their own grammar and perform calculations (Option 2).
Requirements
The following libraries are required for the project:

pandas: For data handling and table creation.
matplotlib: For graph visualization.
networkx: For graph construction and manipulation.
tabulate: For pretty-printing tables.
To install the necessary dependencies, run:
pip install pandas matplotlib networkx tabulate

Features
Interactive Menu: Choose from different options in the menu to either:
Perform a calculation using an example grammar.
Input your own grammar and perform calculations.
Grammar Transformation: The program can generate and manipulate grammars, converting them into different forms and adding helper variables where necessary.
Graphical Representation: The grammar can be visualized as a directed graph using the networkx library.
How to Use
1. Run the Program
Execute the main script (2.py) to start the interactive menu. The program will prompt you with the following options:

Option 1: Perform a calculation with the example grammar.
Option 2: Input your own grammar for processing.
Option 3: Exit the program.

python 2.py

2. Input Grammar
If you choose Option 2, you will be prompted to input the number of non-terminals and terminals. Then, you will input the grammar in the specified format.

3. View Output
After performing the calculations, the program will display:

The grammar table (before and after transformation).
Variables with uncertainties.
A graph representing the grammar.

Functions
generate_undetermined_grammar_sheet(nonterminals_count, terminals_count)
Generates an empty grammar sheet with placeholders for user input.

put_undetermined_units(table)
Identifies and labels the undefined units in the grammar.

create_and_add_helpers(table, units)
Adds helper variables to the grammar and updates the table accordingly.

draw_graph(table)
Visualizes the grammar as a directed graph using networkx and matplotlib.

format_table(table)
Formats and prints a table in a readable format.

format_dict(d)
Formats and prints a dictionary of undefined units.

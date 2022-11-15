from rich.console import Console
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table

'''
* print_symbol_table()
| Display the symbol table in the terminal
| for presentation purposes.

* Parameters
| filename (str): The name of the program file
| symbol_table (dict): Contains tokens and its type.
'''
def print_symbol_table(filename: str, symbol_table: dict):
  # Print a header.
  console = Console()
  console.print()
  console.print(Panel.fit(
    Padding('''[white]
      📁  [bold yellow]Filename:[/] {0}
      💻  [bold blue]Number of Lines:[/] {1}
    '''.format(filename, len(symbol_table.keys())), (0, 6, 0, 0)),

    title='[bold]✅ Lexical Analyzer[/bold]', 
    subtitle='- = -', 
    style='green'
  ))

  # Create the table and its columns.
  table = Table(title="\nSymbol Table", header_style="bold yellow", border_style="bold yellow", title_style="bold italic yellow")
  table.add_column("Lexeme", justify="left", style="bold green", no_wrap=True)
  table.add_column("Type", justify="left", style="bold", no_wrap=True)

  # Create the table rows.
  for v in symbol_table.values():
    for i in range(len(v)):
      table.add_row(v[i][0], v[i][1])

  # Print the table.
  console.print(table, "\n")
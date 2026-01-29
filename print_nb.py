import json

with open(r'c:\Users\alstj\github\DataScience\scikit-learn-ex1.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        print(f"CELL {i} (EXEC {cell.get('execution_count')}):")
        print("".join(cell['source']))
        print("-" * 20)

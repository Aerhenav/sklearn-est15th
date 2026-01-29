import json

with open(r'c:\Users\alstj\github\DataScience\scikit-learn-ex1.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        for output in cell.get('outputs', []):
            if 'data' in output and 'text/html' in output['data']:
                html = "".join(output['data']['text/html'])
                if 'thead' in html:
                    print(f"HTML table found in cell {cell.get('execution_count')}")
                    # Extract column names from thead
                    import re
                    cols = re.findall(r'<th>(.*?)</th>', html)
                    print(f"Columns: {cols}")

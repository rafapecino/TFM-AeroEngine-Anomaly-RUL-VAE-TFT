import json
with open('Main.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)
with open('debug_data_extraction.py', 'w', encoding='utf-8') as f:
    for i in range(25, 34):
        c = nb['cells'][i]
        f.write(f'--- Cell {i} ({c["cell_type"]}) ---\n')
        f.write(''.join(c['source']) + '\n\n')

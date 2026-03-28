import json

known_nodes = {
    # Level 0
    "0": {"n": "Иванова (Ляпина) Полина Дмитриевна", "b": "20.05.1986", "d": "", "g": "F"},
    # Level 1
    "0_M": {"n": "Иванов Дмитрий Вадимович", "b": "18.09.1960", "d": "", "g": "M"},
    "0_F": {"n": "Чарная (Иванова) Елена Николаевна", "b": "15.01.1964", "d": "", "g": "F"},
    # Level 2
    "0_M_M": {"n": "Иванов Вадим Дмитриевич", "b": "16.10.1934", "d": "31.05.2019", "g": "M"},
    "0_M_F": {"n": "Новичкова (Иванова) Александра Ивановна", "b": "02.03.1933", "d": "", "g": "F"},
    "0_F_M": {"n": "Чарный Николай Михайлович", "b": "15.08.1927", "d": "25.01.1978", "g": "M"},
    "0_F_F": {"n": "Привалова (Чарная) Аполлинария Ивановна", "b": "02.06.1926", "d": "28.04.2009", "g": "F"},
    # Level 3
    "0_M_M_M": {"n": "Иванов Дмитрий Филиппович", "b": "15.09.1907", "d": "03.01.1996", "g": "M"},
    "0_M_M_F": {"n": "Уварова (Иванова) Ольга Павловна", "b": "", "d": "01.11.1939", "g": "F"},
    "0_M_F_M": {"n": "Новичков Иван Ефремович", "b": "06.06.1903", "d": "03.1980", "g": "M"},
    "0_M_F_F": {"n": "Крузе (Новичкова) Марта Ивановна", "b": "25.04.1905", "d": "17.04.1946", "g": "F"},
    "0_F_M_M": {"n": "Чарный Михаил Иосифович", "b": "1896", "d": "1979", "g": "M"},
    "0_F_M_F": {"n": "Карченя (Чарная) Наталья Степановна", "b": "1899", "d": "1969", "g": "F"},
    "0_F_F_M": {"n": "Привалов (урожд. Кукушкин) Иван Кириллович", "b": "29.05.1884", "d": "04.04.1949", "g": "M"},
    "0_F_F_F": {"n": "Афоничева (Привалова) Евдокия Николаевна", "b": "27.07.1891", "d": "04.01.1975", "g": "F"},
    # Level 4
    "0_M_M_M_M": {"n": "Иванов Филипп Михайлович", "b": "1874", "d": "02.1942", "g": "M"},
    "0_M_M_M_F": {"n": "Никифорова (Иванова) Агриппина Игнатьевна", "b": "1879", "d": "1910", "g": "F"},
    "0_M_M_F_M": {"n": "Уваров Павел", "b": "", "d": "1918", "g": "M"},
    "0_M_F_M_M": {"n": "Новичков Ефрем", "b": "", "d": "1905", "g": "M"},
    "0_M_F_M_F": {"n": "Неизвестна (Новичкова) Прасковья Георгиевна", "b": "24.07.1867", "d": "после 1930-х", "g": "F"},
    "0_M_F_F_M": {"n": "Круз Иоаннес Янович", "b": "30.01.1867", "d": "13.06.1900", "g": "M"},
    "0_M_F_F_F": {"n": "Парвиайнен (Крузе) Вильгельмина Андреевна", "b": "02.02.1864", "d": "02.04.1941", "g": "F"},
    "0_F_M_M_M": {"n": "Чарный Иосиф", "b": "", "d": "", "g": "M"},
    "0_F_M_F_M": {"n": "Карченя Степан", "b": "", "d": "", "g": "M"},
    "0_F_M_F_F": {"n": "Неизвестна (Карченя) Екатерина Ивановна", "b": "1878", "d": "1931", "g": "F"},
    "0_F_F_M_M": {"n": "Кукушкин Кирилл Егорович", "b": "1852", "d": "17.11.1911", "g": "M"},
    "0_F_F_M_F": {"n": "Неизвестна (Кукушкина) Анна Михайловна", "b": "1852", "d": "12.09.1891", "g": "F"},
    "0_F_F_F_M": {"n": "Афоничев Николай Иванович", "b": "1861", "d": "", "g": "M"},
    "0_F_F_F_F": {"n": "Неизвестна (Афоничева) Параскева Фёдоровна", "b": "10.10.1862", "d": "", "g": "F"},
    # Level 5
    "0_M_M_M_M_M": {"n": "Иванов Михаил", "b": "", "d": "", "g": "M"},
    "0_M_M_M_F_M": {"n": "Никифоров Игнат", "b": "", "d": "", "g": "M"},
    "0_M_F_M_F_M": {"n": "Георгий", "b": "", "d": "", "g": "M"},
    "0_M_F_F_M_M": {"n": "Круз Ян", "b": "", "d": "", "g": "M"},
    "0_M_F_F_F_M": {"n": "Парвиайнен Андрей", "b": "", "d": "", "g": "M"},
    "0_F_M_F_F_M": {"n": "Иван", "b": "", "d": "", "g": "M"},
    "0_F_F_M_M_M": {"n": "Кокушкин Егор Васильевич", "b": "1819", "d": "01.12.1889", "g": "M"},
    "0_F_F_M_F_M": {"n": "Михаил", "b": "", "d": "", "g": "M"},
    "0_F_F_F_M_M": {"n": "Афоничев Иван", "b": "", "d": "", "g": "M"},
    "0_F_F_F_F_M": {"n": "Фёдор Михайлович", "b": "1837", "d": "02.04.1900", "g": "M"},
    "0_F_F_F_F_F": {"n": "Феодосия Михайловна", "b": "1837", "d": "17.10.1909", "g": "F"},
    # Level 6
    "0_F_F_M_M_M_M": {"n": "Кокушкин Василий", "b": "", "d": "", "g": "M"},
    "0_F_F_F_F_M_M": {"n": "Михаил", "b": "", "d": "", "g": "M"},
    "0_F_F_F_F_F_M": {"n": "Михаил", "b": "", "d": "", "g": "M"}
}

MAX_DEPTH = 6

def build_tree(path):
    depth = path.count('_')
    
    if path in known_nodes:
        node_data = known_nodes[path]
        name = node_data['n']
        b = node_data['b']
        d = node_data['d']
        g = node_data['g']
        is_unknown = "Неизвестн" in name or name == ""
    else:
        g = 'M' if path.endswith('M') else 'F'
        name = "Неизвестен" if g == 'M' else "Неизвестна"
        b, d = "", ""
        is_unknown = True

    dates = []
    if b and not d: dates.append(f"род. {b}")
    elif not b and d: dates.append(f"ум. {d}")
    elif b and d: dates.append(f"{b} - {d}")
    
    date_str = f"<div class='dates'>{' '.join(dates)}</div>" if dates else ""
    
    classes = ["card"]
    if is_unknown:
        classes.append("unknown")
    
    html = f"<li><div class='{' '.join(classes)}'><div class='name'>{name}</div>{date_str}</div>"
    
    if depth < MAX_DEPTH:
        html += "<ul>"
        html += build_tree(path + "_M")
        html += build_tree(path + "_F")
        html += "</ul>"
        
    html += "</li>"
    return html

css_bw = """
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #fff;
    margin: 0;
    padding: 60px;
    width: max-content;
}
.tree {
    display: inline-block;
    text-align: center;
}
.tree ul {
    padding-top: 30px; 
    position: relative;
    display: flex;
    justify-content: center;
    padding-left: 0;
    margin: 0;
}
.tree li {
    float: left; text-align: center;
    list-style-type: none;
    position: relative;
    padding: 30px 4px 0 4px;
}
.tree li::before, .tree li::after {
    content: '';
    position: absolute; top: 0; right: 50%;
    border-top: 2px solid #333;
    width: 50%; height: 30px;
}
.tree li::after {
    right: auto; left: 50%;
    border-left: 2px solid #333;
}
.tree li:only-child::after, .tree li:only-child::before {
    display: none;
}
.tree li:only-child { padding-top: 0; }
.tree li:first-child::before, .tree li:last-child::after {
    border: 0 none;
}
.tree li:last-child::before {
    border-right: 2px solid #333;
    border-radius: 0 5px 0 0;
}
.tree li:first-child::after {
    border-radius: 5px 0 0 0;
}
.tree ul ul::before {
    content: '';
    position: absolute; top: 0; left: 50%;
    border-left: 2px solid #333;
    width: 0; height: 30px;
}
.card {
    border: 3px solid #000;
    padding: 10px;
    color: #000;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    background: #fff;
    width: 190px;
    height: 100px;
    box-sizing: border-box;
    box-shadow: 0 3px 6px rgba(0,0,0,0.15);
    margin: 0 auto;
}
.name {
    font-size: 15px;
    font-weight: bold;
    line-height: 1.25;
    margin-bottom: 5px;
}
.dates {
    font-size: 14px;
    color: #222;
}
.unknown {
    border-style: dashed;
    border-width: 2px;
    border-color: #777;
    color: #555;
    background: #fafafa;
}
"""

html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{css_bw}</style>
</head>
<body>
<div class="tree">
    <ul>
        {build_tree("0")}
    </ul>
</div>
</body>
</html>
"""

with open('/root/.openclaw/workspace/tree_v4_bw.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("V4 Full Symmetry HTML generated.")

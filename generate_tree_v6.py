import json

known_nodes = {
    # Level 0
    "0": {"n": "Иванова (Ляпина) Полина Дмитриевна", "b": "20.05.1986", "loc": ""},
    # Level 1
    "0_M": {"n": "Иванов Дмитрий Вадимович", "b": "18.09.1960", "loc": "Родился: Петербург"},
    "0_F": {"n": "Чарная (Иванова) Елена Николаевна", "b": "15.01.1964", "loc": "Родилась: Красная Слобода (Беларусь)<br>Переехала: Петербург"},
    # Level 2
    "0_M_M": {"n": "Иванов Вадим Дмитриевич", "b": "16.10.1934 – 31.05.2019", "loc": "Родился: Петербург"},
    "0_M_F": {"n": "Новичкова (Иванова) Александра Ивановна", "b": "02.03.1933", "loc": "Родилась: Петербург"},
    "0_F_M": {"n": "Чарный Николай Михайлович", "b": "15.08.1927 – 25.01.1978", "loc": "Родился: Красная Слобода (Беларусь)"},
    "0_F_F": {"n": "Привалова (Чарная) Аполлинария Ивановна", "b": "02.06.1926 – 28.04.2009", "loc": "Родилась: Кузьминка (Вологодская обл.)<br>Переехала: Красная Слобода"},
    # Level 3
    "0_M_M_M": {"n": "Иванов Дмитрий Филиппович", "b": "15.09.1907 – 03.01.1996", "loc": "Родился: Петербург"},
    "0_M_M_F": {"n": "Уварова (Иванова) Ольга Павловна", "b": "ум. 01.11.1939", "loc": "Родилась: Самара (Урал??)<br>Переехала: Петербург"},
    "0_M_F_M": {"n": "Новичков Иван Ефремович", "b": "06.06.1903 – 03.1980", "loc": "Родился: Темрюк<br>Переехал: Петербург"},
    "0_M_F_F": {"n": "Крузе (Новичкова) Марта Ивановна", "b": "25.04.1905 – 17.04.1946", "loc": "Родилась: Петербург"},
    "0_F_M_M": {"n": "Чарный Михаил Иосифович", "b": "1896 – 1979", "loc": "Родился: Красная Слобода"},
    "0_F_M_F": {"n": "Карченя (Чарная) Наталья Степановна", "b": "1899 – 1969", "loc": "Родилась: Красная Слобода"},
    "0_F_F_M": {"n": "Кукушкин (Привалов) Иван Кириллович", "b": "29.05.1884 – 04.04.1949", "loc": "Родился: Кузьминка"},
    "0_F_F_F": {"n": "Афоничева (Привалова) Евдокия Николаевна", "b": "27.07.1891 – 04.01.1975", "loc": "Родилась: Кузьминка"},
    # Level 4
    "0_M_M_M_M": {"n": "Иванов Филипп Михайлович", "b": "1874 – 02.1942", "loc": "Родился: Невель<br>Переехал: Петербург"},
    "0_M_M_M_F": {"n": "Никифорова (Иванова) Агриппина Игнатьевна", "b": "1879 – 1910", "loc": "Родилась: Невель<br>Переехала: Петербург"},
    "0_M_M_F_M": {"n": "Уваров Павел", "b": "ум. 1918", "loc": "Родился: Самара (Урал??)"},
    "0_M_F_M_M": {"n": "Новичков Ефрем", "b": "ум. 1905", "loc": "Родился: Темрюк"},
    "0_M_F_M_F": {"n": "Неизвестна (Новичкова) Прасковья Георгиевна", "b": "24.07.1867", "loc": "Родилась: Темрюк"},
    "0_M_F_F_M": {"n": "Круз Иоаннес Янович", "b": "30.01.1867 – 13.06.1900", "loc": "Родился: Эстония<br>Переехал: Петербург"},
    "0_M_F_F_F": {"n": "Парвиайнен (Крузе) Вильгельмина Андреевна", "b": "02.02.1864 – 02.04.1941", "loc": "Родилась: Петербург"},
    "0_F_M_M_M": {"n": "Чарный Иосиф", "b": "", "loc": "Родился: Брестская обл.<br>Переехал: Красная Слобода"},
    "0_F_M_F_M": {"n": "Карченя Степан", "b": "", "loc": "Родился: Красная Слобода"},
    "0_F_M_F_F": {"n": "Неизвестна (Карченя) Екатерина Ивановна", "b": "1878 – 1931", "loc": "Родилась: Красная Слобода"},
    "0_F_F_M_M": {"n": "Кукушкин Кирилл Егорович", "b": "1852 – 17.11.1911", "loc": "Родился: Кузьминка"},
    "0_F_F_M_F": {"n": "Неизвестна (Кукушкина) Анна Михайловна", "b": "1852 – 12.09.1891", "loc": "Родилась: Кузьминка"},
    "0_F_F_F_M": {"n": "Афоничев Николай Иванович", "b": "1861", "loc": "Родился: Кузьминка"},
    "0_F_F_F_F": {"n": "Неизвестна (Афоничева) Параскева Фёдоровна", "b": "10.10.1862", "loc": "Родилась: Кузьминка"},
    # Level 5
    "0_M_M_M_M_M": {"n": "Иванов Михаил", "b": "", "loc": ""},
    "0_M_M_M_F_M": {"n": "Никифоров Игнат", "b": "", "loc": ""},
    "0_M_F_M_F_M": {"n": "Георгий", "b": "", "loc": ""},
    "0_M_F_F_M_M": {"n": "Круз Ян", "b": "", "loc": ""},
    "0_M_F_F_F_M": {"n": "Парвиайнен Андрей", "b": "", "loc": ""},
    "0_F_M_F_F_M": {"n": "Иван", "b": "", "loc": ""},
    "0_F_F_M_M_M": {"n": "Кокушкин Егор Васильевич", "b": "1819 – 01.12.1889", "loc": "Родился: Кузьминка"},
    "0_F_F_M_F_M": {"n": "Михаил", "b": "", "loc": ""},
    "0_F_F_F_M_M": {"n": "Афоничев Иван", "b": "", "loc": ""},
    "0_F_F_F_F_M": {"n": "Фёдор Михайлович", "b": "1837 – 02.04.1900", "loc": "Родился: Кузьминка"},
    "0_F_F_F_F_F": {"n": "Феодосия Михайловна", "b": "1837 – 17.10.1909", "loc": "Родилась: Кузьминка"},
    # Level 6
    "0_F_F_M_M_M_M": {"n": "Кокушкин Василий", "b": "", "loc": ""},
    "0_F_F_F_F_M_M": {"n": "Михаил", "b": "", "loc": ""},
    "0_F_F_F_F_F_M": {"n": "Михаил", "b": "", "loc": ""}
}

MAX_DEPTH = 6

def build_tree(path):
    depth = path.count('_')
    
    if path in known_nodes:
        node_data = known_nodes[path]
        name = node_data['n']
        b = node_data['b']
        loc = node_data.get('loc', '')
        is_unknown = "Неизвестн" in name or name == ""
    else:
        g = 'M' if path.endswith('M') else 'F'
        name = "Неизвестен" if g == 'M' else "Неизвестна"
        b, loc = "", ""
        is_unknown = True

    date_str = f"<div class='dates'>{b}</div>" if b else ""
    loc_str = f"<div class='loc'>{loc}</div>" if loc else ""
    
    classes = ["card"]
    if is_unknown:
        classes.append("unknown")
    
    html = f"<li><div class='{' '.join(classes)}'><div class='photo'></div><div class='name'>{name}</div>{date_str}{loc_str}</div>"
    
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
    background: #ffffff;
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
    border-top: 2px solid #000;
    width: 50%; height: 30px;
}
.tree li::after {
    right: auto; left: 50%;
    border-left: 2px solid #000;
}
.tree li:only-child::after, .tree li:only-child::before {
    display: none;
}
.tree li:only-child { padding-top: 0; }
.tree li:first-child::before, .tree li:last-child::after {
    border: 0 none;
}
.tree li:last-child::before {
    border-right: 2px solid #000;
    border-radius: 0 5px 0 0;
}
.tree li:first-child::after {
    border-radius: 5px 0 0 0;
}
.tree ul ul::before {
    content: '';
    position: absolute; top: 0; left: 50%;
    border-left: 2px solid #000;
    width: 0; height: 30px;
}
.card {
    border: 2px solid #000;
    padding: 10px 8px;
    color: #000;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    border-radius: 10px;
    background: #fff;
    width: 175px;
    min-height: 200px;
    box-sizing: border-box;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin: 0 auto;
}
.photo {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    border: 2px solid #ddd;
    margin-bottom: 8px;
    background: #fafafa;
    flex-shrink: 0;
}
.name {
    font-size: 15px;
    font-weight: bold;
    line-height: 1.25;
    margin-bottom: 6px;
}
.dates {
    font-size: 14px;
    font-weight: bold;
    color: #222;
    margin-bottom: 4px;
}
.loc {
    font-size: 12px;
    color: #333;
    line-height: 1.3;
    margin-top: 4px;
}
.unknown {
    border-style: dashed;
    border-color: #888;
    color: #555;
    background: #fdfdfd;
}
.unknown .name { font-weight: normal; }
.unknown .photo { border: none; background: transparent; height: 5px; margin-bottom: 0;}
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

with open('/root/.openclaw/workspace/family_tree_final.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("V6 Final HTML generated.")

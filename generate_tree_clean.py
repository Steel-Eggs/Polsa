import json

data = {
    "name": "Я:<br>Полина Дмитриевна<br>Иванова (Ляпина)<br><b>20.05.1986</b>",
    "children": [
        {
            "name": "Отец:<br>Дмитрий Вадимович<br>Иванов<br><b>18.09.1960</b>",
            "children": [
                {
                    "name": "Дед:<br>Вадим Дмитриевич<br>Иванов<br><b>16.10.1934 – 31.05.2019</b>",
                    "children": [
                        {
                            "name": "Прадед:<br>Дмитрий Филиппович<br>Иванов<br><b>15.09.1907 – 03.01.1996</b>",
                            "children": [
                                {"name": "Прапрадед:<br>Филипп Михайлович<br>Иванов<br><b>1874 – 02.1942</b>"},
                                {"name": "Прапрабабушка:<br>Агриппина Игнатьевна<br>Никифорова<br><b>1879 – 1910</b>"}
                            ]
                        },
                        {
                            "name": "Прабабушка:<br>Ольга Павловна<br>Уварова<br><b>? – 01.11.1939</b>",
                            "children": [
                                {"name": "Прапрадед:<br>Павел Уваров<br><b>ум. 1918</b>"}
                            ]
                        }
                    ]
                },
                {
                    "name": "Бабушка:<br>Александра Ивановна<br>Новичкова (Иванова)<br><b>02.03.1933</b>",
                    "children": [
                        {
                            "name": "Прадед:<br>Иван Ефремович<br>Новичков<br><b>06.06.1903 – 03.1980</b>",
                            "children": [
                                {"name": "Прапрадед:<br>Ефрем Новичков<br><b>ум. 1905</b>"},
                                {"name": "Прапрабабушка:<br>Прасковья Георгиевна<br>Новичкова<br><b>24.07.1867 – после 1930-х</b>"}
                            ]
                        },
                        {
                            "name": "Прабабушка:<br>Марта Ивановна<br>Крузе (Новичкова)<br><b>25.04.1905 – 17.04.1946</b>",
                            "children": [
                                {"name": "Прапрадед (отчим):<br>Иоаннес Янович<br>Круз<br><b>30.01.1867 – 13.06.1900</b>"},
                                {"name": "Прапрабабушка:<br>Вильгельмина Андреевна<br>Парвиайнен (Крузе)<br><b>02.02.1864 – 02.04.1941</b>"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Мать:<br>Елена Николаевна<br>Чарная<br><b>15.01.1964</b>",
            "children": [
                {
                    "name": "Дед:<br>Николай Михайлович<br>Чарный<br><b>15.08.1927 – 25.01.1978</b>",
                    "children": [
                        {
                            "name": "Прадед:<br>Михаил Иосифович<br>Чарный<br><b>1896 – 1979</b>",
                            "children": [
                                {"name": "Прапрадед:<br>Иосиф Чарный"}
                            ]
                        },
                        {
                            "name": "Прабабушка:<br>Наталья Степановна<br>Карченя (Чарная)<br><b>1899 – 1969</b>",
                            "children": [
                                {"name": "Прапрадед:<br>Степан Карченя"},
                                {"name": "Прапрабабушка:<br>Екатерина Ивановна<br>Карченя<br><b>1878 – 1931</b>"}
                            ]
                        }
                    ]
                },
                {
                    "name": "Бабушка:<br>Аполлинария Ивановна<br>Привалова (Чарная)<br><b>02.06.1926 – 28.04.2009</b>",
                    "children": [
                        {
                            "name": "Прадед:<br>Иван Кириллович<br>Привалов (Кукушкин)<br><b>29.05.1884 – 04.04.1949</b>",
                            "children": [
                                {
                                    "name": "Прапрадед:<br>Кирилл Егорович<br>Кукушкин<br><b>1852 – 17.11.1911</b>",
                                    "children": [
                                        {"name": "Прапрапрадед:<br>Егор Васильевич<br>Кокушкин<br><b>1819 – 01.12.1889</b>"}
                                    ]
                                },
                                {"name": "Прапрабабушка:<br>Анна Михайловна<br>Кукушкина<br><b>1852 – 12.09.1891</b>"}
                            ]
                        },
                        {
                            "name": "Прабабушка:<br>Евдокия Николаевна<br>Афоничева (Привалова)<br><b>27.07.1891 – 04.01.1975</b>",
                            "children": [
                                {"name": "Прапрадед:<br>Николай Иванович<br>Афоничев<br><b>1861 – ?</b>"},
                                {
                                    "name": "Прапрабабушка:<br>Параскева Фёдоровна<br>Афоничева<br><b>10.10.1862 – ?</b>",
                                    "children": [
                                        {"name": "Прапрапрадед:<br>Фёдор Михайлович<br><b>1837 – 02.04.1900</b>"},
                                        {"name": "Прапрапрабабушка:<br>Феодосия Михайловна<br><b>1837 – 17.10.1909</b>"}
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

def build_html(node):
    html = f"<li><a href='#'>{node['name']}</a>"
    if "children" in node and node["children"]:
        html += "<ul>"
        for child in node["children"]:
            html += build_html(child)
        html += "</ul>"
    html += "</li>"
    return html

html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #f4f4f9;
    padding: 20px;
    margin: 0;
}}
.tree {{
    display: inline-block;
    min-width: 100%;
    text-align: center;
}}
.tree ul {{
    padding-top: 20px; position: relative;
    display: flex;
    justify-content: center;
    padding-left: 0;
}}
.tree li {{
    float: left; text-align: center;
    list-style-type: none;
    position: relative;
    padding: 20px 4px 0 4px;
}}
.tree li::before, .tree li::after{{
    content: '';
    position: absolute; top: 0; right: 50%;
    border-top: 2px solid #555;
    width: 50%; height: 20px;
}}
.tree li::after{{
    right: auto; left: 50%;
    border-left: 2px solid #555;
}}
.tree li:only-child::after, .tree li:only-child::before {{
    display: none;
}}
.tree li:only-child{{ padding-top: 0; }}
.tree li:first-child::before, .tree li:last-child::after{{
    border: 0 none;
}}
.tree li:last-child::before{{
    border-right: 2px solid #555;
    border-radius: 0 5px 0 0;
}}
.tree li:first-child::after{{
    border-radius: 5px 0 0 0;
}}
.tree ul ul::before{{
    content: '';
    position: absolute; top: 0; left: 50%;
    border-left: 2px solid #555;
    width: 0; height: 20px;
}}
.tree li a {{
    border: 2px solid #555;
    padding: 8px;
    text-decoration: none;
    color: #222;
    font-size: 13px;
    display: inline-block;
    border-radius: 6px;
    background: #fff;
    width: 170px;
    line-height: 1.3;
    white-space: normal;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}}
.tree > ul > li > a {{
    background: #d0ebff;
    border-color: #0077cc;
    font-size: 15px;
    font-weight: bold;
    width: 200px;
}}
.tree ul ul > li > a {{
    background: #e8f5e9;
    border-color: #2e7d32;
}}
.tree ul ul ul > li > a {{
    background: #fff3e0;
    border-color: #f57c00;
}}
.tree ul ul ul ul > li > a {{
    background: #fce4ec;
    border-color: #d84315;
}}
.tree ul ul ul ul ul > li > a {{
    background: #f3e5f5;
    border-color: #ad1457;
}}
</style>
</head>
<body>
<div style="text-align:center; margin-bottom: 20px;">
    <h2 style="color:#333; margin:0;">Семейное древо</h2>
</div>
<div class="tree" id="tree-container">
    <ul>
        {build_html(data)}
    </ul>
</div>
</body>
</html>
"""

with open('/root/.openclaw/workspace/family_tree_clean.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML clean generated.")

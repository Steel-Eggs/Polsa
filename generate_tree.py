import json

data = {
    "name": "Полина Дмитриевна<br>Иванова (Ляпина)<br><b>20.05.1986</b>",
    "children": [
        {
            "name": "Отец:<br>Иванов Дмитрий Вадимович<br><b>18.09.1960</b><br>Петербург",
            "children": [
                {
                    "name": "Дед:<br>Иванов Вадим Дмитриевич<br><b>16.10.1934 – 31.05.2019</b><br>Петербург",
                    "children": [
                        {
                            "name": "Прадед:<br>Иванов Дмитрий Филиппович<br><b>15.09.1907 – 03.01.1996</b><br>Петербург",
                            "children": [
                                {"name": "Прапрадед:<br>Иванов Филипп Михайлович<br><b>1874 – 02.1942</b><br>Невель → Петербург"},
                                {"name": "Прапрабабушка:<br>Никифорова Агриппина Игнатьевна<br><b>1879 – 1910</b><br>Невель → Петербург"}
                            ]
                        },
                        {
                            "name": "Прабабушка:<br>Уварова Ольга Павловна<br><b>? – 01.11.1939</b><br>Самара? → Петербург",
                            "children": [
                                {"name": "Прапрадед:<br>Уваров Павел<br><b>ум. 1918</b><br>Самара?"}
                            ]
                        }
                    ]
                },
                {
                    "name": "Бабушка:<br>Новичкова (Иванова) Александра Ивановна<br><b>02.03.1933</b><br>Петербург",
                    "children": [
                        {
                            "name": "Прадед:<br>Новичков Иван Ефремович<br><b>06.06.1903 – 03.1980</b><br>Темрюк → Тифлис → Батум → Питер",
                            "children": [
                                {"name": "Прапрадед:<br>Новичков Ефрем<br><b>ум. 1905</b><br>Темрюк. Погиб при восстании."},
                                {"name": "Прапрабабушка:<br>Новичкова Прасковья Георгиевна<br><b>24.07.1867 – после 1930-х</b><br>Темрюк → Тифлис → Батум"}
                            ]
                        },
                        {
                            "name": "Прабабушка:<br>Крузе (Новичкова) Марта Ивановна<br><b>25.04.1905 – 17.04.1946</b><br>Петербург",
                            "children": [
                                {"name": "Прапрадед (отчим):<br>Круз Иоаннес Янович<br><b>30.01.1867 – 13.06.1900</b><br>Эстония → Петербург"},
                                {"name": "Прапрабабушка:<br>Парвиайнен (Крузе) Вильгельмина Андреевна<br><b>02.02.1864 – 02.04.1941</b><br>Петербург"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Мать:<br>Чарная Елена Николаевна<br><b>15.01.1964</b><br>Красная Слобода → Петербург",
            "children": [
                {
                    "name": "Дед:<br>Чарный Николай Михайлович<br><b>15.08.1927 – 25.01.1978</b><br>Красная Слобода",
                    "children": [
                        {
                            "name": "Прадед:<br>Чарный Михаил Иосифович<br><b>1896 – 1979</b><br>Красная Слобода",
                            "children": [
                                {"name": "Прапрадед:<br>Чарный Иосиф<br>Брестская обл. → Красная Слобода"}
                            ]
                        },
                        {
                            "name": "Прабабушка:<br>Карченя (Чарная) Наталья Степановна<br><b>1899 – 1969</b><br>Красная Слобода",
                            "children": [
                                {"name": "Прапрадед:<br>Карченя Степан<br>Красная Слобода"},
                                {"name": "Прапрабабушка:<br>Карченя Екатерина Ивановна<br><b>1878 – 1931</b><br>Красная Слобода"}
                            ]
                        }
                    ]
                },
                {
                    "name": "Бабушка:<br>Привалова (Чарная) Аполлинария Ивановна<br><b>02.06.1926 – 28.04.2009</b><br>Кузьминка → Красная Слобода",
                    "children": [
                        {
                            "name": "Прадед:<br>Привалов (Кукушкин) Иван Кириллович<br><b>29.05.1884 – 04.04.1949</b><br>Кузьминка",
                            "children": [
                                {
                                    "name": "Прапрадед:<br>Кукушкин Кирилл Егорович<br><b>1852 – 17.11.1911</b><br>Кузьминка",
                                    "children": [
                                        {"name": "Прапрапрадед:<br>Кокушкин Егор Васильевич<br><b>1819 – 01.12.1889</b><br>Кузьминка"}
                                    ]
                                },
                                {"name": "Прапрабабушка:<br>Кукушкина Анна Михайловна<br><b>1852 – 12.09.1891</b><br>Кузьминка"}
                            ]
                        },
                        {
                            "name": "Прабабушка:<br>Афоничева (Привалова) Евдокия Николаевна<br><b>27.07.1891 – 04.01.1975</b><br>Кузьминка",
                            "children": [
                                {"name": "Прапрадед:<br>Афоничев Николай Иванович<br><b>1861 – ?</b><br>Кузьминка"},
                                {
                                    "name": "Прапрабабушка:<br>Афоничева Параскева Фёдоровна<br><b>10.10.1862 – ?</b><br>Кузьминка",
                                    "children": [
                                        {"name": "Прапрапрадед:<br>Фёдор Михайлович<br><b>1837 – 02.04.1900</b><br>Кузьминка"},
                                        {"name": "Прапрапрабабушка:<br>Феодосия Михайловна<br><b>1837 – 17.10.1909</b><br>Кузьминка"}
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
    padding: 50px;
    margin: 0;
}}
.tree {{
    display: inline-block;
    min-width: 100%;
    text-align: center;
}}
.tree ul {{
    padding-top: 20px; position: relative;
    transition: all 0.5s;
    -webkit-transition: all 0.5s;
    -moz-transition: all 0.5s;
    display: flex;
    justify-content: center;
    padding-left: 0;
}}
.tree li {{
    float: left; text-align: center;
    list-style-type: none;
    position: relative;
    padding: 20px 5px 0 5px;
    transition: all 0.5s;
    -webkit-transition: all 0.5s;
    -moz-transition: all 0.5s;
}}
.tree li::before, .tree li::after{{
    content: '';
    position: absolute; top: 0; right: 50%;
    border-top: 2px solid #999;
    width: 50%; height: 20px;
}}
.tree li::after{{
    right: auto; left: 50%;
    border-left: 2px solid #999;
}}
.tree li:only-child::after, .tree li:only-child::before {{
    display: none;
}}
.tree li:only-child{{ padding-top: 0; }}
.tree li:first-child::before, .tree li:last-child::after{{
    border: 0 none;
}}
.tree li:last-child::before{{
    border-right: 2px solid #999;
    border-radius: 0 5px 0 0;
}}
.tree li:first-child::after{{
    border-radius: 5px 0 0 0;
}}
.tree ul ul::before{{
    content: '';
    position: absolute; top: 0; left: 50%;
    border-left: 2px solid #999;
    width: 0; height: 20px;
}}
.tree li a {{
    border: 2px solid #999;
    padding: 10px;
    text-decoration: none;
    color: #333;
    font-size: 14px;
    display: inline-block;
    border-radius: 8px;
    background: #fff;
    width: 200px;
    line-height: 1.4;
    white-space: normal;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}}
.tree li a:hover {{
    background: #e8f4f8;
    color: #000;
    border: 2px solid #66a3ff;
}}
.tree > ul > li > a {{
    background: #e6f7ff;
    border-color: #0099ff;
    font-size: 16px;
}}
</style>
</head>
<body>
<div style="text-align:center; margin-bottom: 30px;">
    <h2>Родословное древо: Иванова (Ляпина) Полина</h2>
</div>
<div class="tree" id="tree-container">
    <ul>
        {build_html(data)}
    </ul>
</div>
</body>
</html>
"""

with open('/root/.openclaw/workspace/family_tree.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML generated.")

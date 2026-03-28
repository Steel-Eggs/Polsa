import json

def node(name, gender, birth="", death="", f=None, m=None):
    return {
        "name": name,
        "gender": gender,
        "birth": birth,
        "death": death,
        "f": f,
        "m": m
    }

# L6
vasily_k = node("Василий Кокушкин", "M")
mikhail_f = node("Михаил", "M")
mikhail_feo = node("Михаил", "M")

# L5
mikhail_iv = node("Михаил Иванов", "M")
ignat_nik = node("Игнат Никифоров", "M")
uvarov_unknown = node("Неизвестен (Уваров)", "M")
novichkov_unknown = node("Неизвестен (Новичков)", "M")
georgy = node("Георгий", "M")
yan_kruz = node("Ян Круз", "M")
andrey_parv = node("Андрей Парвиайнен", "M")
charny_unknown = node("Неизвестен (Чарный)", "M")
karchenya_unknown = node("Неизвестен (Карченя)", "M")
ivan_kar = node("Иван", "M")
egor_kokushkin = node("Егор Васильевич Кокушкин", "M", "1819", "01.12.1889", f=vasily_k, m=node("Неизвестна", "F"))
mikhail_kuk = node("Михаил", "M")
ivan_afon = node("Иван Афоничев", "M")
fedor_m = node("Фёдор Михайлович", "M", "1837", "02.04.1900", f=mikhail_f, m=node("Неизвестна", "F"))
feodosia_m = node("Феодосия Михайловна", "F", "1837", "17.10.1909", f=mikhail_feo, m=node("Неизвестна", "F"))

# L4
filipp_iv = node("Филипп Михайлович Иванов", "M", "1874", "02.1942", f=mikhail_iv, m=node("Неизвестна", "F"))
agrippina_nik = node("Агриппина Игнатьевна Никифорова", "F", "1879", "1910", f=ignat_nik, m=node("Неизвестна", "F"))
pavel_uvarov = node("Павел Уваров", "M", "", "1918", f=uvarov_unknown, m=node("Неизвестна", "F"))
efrem_nov = node("Ефрем Новичков", "M", "", "1905", f=novichkov_unknown, m=node("Неизвестна", "F"))
praskovya_nov = node("Прасковья Георгиевна Новичкова", "F", "24.07.1867", "после 1930-х", f=georgy, m=node("Неизвестна", "F"))
ioannes_kruz = node("Иоаннес Янович Круз", "M", "30.01.1867", "13.06.1900", f=yan_kruz, m=node("Неизвестна", "F"))
vilgelmina_parv = node("Вильгельмина Андреевна Парвиайнен", "F", "02.02.1864", "02.04.1941", f=andrey_parv, m=node("Неизвестна", "F"))
iosif_charny = node("Иосиф Чарный", "M", f=charny_unknown, m=node("Неизвестна", "F"))
stepan_kar = node("Степан Карченя", "M", f=karchenya_unknown, m=node("Неизвестна", "F"))
ekaterina_kar = node("Екатерина Ивановна Карченя", "F", "1878", "1931", f=ivan_kar, m=node("Неизвестна", "F"))
kirill_kuk = node("Кирилл Егорович Кукушкин", "M", "1852", "17.11.1911", f=egor_kokushkin, m=node("Неизвестна", "F"))
anna_kuk = node("Анна Михайловна Кукушкина", "F", "1852", "12.09.1891", f=mikhail_kuk, m=node("Неизвестна", "F"))
nikolay_afon = node("Николай Иванович Афоничев", "M", "1861", "", f=ivan_afon, m=node("Неизвестна", "F"))
paraskeva_afon = node("Параскева Фёдоровна Афоничева", "F", "10.10.1862", "", f=fedor_m, m=feodosia_m)

# L3
dmitry_f_iv = node("Дмитрий Филиппович Иванов", "M", "15.09.1907", "03.01.1996", f=filipp_iv, m=agrippina_nik)
olga_uvarova = node("Ольга Павловна Уварова", "F", "", "01.11.1939", f=pavel_uvarov, m=node("Неизвестна", "F"))
ivan_e_nov = node("Иван Ефремович Новичков", "M", "06.06.1903", "03.1980", f=efrem_nov, m=praskovya_nov)
marta_kruze = node("Марта Ивановна Крузе", "F", "25.04.1905", "17.04.1946", f=ioannes_kruz, m=vilgelmina_parv)
mikhail_charny = node("Михаил Иосифович Чарный", "M", "1896", "1979", f=iosif_charny, m=node("Неизвестна", "F"))
natalya_kar = node("Наталья Степановна Карченя", "F", "1899", "1969", f=stepan_kar, m=ekaterina_kar)
ivan_privalov = node("Иван Кириллович Привалов (Кукушкин)", "M", "29.05.1884", "04.04.1949", f=kirill_kuk, m=anna_kuk)
evdokia_afon = node("Евдокия Николаевна Афоничева", "F", "27.07.1891", "04.01.1975", f=nikolay_afon, m=paraskeva_afon)

# L2
vadim_iv = node("Вадим Дмитриевич Иванов", "M", "16.10.1934", "31.05.2019", f=dmitry_f_iv, m=olga_uvarova)
aleksandra_nov = node("Александра Ивановна Новичкова", "F", "02.03.1933", "", f=ivan_e_nov, m=marta_kruze)
nikolay_charny = node("Николай Михайлович Чарный", "M", "15.08.1927", "25.01.1978", f=mikhail_charny, m=natalya_kar)
apollinaria_priv = node("Аполлинария Ивановна Привалова", "F", "02.06.1926", "28.04.2009", f=ivan_privalov, m=evdokia_afon)

# L1
dmitry_iv = node("Дмитрий Вадимович Иванов", "M", "18.09.1960", "", f=vadim_iv, m=aleksandra_nov)
elena_charnaya = node("Елена Николаевна Чарная", "F", "15.01.1964", "", f=nikolay_charny, m=apollinaria_priv)

# L0
polina = node("Полина Дмитриевна Иванова (Ляпина)", "F", "20.05.1986", "", f=dmitry_iv, m=elena_charnaya)

def build_html_tree(n, color_mode="bw"):
    dates = []
    if n["birth"] or n["death"]:
        b = n["birth"] if n["birth"] else "?"
        d = n["death"] if n["death"] else "?"
        if n["birth"] and not n["death"]:
            dates.append(f"род. {n['birth']}")
        elif not n["birth"] and n["death"]:
            dates.append(f"ум. {n['death']}")
        else:
            dates.append(f"{b} - {d}")
            
    date_str = f"<br><span class='dates'>{' '.join(dates)}</span>" if dates else ""
    
    classes = ["card"]
    if color_mode == "color":
        if n["gender"] == "M":
            classes.append("male")
        elif n["gender"] == "F":
            classes.append("female")
            
    if "Неизвест" in n["name"]:
        classes.append("unknown")
        
    html = f"<li><a href='#' class='{' '.join(classes)}'><div class='name'>{n['name']}</div>{date_str}</a>"
    
    if n["f"] or n["m"]:
        html += "<ul>"
        if n["f"]:
            html += build_html_tree(n["f"], color_mode)
        if n["m"]:
            html += build_html_tree(n["m"], color_mode)
        html += "</ul>"
        
    html += "</li>"
    return html

css = """
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #fff;
    margin: 0;
    padding: 40px;
}
.tree {
    display: flex;
    justify-content: center;
    width: max-content;
    margin: 0 auto;
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
    padding: 30px 10px 0 10px;
}
.tree li::before, .tree li::after {
    content: '';
    position: absolute; top: 0; right: 50%;
    border-top: 2px solid #555;
    width: 50%; height: 30px;
}
.tree li::after {
    right: auto; left: 50%;
    border-left: 2px solid #555;
}
.tree li:only-child::after, .tree li:only-child::before {
    display: none;
}
.tree li:only-child { padding-top: 0; }
.tree li:first-child::before, .tree li:last-child::after {
    border: 0 none;
}
.tree li:last-child::before {
    border-right: 2px solid #555;
    border-radius: 0 5px 0 0;
}
.tree li:first-child::after {
    border-radius: 5px 0 0 0;
}
.tree ul ul::before {
    content: '';
    position: absolute; top: 0; left: 50%;
    border-left: 2px solid #555;
    width: 0; height: 30px;
}
.card {
    border: 2px solid #555;
    padding: 10px;
    text-decoration: none;
    color: #000;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    background: #fff;
    width: 140px;
    height: 70px;
    box-sizing: border-box;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.name {
    font-size: 13px;
    font-weight: 600;
    line-height: 1.2;
    margin-bottom: 4px;
}
.dates {
    font-size: 11px;
    color: #444;
}
.unknown {
    border-style: dashed;
    color: #666;
    background: #fafafa;
}

/* Color mode classes */
.card.male {
    background-color: #e3f2fd;
    border-color: #1e88e5;
}
.card.female {
    background-color: #fce4ec;
    border-color: #e91e63;
}
.unknown.male {
    background-color: #f0f8ff;
    border-color: #90caf9;
    border-style: dashed;
}
.unknown.female {
    background-color: #fdf5f6;
    border-color: #f48fb1;
    border-style: dashed;
}
"""

def generate_html(filename, color_mode):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>{css}</style>
    </head>
    <body>
    <div class="tree">
        <ul>
            {build_html_tree(polina, color_mode)}
        </ul>
    </div>
    </body>
    </html>
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

generate_html('/root/.openclaw/workspace/tree_bw.html', 'bw')
generate_html('/root/.openclaw/workspace/tree_color.html', 'color')
print("HTMLs generated.")

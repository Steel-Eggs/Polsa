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

def unk_m(): return node("Неизвестен", "M")
def unk_f(): return node("Неизвестна", "F")

# L6 (Parents of L5)
vasily_kokushkin = node("Василий Кокушкин", "M")
mikhail_fedor_f = node("Михаил", "M")
mikhail_feodosia_f = node("Михаил", "M")

# L5
mikhail_iv = node("Михаил Иванов", "M")
ignat_nik = node("Игнат Никифоров", "M")
georgy_nov = node("Георгий", "M")
yan_kruz = node("Ян Круз", "M")
andrey_parv = node("Андрей Парвиайнен", "M")
ivan_kar = node("Иван Карченя", "M")
egor_kokushkin = node("Егор Васильевич Кокушкин", "M", "1819", "01.12.1889", f=vasily_kokushkin, m=unk_f())
mikhail_kuk = node("Михаил Кукушкин", "M")
ivan_afon = node("Иван Афоничев", "M")
fedor_m = node("Фёдор Михайлович", "M", "1837", "02.04.1900", f=mikhail_fedor_f, m=unk_f())
feodosia_m = node("Феодосия Михайловна", "F", "1837", "17.10.1909", f=mikhail_feodosia_f, m=unk_f())

# L4
filipp_iv = node("Филипп Михайлович Иванов", "M", "1874", "02.1942", f=mikhail_iv, m=unk_f())
agrippina_nik = node("Агриппина Игнатьевна Никифорова", "F", "1879", "1910", f=ignat_nik, m=unk_f())
pavel_uvarov = node("Павел Уваров", "M", "", "1918", f=unk_m(), m=unk_f())
olga_mother = unk_f()

efrem_nov = node("Ефрем Новичков", "M", "", "1905", f=unk_m(), m=unk_f())
praskovya_nov = node("Прасковья Георгиевна Новичкова", "F", "24.07.1867", "после 1930-х", f=georgy_nov, m=unk_f())

ivan_kruze_real = node("Иван Крузе", "M")
ioannes_kruz = node("Иоаннес Янович Круз (отчим)", "M", "30.01.1867", "13.06.1900", f=yan_kruz, m=unk_f())
vilgelmina_parv = node("Вильгельмина Андреевна Парвиайнен", "F", "02.02.1864", "02.04.1941", f=andrey_parv, m=unk_f())

iosif_charny = node("Иосиф Чарный", "M", f=unk_m(), m=unk_f())
stepan_kar = node("Степан Карченя", "M", f=unk_m(), m=unk_f())
ekaterina_kar = node("Екатерина Ивановна Карченя", "F", "1878", "1931", f=ivan_kar, m=unk_f())

kirill_kuk = node("Кирилл Егорович Кукушкин", "M", "1852", "17.11.1911", f=egor_kokushkin, m=unk_f())
anna_kuk = node("Анна Михайловна Кукушкина", "F", "1852", "12.09.1891", f=mikhail_kuk, m=unk_f())

nikolay_afon = node("Николай Иванович Афоничев", "M", "1861", "", f=ivan_afon, m=unk_f())
paraskeva_afon = node("Параскева Фёдоровна Афоничева", "F", "10.10.1862", "", f=fedor_m, m=feodosia_m)

# L3
dmitry_f_iv = node("Дмитрий Филиппович Иванов", "M", "15.09.1907", "03.01.1996", f=filipp_iv, m=agrippina_nik)
olga_uvarova = node("Ольга Павловна Уварова", "F", "", "01.11.1939", f=pavel_uvarov, m=olga_mother)
ivan_e_nov = node("Иван Ефремович Новичков", "M", "06.06.1903", "03.1980", f=efrem_nov, m=praskovya_nov)
marta_kruze = node("Марта Ивановна Крузе", "F", "25.04.1905", "17.04.1946", f=ivan_kruze_real, m=vilgelmina_parv)

mikhail_charny = node("Михаил Иосифович Чарный", "M", "1896", "1979", f=iosif_charny, m=unk_f())
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

def build_html_tree(n):
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
            
    date_str = f"<div class='dates'>{' '.join(dates)}</div>" if dates else ""
    
    classes = ["card"]
    if n["gender"] == "M":
        classes.append("male")
    elif n["gender"] == "F":
        classes.append("female")
            
    if "Неизвест" in n["name"]:
        classes.append("unknown")
        
    html = f"<li><div class='{' '.join(classes)}'><div class='name'>{n['name']}</div>{date_str}</div>"
    
    if n["f"] or n["m"]:
        html += "<ul>"
        if n["f"]:
            html += build_html_tree(n["f"])
        if n["m"]:
            html += build_html_tree(n["m"])
        html += "</ul>"
        
    html += "</li>"
    return html

css_base = """
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
    color: #000;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    background: #fff;
    width: 220px;
    height: 100px;
    box-sizing: border-box;
    box-shadow: 0 3px 6px rgba(0,0,0,0.1);
    margin: 0 auto;
}
.name {
    font-size: 15px;
    font-weight: bold;
    line-height: 1.3;
    margin-bottom: 5px;
}
.dates {
    font-size: 13px;
    color: #444;
}
.unknown {
    border-style: dashed;
    color: #666;
    background: #f9f9f9;
}
"""

css_bw = css_base + """
.card {
    border-color: #444;
    background-color: #fff;
}
.unknown {
    border-color: #999;
    background-color: #fafafa;
}
"""

css_color = css_base + """
.card.male {
    background-color: #e3f2fd;
    border-color: #1565c0;
}
.card.female {
    background-color: #fce4ec;
    border-color: #d81b60;
}
.unknown.male {
    background-color: #f0f8ff;
    border-color: #90caf9;
    border-style: dashed;
}
.unknown.female {
    background-color: #fff0f3;
    border-color: #f48fb1;
    border-style: dashed;
}
"""

def generate_html(filename, css):
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
            {build_html_tree(polina)}
        </ul>
    </div>
    </body>
    </html>
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

generate_html('/root/.openclaw/workspace/tree_v3_bw.html', css_bw)
generate_html('/root/.openclaw/workspace/tree_v3_color.html', css_color)
print("V3 HTMLs generated.")

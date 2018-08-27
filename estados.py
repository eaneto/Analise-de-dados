import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "S": [],
    "NE": [],
    "MO": [],
    "O": [],
}

dados["S"].append(["alabama", 72])
dados["O"].append(["alasca", 68])
dados["O"].append(["arizona", 78])
dados["S"].append(["arkansas", 81])
dados["O"].append(["california", 76])
dados["O"].append(["colorado", 74])
dados["NE"].append(["connecticut", 83])
dados["S"].append(["delaware", 78])
dados["S"].append(["florida", 71])
dados["S"].append(["georgia", 67])
dados["O"].append(["havai", 80])
dados["O"].append(["idaho", 0])
dados["MO"].append(["illinois", 84])
dados["MO"].append(["indiana", 86])
dados["MO"].append(["iowa", 88])
dados["MO"].append(["kansas", 83])
dados["S"].append(["kentucky", 0])
dados["S"].append(["louisiana", 71])
dados["NE"].append(["maine", 84])
dados["S"].append(["maryland", 83])
dados["NE"].append(["massachusetts", 83])
dados["MO"].append(["michigan", 74])
dados["MO"].append(["minnesota", 77])
dados["S"].append(["mississippi", 75])
dados["MO"].append(["misouri", 81])
dados["O"].append(["montana", 82])
dados["MO"].append(["nebraska", 86])
dados["O"].append(["nevada", 62])
dados["NE"].append(["new hamsphire", 86])
dados["NE"].append(["nova_jersey", 83])
dados["O"].append(["novo_mexico", 86])
dados["NE"].append(["nova_iorque", 77])
dados["S"].append(["carolina_do_norte", 78])
dados["MO"].append(["dakota_do_norte", 86])
dados["MO"].append(["ohio", 80])
dados["S"].append(["oklahoma", 0])
dados["O"].append(["oregon", 68])
dados["NE"].append(["pensilvania", 83])
dados["NE"].append(["hode_island", 77])
dados["S"].append(["carolina_do_sul", 74])
dados["MO"].append(["dakota_do_sul", 83])
dados["S"].append(["tenesee", 86])
dados["S"].append(["texas", 86])
dados["O"].append(["utah", 78])
dados["NE"].append(["vermont", 87])
dados["S"].append(["virginia", 82])
dados["O"].append(["washington", 76])
dados["S"].append(["virginia_ocidental", 76])
dados["MO"].append(["wisconsin", 87])
dados["O"].append(["wyoning", 80])
dados["S"].append(["distrito_de_columbia", 59])

for i in range(len(dados["S"]) - len(dados["O"])):
    dados["O"].append(["0", 0])

for i in range(len(dados["S"]) - len(dados["MO"])):
    dados["MO"].append(["0", 0])

for i in range(len(dados["S"]) - len(dados["NE"])):
    dados["NE"].append(["0", 0])

dados = pd.DataFrame(dados)

s = [x[1] for x in dados["S"] if x[1] != 0]
o = [x[1] for x in dados["O"] if x[1] != 0]
mo = [x[1] for x in dados["MO"] if x[1] != 0]
ne = [x[1] for x in dados["NE"] if x[1] != 0]

print(s)
print(o)
print(mo)
print(ne)

print(dados)

fig, axes = plt.subplots()

# for i in dados["S"]:
#    axes.bar(i[0], i[1])

axes.bar(["sul"], s)
axes.bar(["oeste"], o)
axes.bar(["meio-oeste"], mo)
axes.bar(["nordeste"], ne)
plt.show()

"""Extrai as leituras do sensor e as calibrações do dataPoints.jsonl do Exportar.zip (app mySugr/SmartGuide).

Uso:
  unzip Exportar.zip -d <pasta_vazia>
  python3 -I scripts/processar_export.py <pasta>/dataPoints.jsonl relatorios/originais/AAAA-MM-DD_export_cgm.csv [inicio] [fim]

O CSV é cumulativo (desde 13/11). Com [inicio] [fim] ("AAAA-MM-DD HH:MM"), imprime as estatísticas do período.
Só as leituras de glicose vão para o repositório. O zip tem dados da conta e do aparelho e NÃO deve ser salvo.
"""
import csv, json, statistics as st, sys

def extrair(src):
    rows = []
    for l in open(src):
        d = json.loads(l); k = d['data']['code']; t = d['start'][:16].replace('T', ' ')
        if k == 100:  # leitura do sensor
            p = json.loads(d['data']['payload'])
            if p['value'] == 'NaN':
                continue
            q = json.loads(d['meta'][0]['payload']) if d.get('meta') else {}
            rows.append((t, 'sensor', float(p['value']), p.get('trendDirection', ''), q.get('status', {}).get('calibration', '')))
        elif k == 823:  # calibração com ponta de dedo
            p = json.loads(d['data']['payload'])
            rows.append((t, 'calibracao_ponta_de_dedo', p['glucoseConcentration'], '', p['status']))
    return sorted(rows)

def stats(rows, a, b):
    v = [r[2] for r in rows if r[1] == 'sensor' and a <= r[0] <= b]
    pct = lambda f: round(100 * sum(1 for x in v if f(x)) / len(v))
    return (f"n={len(v)} média={st.mean(v):.0f} CV={100*st.pstdev(v)/st.mean(v):.0f}% min={min(v):.0f} max={max(v):.0f} "
            f"<70={pct(lambda x: x < 70)}% 70–140={pct(lambda x: 70 <= x <= 140)}% >140={pct(lambda x: x > 140)}% >180={pct(lambda x: x > 180)}%")

if __name__ == '__main__':
    rows = extrair(sys.argv[1])
    with open(sys.argv[2], 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['data_hora', 'tipo', 'glicose_mg_dl', 'tendencia', 'status']); w.writerows(rows)
    print('última leitura:', rows[-1][0])
    if len(sys.argv) >= 5:
        print(stats(rows, sys.argv[3], sys.argv[4]))

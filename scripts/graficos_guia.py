"""Gera os gráficos do guia alimentar (PNG) a partir do CSV final do sensor.
Uso: python3 -I scripts/graficos_guia.py relatorios/originais/2026-11-23_export_cgm.csv <pasta_saida>"""
import csv, sys, datetime as dt
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

src, out = sys.argv[1], sys.argv[2]
INK, INK2, GRID, SURF = '#0b0b0b', '#52514e', '#e4e3df', '#ffffff'
C_LOW, C_FIB, C_REF = '#2a78d6', '#1baf7a', '#eb6834'  # slots 1, 3, 2 (validados all-pairs)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9, 'axes.edgecolor': GRID,
                     'axes.labelcolor': INK2, 'xtick.color': INK2, 'ytick.color': INK2, 'text.color': INK})

rows = [(dt.datetime.strptime(r[0], '%Y-%m-%d %H:%M'), float(r[2]))
        for r in csv.reader(open(src)) if r[1] == 'sensor']

# 1) Subida por refeição (pico - antes), barras horizontais
dados = [  # (rótulo, subida, categoria)
    ('Café com pouco açúcar', 4, 'ref'), ('Iogurte integral (19/11)', 5, 'low'),
    ('Almoço low-carb (carne + verduras)', 10, 'low'), ('Café da manhã low-carb', 12, 'low'),
    ('Sopa de feijão', 39, 'fib'), ('Fava, porção grande', 45, 'fib'), ('Mungunzá (milho + feijão)', 57, 'fib'),
    ('Coca-Cola (pouca)', 14, 'ref'), ('KitKat (1 barra)', 44, 'ref'), ('Tapioca com queijo', 52, 'ref'),
    ('Chocotone 400 g (tarde)', 52, 'ref'), ('Bolo + café com açúcar', 54, 'ref'),
    ('Panetone + fígado', 56, 'ref'), ('Baião sem batata frita (almoço)', 59, 'ref'),
    ('Pão de forma integral ~190 g', 72, 'ref'), ('Sorvete + pizza (noite)', 85, 'ref'),
    ('Maizena com queijo (noite)', 86, 'ref'), ('Frango + batata frita + baião (noite)', 97, 'ref'),
    ('Pastelão + Coca-Cola (noite)', 104, 'ref')]
dados.sort(key=lambda d: d[1])
cor = {'low': C_LOW, 'fib': C_FIB, 'ref': C_REF}
fig, ax = plt.subplots(figsize=(7.2, 6.2), dpi=200)
y = range(len(dados))
ax.barh(list(y), [d[1] for d in dados], height=0.72, color=[cor[d[2]] for d in dados], edgecolor=SURF, linewidth=1)
for i, d in enumerate(dados):
    ax.text(d[1] + 1.5, i, f'+{d[1]}', va='center', fontsize=8, color=INK)
ax.set_yticks(list(y)); ax.set_yticklabels([d[0] for d in dados], fontsize=8)
ax.set_xlabel('Quanto a glicose subiu (mg/dL, do valor antes da refeição até o pico)')
ax.set_xlim(0, 118); ax.grid(axis='x', color=GRID, linewidth=0.6); ax.set_axisbelow(True)
for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=C_LOW, label='Low-carb / proteína'), Patch(color=C_FIB, label='Carboidrato com fibra (leguminosas)'),
                   Patch(color=C_REF, label='Amido refinado / açúcar')], loc='lower right', frameon=False, fontsize=8)
fig.tight_layout(); fig.savefig(f'{out}/subidas.png'); plt.close(fig)

# 2) Curvas depois da refeição (0 a 6 h)
def curva(inicio):
    t0 = dt.datetime.strptime(inicio, '%Y-%m-%d %H:%M')
    return [((t - t0).total_seconds() / 3600, v) for t, v in rows if t0 - dt.timedelta(minutes=10) <= t <= t0 + dt.timedelta(hours=6)]
series = [('Café da manhã low-carb (19/11)', '2026-11-19 04:57', C_LOW),
          ('Fava, porção grande, almoço (20/11)', '2026-11-20 11:49', C_FIB),
          ('Frango + batata frita + baião, noite (20/11)', '2026-11-20 20:15', C_REF)]
fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=200)
ax.axhspan(70, 140, color='#f1f0ec', zorder=0); ax.text(5.95, 72, 'faixa 70–140', ha='right', fontsize=7, color=INK2)
for nome, ini, c in series:
    pts = curva(ini); ax.plot([p[0] for p in pts], [p[1] for p in pts], color=c, linewidth=2, label=nome)
ax.set_xlim(-0.2, 6); ax.set_ylim(60, 195); ax.set_xlabel('Horas depois de começar a comer'); ax.set_ylabel('Glicose (mg/dL)')
ax.grid(color=GRID, linewidth=0.6); ax.set_axisbelow(True)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
ax.annotate('184,5', xy=(1.05, 184.5), xytext=(1.4, 188), fontsize=8, color=INK, arrowprops=dict(arrowstyle='-', color=INK2, lw=0.6))
ax.annotate('128,5', xy=(1.73, 128.5), xytext=(2.1, 133), fontsize=8, color=INK, arrowprops=dict(arrowstyle='-', color=INK2, lw=0.6))
ax.legend(frameon=False, fontsize=8, loc='upper right')
fig.tight_layout(); fig.savefig(f'{out}/curvas.png'); plt.close(fig)
print('ok')

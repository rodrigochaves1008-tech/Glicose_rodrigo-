"""Gera o guia alimentar em PDF (dados do sensor + conhecimento geral).
Uso: python3 -I scripts/gerar_guia_pdf.py <pasta_com_graficos> <saida.pdf>
Os gráficos vêm de scripts/graficos_guia.py."""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,
                                PageBreak, KeepTogether)

GRAF, OUT = sys.argv[1], sys.argv[2]
F = '/usr/share/fonts/truetype/liberation/LiberationSans-'
for nome, arq in [('DV', 'Regular'), ('DVB', 'Bold'), ('DVI', 'Italic'), ('DVBI', 'BoldItalic')]:
    pdfmetrics.registerFont(TTFont(nome, F + arq + '.ttf'))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DVB', italic='DVI', boldItalic='DVBI')

INK, INK2, LINE, SOFT = colors.HexColor('#1b1b1a'), colors.HexColor('#52514e'), colors.HexColor('#d9d8d3'), colors.HexColor('#f4f3ef')
VERDE, AMAR, VERM = colors.HexColor('#e3f2e6'), colors.HexColor('#fdf1d6'), colors.HexColor('#fbe2dc')
VERDE_T, AMAR_T, VERM_T = colors.HexColor('#1d6b2c'), colors.HexColor('#7a5300'), colors.HexColor('#9b2c16')
AZUL = colors.HexColor('#2a78d6')

st = {
    'tit': ParagraphStyle('tit', fontName='DVB', fontSize=24, leading=30, textColor=INK, alignment=TA_CENTER, spaceAfter=8),
    'sub': ParagraphStyle('sub', fontName='DV', fontSize=12, leading=17, textColor=INK2, alignment=TA_CENTER),
    'h1': ParagraphStyle('h1', fontName='DVB', fontSize=16, leading=21, textColor=INK, spaceBefore=4, spaceAfter=8),
    'h2': ParagraphStyle('h2', fontName='DVB', fontSize=12, leading=16, textColor=INK, spaceBefore=10, spaceAfter=4),
    'p': ParagraphStyle('p', fontName='DV', fontSize=9.6, leading=14, textColor=INK, spaceAfter=5),
    'b': ParagraphStyle('b', fontName='DV', fontSize=9.6, leading=14, textColor=INK, leftIndent=12, bulletIndent=2, spaceAfter=2.5),
    'nota': ParagraphStyle('nota', fontName='DVI', fontSize=8.3, leading=11.5, textColor=INK2, spaceAfter=4),
    'cel': ParagraphStyle('cel', fontName='DV', fontSize=8.5, leading=11.5, textColor=INK),
    'celb': ParagraphStyle('celb', fontName='DVB', fontSize=8.5, leading=11.5, textColor=INK),
}
P = lambda t, s='p': Paragraph(t, st[s])
def B(itens): return [Paragraph(i, st['b'], bulletText='•') for i in itens]
def C(t, s='cel'): return Paragraph(t, st[s])

def tabela(linhas, larguras, cab=True, fundo=None):
    dados = [[C(c, 'celb' if (cab and i == 0) else 'cel') if isinstance(c, str) else c for c in l] for i, l in enumerate(linhas)]
    t = Table(dados, colWidths=larguras, repeatRows=1 if cab else 0)
    estilo = [('GRID', (0, 0), (-1, -1), 0.4, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
              ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
              ('TOPPADDING', (0, 0), (-1, -1), 3.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5)]
    if cab: estilo.append(('BACKGROUND', (0, 0), (-1, 0), SOFT))
    if fundo: estilo += fundo
    t.setStyle(TableStyle(estilo)); return t

def caixa(titulo, itens, bg, cor_t, largura=174 * mm):
    conteudo = [Paragraph(f'<font color="{cor_t.hexval().replace("0x", "#")}"><b>{titulo}</b></font>', st['h2'])] + B(itens)
    t = Table([[conteudo]], colWidths=[largura])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), bg), ('LEFTPADDING', (0, 0), (-1, -1), 9),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 9), ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
    return t

def rodape(c, d):
    c.saveState(); c.setFont('DV', 7.5); c.setFillColor(INK2)
    c.drawString(18 * mm, 10 * mm, 'Guia alimentar pessoal — Rodrigo — baseado no sensor de 13 a 22/11/2026')
    c.drawRightString(192 * mm, 10 * mm, f'página {d.page}'); c.restoreState()

s = []
W = 174 * mm

# ---------- Capa ----------
s += [Spacer(1, 45 * mm), P('Meu mapa alimentar', 'tit'),
      P('O que 9 dias de sensor de glicose mostraram sobre o meu corpo<br/>e os hábitos que valem a pena manter para o longo prazo', 'sub'),
      Spacer(1, 14 * mm)]
capa = tabela([
    ['Período analisado', '13/11 a 22/11/2026 (sensor Accu-Chek SmartGuide, braço direito)'],
    ['Dados válidos', '14/11 16:43 a ~21/11 13h (calibrado). Até 22/11 18:30 só as subidas; depois, falha do sensor'],
    ['Leituras', '~2.300 leituras de 5 em 5 minutos, cruzadas com um diário de refeições, treinos e sintomas'],
    ['Refeições testadas', 'mais de 30, de low-carb a pastelão com Coca-Cola'],
    ['Rotina habitual', 'low-carb, refeições cedo, normalmente sem jantar, treino de força de manhã'],
], [42 * mm, 132 * mm], cab=False, fundo=[('BACKGROUND', (0, 0), (0, -1), SOFT)])
s += [capa, Spacer(1, 16 * mm),
      P('<b>Importante.</b> Este guia junta os seus dados com recomendações gerais de saúde pública. Ele <b>não é diagnóstico '
        'nem prescrição</b> e não substitui médico ou nutricionista. Os números de um sensor de braço têm margem de erro '
        '(~10%) e 9 dias são uma amostra pequena. Leve este documento à sua próxima consulta.', 'nota'),
      PageBreak()]

# ---------- 1. Resumo ----------
s += [P('1. O resumo em uma página', 'h1'),
      P('<b>Sua glicose é bem regulada.</b> No período confiável, a média ficou em ~101 mg/dL, com <b>~94% do tempo entre 70 e 140</b> '
        '(a faixa de quem não tem diabetes), só 0,3% acima de 180 e nenhum valor perigosamente baixo. A glicemia de jejum ficou '
        'entre ~86 e ~100. Esse é o oposto do padrão de pré-diabetes (jejum alto, picos altos, demora para baixar).'),
      P('As 10 lições principais', 'h2')]
s += B([
    '<b>Proteína, gordura e verduras quase não mexem na sua glicose</b> (+5 a +15). Nos dias low-carb, a manhã ficou praticamente reta (variação de 3%).',
    '<b>O pior cenário é amido refinado + fritura/gordura à noite.</b> Os dois únicos picos acima de 180 foram jantares assim: pastelão + Coca (194,5) e frango + batata frita + baião (184,5). Esses jantares também deixam a glicose oscilando por 4 a 6 horas.',
    '<b>O horário importa.</b> Refeições com carboidrato parecidas subiram bem menos de manhã e no almoço do que à noite. Seu hábito de comer cedo e não jantar trabalha a seu favor.',
    '<b>Leguminosas são o carboidrato mais amigo:</b> sopa de feijão (+39) e fava em porção grande (+45), sem queda brusca depois.',
    '<b>Farinha branca, tapioca, maizena e açúcar sobem rápido</b> (+44 a +86), mesmo em porção moderada, e às vezes provocam um "rebote" para 64–76 depois, o que pode trazer fome e moleza.',
    '<b>Pouco açúcar não aparece</b> (um café adoçado: +4). O problema é a quantidade e a combinação, não um pouco de vez em quando.',
    '<b>Gordura junto com carboidrato não "anula" o açúcar:</b> pode baixar um pouco o pico, mas alonga a curva (pizza, chocotone, pastelão: ondas por horas).',
    '<b>Treino de pernas baixa a glicose (−30); treino de braço sobe um pouco (+17)</b>. Os dois são normais e saudáveis.',
    '<b>Vários dias seguidos de carboidrato aumentaram a fome e a vontade de doce</b>, e a glicose da madrugada subiu (75 → 113). Voltando ao low-carb, ela voltou a cair (86).',
    '<b>Sono ruim e inflamação (garganta, virose) parecem elevar a glicose</b> e a fome. Dormir bem também é "dieta".',
])
s += [Spacer(1, 6), caixa('A regra de bolso', [
    'Base do prato: <b>proteína + verduras/legumes + gordura de boa qualidade</b>.',
    'Carboidrato: prefira <b>feijão, fava, lentilha, grão-de-bico, frutas inteiras e tubérculos cozidos</b>, em porção moderada e <b>de manhã ou no almoço</b>.',
    'Deixe para ocasiões especiais: <b>farinha branca + açúcar + fritura, principalmente à noite</b>, e refrigerante.',
], VERDE, VERDE_T), PageBreak()]

# ---------- 2. Seus dados ----------
s += [P('2. O que os seus dados mostraram', 'h1'),
      P('Quanto cada refeição fez a glicose subir', 'h2'),
      P('Diferença entre o valor antes de comer e o pico. Quanto menor a barra, mais estável a glicose. Quantidades e horários variaram, então compare tendências, não décimos.', 'nota'),
      Image(f'{GRAF}/subidas.png', width=W * 0.92, height=W * 0.92 * 6.2 / 7.2), PageBreak(),
      P('A mesma pessoa, três refeições diferentes', 'h2'),
      P('Curvas reais do sensor nas 6 horas depois de começar a comer. A faixa cinza é 70–140.', 'nota'),
      Image(f'{GRAF}/curvas.png', width=W, height=W * 3.6 / 7.2)]
s += B(['<b>Azul (low-carb):</b> sobe ~12 e volta em ~1h30. É o seu padrão de rotina.',
        '<b>Verde (fava, porção grande):</b> sobe devagar até 128,5 e volta em ~3 h, sem cair abaixo da base.',
        '<b>Laranja (batata frita + baião, à noite):</b> chega a 184,5 em 1 hora e fica oscilando por mais de 5 horas.'])
s += [P('Números gerais', 'h2'), tabela([
    ['Indicador', 'Seu resultado', 'Referência (pessoa sem diabetes)'],
    ['Glicose média', '~101 mg/dL', 'em geral 90–110'],
    ['Tempo em 70–140', '~94%', 'acima de ~90%'],
    ['Tempo acima de 180', '0,3% (2 episódios de ~10 min)', 'raro'],
    ['Tempo abaixo de 70', '< 1% (quedas curtas, várias por compressão do sensor)', 'pouco'],
    ['Variabilidade (CV)', '~18% no geral; 3% nas manhãs low-carb', 'abaixo de 36% (quanto menor, melhor)'],
    ['Glicemia de madrugada/jejum', '75–113 (média ~90–96)', '70–99'],
    ['GMI (HbA1c estimada pelo sensor)', '~5,7%', 'só uma estimativa; o exame de sangue é o que vale'],
], [52 * mm, 62 * mm, 60 * mm])]
s += [P('O GMI de 5,7% fica no limite entre normal e pré-diabetes no exame de HbA1c, mas foi puxado pelos dias de teste com '
        'muito carboidrato (fora da sua rotina) e não é um exame. Vale pedir ao médico uma <b>hemoglobina glicada (HbA1c)</b> e uma '
        '<b>glicemia de jejum</b> de laboratório para confirmar.', 'nota'), PageBreak()]

# Tabela completa
s += [P('Todas as refeições analisadas', 'h2')]
s += [tabela([
    ['Refeição', 'Antes → pico', 'Volta à base', 'Observação'],
    ['Café da manhã low-carb (ovo, queijo, carne, verduras)', '~100 → ~112', '~1h30', 'Rotina. +10 a +15'],
    ['Almoço low-carb (carne + brócolis + couve-flor)', '~90 → 101', '< 1 h', ''],
    ['Iogurte natural integral', '98 → 103 / 87 → 116', '~1 h', '+5 num dia, +30 no outro (porção maior?)'],
    ['Café com pouco açúcar', '96 → 100', '—', 'Sem efeito'],
    ['Sopa de feijão', '88 → 127', '~2 h', 'Subida lenta, sem rebote'],
    ['Fava com toucinho, porção grande', '84 → 128,5', '~3 h', 'Subida lenta, sem rebote'],
    ['Mungunzá (milho, feijão, carnes)', '88 → 145', '~1h20', 'Rebote para 76'],
    ['Mungunzá com queijo e nata', '97 → 113', '—', 'Sensor já falhando: pouco confiável'],
    ['KitKat (1 barra), 2 vezes', '95 → 138 / 100 → 145', '1–2,5 h', 'Resposta repetida'],
    ['Coca-Cola (pouca)', '110 → 124', '~45 min', ''],
    ['Tapioca com queijo', '92 → 144', '> 3 h', 'Platô longo 104–121'],
    ['Pão de forma integral ~190 g', '92 → 164', '~2h45', '"Integral" industrializado sobe como pão branco'],
    ['Bolo + café com açúcar (jejum)', '94 → 148', '~1h20', 'Leve queda para ~80 depois'],
    ['Bolo / cuscuz repetidos na manhã', '78–97 → 120–145', '~1–1,5 h cada', '3 ondas'],
    ['Baião com carne, sem batata frita (almoço)', '74 → 133', '~45 min', 'Queda para 64 depois'],
    ['Panetone + bife de fígado', '94 → 150', '~3 h', 'Ondas 110–121'],
    ['Chocotone 400 g (tarde)', '94 → 146', '~8 h', 'Pico baixo, curva muito longa'],
    ['Maizena com queijo/manteiga (noite)', '82 → 168', '~2h35', 'Rebote para 68'],
    ['Sorvete grande + pizza (noite)', '87 → 172', '~6 h', '3 ondas'],
    ['Frango + batata frita + baião (noite)', '88 → 184,5', '~5h15', '4 ondas'],
    ['Pastelão + Coca-Cola (noite)', '91 → 194,5', '~4h20', 'Maior pico; madrugada alta depois'],
    ['Treino de pernas (jejum)', '125 → 95', '—', 'Baixa a glicose'],
    ['Treino de braço (jejum / após café)', '100 → 117 / 94 → 120', '~30 min / ~2 h', 'Sobe (adrenalina); normal'],
], [62 * mm, 32 * mm, 24 * mm, 56 * mm]), PageBreak()]

# ---------- 3. Mapa ----------
s += [P('3. Seu mapa alimentar', 'h1'),
      P('Combina o que o sensor mostrou em você (<b>[dado]</b>) com o que a ciência da nutrição recomenda para a população em geral (<b>[geral]</b>).', 'nota')]
s += [caixa('VERDE — base do dia a dia, à vontade', [
    '<b>Ovos, carnes frescas, frango, peixes</b> (sardinha, atum, salmão, tilápia) [dado: +10]. Peixe 2x por semana é uma das recomendações mais consistentes para coração e cérebro [geral].',
    '<b>Verduras e legumes sem amido:</b> brócolis, couve, couve-flor, repolho, abobrinha, berinjela, chuchu, quiabo, pepino, tomate, folhas, pimentão, cebola [dado + geral]. Meta: metade do prato.',
    '<b>Queijos, iogurte natural sem açúcar, manteiga, nata</b> em quantidade moderada [dado: +5].',
    '<b>Gorduras de boa qualidade:</b> azeite de oliva, abacate, castanhas (do Pará, de caju), amendoim, nozes, sementes (chia, linhaça, gergelim) [geral].',
    '<b>Limão, temperos, ervas, alho, vinagre</b> [geral]. Vinagre e limão na refeição podem reduzir um pouco a subida da glicose.',
    '<b>Água, café puro, chá sem açúcar, água com gás</b> [dado: café puro não mexe].',
], VERDE, VERDE_T), Spacer(1, 6),
    caixa('AMARELO — bom, mas em porção moderada e de preferência de manhã ou no almoço', [
    '<b>Feijão, fava, lentilha, grão-de-bico, ervilha</b> [dado: +39 a +45, sem rebote]. São o seu melhor carboidrato: fibra, proteína, minerais. Concha média.',
    '<b>Frutas inteiras</b> (não suco): frutas vermelhas, goiaba, maçã, pera, laranja com bagaço, mamão, abacate [geral]. Banana e manga: meia ou uma pequena. Junto com iogurte/castanhas, sobem menos.',
    '<b>Tubérculos cozidos e frios</b> (mandioca, batata-doce, inhame, batata cozida e resfriada): o resfriamento cria "amido resistente", que sobe menos [geral]. Nunca fritos.',
    '<b>Arroz (de preferência integral ou parboilizado), milho, cuscuz, mungunzá</b> [dado: baião +59, mungunzá +57]. Porção pequena (2–3 colheres), sempre com proteína e verdura, e de dia.',
    '<b>Pão integral de verdade</b> (com grãos visíveis, fermentação natural) em vez de pão de forma "integral" industrializado [dado: 164].',
    '<b>Chocolate 70% cacau ou mais</b>, 1–2 quadradinhos [geral].',
    '<b>Café com um pouco de açúcar</b> [dado: +4]. Uma colher não é problema; o hábito diário de muito açúcar é.',
], AMAR, AMAR_T), Spacer(1, 6),
    caixa('VERMELHO — ocasional (festas, fins de semana), nunca rotina, e evitar à noite', [
    '<b>Frituras de massa ou amido:</b> pastel, batata frita, coxinha, salgados [dado: 184,5 e 194,5].',
    '<b>Refrigerante comum, sucos de caixinha e sucos de fruta em quantidade</b> [dado + geral]. Açúcar líquido é absorvido em minutos e não dá saciedade.',
    '<b>Farinha branca + açúcar:</b> bolo, panetone/chocotone, biscoito recheado, doces de padaria, pizza [dado: +52 a +86, curvas longas].',
    '<b>Amidos refinados "puros":</b> maizena, tapioca, pão branco, cuscuz em grande quantidade [dado: maizena 168, tapioca 144].',
    '<b>Sorvete, chocolate ao leite, KitKat e similares</b> [dado: +44].',
    '<b>Carnes processadas:</b> salsicha, linguiça, calabresa, presunto, mortadela, bacon/toucinho em excesso. A OMS (IARC) classifica carne processada como cancerígena (grupo 1) para câncer de intestino [geral]. Usar como tempero, não como base.',
    '<b>Ultraprocessados em geral</b> (lista longa de ingredientes que você não teria em casa) [geral: Guia Alimentar para a População Brasileira].',
    '<b>Álcool</b>, principalmente cerveja e drinks doces. Não existe dose "saudável"; se beber, pouco e com comida [geral].',
], VERM, VERM_T), PageBreak()]

# ---------- 4. Estratégias ----------
s += [P('4. Estratégias que funcionam para você', 'h1'),
      P('Quando for comer carboidrato, estas táticas reduzem o estrago. As marcadas com [dado] apareceram no seu sensor; as outras têm boa evidência em estudos, mas não foram testadas em você.', 'nota')]
s += [tabela([
    ['Estratégia', 'Por quê', 'Fonte'],
    ['<b>Coma o carboidrato cedo</b> (café ou almoço), não à noite', 'À noite a sensibilidade à insulina é menor. Seus 2 picos acima de 180 foram jantares', '[dado]'],
    ['<b>Prefira leguminosas</b> ao arroz, pão e farinhas', 'Fibra e proteína deixam a subida lenta e sem rebote', '[dado]'],
    ['<b>Não junte amido + fritura</b> (batata frita com arroz, pastel)', 'A gordura em excesso alonga a curva por 4–6 h, em ondas', '[dado]'],
    ['<b>Coma primeiro a salada e a proteína</b>, o carboidrato por último', 'Estudos mostram picos até ~30–40% menores', '[geral]'],
    ['<b>Caminhe 10–15 min depois de comer</b>', 'Músculo em uso puxa glicose do sangue. Reduz bem o pico', '[geral]'],
    ['<b>Treino de pernas</b> nos dias de mais carboidrato', 'Baixou sua glicose em 30 mg/dL', '[dado]'],
    ['<b>Porção, não proibição</b>', 'Pouco açúcar (+4) não aparece; 400 g de chocotone alongou a curva por 8 h', '[dado]'],
    ['<b>Fruta inteira em vez de suco ou doce</b>', 'A fibra da fruta inteira segura a absorção', '[geral]'],
    ['<b>Resfriar arroz/batata/mandioca cozidos</b> e esquentar depois', 'Forma amido resistente, que sobe menos', '[geral]'],
    ['<b>Vinagre ou limão na salada</b> antes do prato principal', 'Pode reduzir um pouco a subida da glicose', '[geral]'],
    ['<b>Não pule refeições para "compensar" um doce</b>', 'Jejum seguido de carboidrato grande tende a dar pico maior e mais fome', '[geral]'],
    ['<b>Se exagerar num dia, volte à rotina no seguinte</b>', 'Depois dos dias de carboidrato, 1–2 dias low-carb já baixaram a madrugada de 96 para 86', '[dado]'],
], [62 * mm, 92 * mm, 20 * mm])]
s += [P('Montando o prato', 'h2')]
s += [tabela([
    ['Parte do prato', 'O que colocar', 'Exemplo'],
    ['1/2 do prato', 'Verduras e legumes sem amido (cru + cozido)', 'Salada de folhas, tomate e pepino + brócolis e couve refogados'],
    ['1/4 do prato', 'Proteína', 'Frango, carne, peixe, ovos'],
    ['1/4 do prato (opcional)', 'Carboidrato com fibra', 'Feijão, fava, lentilha, ou 2–3 colheres de arroz/mandioca cozida'],
    ['Por cima', 'Gordura de qualidade', 'Fio de azeite, abacate, castanhas'],
    ['Para beber', 'Sem açúcar', 'Água, água com gás e limão, chá, café puro'],
], [36 * mm, 60 * mm, 78 * mm]), PageBreak()]

# ---------- 5. Hábitos de longo prazo ----------
s += [P('5. Hábitos para uma vida melhor no longo prazo', 'h1'),
      P('Recomendações gerais de saúde pública (OMS, Ministério da Saúde, sociedades médicas), adaptadas à sua rotina.', 'nota')]
s += [P('Alimentação', 'h2')] + B([
    '<b>"Comida de verdade" como base:</b> o Guia Alimentar para a População Brasileira resume em: alimentos in natura ou minimamente processados como base; processados com moderação; <b>evitar ultraprocessados</b>.',
    '<b>Fibras: 25–30 g por dia ou mais.</b> É o ponto mais fácil de faltar em dieta low-carb. Fontes que combinam com você: verduras, legumes, leguminosas, sementes de chia/linhaça, castanhas, abacate, frutas vermelhas. Fibra alimenta a flora intestinal e protege intestino e coração.',
    '<b>Proteína adequada:</b> para quem faz musculação, a faixa usual é de ~1,2 a 1,6 g por kg de peso por dia, distribuída nas refeições. Peça ao nutricionista o valor para o seu peso.',
    '<b>Variedade de proteínas:</b> alternar carne vermelha com frango, peixe, ovos e leguminosas. Carne vermelha: até ~350–500 g cozida por semana (recomendação do World Cancer Research Fund); carne processada, o mínimo possível.',
    '<b>Gorduras:</b> priorizar azeite, peixes, castanhas e abacate. Manteiga, nata, queijo e toucinho com moderação, principalmente se o colesterol LDL estiver alto.',
    '<b>Açúcar livre:</b> a OMS recomenda menos de 10% das calorias (o ideal é menos de 5%, ~25 g ou 6 colheres de chá por dia), somando o açúcar do café, doces e bebidas.',
    '<b>Sal:</b> menos de 5 g por dia (OMS), ou ~1 colher de chá rasa no total. Atenção a embutidos, queijos amarelos e temperos prontos.',
    '<b>Água:</b> beba ao longo do dia, até a urina ficar clara. No low-carb/cetose se perde mais água e sódio no início.',
])
s += [P('Movimento', 'h2')] + B([
    '<b>Mantenha a musculação</b> 2 ou mais vezes por semana (você já faz). Músculo é o maior "consumidor" de glicose do corpo e protege contra diabetes com a idade.',
    '<b>Some atividade aeróbica:</b> a OMS recomenda 150–300 min por semana de atividade moderada (caminhada rápida, bicicleta) ou 75–150 min de intensa.',
    '<b>Caminhada curta depois das refeições maiores</b>: barata e eficaz.',
    '<b>Evite ficar sentado por horas</b>: levante e se mova a cada 30–60 min.',
])
s += [P('Sono, estresse e saúde em geral', 'h2')] + B([
    '<b>Durma 7–9 horas.</b> Uma noite ruim já reduz a sensibilidade à insulina no dia seguinte e aumenta a fome e a vontade de doce. Como você acorda ~04h, isso significa deitar por volta de 20h–21h.',
    '<b>Estresse e infecções sobem a glicose</b> (cortisol, adrenalina). Você viu isso na madrugada de 17/11 com a garganta inflamada.',
    '<b>Não fumar</b> e manter o álcool no mínimo.',
    '<b>Peso e cintura:</b> a circunferência abdominal é um bom termômetro de risco metabólico. Referência usual para homens: abaixo de ~94 cm (ideal) e de ~102 cm (limite).',
]) + [PageBreak()]

# ---------- 6. Low-carb ----------
s += [P('6. Sobre a sua dieta low-carb no longo prazo', 'h1')]
s += [P('O que os dados mostram a favor', 'h2')] + B([
    'Glicose estável, sem picos, com refeições de proteína e verduras. Menos fome e menos vontade de doce quando você está na rotina.',
    'Ela combina com o seu jeito de comer (cedo, sem jantar) e você consegue manter.',
])
s += [P('Pontos de atenção (gerais)', 'h2')] + B([
    '<b>Colesterol:</b> em parte das pessoas, dietas com muita gordura saturada (manteiga, nata, carne gorda, toucinho) sobem o LDL. Faça o perfil lipídico e ajuste o tipo de gordura se precisar.',
    '<b>Fibra e variedade:</b> sem planejamento, low-carb vira "carne, ovo e queijo". Inclua verduras, sementes, castanhas e um pouco de leguminosa.',
    '<b>Não precisa ser 8 ou 80.</b> Seus dados mostram que leguminosas, frutas inteiras e tubérculos cozidos em porção moderada, de dia, cabem bem. Uma rotina "low-carb moderada" pode ser mais fácil de manter por anos que a cetose estrita.',
    '<b>Entrar e sair da cetose</b> traz fome, vontade de doce e sensação de corpo pesado nos primeiros dias, como você sentiu. Ter uma rotina estável evita essa montanha-russa.',
    '<b>Rins, ácido úrico e intestino:</b> com muita proteína ou pouca fibra, vale o médico acompanhar nos exames de rotina.',
])
s += [P('Exames para conversar com o médico', 'h2'), tabela([
    ['Exame', 'Para quê'],
    ['Glicemia de jejum e hemoglobina glicada (HbA1c)', 'Confirmar a boa regulação vista no sensor (o GMI deu ~5,7%, valor que merece confirmação)'],
    ['Perfil lipídico (colesterol total, LDL, HDL, triglicerídeos)', 'Ver se a gordura da dieta está afetando o colesterol'],
    ['Creatinina / função renal, ácido úrico', 'Acompanhar com dieta rica em proteína'],
    ['Pressão arterial, peso, circunferência abdominal', 'Risco cardiometabólico'],
    ['Outros que o médico julgar necessários', 'Ex.: vitamina D, B12, TSH, conforme o caso'],
], [78 * mm, 96 * mm])]
s += [P('Quando procurar o médico antes da consulta de rotina', 'h2')] + B([
    'Sede excessiva, urinar muito, perda de peso sem motivo, visão embaçada ou cansaço persistente.',
    'Tremor, suor frio, tontura ou confusão algumas horas depois de comer, se começarem a acontecer com frequência.',
    'Rouquidão que dure mais de 2–3 semanas (você teve perda de voz em 19/11).',
]) + [PageBreak()]

# ---------- 7. Cardápio ----------
s += [P('7. Exemplo prático: um dia e uma semana', 'h1'),
      P('Sugestão no seu horário de sempre (acorda ~04h, treina cedo, sem jantar). Ajuste com um nutricionista.', 'nota')]
s += [tabela([
    ['Horário', 'Refeição', 'Ideia'],
    ['~04h30', 'Café da manhã', 'Ovos mexidos com queijo e tomate + couve/brócolis refogados no azeite + café puro. Opcional: 1 fruta (mamão ou frutas vermelhas)'],
    ['~05h15', 'Treino', 'Alternar pernas e braços; uma caminhada leve no fim ajuda'],
    ['~09h', 'Lanche (se tiver fome)', 'Iogurte natural integral com chia e castanhas, ou 1 ovo cozido + abacate'],
    ['~12h', 'Almoço', '1/2 prato de salada e legumes + peixe/frango/carne + concha de feijão ou fava (ou 2–3 colheres de arroz). Caminhar 10 min depois'],
    ['~16h', 'Última refeição', 'Igual ao café (ovos, carne, queijo, verduras) ou omelete com legumes. Sem carboidrato refinado'],
    ['Noite', 'Sem jantar', 'Água, chá. Se tiver muita fome: algo low-carb (ovo, queijo, castanhas), nunca massa ou fritura'],
], [22 * mm, 34 * mm, 118 * mm])]
s += [P('Ideias para a semana', 'h2'), tabela([
    ['Proteínas', 'Acompanhamentos', 'Carboidrato com fibra (almoço)'],
    ['Peixe 2x (sardinha, tilápia, salmão)', 'Brócolis, couve-flor, abobrinha, berinjela, chuchu, quiabo', 'Feijão, fava, lentilha, grão-de-bico'],
    ['Frango 2–3x', 'Saladas variadas com azeite e limão', 'Mandioca ou batata-doce cozida (resfriada)'],
    ['Carne vermelha 2–3x', 'Repolho, couve, vagem, cenoura', 'Arroz integral (pequena porção)'],
    ['Ovos todos os dias', 'Abacate, castanhas, sementes', 'Fruta inteira'],
], [58 * mm, 64 * mm, 52 * mm])]
s += [P('Trocas inteligentes', 'h2'), tabela([
    ['Em vez de...', 'Experimente...'],
    ['Batata frita', 'Batata-doce, mandioca ou abóbora assadas; legumes assados no azeite'],
    ['Pastel, coxinha, salgado', 'Omelete recheada, espetinho de frango, queijo coalho assado'],
    ['Refrigerante', 'Água com gás + limão; refrigerante zero de vez em quando'],
    ['Bolo, panetone, biscoito', 'Iogurte natural com frutas vermelhas e castanhas; chocolate 70%'],
    ['Pão de forma', 'Ovos; pão de fermentação natural integral, se for comer pão'],
    ['Tapioca / cuscuz em quantidade', 'Crepioca (1 ovo + 1 colher de tapioca); cuscuz em porção pequena com ovo e verdura'],
    ['Arroz + batata + farinha no mesmo prato', 'Um carboidrato só, de preferência o feijão'],
    ['Jantar pesado', 'Última refeição às ~16h, como já é o seu hábito'],
], [64 * mm, 110 * mm]), PageBreak()]

# ---------- 8. Limitações e referências ----------
s += [P('8. Limites deste guia', 'h1')] + B([
    'Foram 9 dias de sensor, com dados realmente confiáveis por ~7 dias. Cada refeição foi testada uma ou duas vezes.',
    'O sensor mede o líquido sob a pele, com atraso de ~10–15 min e erro de ~10% em relação ao sangue. Foi calibrado 2 vezes; nos últimos 1–2 dias leu abaixo do real e depois falhou.',
    'As quantidades nem sempre foram medidas, e várias refeições tinham mais de um alimento.',
    'Fatores como sono ruim, treino e uma virose leve mudaram os resultados em alguns dias.',
    'As recomendações gerais valem para adultos saudáveis. Doenças, remédios ou objetivos específicos mudam a orientação.',
])
s += [P('Referências gerais', 'h1')] + B([
    'Ministério da Saúde. <i>Guia Alimentar para a População Brasileira</i>, 2ª ed., 2014.',
    'Organização Mundial da Saúde (OMS). <i>Guideline: sugars intake for adults and children</i>, 2015.',
    'OMS. Recomendação de consumo de sódio/sal (menos de 5 g de sal por dia), 2012.',
    'OMS. <i>Guidelines on physical activity and sedentary behaviour</i>, 2020.',
    'IARC/OMS. Avaliação do consumo de carne vermelha e processada (Monografia 114), 2015.',
    'World Cancer Research Fund / AICR. <i>Diet, Nutrition, Physical Activity and Cancer: a Global Perspective</i>, 2018.',
    'American Diabetes Association. <i>Standards of Care in Diabetes</i> (critérios de glicemia de jejum e HbA1c).',
    'Battelino T. et al. Consenso internacional sobre métricas de tempo no alvo (Time in Range) para CGM, <i>Diabetes Care</i>, 2019.',
    'Dados próprios: repositório do projeto (diário, relatórios e exportações do sensor, 13–23/11/2026).',
])

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=16 * mm,
                        title='Meu mapa alimentar', author='Projeto glicose (Rodrigo)')
doc.build(s, onFirstPage=lambda c, d: None, onLaterPages=rodape)
print('ok', OUT)

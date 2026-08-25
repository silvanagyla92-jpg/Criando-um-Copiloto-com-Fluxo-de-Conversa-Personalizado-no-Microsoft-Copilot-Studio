from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "diagramas"
OUT.mkdir(exist_ok=True)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
regular = ImageFont.truetype(FONT, 28)
bold = ImageFont.truetype(BOLD, 30)
title_font = ImageFont.truetype(BOLD, 40)
small = ImageFont.truetype(FONT, 22)


def centered(draw, box, text, font):
    x1, y1, x2, y2 = box
    bb = draw.multiline_textbbox((0, 0), text, font=font, align="center")
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    draw.multiline_text(((x1+x2-tw)/2, (y1+y2-th)/2), text, font=font,
                        fill=(25,25,25), align="center")


def box(draw, xy, text):
    draw.rounded_rectangle(xy, radius=18, outline=(40,40,40), width=3, fill=(245,245,245))
    centered(draw, xy, text, bold)


def arrow(draw, p1, p2):
    draw.line([p1, p2], fill=(40,40,40), width=4)
    ang = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    length = 16
    pts = [
        p2,
        (p2[0]-length*math.cos(ang-0.45), p2[1]-length*math.sin(ang-0.45)),
        (p2[0]-length*math.cos(ang+0.45), p2[1]-length*math.sin(ang+0.45)),
    ]
    draw.polygon(pts, fill=(40,40,40))


# Arquitetura conceitual
img = Image.new("RGB", (1800, 1500), "white")
d = ImageDraw.Draw(img)
centered(d, (50,30,1750,100), "Arquitetura Conceitual — Assistente de Atendimento e Suporte", title_font)

nodes = {
    "u": (650,150,1150,250), "i": (650,320,1150,420), "a": (650,490,1150,590),
    "d": (80,700,480,820), "s": (510,700,910,820), "info": (940,700,1340,820),
    "f": (1370,700,1770,820), "r": (650,940,1150,1060),
    "c": (420,1190,820,1310), "e": (980,1190,1380,1310)
}
labels = {"u":"Usuário", "i":"Interface de interação", "a":"Agente conversacional",
          "d":"Dúvidas", "s":"Suporte", "info":"Informações", "f":"Fora do escopo",
          "r":"Resposta", "c":"Continuar", "e":"Encerrar"}
for key, xy in nodes.items():
    box(d, xy, labels[key])
arrow(d,(900,250),(900,320)); arrow(d,(900,420),(900,490))
for x in [280,710,1140,1570]:
    arrow(d,(900,590),(x,700)); arrow(d,(x,820),(900,940))
arrow(d,(900,1060),(620,1190)); arrow(d,(900,1060),(1180,1190))
centered(d,(200,1360,1600,1430),"Modelo conceitual do projeto — não representa configuração de uma plataforma.",small)
img.save(OUT / "arquitetura-conceitual.png", optimize=True)

# Fluxo conversacional
img = Image.new("RGB", (1800, 1600), "white")
d = ImageDraw.Draw(img)
centered(d, (50,30,1750,100), "Fluxo Conversacional — Assistente de Atendimento e Suporte", title_font)
nodes = [
    ("Início",(650,140,1150,240)), ("Saudação",(650,300,1150,400)),
    ("Identificar necessidade",(650,460,1150,560)), ("Dúvidas",(80,700,480,820)),
    ("Suporte",(510,700,910,820)), ("Informações",(940,700,1340,820)),
    ("Fora do escopo",(1370,700,1770,820)), ("Solicitar esclarecimento",(80,970,480,1090)),
    ("Resposta",(650,970,1150,1090)), ("Continuar",(510,1230,910,1350)),
    ("Encerrar",(940,1230,1340,1350)), ("Nova solicitação",(510,1450,910,1550))
]
for text, xy in nodes: box(d, xy, text)
arrow(d,(900,240),(900,300)); arrow(d,(900,400),(900,460))
for x in [280,710,1140,1570]: arrow(d,(900,560),(x,700))
for x in [280,710,1140]: arrow(d,(x,820),(900,970))
arrow(d,(1570,820),(280,970)); arrow(d,(280,1090),(650,1020))
arrow(d,(900,1090),(710,1230)); arrow(d,(900,1090),(1140,1230))
arrow(d,(710,1350),(710,1450)); arrow(d,(710,1450),(900,560))
centered(d,(180,1560,1620,1595),"Modelo conceitual do projeto — não representa execução em uma plataforma.",small)
img.save(OUT / "fluxo-conversacional.png", optimize=True)

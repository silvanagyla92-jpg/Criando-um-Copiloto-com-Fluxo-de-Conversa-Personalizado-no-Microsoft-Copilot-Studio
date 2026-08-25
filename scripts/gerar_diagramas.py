from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "diagramas"
OUT.mkdir(exist_ok=True)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
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
img = Image.new("RGB", (1900, 1800), "white")
d = ImageDraw.Draw(img)
centered(d, (50,30,1850,100), "Arquitetura Conceitual — Assistente de Atendimento e Suporte", title_font)

nodes = {
    "u": (700,150,1200,250),
    "i": (700,320,1200,420),
    "a": (700,490,1200,590),
    "d": (40,700,400,820),
    "s": (430,700,790,820),
    "info": (820,700,1180,820),
    "amb": (1210,700,1590,820),
    "f": (1620,700,1860,820),
    "clar": (1210,900,1590,1020),
    "r": (700,1080,1200,1200),
    "c": (470,1330,870,1450),
    "e": (1030,1330,1430,1450),
}
labels = {
    "u":"Usuário",
    "i":"Interface de interação",
    "a":"Agente conversacional",
    "d":"Dúvidas",
    "s":"Suporte",
    "info":"Informações",
    "amb":"Entrada ambígua",
    "f":"Fora do escopo",
    "clar":"Solicitar esclarecimento",
    "r":"Resposta",
    "c":"Continuar",
    "e":"Encerrar",
}
for key, xy in nodes.items():
    box(d, xy, labels[key])

arrow(d,(950,250),(950,320))
arrow(d,(950,420),(950,490))
arrow(d,(950,590),(220,700))
arrow(d,(950,590),(610,700))
arrow(d,(950,590),(1000,700))
arrow(d,(950,590),(1400,700))
arrow(d,(950,590),(1740,700))
arrow(d,(220,820),(950,1080))
arrow(d,(610,820),(950,1080))
arrow(d,(1000,820),(950,1080))
arrow(d,(1400,820),(1400,900))
arrow(d,(1400,1020),(950,490))
arrow(d,(1740,820),(950,1080))
arrow(d,(950,1200),(670,1330))
arrow(d,(950,1200),(1230,1330))

centered(d,(40,1500,1860,1580),
         "Fora do escopo: informar a limitação e orientar sobre os caminhos disponíveis.", small)
centered(d,(40,1600,1860,1670),
         "Entrada ambígua: solicitar esclarecimento e retornar à identificação da necessidade.", small)
centered(d,(40,1690,1860,1760),
         "Modelo conceitual do projeto — não representa configuração de uma plataforma.", small)
img.save(OUT / "arquitetura-conceitual.png", optimize=True)

# Fluxo conversacional
img = Image.new("RGB", (1900, 1750), "white")
d = ImageDraw.Draw(img)
centered(d, (50,30,1850,100), "Fluxo Conversacional — Assistente de Atendimento e Suporte", title_font)
nodes = [
    ("Início",(700,140,1200,240)),
    ("Saudação",(700,300,1200,400)),
    ("Identificar necessidade",(700,460,1200,560)),
    ("Dúvidas",(40,700,400,820)),
    ("Suporte",(430,700,790,820)),
    ("Informações",(820,700,1180,820)),
    ("Entrada ambígua",(1210,700,1590,820)),
    ("Fora do escopo",(1620,700,1860,820)),
    ("Solicitar esclarecimento",(1210,930,1590,1050)),
    ("Resposta",(700,930,1200,1050)),
    ("Continuar",(500,1220,900,1340)),
    ("Encerrar",(1000,1220,1400,1340)),
    ("Nova solicitação",(500,1440,900,1540)),
]
for text, xy in nodes:
    box(d, xy, text)

arrow(d,(950,240),(950,300))
arrow(d,(950,400),(950,460))
arrow(d,(950,560),(220,700))
arrow(d,(950,560),(610,700))
arrow(d,(950,560),(1000,700))
arrow(d,(950,560),(1400,700))
arrow(d,(950,560),(1740,700))
arrow(d,(220,820),(950,930))
arrow(d,(610,820),(950,930))
arrow(d,(1000,820),(950,930))
arrow(d,(1400,820),(1400,930))
arrow(d,(1400,1050),(950,460))
arrow(d,(1740,820),(950,930))
arrow(d,(950,1050),(700,1220))
arrow(d,(950,1050),(1200,1220))
arrow(d,(700,1340),(700,1440))
arrow(d,(700,1440),(950,460))
centered(d,(60,1580,1840,1660),
         "Fora do escopo: informar a limitação e orientar sobre os caminhos disponíveis.", small)
centered(d,(40,1680,1860,1720),
         "Modelo conceitual do projeto — não representa execução em uma plataforma.", small)
img.save(OUT / "fluxo-conversacional.png", optimize=True)

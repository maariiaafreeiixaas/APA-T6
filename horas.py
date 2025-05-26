"""
Maria Freixas Solé
Modulo para normalizar expresiones horarias en textos.
"""

import re

def normalizaHoras(ficText, ficNorm):
    # Expresiones horarias correctas comunes
    patrones = [
        #18h45m
        (re.compile(r'\b(\d{1,2})h(\d{1,2})m\b'), 
         lambda h, m: f"{int(h):02d}:{int(m):02d}" if int(h) < 24 and int(m) < 60 else f"{h}h{m}m"),
        
        #7h
        (re.compile(r'\b(\d{1,2})h\b'), 
         lambda h: f"{int(h):02d}:00" if int(h) < 24 else f"{h}h"),
        
        #8:05
        (re.compile(r'\b(\d{1,2}):(\d{2})\b'), 
         lambda h, m: f"{int(h):02d}:{int(m):02d}" if int(h) < 24 and int(m) < 60 else f"{h}:{m}"),
    ]

    with open(ficText, encoding="utf-8") as fin, open(ficNorm, "w", encoding="utf-8") as fout:
        for linea in fin:
            nueva = linea
            for patron, reemplazo in patrones:
                nueva = patron.sub(lambda m: reemplazo(*m.groups()), nueva)
            fout.write(nueva)
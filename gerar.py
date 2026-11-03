# Site principal da Real Time (SEO) · conta Leandro, 03/11/2026. Composição copiada do template GAFFER (Framer) na marca v1.
# Mesmo método do site da Desentupidora SF (gerar.py: uma página por serviço, FAQ, schema, sitemap, links internos).
# Gera: index.html (home), uma pasta por serviço, equipamentos/, sitemap.xml e robots.txt. O mini site da bio fica em bio/ (noindex).
# Uso: python3 gerar.py
import json, html, os, urllib.parse
BASE = 'https://realtimeslz.pages.dev'
WA = '5598991331727'
CIDADE = 'São Luís'   # a confirmar com o cliente (o briefing diz só "Maranhão"); ao confirmar, trocar aqui e gerar de novo
def wa(txt): return f'https://wa.me/{WA}?text=' + urllib.parse.quote(txt)
E = '/img/eq/'

# ---------- serviços (uma página cada) ----------
SERV = [
 dict(slug='aluguel-de-camera-sony-fx3', nav='Kit Cinema', cod='RT-CINEMA', foto=E+'sony-fx3.webp',
  title=f'Aluguel de Câmera Sony FX3 em {CIDADE} | Kit Cinema · Real Time',
  desc=f'Aluguel da câmera de cinema Sony FX3 em {CIDADE} (MA) com cage Tilta, matte box Tilta Mirage e transmissão sem fio Hollyland Pyro 7. Diária ou kit. Reserve pelo WhatsApp.',
  h1='Aluguel de câmera Sony FX3', sub='Kit Cinema completo, montado e pronto para a diária.',
  ficha=[('Câmera','Sony FX3'),('Estrutura','Cage Tilta'),('Matte box','Tilta Mirage'),('Monitor','Hollyland Pyro 7'),('Locação','Diária ou kit')],
  intro=['A Sony FX3 é a câmera de cinema compacta da linha Cinema Line: sensor full-frame, gravação em 4K e o perfil de cor S-Cinetone. Na Real Time ela sai pronta para gravar, no cage Tilta, com matte box e monitor sem fio.',
         'É a escolha de produtoras, videomakers e diretores de fotografia que precisam de imagem de cinema sem comprar equipamento.'],
  vem=[('Câmera Sony FX3','full-frame, 4K, S-Cinetone'),('Cage completo Tilta','alça superior e punho lateral'),('Matte box Tilta Mirage','com acessórios, segura filtros e controla reflexo'),('Hollyland Pyro 7','transmissão sem fio para o diretor e o cliente verem o take'),('Lentes e acessórios','à parte: VESPID Prime 2, Sony G Master e ZEISS')],
  para='Campanhas publicitárias, videoclipes, filmes de marca, documentários, eventos e conteúdo para redes.',
  ex='Uma produtora tem uma campanha de dois dias. Em vez de comprar um kit novo, reserva a FX3 com as lentes VESPID e o Pyro 7: o diretor acompanha o quadro no monitor, o cliente aprova na hora e o job sai com cara de cinema.',
  gal=[(E+'sony-fx3.webp','Sony FX3 · foto Henry Söderlund, Wikimedia Commons, CC BY 2.0'),(E+'kit-cinema-em-uso.webp','Cage Tilta para FX3 em uso · imagem Tilta'),(E+'tilta-mirage.webp','Matte box Tilta Mirage · imagem Tilta'),(E+'hollyland-pyro7.webp','Hollyland Pyro 7 · imagem Hollyland')],
  faq=[('Posso alugar só a câmera, sem o kit?','Sim. A locação pode ser só da câmera ou do kit completo. Fale no WhatsApp qual é a gravação que a gente indica a melhor opção.'),
       ('A FX3 grava em 4K?','Sim. A Sony FX3 grava em 4K e tem sensor full-frame, com o perfil de cor S-Cinetone das câmeras de cinema da Sony.'),
       ('Dá para usar lente de cinema PL na FX3?','Sim, com o adaptador Metabones PL–E, que também está disponível para locação junto com as lentes DZOFilm VESPID Prime 2.')]),
 dict(slug='aluguel-de-iluminacao-aputure', nav='Kit Luz', cod='RT-LUZ', foto=E+'aputure-storm-1200x.webp',
  title=f'Aluguel de Iluminação Aputure STORM em {CIDADE} | Kit Luz · Real Time',
  desc=f'Aluguel de iluminação profissional em {CIDADE} (MA): Aputure STORM 1200x, 400x e 80c, amaran 300c e modificadores. Locação avulsa ou por kit, com suporte técnico. Reserve pelo WhatsApp.',
  h1='Aluguel de iluminação Aputure', sub='Luz de cinema para estúdio, locação, chuva e diária longa.',
  ficha=[('Principal','STORM 1200x'),('Média','STORM 400x'),('Cor','STORM 80c ×3'),('Estúdio','amaran 300c'),('Locação','Avulsa ou kit')],
  intro=['A linha STORM da Aputure foi feita para set de verdade: estúdio, externa e diária longa. A Real Time aluga os refletores avulsos ou em kits montados para o porte da sua produção.',
         'Câmera boa com luz ruim entrega imagem ruim. A luz certa poupa tempo de edição e deixa a imagem com cara de cinema já na câmera.'],
  vem=[('Aputure STORM 1200x','bicolor, a luz principal da cena grande'),('Aputure STORM 400x','bicolor, força para entrevista e set médio'),('Aputure STORM 80c · 3 unidades','colorida, preenchimento, recorte e cor de fundo'),('amaran 300c','colorida, para estúdio e conteúdo'),('Modificadores','softbox e acessórios do inventário'),('Suporte técnico','opcional, para montar a luz com você')],
  para='Produtoras, diretores de fotografia, publicidade, videoclipes, entrevistas e projetos independentes.',
  ex='Numa gravação noturna na rua, a STORM 1200x faz a luz principal e as três 80c colorem o fundo. Para uma entrevista, uma 400x com difusor vira a luz do rosto e uma 80c separa a pessoa do fundo.',
  gal=[(E+'aputure-storm-1200x.webp','Aputure STORM 1200x · imagem Aputure'),(E+'aputure-storm-400x.webp','Aputure STORM 400x em locação · imagem Aputure'),(E+'aputure-storm-80c.webp','Aputure STORM 80c em uso · imagem Aputure'),(E+'aputure-storm-80c-chuva.webp','STORM 80c na chuva · imagem Aputure')],
  faq=[('Vocês alugam a luz com técnico?','Sim. A locação pode ser avulsa, por kit ou com suporte técnico para montar a luz na sua gravação.'),
       ('Qual kit de luz escolher para uma entrevista?','Em geral, uma luz principal (STORM 400x com difusor) e uma ou duas STORM 80c para preencher e separar do fundo. Conte a gravação no WhatsApp e a gente monta o kit.'),
       ('A STORM pode ser usada em externa?','A linha STORM foi feita para trabalho de set, inclusive em externa. Confirme no WhatsApp as condições da sua gravação.')]),
 dict(slug='aluguel-de-lentes-de-cinema', nav='Lentes', cod='RT-CINEMA', foto=E+'dzofilm-vespid-prime-2.webp',
  title=f'Aluguel de Lentes de Cinema em {CIDADE} | DZOFilm VESPID, Sony e ZEISS · Real Time',
  desc=f'Aluguel de lentes em {CIDADE} (MA): kit de cinema DZOFilm VESPID Prime 2, Sony G Master (14mm, 24–70mm, 90mm Macro), Sony 85mm, ZEISS 35mm e 50mm e adaptador Metabones PL–E. Por lente ou kit.',
  h1='Aluguel de lentes de cinema', sub='Kit Ópticas: VESPID Prime 2, Sony e ZEISS, por lente ou o conjunto.',
  ficha=[('Cinema','VESPID Prime 2'),('Zoom','24–70 GM ×2'),('Retrato','85mm F1.8'),('ZEISS','35 e 50 F1.4'),('Adaptador','Metabones PL–E')],
  intro=['Lente muda a imagem: foco, fundo desfocado e o mesmo visual em todas as cenas. A Real Time reúne o kit de cinema DZOFilm VESPID Prime 2 e as lentes Sony e ZEISS do inventário numa oferta só.',
         'Você aluga só a lente que a cena pede ou o conjunto inteiro. Com o adaptador Metabones PL–E, as lentes de cinema vão na Sony FX3 do Kit Cinema.'],
  vem=[('Kit DZOFilm VESPID Prime 2','lentes de cinema'),('Sony FE 14mm F1.8 GM','grande-angular'),('Sony FE 24–70mm F2.8 GM · 2 unidades','zoom para quase tudo'),('Sony FE 85mm F1.8','retrato e entrevista'),('Sony FE 90mm F2.8 Macro G OSS','detalhe e produto'),('ZEISS Distagon T* FE 35mm F1.4 ZA','plano médio natural'),('ZEISS Planar T* FE 50mm F1.4 ZA','o clássico 50'),('Adaptador Metabones PL–E Mount','lente PL na câmera Sony')],
  para='Publicidade, videoclipes, filmes, documentários, entrevistas e vídeo de produto.',
  ex='Num clipe, o plano aberto vai com uma lente grande-angular e o close com uma lente longa, todas VESPID, com a mesma cor. Num vídeo de produto, a 90mm Macro mostra cada detalhe do acabamento.',
  gal=[(E+'dzofilm-vespid-prime-2.webp','Kit DZOFilm VESPID Prime 2 · imagem DZOFilm'),(E+'sony-24-70-gm.webp','Sony FE 24–70mm F2.8 GM · Wikimedia Commons (CC)'),(E+'zeiss-50mm.webp','ZEISS Planar 50mm F1.4 ZA · Wikimedia Commons (CC)'),(E+'sony-85mm.webp','Sony FE 85mm F1.8 · Sony, Wikimedia Commons (CC)'),(E+'sony-14mm-gm.webp','Sony FE 14mm F1.8 GM · Wikimedia Commons (CC)'),(E+'metabones-pl-e.webp','Metabones PL–E · imagem Metabones')],
  faq=[('Posso alugar só uma lente?','Sim. A locação é por lente ou pelo conjunto, conforme a cena pede.'),
       ('As lentes VESPID encaixam na Sony FX3?','Sim, com o adaptador Metabones PL–E Mount, que também está disponível.'),
       ('Qual lente é melhor para entrevista?','A Sony FE 85mm F1.8 deixa o rosto nítido e o fundo suave. Para plano mais aberto, a ZEISS 35mm ou a 24–70mm GM.')]),
 dict(slug='estudio-com-fundo-verde-chroma-key', nav='Estúdio', cod='RT-ESTUDIO', foto=E+'gravacao-chroma-key.webp',
  title=f'Estúdio com Fundo Verde (Chroma Key) em {CIDADE} | Real Time',
  desc=f'Estúdio com fundo verde (chroma key) para alugar em {CIDADE} (MA): grave campanhas, videocasts, entrevistas e conteúdo, com teleprompter e intercomunicadores. Reserve a data pelo WhatsApp.',
  h1='Estúdio com fundo verde (chroma key)', sub='Estúdio pronto: fundo verde, luz e equipe. É só gravar.',
  ficha=[('Fundo','Chroma key'),('Texto','Teleprompter'),('Equipe','6 intercoms'),('Luz','Kit Luz Aputure'),('Reserva','Por data')],
  intro=['Gravar em casa ou no escritório quase sempre dá no mesmo: luz ruim, barulho e um fundo que não combina com a marca. No estúdio da Real Time o fundo verde já está montado, com a luz pronta.',
         'O fundo verde some na edição e no lugar dele entra o cenário que você quiser: a cor da sua marca, uma cidade, um gráfico, um ambiente 3D.'],
  vem=[('Fundo verde (chroma key)','montado, com a grade de luz do estúdio'),('Teleprompter SmallRig com tablet','para falar olhando para a câmera'),('Intercomunicadores Hollyland · 6 unidades','a equipe fala no set sem fio'),('Kit Luz e Kit Cinema','à parte, para completar a gravação')],
  para='Campanhas, videocasts e programas, entrevistas e vídeos corporativos, aulas, foto e vídeo de produto e conteúdo para redes.',
  ex='Uma empresa precisa de quatro vídeos de lançamento. Grava tudo numa manhã, no fundo verde, com a luz pronta e o texto no teleprompter. Na edição, cada vídeo ganha um cenário diferente, sem trocar de locação.',
  gal=[('/img/rt-mascote.webp','Gravação no estúdio da Real Time'),('/img/rt-estudio.webp','Estúdio da Real Time'),(E+'teleprompter-smallrig.webp','Teleprompter SmallRig · imagem SmallRig'),(E+'intercomunicador-hollyland.webp','Intercomunicadores Hollyland · imagem Hollyland')],
  faq=[('O que é chroma key?','É a técnica do fundo verde: na edição, o verde é substituído por qualquer imagem ou cenário.'),
       ('Posso alugar o estúdio com câmera e luz?','Sim. O estúdio pode ser alugado sozinho ou com o Kit Cinema e o Kit Luz.'),
       ('Tem teleprompter no estúdio?','Sim, teleprompter SmallRig com tablet, para quem fala para a câmera.')]),
 dict(slug='produtora-de-video', nav='Produções', cod='RT-PROD', foto=E+'kit-cinema-em-uso.webp',
  title=f'Produtora de Vídeo em {CIDADE} | Campanhas e Filmes de Marca · Real Time Produções',
  desc=f'Produtora de vídeo em {CIDADE} (MA): campanhas publicitárias, filmes de marca, vídeos corporativos, documentários, videoclipes e eventos, do roteiro à entrega com a mesma equipe. Peça um orçamento.',
  h1='Produtora de vídeo', sub='Realtime Produções: da ideia ao filme pronto, com a mesma equipe.',
  ficha=[('Etapa 1','Conceito e roteiro'),('Etapa 2','Orçamento'),('Etapa 3','Pré-produção'),('Etapa 4','Direção e gravação'),('Etapa 5','Edição e entrega')],
  intro=['Contratar roteirista, equipe de set e editor separados dá trabalho e quase sempre gera retrabalho. Na Realtime Produções o projeto vai da ideia ao final com a mesma equipe e a estrutura de cinema da Real Time.',
         'Quem escreveu o roteiro está no set. Quem esteve no set acompanha a edição. A ideia chega ao final do jeito que foi pensada.'],
  vem=[('Campanhas publicitárias','para TV e redes'),('Filmes de marca e vídeos corporativos','para empresas e instituições'),('Documentários','histórias reais, cultura e território'),('Videoclipes','para artistas e gravadoras'),('Eventos','cobertura e conteúdo')],
  para='Agências, marcas, empresas e instituições.',
  ex='Uma marca quer um filme para o lançamento de um produto. A equipe escreve o roteiro, monta o set no estúdio, grava, edita e entrega o filme pronto para as redes e para a TV.',
  gal=[('/img/rt-set.webp','Set da Real Time'),('/img/rt-filme.webp','Produção da Real Time'),('/img/rt-musico.webp','Videoclipe · Real Time'),('/img/rt-apresentadora.webp','Gravação no estúdio · Real Time')],
  faq=[('Quanto custa produzir um vídeo?','Depende do roteiro, dos dias de gravação e da edição. Mande a ideia pelo WhatsApp e a Real Time prepara um orçamento por projeto.'),
       ('Vocês fazem o roteiro?','Sim. O projeto completo começa no conceito e no roteiro e vai até a entrega.'),
       ('Atendem agências?','Sim. A Realtime Produções atende agências, marcas, empresas e instituições.')]),
 dict(slug='producao-de-conteudo-para-empresas', nav='Conteúdo mensal', cod='RT-MENSAL', foto=E+'gravacao-chroma-key.webp',
  title=f'Produção de Conteúdo em Vídeo para Empresas em {CIDADE} | Realtime Conteúdo',
  desc=f'Produção de vídeo todo mês para empresas em {CIDADE} (MA): entrevistas, corporativo, campanhas digitais, videocasts e programas, gravados no estúdio da Real Time e entregues prontos para postar.',
  h1='Conteúdo em vídeo para empresas', sub='Realtime Conteúdo: vídeo todo mês, sem montar set.',
  ficha=[('Entrevistas','e corporativo'),('Campanhas','digitais'),('Videocasts','e programas'),('Captação','e pós-produção'),('Contrato','Mensal ou pacote')],
  intro=['A sua empresa sabe que precisa postar vídeo, mas toda gravação vira uma maratona: achar lugar, câmera, luz e alguém para editar. No fim, o vídeo não sai.',
         'Na Realtime Conteúdo a sua empresa grava no estúdio da Real Time, com calendário combinado, e recebe os vídeos prontos para postar.'],
  vem=[('Entrevistas e vídeos corporativos','para a marca e para o time'),('Campanhas para redes sociais','no formato de cada rede'),('Videocasts e programas','gravados no estúdio'),('Captação e pós-produção','edição, cor e som')],
  para='Empresas, marcas, agências e instituições que precisam de vídeo com frequência.',
  ex='Uma clínica reserva uma manhã por mês no estúdio. A equipe grava as dicas do mês de uma vez e recebe os vídeos editados, no formato de Reels, para postar nas semanas seguintes.',
  gal=[('/img/rt-apresentadora.webp','Gravação no estúdio da Real Time'),('/img/rt-mascote.webp','Fundo verde · Real Time'),(E+'teleprompter-smallrig.webp','Teleprompter SmallRig · imagem SmallRig')],
  faq=[('Como funciona o contrato mensal?','A empresa combina um calendário de gravações no estúdio e recebe os vídeos prontos. Pode ser contrato mensal ou pacote.'),
       ('Vocês editam os vídeos?','Sim, captação e pós-produção (edição, cor e som) fazem parte do serviço.'),
       ('Preciso levar equipamento?','Não. O estúdio, a câmera, a luz e o teleprompter são da Real Time.')]),
]
# ---------- inventário (lista do cliente, 20/10) ----------
INV = [('Iluminação',[('Aputure STORM 80c','3 un.'),('Aputure STORM 1200x','1 un.'),('Aputure STORM 1200 (modelo a confirmar)','1 un.'),('Aputure STORM 400x','1 un.'),('amaran 300c (modelo a confirmar)','1 un.')],'aluguel-de-iluminacao-aputure'),
       ('Lentes de cinema',[('Kit DZOFilm VESPID Prime 2','1 kit')],'aluguel-de-lentes-de-cinema'),
       ('Lentes Sony e ZEISS',[('Sony FE 14mm F1.8 GM','1 un.'),('Sony FE 85mm F1.8','1 un.'),('ZEISS Distagon T* FE 35mm F1.4 ZA','1 un.'),('ZEISS Planar T* FE 50mm F1.4 ZA','1 un.'),('Sony FE 24–70mm F2.8 GM','2 un.'),('Sony FE 90mm F2.8 Macro G OSS','1 un.')],'aluguel-de-lentes-de-cinema'),
       ('Adaptadores',[('Metabones PL–E Mount','1 un.')],'aluguel-de-lentes-de-cinema'),
       ('Câmera Sony FX3',[('Câmera Sony FX3','1 un.'),('Cage completo Tilta para Sony FX3','1 un.'),('Matte box Tilta Mirage com acessórios','1 kit'),('Transmissão sem fio Hollyland Pyro 7','1 sistema')],'aluguel-de-camera-sony-fx3'),
       ('Teleprompter',[('Teleprompter SmallRig','1 un.'),('Tablet para o teleprompter','1 un.')],'estudio-com-fundo-verde-chroma-key'),
       ('Comunicação de equipe',[('Intercomunicadores Hollyland','kit com 6')],'estudio-com-fundo-verde-chroma-key')]

def topo():
    links = ''.join(f'<a href="/{s["slug"]}/">{s["nav"]}</a>' for s in SERV[:5]) + '<a href="/equipamentos/">Equipamentos</a>'
    return f'<header class="top"><div class="w"><a href="/" aria-label="Real Time, início"><img src="/img/assinatura-horizontal.svg" alt="Real Time · Full Jobs"></a><nav aria-label="Páginas">{links}</nav><a class="btn" href="{wa("Oi! Vim pelo site da Real Time e quero reservar.")}" target="_blank" rel="noopener">Reservar</a></div></header>'
def rodape():
    s1 = ''.join(f'<a href="/{s["slug"]}/">{s["nav"]}</a>' for s in SERV)
    return f'''<section class="w"><div class="cta-fim"><h2>Tem um job<br><span style="color:var(--cz2)">para gravar?</span></h2><div><p style="color:var(--cz);max-width:380px;margin-bottom:18px">Diga a data e o que vai gravar. A gente indica o kit certo e confirma a disponibilidade.</p><a class="btn" href="{wa("Oi! Quero reservar com a Real Time. A gravação é no dia: ")}" target="_blank" rel="noopener">Reservar no WhatsApp</a></div></div></section>
<footer class="rod"><div class="w"><div class="cols"><div><b>Real Time · Full Jobs</b>Locação de equipamentos audiovisuais, estúdio com fundo verde e produção de vídeo em {CIDADE} e no Maranhão.<br><br>WhatsApp <a href="https://wa.me/{WA}" style="display:inline">(98) 99133-1727</a></div><div><b>Serviços</b>{s1}</div><div><b>Site</b><a href="/">Início</a><a href="/equipamentos/">Equipamentos</a><a href="/bio/">Links da bio</a></div><div><b>Siga</b><a href="https://www.instagram.com/realtime_fulljobs/" target="_blank" rel="noopener">Instagram @realtime_fulljobs</a></div></div>
<div class="gigante" aria-hidden="true">real<b>time</b></div><div class="baixo"><span>© 2026 Real Time · RT Full Jobs</span><span>Fotos de produto: fabricantes e Wikimedia Commons (créditos em cada foto)</span><span class="rec">Seu job é na Real Time</span></div></div></footer>
<a class="btn wa-fixo" href="{wa("Oi! Vim pelo site da Real Time.")}" target="_blank" rel="noopener">WhatsApp</a>'''
EMP = {"@type": "LocalBusiness", "@id": BASE + "/#empresa", "name": "Real Time · RT Full Jobs", "alternateName": ["Realtime", "RT Full Jobs", "Real Time BR"],
       "description": "Locação de equipamentos audiovisuais, estúdio com fundo verde (chroma key) e produção audiovisual para marcas e empresas.", "url": BASE + "/",
       "logo": BASE + "/img/apple-touch-icon.png", "image": BASE + "/img/og.jpg", "telephone": "+55-98-99133-1727", "sameAs": ["https://www.instagram.com/realtime_fulljobs/"],
       "areaServed": [{"@type": "City", "name": CIDADE}, {"@type": "State", "name": "Maranhão"}], "priceRange": "Sob consulta"}
def doc(path, title, desc, corpo, ld, img=BASE + '/img/og.jpg'):
    url = BASE + path
    return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large"><meta name="geo.region" content="BR-MA"><meta name="geo.placename" content="{CIDADE}"><meta name="theme-color" content="#0E0E0F">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Real Time · RT Full Jobs">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/img/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Geist+Mono:wght@500&display=swap" rel="stylesheet"><link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": ld}, ensure_ascii=False)}</script></head>
<body>{topo()}<main>{corpo}</main>{rodape()}</body></html>'''
def migalha(itens):
    vis = ' / '.join(f'<a href="{u}">{n}</a>' if i < len(itens) - 1 else n for i, (n, u) in enumerate(itens))
    ld = {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u} for i, (n, u) in enumerate(itens)]}
    return f'<div class="migalha">{vis}</div>', ld
def faq_html(fq):
    return '<div class="faq">' + ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in fq) + '</div>', \
           {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in fq]}
def visor(foto, tc, alt=''):
    return f'<div class="visor"><i></i><i></i><i></i><i></i><div class="f" role="img" aria-label="{html.escape(alt)}" style="background-image:url({foto})"></div><span class="r rec">REC</span><span class="tc">{tc}</span></div>'

# ---------- páginas de serviço ----------
for n, s in enumerate(SERV, 1):
    mg, ldm = migalha([('Início', '/'), (s['nav'], f'/{s["slug"]}/')])
    fh, ldf = faq_html(s['faq'])
    ficha = ''.join(f'<div><small>{k}</small>{v}</div>' for k, v in s['ficha'])
    vem = ''.join(f'<li><b>{a}</b> · {b}</li>' for a, b in s['vem'])
    gal = ''.join(f'<figure><img src="{f}" alt="{html.escape(c.split(" · ")[0])}" loading="lazy" width="600" height="450"><figcaption>{html.escape(c)}</figcaption></figure>' for f, c in s['gal'])
    rel = ''.join(f'<a href="/{o["slug"]}/"><span class="mono">{o["nav"]}</span><h3 style="margin-top:8px">{o["h1"]}</h3></a>' for o in SERV if o is not s)[:]
    rel_l = [o for o in SERV if o is not s][:3]
    rel = ''.join(f'<a href="/{o["slug"]}/"><span class="mono">{o["nav"]}</span><h3 style="margin-top:8px">{o["h1"]}</h3></a>' for o in rel_l)
    zap = wa(f'Oi! Vim pelo site e quero saber sobre: {s["nav"]}. Código {s["cod"]}')
    corpo = f'''<section class="heroi"><div class="bg" style="background-image:url({s["foto"]})"></div><div class="w" style="padding-bottom:60px">{mg}
<div class="mono rec">{s["nav"]} · {CIDADE} · Maranhão</div><h1 class="h" style="margin-top:14px">{s["h1"]}<br><span style="color:var(--cz)">em {CIDADE}</span></h1>
<p class="lead">{s["sub"]}</p><a class="btn" href="{zap}" target="_blank" rel="noopener">Reservar no WhatsApp</a>
<div class="ficha" style="position:relative;left:0;right:0;bottom:0;margin-top:56px">{ficha}</div></div></section>
<section class="sec"><div class="w duas"><div class="txt">{"".join(f"<p>{p}</p>" for p in s["intro"])}<h2>O que vem</h2><ul>{vem}</ul><h2>Para quem é</h2><p>{s["para"]}</p><h2>Na prática</h2><p>{s["ex"]}</p>
<a class="btn" href="{zap}" target="_blank" rel="noopener">Consultar disponibilidade</a></div><div style="position:sticky;top:90px">{visor(s["gal"][0][0], f"00:00:0{n}:00", s["gal"][0][1])}</div></div></section>
<section class="sec"><div class="w"><div class="cab"><h2>Fotos</h2><span class="mono">Equipamento e set</span></div><div class="gal">{gal}</div></div></section>
<section class="sec"><div class="w"><div class="cab"><h2>Perguntas<br><span style="color:var(--cz2)">frequentes</span></h2></div>{fh}</div></section>
<section class="sec"><div class="w"><div class="cab"><h2>Veja também</h2></div><div class="rel">{rel}</div></div></section>'''
    ld = [EMP, ldm, ldf, {"@type": "Service", "name": s['h1'] + ' em ' + CIDADE, "serviceType": s['nav'], "description": s['desc'], "provider": {"@id": BASE + "/#empresa"}, "areaServed": CIDADE, "url": f'{BASE}/{s["slug"]}/'}]
    os.makedirs(s['slug'], exist_ok=True)
    open(f'{s["slug"]}/index.html', 'w').write(doc(f'/{s["slug"]}/', s['title'], s['desc'], corpo, ld, BASE + s['foto']))

# ---------- equipamentos ----------
mg, ldm = migalha([('Início', '/'), ('Equipamentos', '/equipamentos/')])
k = 0; blocos = ''
for cat, itens, link in INV:
    linhas = ''
    for nome, q in itens:
        k += 1; linhas += f'<a href="/{link}/"><span class="n">{k:02d}</span><h3>{html.escape(nome)}</h3><span class="c">{cat}</span><span class="q">{q}</span></a>'
    blocos += f'<div style="margin-bottom:40px"><div class="mono" style="margin-bottom:10px">{cat}</div><div class="lista">{linhas}</div></div>'
desc_eq = f'Lista completa de equipamentos audiovisuais para locação em {CIDADE} (MA): câmera Sony FX3, lentes DZOFilm VESPID, Sony e ZEISS, luz Aputure STORM e amaran, teleprompter e intercomunicadores.'
corpo = f'''<section class="heroi"><div class="w" style="padding-bottom:50px">{mg}<div class="mono rec">Inventário · levantamento de 20/10/2026</div><h1 class="h" style="margin-top:14px">Equipamentos<br><span style="color:var(--cz)">para locação</span></h1>
<p class="lead">Tudo o que a Real Time tem para o seu job, por categoria. Toque em um item para ver o kit. Disponibilidade por data: confirme no WhatsApp.</p></div></section>
<section class="sec"><div class="w">{blocos}</div></section>'''
os.makedirs('equipamentos', exist_ok=True)
open('equipamentos/index.html', 'w').write(doc('/equipamentos/', f'Equipamentos Audiovisuais para Locação em {CIDADE} | Real Time', desc_eq, corpo, [EMP, ldm]))

# ---------- home (GAFFER) ----------
lista_her = ''.join(f'<li><span>{i:02d}</span><a href="/{s["slug"]}/">{s["nav"]}</a></li>' for i, s in enumerate(SERV, 1))
kits = ''.join(f'''<a class="kit" href="/{s["slug"]}/"><div class="f" style="background-image:url({s["foto"]})"></div><div class="t"><span class="mono rec">{s["h1"]}</span><h3>{s["nav"]}</h3></div><div class="ficha">{"".join(f"<div><small>{a}</small>{b}</div>" for a, b in s["ficha"])}</div></a>''' for s in SERV[:4])
k = 0; full = ''
for cat, itens, link in INV:
    for nome, q in itens:
        k += 1
        if k <= 10: full += f'<a href="/{link}/"><span class="n">{k:02d}</span><h3>{html.escape(nome)}</h3><span class="c">{cat}</span><span class="q">{q}</span></a>'
ways = [('Locação de equipamentos', 'Câmera, lentes e luz por diária, avulsos ou em kits montados.', '/aluguel-de-camera-sony-fx3/'),
        ('Estúdio com fundo verde', 'Chroma key montado, teleprompter e intercom. Reserve a data.', '/estudio-com-fundo-verde-chroma-key/'),
        ('Conteúdo todo mês', 'A sua empresa grava no estúdio e recebe os vídeos prontos para postar.', '/producao-de-conteudo-para-empresas/'),
        ('Produções completas', 'Campanhas, filmes de marca, clipes e documentários, do roteiro à entrega.', '/produtora-de-video/')]
ways_h = ''.join(f'<a href="{u}"><span class="mono">{i:02d}</span><h3>{t}</h3><p>{d}</p><span class="seta">↗</span></a>' for i, (t, d, u) in enumerate(ways, 1))
etapas = [('Mensagem', 'Você diz a data e o que vai gravar pelo WhatsApp.'), ('Kit indicado', 'A gente sugere o equipamento certo para o seu tipo de gravação.'),
          ('Reserva', 'Data bloqueada, condições combinadas e lembrete na véspera.'), ('Gravação', 'Equipamento pronto e testado. Suporte técnico se você quiser.'),
          ('Devolução', 'Conferência do kit e, se quiser, a gente posta o bastidor do seu job.')]
etapas_h = ''.join(f'<div class="etapa"><span class="mono">0{i} · etapa</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(etapas, 1))
HFAQ = [('A Real Time aluga equipamento por diária?', 'Sim. Câmera, lentes e luz podem ser alugados por diária, avulsos ou em kits.'),
        (f'Onde fica o estúdio com fundo verde?', f'O estúdio fica em {CIDADE}, no Maranhão. Peça a localização e as datas livres pelo WhatsApp.'),
        ('Vocês fazem a produção do vídeo inteiro?', 'Sim. A Realtime Produções faz campanhas, filmes de marca, corporativos, documentários e videoclipes, do roteiro à entrega.'),
        ('Como reservo?', 'Pelo WhatsApp (98) 99133-1727: diga a data e o que vai gravar, e a gente confirma a disponibilidade.')]
fh, ldf = faq_html(HFAQ)
corpo = f'''<section class="heroi"><div class="bg" style="background-image:url(/img/eq/kit-cinema-em-uso.webp)"></div><div class="w"><div class="lin"><div><div class="mono rec">Locação · Estúdio · Produções · {CIDADE} · MA</div>
<h1 class="h" style="margin-top:16px;font-size:clamp(30px,4.6vw,52px)">Locação de equipamentos audiovisuais<br><span style="color:var(--cz)">e estúdio em {CIDADE}</span></h1>
<p class="lead">Câmera, lente, luz e estúdio de cinema prontos para a sua gravação. E uma equipe para produzir o seu vídeo do roteiro à entrega.</p>
<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="{wa("Oi! Vim pelo site da Real Time e quero reservar.")}" target="_blank" rel="noopener">Reservar no WhatsApp</a><a class="btn ln" href="/equipamentos/">Ver equipamentos</a></div></div>
<ul aria-label="Serviços">{lista_her}</ul></div><div class="gigante" aria-hidden="true">real<b>time</b></div></div></section>
<section class="sec"><div class="w"><div class="cab"><h2>Kits prontos<br><span style="color:var(--cz2)">para a sua diária</span></h2><a class="mono" href="/equipamentos/">Ver tudo ↗</a></div>{kits}</div></section>
<section class="w"><div class="manif">Seu job<br><span>é na Real Time.</span></div></section>
<section class="sec"><div class="w"><div class="cab"><h2>O inventário</h2><a class="mono" href="/equipamentos/">Lista completa ↗</a></div><div class="lista">{full}</div></div></section>
<section class="sec"><div class="w"><div class="cab"><h2>Quatro formas<br><span style="color:var(--cz2)">de trabalhar com a gente</span></h2></div><div class="ways">{ways_h}</div></div></section>
<section class="sec"><div class="w"><div class="nums" style="background-image:url(/img/eq/aputure-storm-80c.webp)"><div class="in"><h2>Estúdio pequeno.<br>Imagem de cinema.</h2>
<div class="g"><div><b>7 mil</b><span class="mono">seguidores no Instagram</span></div><div><b>6</b><span class="mono">refletores Aputure STORM</span></div><div><b>6</b><span class="mono">intercomunicadores</span></div><div><b>1</b><span class="mono">estúdio com fundo verde</span></div></div></div></div></div></section>
<section class="sec"><div class="w proc"><div class="gruda"><div class="mono">Como funciona</div><h2 style="margin-top:12px">Da mensagem<br><span style="color:var(--cz2)">à diária</span></h2><p style="color:var(--cz);margin:16px 0 24px;max-width:380px">Cinco passos, tudo pelo WhatsApp. Sem formulário.</p>{visor("/img/rt-kit.webp", "00:00:05:00", "Kit de câmera da Real Time")}</div><div>{etapas_h}</div></div></section>
<section class="sec"><div class="w"><div class="cab"><h2>Perguntas<br><span style="color:var(--cz2)">frequentes</span></h2></div>{fh}</div></section>'''
open('index.html', 'w').write(doc('/', f'Locação de Equipamentos Audiovisuais em {CIDADE} | Real Time · RT Full Jobs',
     f'Locação de equipamentos audiovisuais em {CIDADE} (MA): câmera Sony FX3, lentes de cinema DZOFilm, Sony e ZEISS, luz Aputure STORM, estúdio com fundo verde (chroma key) e produção de vídeo. Reserve pelo WhatsApp.',
     corpo, [EMP, {"@type": "WebSite", "url": BASE + "/", "name": "Real Time · RT Full Jobs", "inLanguage": "pt-BR"}, ldf]))

# ---------- sitemap e robots ----------
urls = ['/'] + [f'/{s["slug"]}/' for s in SERV] + ['/equipamentos/']
open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{BASE}{u}</loc><changefreq>monthly</changefreq><priority>{"1.0" if u == "/" else "0.8"}</priority></url>\n' for u in urls) + '</urlset>\n')
open('robots.txt', 'w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
print('páginas:', len(urls), '+ bio/')

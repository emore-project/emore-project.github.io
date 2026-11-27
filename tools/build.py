#!/usr/bin/env python3
"""Generate the static pages (header, footer and accessibility options are shared). Run: python3 tools/build.py"""
import os, random, math
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAV = [("index.html", "Home"), ("about.html", "About"), ("research.html", "Research"), ("team.html", "Team"), ("funding.html", "Funding")]
UPDATED = "25 November 2026"

def svgicon(p): return f'<span class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false">{p}</svg></span>'
I = {
 "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "sliders": '<path d="M4 6h8M18 6h2M4 12h2M12 12h8M4 18h10M20 18h0"/><circle cx="15" cy="6" r="2"/><circle cx="9" cy="12" r="2"/><circle cx="17" cy="18" r="2"/>',
 "tree": '<circle cx="12" cy="5" r="2"/><circle cx="6" cy="19" r="2"/><circle cx="18" cy="19" r="2"/><path d="M12 7v4M12 11H6v6M12 11h6v6"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5L16 9.5"/>',
 "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 "funnel": '<path d="M3 4h18l-7 8v7l-4 2v-9z"/>',
 "loop": '<path d="M20 12a8 8 0 1 1-3-6.2"/><path d="M20 4v5h-5"/>',
}
A11Y_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="4.5" r="2"/><path d="M5 8.5h14M12 8.5v5M12 13.5l-3.5 6.5M12 13.5l3.5 6.5"/></svg>'
LOGO_FULL_ALT = "Spanish Ministry of Science, Innovation and Universities; co-funded by the European Union; State Research Agency"

def page(fname, title, desc, body, head_extra=""):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV)
    full = "E-MORE" if fname == "index.html" else f"{title} · E-MORE"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://emore-project.github.io/assets/og-image.png">
<meta name="theme-color" content="#17222F">
<link rel="icon" type="image/svg+xml" href="assets/icons/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="assets/icons/favicon-32.png">
<link rel="apple-touch-icon" href="assets/icons/apple-touch-icon.png">
<link rel="stylesheet" href="css/style.css">
<script src="assets/js/a11y.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html"><img src="assets/logos/emore-dark-800.png" alt="E-MORE – Efficient Models of Multimodal Representations, home" width="800" height="229"></a>
<div class="head-right">
<nav class="nav" aria-label="Main">{links}</nav>
<div class="a11y">
<button type="button" id="a11y-btn" class="a11y-btn" aria-expanded="false" aria-controls="a11y-panel">{A11Y_ICON}<span>Accessibility</span></button>
<div id="a11y-panel" class="a11y-panel" role="group" aria-labelledby="a11y-title" hidden>
<p id="a11y-title" class="a11y-title">Display options</p>
<label><input type="checkbox" data-opt="contrast"> High contrast</label>
<label><input type="checkbox" data-opt="text"> Larger text</label>
<label><input type="checkbox" data-opt="spacing"> Wider text spacing</label>
<label><input type="checkbox" data-opt="links"> Underline all links</label>
<div class="a11y-actions"><button type="button" id="a11y-reset" class="a11y-reset">Reset</button><a href="accessibility.html">Accessibility statement</a></div>
</div>
</div>
</div>
</div></header>
<main id="main" tabindex="-1">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<p>E-MORE – Efficient Models of Multimodal Representations. Grant PID2025-170489NB-I00 funded by MICIU/AEI/10.13039/501100011033 and by ESF+. Universitat de Barcelona, Facultat de Matemàtiques i Informàtica.</p>
<div class="flogos"><img src="assets/logos/micin-ue-aei.png" alt="" width="2521" height="369"><img src="assets/logos/ub.png" alt="" width="1734" height="465"></div>
<nav class="foot-nav" aria-label="Footer"><ul><li><a href="accessibility.html">Accessibility statement</a></li><li><a href="https://github.com/emore-project/emore-project.github.io">Website source on GitHub</a></li></ul></nav>
</div></footer>
</body>
</html>
'''

def write(fname, *a, **k):
    open(os.path.join(ROOT, fname), "w", encoding="utf-8").write(page(fname, *a, **k))

def pillar(ic, t, d): return f'<div class="card"><{"span"} class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false">{I[ic]}</svg></span><h3>{t}</h3><p>{d}</p></div>'

# ---- index
write("index.html", "Home", "E-MORE develops efficient, trustworthy and structured models for multimodal AI. A research project of the Universitat de Barcelona.", f'''<section class="hero"><div class="wrap hero-grid">
<div class="hero-text">
<p class="eyebrow">Research project · Universitat de Barcelona</p>
<h1>Efficient Models of Multimodal Representations</h1>
<p class="lead">E-MORE studies how to build multimodal AI models that are compact, adaptable and trustworthy, so that they can learn from and reason about vision, language, audio and more without prohibitive computational cost.</p>
<a class="btn" href="about.html">About the project</a><a class="btn ghost" href="research.html">Research lines</a>
</div>
<div class="hero-visual"><picture><source media="(max-width:48rem)" srcset="assets/img/converge-mobile.svg"><img src="assets/img/converge.svg" alt="Diagram: vision, text, audio, skeleton and 3D data converge into one efficient shared representation that is compact, adaptable and trustworthy." width="960" height="420"></picture></div>
</div></section>
<section><div class="wrap">
<h2>What E-MORE is about</h2>
<div class="pillars">
{pillar("bolt","Efficient","Smaller, cheaper models that keep their performance.")}
{pillar("sliders","Adaptable","Quick specialization to new tasks and modalities.")}
{pillar("tree","Structured","Representations that capture hierarchy and meaning.")}
{pillar("shield","Trustworthy","Privacy, unlearning and auditability by design.")}
</div>
</div></section>
<section class="band"><div class="wrap">
<h2>At a glance</h2>
<dl class="facts">
<div><dt>Project</dt><dd>PID2025-170489NB-I00</dd></div>
<div><dt>Host</dt><dd>Universitat de Barcelona</dd></div>
<div><dt>Duration</dt><dd>3 years, from September 2026</dd></div>
<div><dt>Funded by</dt><dd>MICIU / AEI</dd></div>
</dl>
</div></section>
<section><div class="wrap">
<h2>Explore</h2>
<div class="grid">
<div class="card"><h3>About</h3><p>The motivation, the goals and the setting of the project.</p><a class="more" href="about.html">Read more<span class="sr-only"> about the project</span></a></div>
<div class="card"><h3>Research</h3><p>The scientific lines that E-MORE pursues, from efficient adaptation to trustworthy AI.</p><a class="more" href="research.html">Read more<span class="sr-only"> about the research lines</span></a></div>
<div class="card"><h3>Funding</h3><p>The funding bodies and the host institution of the project.</p><a class="more" href="funding.html">Read more<span class="sr-only"> about the funding</span></a></div>
</div></div></section>''')

# ---- about
write("about.html", "About", "Motivation, goals and setting of the E-MORE project on efficient multimodal representations.", '''<div class="page-head"><div class="wrap"><h1>About E-MORE</h1><p>Efficient Models of Multimodal Representations</p></div></div>
<section><div class="wrap">
<h2>Why this project</h2>
<p>Large multimodal models have changed vision–language learning. They combine massive pretraining data with powerful architectures and transfer remarkably well to new tasks. Adapting and deploying them, however, remains costly because of their size, their modality-specific components and their task-specific requirements.</p>
<p>E-MORE addresses this gap. Its aim is to make multimodal models efficient to adapt and run, without giving up robustness, reliability or the ability to handle heterogeneous modalities such as images, text, audio, skeletons or 3D data.</p>
<h2>What we want to achieve</h2>
<p>The project brings together several complementary ideas: parameter-efficient adaptation, compact models obtained by distillation, learning strategies based on reinforcement learning, structured and geometric representations, and methods for trustworthy and privacy-aware AI. Together they aim at multimodal models that are smaller, more adaptable and easier to trust.</p>
<h2>Where it takes place</h2>
<p>E-MORE is carried out at the Facultat de Matemàtiques i Informàtica of the Universitat de Barcelona, and is the continuation of previous work of the group on multimodal learning.</p>
</div></section>
<section class="band"><div class="wrap">
<h2>From large to compact</h2>
<p>A central idea of the project is to transfer the knowledge of very large multimodal models into compact ones that are cheaper to adapt, easier to deploy and more robust.</p>
<div class="panel-wrap panel"><picture><source media="(max-width:40rem)" srcset="assets/img/distill-mobile.svg"><img src="assets/img/distill.svg" alt="Diagram: a large multimodal model, costly to adapt and run, is distilled into a compact model that is efficient, robust and adaptable." width="900" height="360"></picture></div>
</div></section>''')

# ---- research
cards = [("Efficient adaptation","layers","Parameter-efficient fine-tuning, quantization and cross-modal transfer to specialize large models at a small fraction of the cost."),
 ("Multimodal distillation","funnel","Transferring the knowledge of very large multimodal models into compact students that stay robust and adaptable."),
 ("Reinforcement learning for adaptation","loop","Learning to prompt and adapt multimodal systems, with reward models that take several modalities into account."),
 ("Structured representations","tree","Geometric and neurosymbolic representations that capture hierarchy and meaning beyond flat embeddings."),
 ("Trustworthy multimodal AI","shield","Unlearning, privacy and auditability for multimodal models, so that they can be used responsibly.")]
cardhtml = "".join(f'<div class="card">{svgicon(I[ic])}<h3>{t}</h3><p>{d}</p></div>' for t, ic, d in cards)
write("research.html", "Research", "The research lines of E-MORE: efficient adaptation, distillation, reinforcement learning, structured representations and trustworthy AI.", f'''<div class="page-head"><div class="wrap"><h1>Research</h1><p>The scientific lines of the project. More detail will be added as the work advances.</p></div></div>
<section><div class="wrap">
<h2>Research lines</h2>
<div class="panel hide-sm"><img src="assets/img/hub.svg" alt="Diagram: the five research lines of E-MORE (efficient adaptation, multimodal distillation, reinforcement learning, structured representations and trustworthy AI) arranged around the project." width="1040" height="480"></div>
<div class="grid" style="margin-top:2rem">{cardhtml}</div>
</div></section>''')


# ---- team
# url: personal web page (add later); orcid: public ORCID iD. Source: project proposal.
RESEARCH = [
 ("Sergio Escalera", "Principal investigator", "Full Professor", "0000-0003-0617-8873", ""),
 ("Xavier Baró", "Principal investigator", "Associate Professor", "0000-0001-5338-3007", ""),
 ("Jordi Vitrià", "Researcher", "Full Professor", "0000-0003-1484-539X", ""),
 ("Oriol Pujol", "Researcher", "Full Professor", "0000-0001-7573-009X", ""),
 ("Laura Igual", "Researcher", "Associate Professor", "0000-0002-7225-7441", ""),
 ("Mireia Ribera", "Researcher", "Associate Professor", "0000-0003-1455-1869", ""),
 ("Santi Segui", "Researcher", "Associate Professor", "0000-0002-8603-138X", ""),
 ("Eloi Puertas", "Researcher", "Lecturer", "0000-0001-6292-6448", ""),
 ("Nahuel Statuto", "Researcher", "Assistant Professor", "0000-0002-0062-760X", ""),
 ("Albert Clapés", "Researcher", "Assistant Professor", "0000-0002-4089-9060", ""),
 ("Julio C. S. Jacques Junior", "Researcher", "Assistant Professor", "0000-0001-6785-7146", ""),
 ("Muriel Rovira", "Researcher", "Assistant Professor", "0000-0003-0331-258X", ""),
]
WORK = [
 ("Artur Xarles", "Universitat de Barcelona", "0000-0002-0800-0270", ""),
 ("David Pujol-Perich", "", "0000-0001-8853-8486", ""),
 ("Phat Truong", "", "0009-0009-1188-0051", ""),
 ("Michal Choinski", "", "0009-0004-1545-0108", ""),
 ("Iñaki Erregue", "", "0009-0004-1943-5554", ""),
 ("Oriol Camacho", "", "0000-0001-6950-7211", ""),
 ("Marc Soler", "", "0000-0001-8039-7842", ""),
 ("Arnau Barrera", "", "0009-0008-4594-3965", ""),
 ("Oriol Rabasseda", "", "0009-0007-5121-1317", ""),
 ("Meysam Madadi", "", "0000-0002-7384-5712", ""),
 ("Cristina Palmero", "King\u2019s College London", "0000-0002-6085-6527", ""),
]
def member(name, line1, line2, orcid, url):
    nm = f'<a href="{url}">{name}</a>' if url else name
    meta = "".join(f'<p class="role">{x}</p>' for x in (line1, line2) if x)
    oc = f'<a class="orcid" href="https://orcid.org/{orcid}">ORCID<span class="sr-only"> profile of {name}</span></a>' if orcid else ""
    return f'<li class="card member"><h3>{nm}</h3>{meta}{oc}</li>'
rteam = "".join(member(n, r, a, o, u) for n, r, a, o, u in RESEARCH)
wteam = "".join(member(n, a, "", o, u) for n, a, o, u in WORK)
write("team.html", "Team", "The research team and the work team of the E-MORE project at the Universitat de Barcelona.", f'''<div class="page-head"><div class="wrap"><h1>Team</h1><p>The people behind E-MORE, at the Universitat de Barcelona and partner institutions.</p></div></div>
<section><div class="wrap">
<h2>Research team</h2>
<p>Faculty of the Universitat de Barcelona who lead and carry out the research of the project.</p>
<ul class="grid team">{rteam}</ul>
</div></section>
<section class="band"><div class="wrap">
<h2>Work team</h2>
<p>Early-career researchers and collaborators who contribute to the work of the project.</p>
<ul class="grid team">{wteam}</ul>
</div></section>''')

# ---- funding
write("funding.html", "Funding", "Funding bodies and host institution of the E-MORE project PID2025-170489NB-I00.", f'''<div class="page-head"><div class="wrap"><h1>Funding</h1><p>Institutions and funding bodies behind E-MORE.</p></div></div>
<section><div class="wrap">
<h2>Funded by</h2>
<p>E-MORE is a project of the call “<span lang="es">Proyectos de Generación de Conocimiento 2025</span>”, funded by the Spanish Ministry of Science, Innovation and Universities and the State Research Agency, and co-funded by the European Union through the European Social Fund Plus (ESF+). It is hosted by the Universitat de Barcelona.</p>
<div class="logos"><img src="assets/logos/micin-ue-aei.png" alt="{LOGO_FULL_ALT}" width="2521" height="369"><img src="assets/logos/ub.png" alt="Universitat de Barcelona" width="1734" height="465"></div>
</div></section>''')

# ---- accessibility statement
write("accessibility.html", "Accessibility statement", "Accessibility statement of the E-MORE website: standard, current status, available options and how to report problems.", f'''<div class="page-head"><div class="wrap"><h1>Accessibility statement</h1><p>Last reviewed: {UPDATED}</p></div></div>
<section><div class="wrap">
<h2>Our commitment</h2>
<p>We want the E-MORE website to be usable by everyone. We design it to meet the Web Content Accessibility Guidelines (WCAG) 2.2, level AA.</p>
<h2>Current status</h2>
<p>This is a <strong>self-assessment</strong>; the website has not been audited or certified by an external body. We believe it meets WCAG 2.2 AA for the checks below, with the limitations listed further down.</p>
<h3>How it was checked</h3>
<ul class="plain">
<li>Automated tests with axe-core on every page.</li>
<li>Calculation of colour contrast for all text and interface colours, in the default and in the high-contrast display.</li>
<li>Manual review of structure: headings, landmarks, links, images and keyboard navigation.</li>
</ul>
<h2>What you can do on this site</h2>
<ul class="plain">
<li><strong>Display options</strong> (button “Accessibility” in the header): high contrast, larger text, wider text spacing and underlined links. Your choice is remembered in your browser.</li>
<li>High contrast turns on automatically if your system asks for more contrast.</li>
<li>Skip link to jump to the main content, and a visible focus indicator for keyboard use.</li>
<li>All pages work with the keyboard alone, with browser zoom up to 200 % and on small screens.</li>
<li>Images and diagrams have text descriptions. No content moves or plays automatically.</li>
</ul>
<h2>Known limitations</h2>
<ul class="plain">
<li>We have not yet tested with screen readers on every platform.</li>
<li>Diagrams are described in text, but the description is a summary of what they show.</li>
<li>The names of some institutions and calls are in Spanish; text is marked with its language, but image descriptions are not.</li>
</ul>
<h2>Report a problem</h2>
<p>If you find a barrier or need information in another format, please tell us by opening an issue at <a href="https://github.com/emore-project/emore-project.github.io/issues">the project’s issue tracker on GitHub</a>. Describe the page and the difficulty you had.</p>
</div></section>''')
print("pages ok")

# ---- mobile distill svg
F = "font-family=\"Calibri,'Segoe UI',system-ui,-apple-system,Arial,sans-serif\""
INK="#1F2F44";SLATE="#34495E";MIST="#9FB4C7";AQUA="#4FB3BF";AMBER="#E9A23B";PAPER="#DCE4EC"
random.seed(4)
W,H=420,620;cx=210
g=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="A large multimodal model is distilled into a compact model">'
tcy,tr=130,100
g+=f'<circle cx="{cx}" cy="{tcy}" r="{tr}" fill="{SLATE}" stroke="{MIST}" stroke-width="2"/>'
for i in range(55):
    a=random.random()*2*math.pi;r=math.sqrt(random.random())*(tr-12)
    g+=f'<circle cx="{cx+r*math.cos(a):.1f}" cy="{tcy+r*math.sin(a):.1f}" r="{random.choice([4,5,6,8])}" fill="{[MIST,AQUA,PAPER][i%3]}" opacity=".75"/>'
g+=f'<text x="{cx}" y="{tcy+tr+36}" text-anchor="middle" {F} font-size="21" font-weight="700" fill="{PAPER}">Large multimodal model</text><text x="{cx}" y="{tcy+tr+62}" text-anchor="middle" {F} font-size="17" fill="{MIST}">costly to adapt and run</text>'
ay=tcy+tr+90
g+=f'<path d="M{cx} {ay} V{ay+70}" stroke="{AMBER}" stroke-width="3.5"/><path d="M{cx-12} {ay+58} l12 14 12 -14" fill="none" stroke="{AMBER}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><text x="{cx+26}" y="{ay+42}" {F} font-size="20" font-weight="700" fill="{AMBER}">distillation</text>'
scy=ay+135
g+=f'<circle cx="{cx}" cy="{scy}" r="68" fill="none" stroke="{AMBER}" stroke-width="1.5" opacity=".5" stroke-dasharray="3 6"/><circle cx="{cx}" cy="{scy}" r="48" fill="{INK}" stroke="{AQUA}" stroke-width="2.5"/>'
for i,(dx,dy,r) in enumerate([(-18,-13,8),(13,-20,6),(22,6,7),(-5,16,8),(-24,13,5),(5,-2,5)]):
    g+=f'<circle cx="{cx+dx}" cy="{scy+dy}" r="{r}" fill="{[AQUA,PAPER,AMBER][i%3]}" opacity=".9"/>'
g+=f'<text x="{cx}" y="{scy+100}" text-anchor="middle" {F} font-size="21" font-weight="700" fill="{PAPER}">Compact model</text><text x="{cx}" y="{scy+126}" text-anchor="middle" {F} font-size="17" fill="{MIST}">efficient, robust, adaptable</text></svg>'
open(os.path.join(ROOT,"assets/img/distill-mobile.svg"),"w").write(g)
print("svg ok")

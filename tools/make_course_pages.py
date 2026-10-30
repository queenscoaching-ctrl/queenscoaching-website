"""Builds QueensCoaching course pages from one shared template.
Usage: python3 make_course_pages.py <site_folder>
To add a course page later: add an entry to COURSES and re-run.
"""
import json, sys, os, html

SITE = "https://queenscoaching.ca"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfSMPITgPyIUz1aoePzP-xrCxtcTHLrMQD9j2fo_-lP_f5hBA/viewform"

COURSES = [
    {
        "slug": "sch4u-chemistry-tutor-ottawa",
        "code": "SCH4U", "short": "Grade 12 Chemistry",
        "title": "SCH4U Chemistry Tutor in Ottawa & Online | QueensCoaching",
        "desc": "1-on-1 Grade 12 Chemistry (SCH4U) tutoring in Ottawa and online. Every unit from organic chemistry to electrochemistry, with personalized notes and stationery included. Book a free assessment.",
        "h1": "Grade 12 Chemistry (SCH4U) Tutor in Ottawa & Online",
        "intro": "Personalized 1-on-1 SCH4U coaching that closes Grade 11 gaps while covering every unit, from organic chemistry to electrochemistry. Notes and stationery included.",
        "facts": [("Course", "Chemistry, Grade 12, University Preparation"), ("Prerequisite", "SCH3U, Grade 11 Chemistry"), ("Units", "5 strands, from organic to electrochemistry"), ("Needed for", "Many health science, life science and engineering programs"), ("Format", "1-on-1, in person in Ottawa or online")],
        "units": [
            ("Organic Chemistry", "Naming, functional groups, reactions and polymers.", "bonding and molecular shape"),
            ("Structure & Properties", "Atomic models, electron configuration, intermolecular forces.", "periodic trends"),
            ("Energy Changes & Rates", "Enthalpy, Hess's law, calorimetry and reaction rates.", "unit conversions and algebra"),
            ("Chemical Systems & Equilibrium", "Le Châtelier's principle, K values, acids, bases and pH.", "stoichiometry and the mole"),
            ("Electrochemistry", "Oxidation-reduction, galvanic and electrolytic cells.", "balancing equations"),
        ],
        "plus": "Unit test and final exam prep, lab report writing, and optional Waterloo Chem 13 News Exam practice.",
        "gap_line": "Most SCH4U struggles trace back to a Grade 11 skill, like the mole or balancing equations. We find those gaps in the free assessment and close them as we go.",
        "faq": [
            ("Is SCH4U hard?", "It is one of the most demanding Grade 12 courses, mostly because it builds on SCH3U skills. With the basics rebuilt, it becomes very manageable."),
            ("Do I need SCH4U for university?", "Many Ontario health science, life science and engineering programs require it. Check each program's admission requirements, and we can help you plan."),
            ("When should we start tutoring?", "Ideally at the start of the semester, or in the summer before. We also help students who join mid-course to catch up before the final exam."),
            ("Can you help with online or summer school SCH4U?", "Yes. We follow the same Ontario curriculum whether your child takes SCH4U in day school, summer school or online."),
        ],
        "related": [("SCH3U", "Grade 11 Chemistry", "/sch3u-chemistry-tutor-ottawa/"), ("SBI4U", "Grade 12 Biology", None), ("MHF4U", "Advanced Functions", None), ("MCV4U", "Calculus & Vectors", None), ("SPH4U", "Grade 12 Physics", None)],
    },
    {
        "slug": "sch3u-chemistry-tutor-ottawa",
        "code": "SCH3U", "short": "Grade 11 Chemistry",
        "title": "SCH3U Chemistry Tutor in Ottawa & Online | QueensCoaching",
        "desc": "1-on-1 Grade 11 Chemistry (SCH3U) tutoring in Ottawa and online. Master bonding, reactions, the mole, solutions and gases, with personalized notes and stationery included. Book a free assessment.",
        "h1": "Grade 11 Chemistry (SCH3U) Tutor in Ottawa & Online",
        "intro": "Personalized 1-on-1 SCH3U coaching for a student's first real chemistry course. We build the foundation that Grade 12 Chemistry and university depend on. Notes and stationery included.",
        "facts": [("Course", "Chemistry, Grade 11, University Preparation"), ("Prerequisite", "SNC2D, Grade 10 Science (academic)"), ("Units", "5 strands, from bonding to gases"), ("Leads to", "SCH4U, Grade 12 Chemistry"), ("Format", "1-on-1, in person in Ottawa or online")],
        "units": [
            ("Matter, Chemical Trends & Bonding", "Atomic structure, the periodic table, ionic and covalent bonds.", "Grade 10 atoms and ions"),
            ("Chemical Reactions", "Reaction types, writing and balancing equations.", "chemical formulas and naming"),
            ("Quantities in Chemical Reactions", "The mole, molar mass, stoichiometry and percentage yield.", "ratios, fractions and unit conversions"),
            ("Solutions & Solubility", "Concentration, dilution, solubility and acids and bases.", "rearranging formulas"),
            ("Gases & Atmospheric Chemistry", "Gas laws, the ideal gas law and air quality.", "algebra with several variables"),
        ],
        "plus": "Unit test and final exam prep, lab report writing, and optional Waterloo Avogadro Exam practice.",
        "gap_line": "SCH3U is where many students first meet the mole and stoichiometry. Most struggles trace back to fractions, ratios or algebra, so we check those in the free assessment and fix them as we go.",
        "faq": [
            ("Is SCH3U hard?", "It is a big step up from Grade 10 Science because of the math involved. Students who get help with the mole and stoichiometry early usually do well."),
            ("Do I need SCH3U?", "SCH3U is the prerequisite for SCH4U, which many Ontario health science, life science and engineering programs require."),
            ("When should we start tutoring?", "At the start of the course, or before the Quantities in Chemical Reactions unit, where most students first struggle."),
            ("Can you help with online or summer school SCH3U?", "Yes. We follow the same Ontario curriculum whether your child takes SCH3U in day school, summer school or online."),
        ],
        "related": [("SCH4U", "Grade 12 Chemistry", "/sch4u-chemistry-tutor-ottawa/"), ("SBI3U", "Grade 11 Biology", None), ("MCR3U", "Grade 11 Functions", None), ("SPH3U", "Grade 11 Physics", None), ("SNC2D", "Grade 10 Science", None)],
    },
    {
        "slug": "sbi4u-biology-tutor-ottawa",
        "code": "SBI4U", "short": "Grade 12 Biology",
        "crumb_name": "Biology", "crumb_href": "/#courses", "nav": "Courses", "badge": "Grade 12 · University",
        "title": "SBI4U Biology Tutor in Ottawa & Online | QueensCoaching",
        "desc": "1-on-1 Grade 12 Biology (SBI4U) tutoring in Ottawa and online. Biochemistry, metabolism, genetics, homeostasis and population dynamics, with personalized notes and stationery included. Book a free assessment.",
        "h1": "Grade 12 Biology (SBI4U) Tutor in Ottawa & Online",
        "intro": "Personalized 1-on-1 SBI4U coaching for students heading into health science, life science and nursing programs. We make the big ideas stick and the details easy to remember. Notes and stationery included.",
        "facts": [("Course", "Biology, Grade 12, University Preparation"), ("Prerequisite", "SBI3U, Grade 11 Biology"), ("Units", "5 strands, from biochemistry to population dynamics"), ("Needed for", "Many health science, life science and nursing programs"), ("Format", "1-on-1, in person in Ottawa or online")],
        "units": [
            ("Biochemistry", "Biological molecules, enzymes and how cell membranes work.", "Grade 11 Chemistry basics: bonding and functional groups"),
            ("Metabolic Processes", "Cellular respiration and photosynthesis, step by step.", "energy and chemical reaction basics"),
            ("Molecular Genetics", "DNA replication, protein synthesis, gene regulation and biotechnology.", "Grade 11 genetics and cell division"),
            ("Homeostasis", "The nervous, endocrine and excretory systems and feedback loops.", "Grade 11 body systems"),
            ("Population Dynamics", "Population growth, carrying capacity and human impact.", "reading graphs and working with data"),
        ],
        "plus": "Unit test and final exam prep, lab report writing, and help with diagrams and long-answer questions.",
        "gap_line": "SBI4U has a lot of detail, and much of it builds on Grade 11 Biology and Chemistry. We check those foundations in the free assessment, then teach memory techniques and clear summaries so students can recall it all on test day.",
        "faq": [
            ("Is SBI4U hard?", "It is content-heavy rather than math-heavy. Students who organize the material well and practise applying it usually do very well."),
            ("Do I need SBI4U for university?", "Many Ontario health science, life science, kinesiology and nursing programs require it. Check each program's admission requirements, and we can help you plan."),
            ("Does SBI4U need Chemistry?", "SBI4U builds on SBI3U, and the Biochemistry and Metabolism units use Grade 11 Chemistry ideas. We fill any Chemistry gaps as we go."),
            ("Can you help with online or summer school SBI4U?", "Yes. We follow the same Ontario curriculum whether your child takes SBI4U in day school, summer school or online."),
        ],
        "related": [("SCH4U", "Grade 12 Chemistry", "/sch4u-chemistry-tutor-ottawa/"), ("SBI3U", "Grade 11 Biology", None), ("SCH3U", "Grade 11 Chemistry", "/sch3u-chemistry-tutor-ottawa/"), ("MHF4U", "Advanced Functions", None), ("SPH4U", "Grade 12 Physics", None)],
    },
    {
        "slug": "mpm2d-math-tutor-ottawa",
        "code": "MPM2D", "short": "Grade 10 Math",
        "crumb_name": "Math", "crumb_href": "/#courses", "nav": "Courses", "badge": "Grade 10 · Advanced (academic)",
        "unit_label": "Strand",
        "title": "MPM2D Grade 10 Math Tutor in Ottawa & Online | QueensCoaching",
        "desc": "1-on-1 Grade 10 Academic Math (MPM2D) tutoring in Ottawa and online. Quadratics, analytic geometry and trigonometry, with personalized notes and stationery included. Book a free assessment.",
        "h1": "Grade 10 Math (MPM2D) Tutor in Ottawa & Online",
        "intro": "Personalized 1-on-1 MPM2D coaching for Grade 10 Advanced (academic) Math. We fix Grade 9 gaps while covering quadratics, analytic geometry and trigonometry. Notes and stationery included.",
        "facts": [("Course", "Principles of Mathematics, Grade 10, Academic"), ("Prerequisite", "MTH1W, Grade 9 Math"), ("Strands", "Quadratics, analytic geometry, trigonometry"), ("Leads to", "MCR3U, Grade 11 Functions"), ("Format", "1-on-1, in person in Ottawa or online")],
        "units": [
            ("Quadratic Relations", "Graphing parabolas, expanding, factoring and solving quadratic equations.", "integers, exponents and Grade 9 algebra"),
            ("Analytic Geometry", "Linear systems, distance, midpoint and properties of shapes on the grid.", "slope and equations of lines"),
            ("Trigonometry", "Similar triangles, the primary trig ratios and the sine and cosine laws.", "ratios, proportions and rearranging formulas"),
        ],
        "plus": "Unit test and final exam prep, plus a head start on MCR3U so Grade 11 Functions feels familiar.",
        "gap_line": "MPM2D is where algebra becomes essential. Most struggles come from Grade 9 skills like integers, exponents or solving equations, so we check those in the free assessment and close the gaps as we go.",
        "faq": [
            ("What is the difference between MPM2D and MFM2P?", "MPM2D is the academic (Advanced) Grade 10 Math course and leads to MCR3U. MFM2P is the applied (Basic) course with more hands-on problems. We tutor both."),
            ("Is MPM2D hard?", "It is a big step up in algebra, especially factoring and quadratics. With strong Grade 9 foundations, most students do well."),
            ("Why does MPM2D matter?", "It is the usual prerequisite for MCR3U, Grade 11 Functions, which leads to the Grade 12 university math courses."),
            ("When should we start tutoring?", "At the start of the semester, or as soon as factoring or quadratics feel shaky. Early help is much easier than catching up."),
        ],
        "related": [("MTH1W", "Grade 9 Math", "/mth1w-grade-9-math-tutor-ottawa/"), ("MFM2P", "Grade 10 Basic Math", None), ("MCR3U", "Grade 11 Functions", None), ("SNC2D", "Grade 10 Science", None), ("MHF4U", "Advanced Functions", None)],
    },
    {
        "slug": "mth1w-grade-9-math-tutor-ottawa",
        "code": "MTH1W", "short": "Grade 9 Math",
        "crumb_name": "Math", "crumb_href": "/#courses", "nav": "Courses", "badge": "Grade 9 · EQAO prep included",
        "unit_label": "Strand",
        "title": "MTH1W Grade 9 Math Tutor & EQAO Prep in Ottawa | QueensCoaching",
        "desc": "1-on-1 Grade 9 Math (MTH1W) tutoring and EQAO prep in Ottawa and online. Number, algebra, data, geometry and financial literacy, with personalized notes and stationery included. Book a free assessment.",
        "h1": "Grade 9 Math (MTH1W) Tutor & EQAO Prep in Ottawa & Online",
        "intro": "Personalized 1-on-1 MTH1W coaching for Ontario's Grade 9 de-streamed Math course, including preparation for the EQAO Grade 9 Math assessment. We build the foundation every later math course depends on.",
        "facts": [("Course", "Mathematics, Grade 9, de-streamed"), ("Assessment", "EQAO Grade 9 Math, written online, counts toward the final mark"), ("Strands", "Number, algebra, data, geometry and measurement, financial literacy"), ("Leads to", "MPM2D (academic) or MFM2P (applied)"), ("Format", "1-on-1, in person in Ottawa or online")],
        "units": [
            ("Number", "Rational numbers, powers and exponent rules, and proportional reasoning.", "fractions, decimals and percentages"),
            ("Algebra", "Expressions, equations, linear relations and coding.", "order of operations and integers"),
            ("Data", "Collecting, displaying and analysing data, and making predictions.", "reading graphs and tables"),
            ("Geometry & Measurement", "Area, volume, angle relationships and optimization.", "formulas and units of measure"),
            ("Financial Literacy", "Budgets, interest and smart money decisions.", "percentages and rates"),
        ],
        "plus": "EQAO Grade 9 Math practice in the online format, plus unit test and final exam prep.",
        "gap_line": "Grade 9 Math brings together everything from elementary school. Gaps in fractions, integers or percentages show up fast, so we check them in the free assessment and fix them while teaching MTH1W.",
        "faq": [
            ("Does EQAO count toward my child's mark?", "Yes. EQAO Grade 9 Math results are included in the final MTH1W course mark. We prepare students for its online format."),
            ("What does de-streamed mean?", "Since 2021, all Ontario Grade 9 students take the same math course, MTH1W, instead of choosing academic or applied."),
            ("What comes after MTH1W?", "Most students take MPM2D (academic) in Grade 10, which leads to university math. Others take MFM2P (applied). We help you choose."),
            ("When should we start tutoring?", "Ideally at the start of Grade 9, or in the summer after Grade 8 to strengthen the basics before high school."),
        ],
        "related": [("MPM2D", "Grade 10 Math", "/mpm2d-math-tutor-ottawa/"), ("MFM2P", "Grade 10 Basic Math", None), ("SNC1W", "Grade 9 Science", None), ("SNC2D", "Grade 10 Science", None), ("SCH3U", "Grade 11 Chemistry", "/sch3u-chemistry-tutor-ottawa/")],
    },
]

e = html.escape

HEAD_FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'

LOGO = '<svg width="48" height="48" viewBox="0 0 80 80" aria-hidden="true"><path d="M12 30 L17 10 L28 22 L40 4 L52 22 L63 10 L68 30 Z" fill="#D4A73C"/><path d="M6 36 Q22 30 39 37 V74 Q22 67 6 73 Z" fill="#4B2A7B"/><path d="M74 36 Q58 30 41 37 V74 Q58 67 74 73 Z" fill="#6B45A3"/></svg>'

WA_ICON = '<svg width="30" height="30" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7.5-.1 1.5-.6 1.8-1.2.2-.6.2-1.1.1-1.2l-.4-.2z"/></svg>'

FOOTER = '''<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-col">
      <strong style="font-family:var(--serif);font-size:24px">QueensCoaching</strong>
      <span>Grade 9–12 Math &amp; Science coaching. In person in Ottawa, online worldwide.</span>
      <a class="hl" href="mailto:myqueenscoaching@gmail.com">myqueenscoaching@gmail.com</a>
      <a class="hl" href="tel:+16132976844">+1 613.297.6844</a>
    </div>
    <div class="footer-col"><strong>Courses</strong><a href="/mth1w-grade-9-math-tutor-ottawa/">MTH1W Grade 9 Math</a><a href="/mpm2d-math-tutor-ottawa/">MPM2D Grade 10 Math</a><a href="/sch3u-chemistry-tutor-ottawa/">SCH3U Chemistry</a><a href="/sch4u-chemistry-tutor-ottawa/">SCH4U Chemistry</a><a href="/sbi4u-biology-tutor-ottawa/">SBI4U Biology</a><a href="/#courses">All courses</a></div>
    <div class="footer-col"><strong>Exam prep</strong><a href="/#exams">EQAO Grade 9 Math</a><a href="/#exams">SAT &amp; ACT</a><a href="/#exams">AP &amp; IB</a><a href="/#exams">GCSE &amp; A-levels</a><a href="/#exams">CBSE &amp; NEET</a></div>
    <div class="footer-col"><strong>Get started</strong><a href="/#book">Book a free assessment</a><a href="https://wa.me/16132976844">WhatsApp us</a><a href="/#faq">FAQ</a></div>
  </div>
  <div class="wrap footer-legal">
    <p>Disclaimer: Results vary by learner. QueensCoaching is an independent tutoring service and is not affiliated with any school board, university or exam body, including EQAO, College Board, ACT, the International Baccalaureate Organization, Cambridge, CBSE, Qualifications Scotland or the University of Waterloo. Exam names are trademarks of their owners.</p>
    <p>© 2026 QueensCoaching</p>
  </div>
</footer>'''


def page(c):
    url = f"{SITE}/{c['slug']}/"
    course_ld = {
        "@context": "https://schema.org", "@type": "Course",
        "name": f"{c['code']} {c['short']} Tutoring",
        "courseCode": c["code"], "description": c["desc"],
        "provider": {"@type": "EducationalOrganization", "@id": f"{SITE}/#business", "name": "QueensCoaching", "url": SITE + "/"},
        "hasCourseInstance": [
            {"@type": "CourseInstance", "courseMode": "Onsite", "location": "Ottawa, ON"},
            {"@type": "CourseInstance", "courseMode": "Online"},
        ],
    }
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]}
    crumb_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": c.get("crumb_name", "Chemistry"), "item": SITE + c.get("crumb_href", "/#chemistry")},
        {"@type": "ListItem", "position": 3, "name": f"{c['code']} {c['short']}", "item": url}]}
    lds = "\n".join(f'<script type="application/ld+json">\n{json.dumps(x, ensure_ascii=False, indent=2)}\n</script>' for x in (course_ld, faq_ld, crumb_ld))

    facts = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in c["facts"])
    units = "".join(
        f'<article class="unit"><p class="num">{c.get("unit_label", "Unit")} {i}</p><h3>{e(t)}</h3><p>{e(d)}</p><p class="rebuild"><strong>Basics we rebuild:</strong> {e(b)}</p></article>'
        for i, (t, d, b) in enumerate(c["units"], 1))
    units += f'<article class="unit card-feature"><p class="num">Plus</p><h3>Exams &amp; lab reports</h3><p>{e(c["plus"])}</p></article>'
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in c["faq"])
    related = "".join(
        (f'<a class="pill" href="{h}"><strong>{e(code)}</strong> {e(n)}</a>' if h else f'<span class="pill"><strong>{e(code)}</strong> {e(n)}</span>')
        for code, n, h in c["related"])

    return f'''<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(c['title'])}</title>
<meta name="description" content="{e(c['desc'])}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#4B2A7B">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="QueensCoaching">
<meta property="og:title" content="{e(c['title'])}">
<meta property="og:description" content="{e(c['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
{HEAD_FONTS}
<link rel="stylesheet" href="/styles.css">
{lds}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <span>Grade 9–12 Math &amp; Science · Free assessment · In person in Ottawa · Online worldwide</span>
  <a href="tel:+16132976844">Call or WhatsApp +1 613.297.6844</a>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="logo" href="/" aria-label="QueensCoaching home">{LOGO}<span><span class="logo-name">QueensCoaching</span><span class="logo-tag">Rule your subject</span></span></a>
  <nav class="nav" aria-label="Main">
    <a href="/#courses"{' aria-current="page"' if c.get('nav') == 'Courses' else ''}>Courses</a>
    <a href="/sch4u-chemistry-tutor-ottawa/"{' aria-current="page"' if c.get('nav', 'Chemistry') == 'Chemistry' else ''}>Chemistry</a>
    <a href="/#exams">Exam Prep</a>
    <a href="/#method">How It Works</a>
    <a href="/#faq">FAQ</a>
  </nav>
  <a class="btn btn-gold" href="/#book">Book Free Assessment</a>
</div></header>

<main id="main">
<section class="brand">
  <div class="wrap"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="{c.get('crumb_href', '/#chemistry')}">{e(c.get('crumb_name', 'Chemistry'))}</a> › <span>{e(c['code'])} {e(c['short'])}</span></nav></div>
  <div class="wrap hero" style="display:grid;gap:48px;grid-template-columns:repeat(auto-fit,minmax(min(100%,460px),1fr));align-items:center;padding-top:40px;padding-bottom:72px">
    <div class="hero-copy">
      <span class="badge badge-solid">{e(c.get('badge', 'Signature program'))}</span>
      <h1 style="margin:0;font-family:var(--serif);font-weight:600;font-size:clamp(34px,4.4vw,54px);letter-spacing:-.02em;line-height:1.08">{e(c['h1'])}</h1>
      <p class="hero-sub">{e(c['intro'])}</p>
      <div class="btn-row">
        <a class="btn btn-gold" href="/#book">Book a Free {e(c['code'])} Assessment</a>
        <a class="btn btn-outline" href="https://wa.me/16132976844">WhatsApp us</a>
      </div>
    </div>
    <div class="white-card">
      <h2 style="margin:0;font-family:var(--serif);font-size:24px;font-weight:600;color:var(--purple)">{e(c['code'])} at a glance</h2>
      <dl class="facts">{facts}</dl>
    </div>
  </div>
</section>

<section class="section"><div class="wrap">
  <p class="eyebrow">What we cover</p>
  <h2 class="h2">Every {e(c['code'])} unit, and the basics behind it</h2>
  <p class="lead">For each unit we cover the course material and the earlier skill students most often need to rebuild.</p>
  <div class="grid-wide">{units}</div>
</div></section>

<section class="section alt"><div class="wrap grid-2">
  <div>
    <p class="eyebrow">Included with {e(c['code'])} coaching</p>
    <h2 class="h2">We fix the basics while we cover the curriculum.</h2>
    <p style="margin:0;font-size:18px;color:var(--ink-soft)">{e(c['gap_line'])}</p>
  </div>
  <ul class="check-list">
    <li><strong>Personalized notes</strong> for every unit, kept in a binder</li>
    <li><strong>All stationery included</strong>: notebooks, binders, worksheets</li>
    <li><strong>True 1-on-1 attention</strong> every session</li>
    <li><strong>Practice tests</strong> before every unit test and the final exam</li>
    <li><strong>Monthly progress note</strong> for parents</li>
  </ul>
</div></section>

<section class="section"><div class="wrap narrow">
  <h2 class="h2" style="margin-bottom:28px">{e(c['code'])} questions</h2>
  <div class="faq">{faqs}</div>
</div></section>

<section style="padding-bottom:80px"><div class="wrap">
  <h2 style="margin:0 0 16px;font-size:20px">Related courses</h2>
  <div class="pills">{related}</div>
</div></section>

<section class="section brand cta"><div class="wrap narrow">
  <h2>Ready to master {e(c['code'])}?</h2>
  <p>Book a free assessment with a foundations check. No obligation.</p>
  <div class="btn-row" style="justify-content:center">
    <a class="btn btn-gold" href="/#book">Book Free Assessment</a>
    <a class="btn btn-outline" href="https://wa.me/16132976844">Chat on WhatsApp</a>
  </div>
</div></section>
</main>

{FOOTER}

<a class="wa-float" href="https://wa.me/16132976844" aria-label="Chat with QueensCoaching on WhatsApp">{WA_ICON}</a>
</body>
</html>
'''


if __name__ == "__main__":
    root = sys.argv[1]
    for c in COURSES:
        d = os.path.join(root, c["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(c))
        print("wrote", c["slug"])

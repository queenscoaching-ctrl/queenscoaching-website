"""Builds QueensCoaching parent guides and subject hub pages, plus the /guides/ index.
Usage: python3 -I tools/make_guides.py <site_folder>
To add a guide: add an entry to GUIDES (kind "guide" or "hub"), add it to NAV_GUIDES in
make_course_pages.py if it should appear in the menu, add it to sitemap.xml, and re-run.
Rules: accurate to the Ontario curriculum, no invented statistics, results, testimonials or prices.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_course_pages import SITE, e, shell, ld, crumbs_ld, breadcrumb, cta_band  # noqa: E402

WA = "https://wa.me/16132976844"
PUBLISHED = "2026-11-13"

INLINE_CTA = ('<div class="inline-cta"><p>Not sure where the gaps are? A free assessment finds them, '
              'and you get a written plan within 24 hours.</p>'
              '<a class="btn btn-gold" href="/book/">Book Free Assessment</a></div>')

GUIDES = [
    {
        "slug": "is-sch3u-hard", "kind": "guide", "card": "Grade 11 Chemistry",
        "title": "Is SCH3U Hard? Grade 11 Chemistry Explained for Parents & Students | QueensCoaching",
        "desc": "Is SCH3U (Grade 11 Chemistry) hard? What makes it a step up, which units students find hardest, the warning signs, and how to do well. A plain-English guide for Ontario families.",
        "h1": "Is SCH3U hard? Grade 11 Chemistry explained",
        "sub": "A plain-English guide for Ontario parents and students: what makes SCH3U a step up, where students usually get stuck, and how to do well.",
        "answer": "SCH3U is a real step up from Grade 10 Science, mainly because it is the first course where chemistry becomes math-heavy. Most students find the Quantities in Chemical Reactions unit (the mole and stoichiometry) the hardest. With solid fractions, ratios and algebra, and steady practice, it is very manageable.",
        "sections": [
            ("What is SCH3U?", """<p>SCH3U is the Ontario Grade 11 Chemistry course, University Preparation. Its prerequisite is Grade 10 Science (SNC2D), and it leads to Grade 12 Chemistry (SCH4U). It has five content strands, plus scientific investigation skills that run through the whole course:</p>
<ul><li><strong>Matter, Chemical Trends and Chemical Bonding</strong>: atomic structure, the periodic table, ionic and covalent bonds</li>
<li><strong>Chemical Reactions</strong>: reaction types, writing and balancing equations</li>
<li><strong>Quantities in Chemical Reactions</strong>: the mole, molar mass, stoichiometry and percentage yield</li>
<li><strong>Solutions and Solubility</strong>: concentration, dilution, solubility, acids and bases</li>
<li><strong>Gases and Atmospheric Chemistry</strong>: the gas laws, the ideal gas law and air quality</li></ul>
<p>See the full <a href="/sch3u-chemistry-tutor-ottawa/">SCH3U course page</a> for how we coach each unit.</p>"""),
            ("Why do students find SCH3U hard?", """<p>SCH3U is not hard because students are "not science people". It is hard for four practical reasons:</p>
<ul><li><strong>A new language.</strong> Naming compounds and writing formulas feels like learning vocabulary in a new language, and everything after depends on it.</li>
<li><strong>Much more math.</strong> The mole, stoichiometry, concentration and the gas laws all use ratios, unit conversions, scientific notation and rearranging formulas.</li>
<li><strong>Each unit builds on the last.</strong> If balancing equations is shaky, stoichiometry falls apart. If stoichiometry is shaky, solutions and gases feel impossible.</li>
<li><strong>Lab reports.</strong> Many students have not written a full lab report with data, sources of error and conclusions before.</li></ul>"""),
            ("Which SCH3U units are hardest?", """<div class="table-wrap"><table class="compare"><thead><tr><th>Unit</th><th>What students find tricky</th><th>The basics behind it</th></tr></thead><tbody>
<tr><td>Bonding</td><td>Predicting bond type, drawing Lewis structures</td><td>Grade 10 atoms, ions and the periodic table</td></tr>
<tr><td>Chemical Reactions</td><td>Balancing equations, predicting products</td><td>Writing correct chemical formulas</td></tr>
<tr><td>Quantities (the mole)</td><td>Mole conversions, stoichiometry, limiting reagent</td><td>Fractions, ratios and unit conversions</td></tr>
<tr><td>Solutions</td><td>Concentration and dilution problems</td><td>Rearranging formulas</td></tr>
<tr><td>Gases</td><td>Choosing and using the right gas law</td><td>Algebra with several variables, units of temperature and pressure</td></tr>
</tbody></table></div>
<p>The mole unit is the turning point for most students. Getting help before or during it makes the rest of the course much smoother.</p>"""),
            ("Signs your teen needs help in SCH3U", """<ul><li>They understand it in class but blank on the test</li>
<li>Marks drop when the mole and stoichiometry unit starts</li>
<li>They can get an answer but cannot explain the steps</li>
<li>They spend hours on homework with little progress</li>
<li>Units and significant figures keep costing marks</li></ul>
<p>Each of these usually points to one or two specific gaps, often from Grade 9 or 10 math, rather than the whole course.</p>"""),
            ("How to do well in SCH3U", """<ul><li><strong>Master naming and formulas early.</strong> Short daily practice beats one long session.</li>
<li><strong>Learn one method for the mole</strong>, such as dimensional analysis, and use it every time.</li>
<li><strong>Write units on every number.</strong> Units catch most mistakes before the teacher does.</li>
<li><strong>Balance equations until it is automatic.</strong> Stoichiometry depends on it.</li>
<li><strong>Do practice tests</strong> before every unit test, under time, then review every mistake.</li></ul>"""),
            ("What parents can do", """<p>You do not need to remember chemistry to help:</p>
<ul><li>Ask your teen to teach you one step. Explaining it shows what they really understand.</li>
<li>Look at the course outline together and mark when the mole unit starts.</li>
<li>Get help early, before marks drop, not after the first low test.</li>
<li>Book a free assessment to find the exact gaps. We check the Grade 9 and 10 skills SCH3U depends on.</li></ul>"""),
            ("Do you need SCH3U for university?", """<p>SCH3U is the prerequisite for SCH4U, and SCH4U is required by many Ontario health science, life science and engineering programs. Requirements differ by program and university, so always check each program's admission page. Our guide <a href="/sch3u-vs-sch4u/">SCH3U vs SCH4U</a> explains what changes in Grade 12.</p>"""),
        ],
        "faq": [
            ("Is SCH3U harder than SBI3U?", "Many students find SCH3U more math-heavy than Grade 11 Biology, which has more reading and memorizing. Which feels harder depends on your teen's strengths."),
            ("What is the hardest unit in SCH3U?", "For most students it is Quantities in Chemical Reactions, which covers the mole and stoichiometry. It relies on fractions, ratios and unit conversions."),
            ("Can you help with SCH3U taken online or in summer school?", "Yes. We follow the same Ontario curriculum whether SCH3U is taken in day school, summer school or online."),
            ("When should we start SCH3U tutoring?", "At the start of the course, or at the latest before the mole unit. Students who join mid-course can still catch up before the final exam."),
        ],
        "related": [("SCH3U", "Grade 11 Chemistry", "/sch3u-chemistry-tutor-ottawa/"), ("SCH4U", "Grade 12 Chemistry", "/sch4u-chemistry-tutor-ottawa/"), ("SCH3U vs SCH4U", "Guide", "/sch3u-vs-sch4u/"), ("Chemistry", "Tutor in Ottawa", "/chemistry-tutor-ottawa/")],
    },
    {
        "slug": "sch3u-vs-sch4u", "kind": "guide", "card": "Grade 11 vs Grade 12 Chemistry",
        "title": "SCH3U vs SCH4U: What Changes in Grade 12 Chemistry | QueensCoaching",
        "desc": "SCH3U vs SCH4U compared: units, math level, prerequisites and who needs Grade 12 Chemistry. Which SCH3U skills matter most in SCH4U, and how to prepare. A guide for Ontario families.",
        "h1": "SCH3U vs SCH4U: what changes in Grade 12 Chemistry",
        "sub": "A side-by-side guide to Ontario Grade 11 and Grade 12 Chemistry, and the SCH3U skills that decide how SCH4U goes.",
        "answer": "SCH3U (Grade 11) builds the foundations: bonding, reactions, the mole, solutions and gases. SCH4U (Grade 12) applies them to university-level topics: organic chemistry, structure and properties, energy and rates, equilibrium and electrochemistry. SCH3U is the prerequisite for SCH4U, and most SCH4U struggles trace back to SCH3U skills.",
        "sections": [
            ("SCH3U and SCH4U side by side", """<div class="table-wrap"><table class="compare"><thead><tr><th></th><th>SCH3U · Grade 11</th><th>SCH4U · Grade 12</th></tr></thead><tbody>
<tr><td><strong>Course type</strong></td><td>University Preparation</td><td>University Preparation</td></tr>
<tr><td><strong>Prerequisite</strong></td><td>Grade 10 Science (SNC2D)</td><td>SCH3U</td></tr>
<tr><td><strong>Content strands</strong></td><td>Matter, chemical trends and bonding · Chemical reactions · Quantities in chemical reactions · Solutions and solubility · Gases and atmospheric chemistry</td><td>Organic chemistry · Structure and properties of matter · Energy changes and rates of reaction · Chemical systems and equilibrium · Electrochemistry</td></tr>
<tr><td><strong>Math</strong></td><td>Ratios, unit conversions, scientific notation, rearranging formulas</td><td>All of SCH3U, plus longer multi-step problems, equilibrium expressions and logarithms for pH</td></tr>
<tr><td><strong>Why it matters</strong></td><td>Prerequisite for SCH4U</td><td>Required by many health science, life science and engineering programs</td></tr>
</tbody></table></div>"""),
            ("Which SCH3U skills matter most in SCH4U?", """<ul><li><strong>Stoichiometry and the mole</strong> come back in energy changes, rates and equilibrium.</li>
<li><strong>Balancing equations</strong> becomes balancing redox reactions in electrochemistry.</li>
<li><strong>Bonding and molecular shape</strong> are the starting point for organic chemistry and structure and properties.</li>
<li><strong>Acids and bases</strong> from the solutions unit grow into pH and equilibrium calculations.</li></ul>
<p>If any of these felt shaky in Grade 11, it is worth fixing before SCH4U starts. See <a href="/is-sch3u-hard/">Is SCH3U hard?</a> for the most common gaps.</p>"""),
            ("Is SCH4U harder than SCH3U?", """<p>Most students find SCH4U harder, for two reasons: the topics are more abstract, and each calculation has more steps. But SCH4U is also more predictable. Students who start with strong SCH3U skills often find Grade 12 goes better than Grade 11 did, because the methods are familiar.</p>"""),
            ("Should you take SCH4U if SCH3U was a struggle?", """<p>If your teen's university program needs SCH4U, a hard SCH3U year is a reason to prepare, not a reason to drop it. The usual fix is to close the specific SCH3U gaps first (often the mole, stoichiometry or balancing equations) during the summer or the first weeks of the semester.</p>"""),
            ("What parents can do", """<ul><li>Check which university programs your teen is considering and whether they list SCH4U.</li>
<li>Look back at the SCH3U units with the lowest marks. Those are the gaps to close.</li>
<li>Start support at the beginning of SCH4U, not after the first test.</li>
<li>Book a free assessment. We check the SCH3U skills SCH4U depends on and send a written plan within 24 hours.</li></ul>"""),
        ],
        "faq": [
            ("Can you take SCH4U without SCH3U?", "SCH3U is the official prerequisite for SCH4U. Schools decide on any exceptions, so ask your child's guidance counsellor."),
            ("Do I need SCH4U for university?", "Many Ontario health science, life science and engineering programs require it. Always check each program's admission requirements."),
            ("When should my teen start preparing for SCH4U?", "The summer before, or the first weeks of the semester. Reviewing stoichiometry and balancing equations first makes the biggest difference."),
            ("Do you teach both SCH3U and SCH4U?", "Yes. Both are part of our signature Chemistry program, 1-on-1 in Ottawa or online, with personalized notes and stationery included."),
        ],
        "related": [("SCH3U", "Grade 11 Chemistry", "/sch3u-chemistry-tutor-ottawa/"), ("SCH4U", "Grade 12 Chemistry", "/sch4u-chemistry-tutor-ottawa/"), ("Is SCH3U hard?", "Guide", "/is-sch3u-hard/"), ("Chemistry", "Tutor in Ottawa", "/chemistry-tutor-ottawa/")],
    },
    {
        "slug": "is-mhf4u-hard", "kind": "guide", "card": "Grade 12 Advanced Functions",
        "title": "Is MHF4U Hard? Grade 12 Advanced Functions Explained | QueensCoaching",
        "desc": "Is MHF4U (Grade 12 Advanced Functions) hard? What makes it challenging, the hardest units, warning signs, how it connects to Calculus (MCV4U), and how to do well. A guide for Ontario families.",
        "h1": "Is MHF4U hard? Grade 12 Advanced Functions explained",
        "sub": "A plain-English guide for Ontario parents and students: what makes Advanced Functions challenging, where students get stuck, and how to do well.",
        "answer": "MHF4U is one of the more demanding Grade 12 math courses because it brings together everything from Grade 11 Functions and adds logarithms, radians and rational functions. Students who are solid on MCR3U functions, factoring and trigonometry usually manage it well with regular practice.",
        "sections": [
            ("What is MHF4U?", """<p>MHF4U is the Ontario Grade 12 Advanced Functions course, University Preparation. Its prerequisite is Grade 11 Functions (MCR3U), or Grade 12 Mathematics for College Technology (MCT4C). It must be taken before or at the same time as Calculus and Vectors (MCV4U). It has four strands:</p>
<ul><li><strong>Exponential and Logarithmic Functions</strong>: logarithms, their laws, and solving exponential equations</li>
<li><strong>Trigonometric Functions</strong>: radians, trig graphs, identities and trig equations</li>
<li><strong>Polynomial and Rational Functions</strong>: polynomial graphs, factoring, inequalities and asymptotes</li>
<li><strong>Characteristics of Functions</strong>: rates of change and combining functions</li></ul>
<p>See the full <a href="/mhf4u-advanced-functions-tutor-ottawa/">MHF4U course page</a> for how we coach each unit.</p>"""),
            ("Why do students find MHF4U hard?", """<ul><li><strong>It assumes Grade 11 is solid.</strong> Transformations, factoring and trig ratios from MCR3U are used in every unit.</li>
<li><strong>Logarithms are new.</strong> They work "backwards" from exponents, which feels unfamiliar at first.</li>
<li><strong>Radians and identities.</strong> Switching from degrees to radians and proving trig identities need a new way of thinking.</li>
<li><strong>More abstract questions.</strong> Many questions ask students to explain or prove, not just calculate.</li></ul>"""),
            ("Which MHF4U units are hardest?", """<div class="table-wrap"><table class="compare"><thead><tr><th>Unit</th><th>What students find tricky</th><th>The basics behind it</th></tr></thead><tbody>
<tr><td>Polynomial functions</td><td>Factoring higher-degree polynomials, sketching from factors</td><td>Grade 10 and 11 factoring</td></tr>
<tr><td>Rational functions</td><td>Asymptotes, inequalities, sign charts</td><td>Fractions with variables, factoring</td></tr>
<tr><td>Trigonometric functions</td><td>Radians, identities, trig equations</td><td>MCR3U trig ratios and transformations</td></tr>
<tr><td>Exponential and logarithmic</td><td>Log laws, solving with logs</td><td>Exponent laws</td></tr>
<tr><td>Characteristics of functions</td><td>Rates of change, combining functions</td><td>Function notation, slope</td></tr>
</tbody></table></div>"""),
            ("Signs your teen needs help in MHF4U", """<ul><li>They can follow examples in class but get stuck on new questions</li>
<li>Factoring or exponent laws still cause mistakes</li>
<li>Trig identities feel like guessing</li>
<li>Marks drop in the logarithms or rational functions unit</li></ul>"""),
            ("How to do well in MHF4U", """<ul><li><strong>Refresh MCR3U first</strong>, especially transformations, factoring and trig ratios.</li>
<li><strong>Practise a little every day.</strong> Advanced Functions rewards steady practice more than long study sessions.</li>
<li><strong>Keep a page of laws and identities</strong> and use it until it is memorized.</li>
<li><strong>Explain each step in words.</strong> It prepares students for "show" and "prove" questions.</li></ul>"""),
            ("MHF4U and MCV4U (Calculus)", """<p>MHF4U is the foundation for Calculus and Vectors (MCV4U), which many Ontario engineering, math, science and business programs require. Weak MHF4U skills, especially in rational functions and trigonometry, are the most common reason students struggle in Calculus. See our <a href="/mcv4u-calculus-vectors-tutor-ottawa/">MCV4U course page</a>.</p>"""),
            ("What parents can do", """<ul><li>Ask your teen which unit felt hardest in Grade 11 Functions. That is usually where MHF4U gaps start.</li>
<li>Encourage short daily practice instead of last-minute cramming.</li>
<li>Get help at the start of the course if university programs need MHF4U or MCV4U.</li>
<li>Book a free assessment. We check the MCR3U skills MHF4U depends on and send a written plan within 24 hours.</li></ul>"""),
        ],
        "faq": [
            ("Is MHF4U harder than MCR3U?", "Most students find it harder because it builds on everything in MCR3U and adds logarithms, radians and rational functions. Strong MCR3U skills make the jump much smaller."),
            ("Do I need MHF4U for university?", "Many Ontario engineering, math, science and business programs require MHF4U, and it must come before or alongside MCV4U. Check each program's admission requirements."),
            ("Can I take MHF4U and MCV4U at the same time?", "Ontario allows MHF4U to be taken before or at the same time as MCV4U. Schools decide on scheduling, so ask your guidance counsellor."),
            ("Can you help with MHF4U taken online or in summer school?", "Yes. We follow the same Ontario curriculum whether MHF4U is taken in day school, summer school or online."),
        ],
        "related": [("MHF4U", "Advanced Functions", "/mhf4u-advanced-functions-tutor-ottawa/"), ("MCR3U", "Grade 11 Functions", "/mcr3u-functions-tutor-ottawa/"), ("MCV4U", "Calculus & Vectors", "/mcv4u-calculus-vectors-tutor-ottawa/"), ("SPH4U", "Grade 12 Physics", "/sph4u-physics-tutor-ottawa/")],
    },
    {
        "slug": "chemistry-tutor-ottawa", "kind": "hub", "card": "Grade 11 & 12 Chemistry",
        "title": "Chemistry Tutor in Ottawa: Grade 11 & 12 (SCH3U, SCH4U, SCH4C) | QueensCoaching",
        "desc": "1-on-1 Chemistry tutoring in Ottawa and online for Grade 11 and 12: SCH3U, SCH4U and SCH4C. Personalized notes and stationery included. Kanata, Barrhaven, Orléans, Nepean and Stittsville. Book a free assessment.",
        "h1": "Chemistry tutor in Ottawa for Grade 11 &amp; 12",
        "sub": "Our signature program: personalized 1-on-1 SCH3U, SCH4U and SCH4C coaching, in person across Ottawa or live online. We fix the basics while we cover the curriculum.",
        "answer": "QueensCoaching offers 1-on-1 Grade 11 and 12 Chemistry tutoring in Ottawa and online, following the Ontario curriculum unit by unit. Every student starts with a free assessment and gets personalized notes, stationery and practice tests.",
        "sections": [
            ("Chemistry courses we coach", """<div class="grid" style="margin-top:8px">
<article class="card card-feature"><span class="tag">SCH3U</span><h3>Grade 11 Chemistry</h3><p>Bonding, reactions, the mole, solutions and gases.</p><a class="card-link" href="/sch3u-chemistry-tutor-ottawa/">View SCH3U →</a></article>
<article class="card card-feature"><span class="tag">SCH4U</span><h3>Grade 12 Chemistry</h3><p>Organic, structure and properties, energy and rates, equilibrium, electrochemistry.</p><a class="card-link" href="/sch4u-chemistry-tutor-ottawa/">View SCH4U →</a></article>
<article class="card card-feature"><span class="tag">SCH4C</span><h3>Grade 12 College Chemistry</h3><p>Practical chemistry for college pathways.</p><a class="card-link" href="/sch4c-college-chemistry-tutor-ottawa/">View SCH4C →</a></article>
</div>"""),
            ("Why Chemistry is our signature program", """<p>Chemistry is where many students hit a wall, and it opens the door to health, science and engineering programs. Founder and lead coach <a href="/about-harleen-kaur/">Harleen Kaur</a> holds a B.Sc. and M.Sc. with a background in pharmacy, and personally coaches Grade 11 and 12 Chemistry.</p>
<ul><li>A starting check of Grade 10 Science and Math gaps</li>
<li>Personalized notes for every unit, kept in a binder</li>
<li>All stationery included</li>
<li>Practice tests before every school test and the final exam</li>
<li>Stoichiometry and equation-balancing drills</li>
<li>A monthly progress note for parents</li></ul>"""),
            ("In person across Ottawa, or online", """<p>We coach Chemistry students in person in <a href="/tutor-kanata-ottawa/">Kanata</a>, <a href="/tutor-barrhaven-ottawa/">Barrhaven</a>, <a href="/tutor-orleans-ottawa/">Orléans</a>, <a href="/tutor-nepean-ottawa/">Nepean</a> and <a href="/tutor-stittsville-ottawa/">Stittsville</a>, and live online anywhere. See <a href="/online-chemistry-tutor-ontario/">online Chemistry tutoring</a>.</p>"""),
            ("Parent guides", """<p>Start with our plain-English guides: <a href="/is-sch3u-hard/">Is SCH3U hard?</a> and <a href="/sch3u-vs-sch4u/">SCH3U vs SCH4U</a>.</p>"""),
        ],
        "faq": [
            ("Which Chemistry courses do you tutor?", "Grade 11 SCH3U, Grade 12 SCH4U and Grade 12 College SCH4C, plus Grade 9 and 10 Science. We also coach AP, IB and GCSE Chemistry online."),
            ("Is tutoring 1-on-1?", "Yes. Every session is one coach and one student, in person in Ottawa or live online."),
            ("How much does Chemistry tutoring cost?", "Every student's needs are different, so we share pricing after the free assessment, along with a written plan."),
            ("Can you help with Waterloo chemistry contests?", "Yes. We offer optional practice for the Waterloo Avogadro Exam (Grade 11) and Chem 13 News Exam (Grade 12)."),
        ],
        "related": [("SCH3U", "Grade 11 Chemistry", "/sch3u-chemistry-tutor-ottawa/"), ("SCH4U", "Grade 12 Chemistry", "/sch4u-chemistry-tutor-ottawa/"), ("SCH4C", "College Chemistry", "/sch4c-college-chemistry-tutor-ottawa/"), ("SBI4U", "Grade 12 Biology", "/sbi4u-biology-tutor-ottawa/")],
    },
    {
        "slug": "online-chemistry-tutor-ontario", "kind": "hub", "card": "Online Chemistry tutoring",
        "title": "Online Chemistry Tutor (Ontario Curriculum): SCH3U, SCH4U, SCH4C | QueensCoaching",
        "desc": "Live 1-on-1 online Chemistry tutoring for the Ontario curriculum: SCH3U, SCH4U and SCH4C, including students taking Chemistry through an online or summer school. Book a free assessment.",
        "h1": "Online Chemistry tutor for the Ontario curriculum",
        "sub": "Live 1-on-1 SCH3U, SCH4U and SCH4C coaching by video, for students anywhere in Ontario, Canada or abroad, including students taking Chemistry through an online school.",
        "answer": "QueensCoaching offers live 1-on-1 online Chemistry tutoring that follows the Ontario curriculum for SCH3U, SCH4U and SCH4C. Sessions use video with a shared whiteboard, notes are sent digitally, and every student starts with a free assessment.",
        "sections": [
            ("How online sessions work", """<ul><li><strong>Live 1-on-1 video</strong> with a shared whiteboard, so students can write and solve together with the coach</li>
<li><strong>Personalized digital notes</strong> for every unit, and stationery shipped within Canada</li>
<li><strong>Practice tests</strong> before every school test and the final exam</li>
<li><strong>Your time zone.</strong> Sessions are scheduled around school and activities</li></ul>"""),
            ("Taking SCH4U or SCH3U through an online school?", """<p>Many students take Chemistry through an online or summer school, often in a shorter time frame with less live teaching. We tutor alongside any Ontario SCH3U, SCH4U or SCH4C course, following the same curriculum. QueensCoaching is a tutoring service, so we do not grant credits: the credit always comes from the student's school.</p>"""),
            ("Courses we coach online", """<div class="pills"><a class="pill" href="/sch3u-chemistry-tutor-ottawa/"><strong>SCH3U</strong> Grade 11 Chemistry</a><a class="pill" href="/sch4u-chemistry-tutor-ottawa/"><strong>SCH4U</strong> Grade 12 Chemistry</a><a class="pill" href="/sch4c-college-chemistry-tutor-ottawa/"><strong>SCH4C</strong> College Chemistry</a><span class="pill">AP, IB &amp; GCSE Chemistry</span></div>
<p>Live in Ottawa? We also coach in person: see <a href="/chemistry-tutor-ottawa/">Chemistry tutor in Ottawa</a>.</p>"""),
        ],
        "faq": [
            ("Can you help with an online SCH4U credit course?", "Yes. We tutor students taking SCH4U through online and summer schools, following the Ontario curriculum. We do not grant credits; the credit comes from the student's school."),
            ("Is online tutoring as effective as in person?", "For many students it works very well, because sessions are live, 1-on-1 and use a shared whiteboard. The free assessment helps decide which format suits your child."),
            ("Do you tutor students outside Ontario?", "Yes. We coach students across Canada and abroad, including AP, IB and GCSE Chemistry, in their time zone."),
            ("How much does online Chemistry tutoring cost?", "Every student's needs are different, so we share pricing after the free assessment, along with a written plan."),
        ],
        "related": [("SCH3U", "Grade 11 Chemistry", "/sch3u-chemistry-tutor-ottawa/"), ("SCH4U", "Grade 12 Chemistry", "/sch4u-chemistry-tutor-ottawa/"), ("SCH4C", "College Chemistry", "/sch4c-college-chemistry-tutor-ottawa/"), ("Chemistry", "Tutor in Ottawa", "/chemistry-tutor-ottawa/")],
    },
]


def guide_page(g):
    path = f"/{g['slug']}/"
    is_guide = g["kind"] == "guide"
    crumb_mid = ("Parent Guides", "/guides/") if is_guide else ("Courses", "/courses/")
    secs = ""
    for i, (h, html) in enumerate(g["sections"]):
        secs += f"<h2>{e(h)}</h2>\n{html}\n"
        if i == 1:
            secs += INLINE_CTA + "\n"
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in g["faq"])
    related = "".join(f'<a class="pill" href="{h}"><strong>{e(a)}</strong> {e(b)}</a>' for a, b, h in g["related"])
    byline = '<p class="byline">QueensCoaching parent guide · Updated November 2026</p>' if is_guide else ""
    body = f'''<section class="brand">
  {breadcrumb([("Home", "/"), crumb_mid, (g["h1"].replace("&amp;", "&"), None)])}
  <div class="wrap page-hero">
    <p class="eyebrow">{"Parent guide" if is_guide else "Signature program"}</p>
    <h1>{g["h1"]}</h1>
    <p class="hero-sub">{e(g["sub"])}</p>
    <div class="btn-row"><a class="btn btn-gold" href="/book/">Book Free Assessment</a><a class="btn btn-outline" href="{WA}">WhatsApp us</a></div>
  </div>
</section>

<section class="section"><div class="wrap"><div class="prose">
  {byline}
  <div class="answer-box"><strong>The short answer</strong>{e(g["answer"])}</div>
  {secs}
</div></div></section>

<section class="section alt"><div class="wrap narrow">
  <h2 class="h2" style="margin-bottom:28px">Questions families ask</h2>
  <div class="faq">{faqs}</div>
</div></section>

<section style="padding:48px 0 80px"><div class="wrap">
  <h2 style="margin:0 0 16px;font-size:20px">Related</h2>
  <div class="pills">{related}</div>
</div></section>

{cta_band("Find the gaps before the next test.", "Book a free assessment and get a written plan with a winning strategy within 24 hours. No obligation.")}'''
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}
    crumbs = crumbs_ld([("Home", "/"), crumb_mid, (g["h1"].replace("&amp;", "&"), path)])
    if is_guide:
        main_ld = {"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["desc"],
                   "url": SITE + path, "datePublished": PUBLISHED, "dateModified": PUBLISHED, "inLanguage": "en-CA",
                   "author": {"@type": "Organization", "name": "QueensCoaching", "url": SITE + "/"},
                   "publisher": {"@type": "Organization", "@id": f"{SITE}/#business", "name": "QueensCoaching", "logo": {"@type": "ImageObject", "url": SITE + "/logo.png"}},
                   "image": SITE + "/og-image.png"}
    else:
        main_ld = {"@context": "https://schema.org", "@type": "Service", "name": g["h1"].replace("&amp;", "&"), "description": g["desc"],
                   "serviceType": "Chemistry tutoring", "url": SITE + path,
                   "provider": {"@type": ["EducationalOrganization", "LocalBusiness"], "@id": f"{SITE}/#business", "name": "QueensCoaching", "telephone": "+1-613-297-6844"},
                   "areaServed": [{"@type": "City", "name": "Ottawa"}, {"@type": "State", "name": "Ontario"}] if g["slug"] == "chemistry-tutor-ottawa" else [{"@type": "Country", "name": "Canada"}]}
    return shell(g["title"], g["desc"], path, body, ld(main_ld, faq_ld, crumbs), active="Guides" if is_guide else "Courses")


def guides_index():
    cards = "".join(
        f'<article class="card{"" if g["kind"] == "guide" else " card-feature"}"><span class="tag">{e(g["card"])}</span>'
        f'<h3>{g["h1"]}</h3><p>{e(g["answer"].split(". ")[0])}.</p><a class="card-link" href="/{g["slug"]}/">Read more →</a></article>'
        for g in GUIDES)
    body = f'''<section class="brand">
  {breadcrumb([("Home", "/"), ("Parent Guides", None)])}
  <div class="wrap page-hero">
    <p class="eyebrow">Parent guides</p>
    <h1>Guides to Ontario Grade 9–12 Math &amp; Science</h1>
    <p class="hero-sub">Plain-English answers to the questions Ottawa families ask most: which courses are hard, what changes from Grade 11 to 12, and how to help at home.</p>
  </div>
</section>
<section class="section"><div class="wrap"><div class="grid">{cards}</div></div></section>
{cta_band()}'''
    items = [{"@type": "ListItem", "position": i, "url": f'{SITE}/{g["slug"]}/', "name": g["h1"].replace("&amp;", "&")} for i, g in enumerate(GUIDES, 1)]
    return shell("Parent Guides: Ontario Grade 9–12 Math & Science | QueensCoaching",
                 "Plain-English guides for Ontario families: Is SCH3U hard? SCH3U vs SCH4U, Is MHF4U hard? and more, from QueensCoaching in Ottawa.",
                 "/guides/", body, ld({"@context": "https://schema.org", "@type": "ItemList", "itemListElement": items},
                                      crumbs_ld([("Home", "/"), ("Parent Guides", "/guides/")])), active="Guides")


if __name__ == "__main__":
    root = sys.argv[1]
    for g in GUIDES:
        d = os.path.join(root, g["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(guide_page(g))
        print("wrote", g["slug"])
    os.makedirs(os.path.join(root, "guides"), exist_ok=True)
    with open(os.path.join(root, "guides", "index.html"), "w", encoding="utf-8") as f:
        f.write(guides_index())
    print("wrote guides")

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
        "slug": "exponent-laws-guide", "kind": "guide", "card": "Grade 9–11 Math", "published": "2026-11-15",
        "title": "Exponent Laws Explained: Grade 10–11 Math (Ontario) | QueensCoaching",
        "desc": "The exponent laws explained in plain English, with examples: product, quotient, power, zero, negative and rational exponents. Where they appear in Ontario MTH1W, MPM2D, MCR3U and MHF4U, and the mistakes that cost marks.",
        "h1": "Exponent laws explained (Grade 10–11 math)",
        "sub": "A plain-English guide for Ontario students and parents: every exponent law with an example, where each one shows up in high school math, and the mistakes that cost the most marks.",
        "answer": "Exponent laws are shortcuts for working with powers. When you multiply powers with the same base you add the exponents, when you divide you subtract them, and when you raise a power to a power you multiply them. Zero, negative and fractional exponents follow from these same rules, and they matter in every Ontario math course from Grade 9 to Grade 12.",
        "sections": [
            ("What is an exponent?", """<p>A power has a <strong>base</strong> and an <strong>exponent</strong>. In 2<sup>5</sup>, the base is 2 and the exponent is 5, which means 2 × 2 × 2 × 2 × 2 = 32. The exponent tells you how many times the base is used as a factor.</p>
<p>Every exponent law comes from that one idea. If your teen ever forgets a law, they can write the powers out the long way and see the pattern again. That habit alone fixes many mistakes.</p>"""),
            ("The exponent laws, with examples", """<div class="table-wrap"><table class="compare"><thead><tr><th>Law</th><th>Rule</th><th>Example</th></tr></thead><tbody>
<tr><td>Product law</td><td>a<sup>m</sup> × a<sup>n</sup> = a<sup>m+n</sup></td><td>x<sup>3</sup> × x<sup>4</sup> = x<sup>7</sup></td></tr>
<tr><td>Quotient law</td><td>a<sup>m</sup> ÷ a<sup>n</sup> = a<sup>m−n</sup> (a ≠ 0)</td><td>5<sup>6</sup> ÷ 5<sup>2</sup> = 5<sup>4</sup></td></tr>
<tr><td>Power of a power</td><td>(a<sup>m</sup>)<sup>n</sup> = a<sup>mn</sup></td><td>(y<sup>2</sup>)<sup>5</sup> = y<sup>10</sup></td></tr>
<tr><td>Power of a product</td><td>(ab)<sup>n</sup> = a<sup>n</sup>b<sup>n</sup></td><td>(2x)<sup>3</sup> = 8x<sup>3</sup></td></tr>
<tr><td>Power of a quotient</td><td>(a/b)<sup>n</sup> = a<sup>n</sup>/b<sup>n</sup> (b ≠ 0)</td><td>(x/3)<sup>2</sup> = x<sup>2</sup>/9</td></tr>
<tr><td>Zero exponent</td><td>a<sup>0</sup> = 1 (a ≠ 0)</td><td>7<sup>0</sup> = 1</td></tr>
<tr><td>Negative exponent</td><td>a<sup>−n</sup> = 1/a<sup>n</sup> (a ≠ 0)</td><td>2<sup>−3</sup> = 1/8</td></tr>
<tr><td>Rational exponent</td><td>a<sup>1/n</sup> = ⁿ√a, and a<sup>m/n</sup> = (ⁿ√a)<sup>m</sup></td><td>8<sup>2/3</sup> = (∛8)<sup>2</sup> = 4</td></tr>
</tbody></table></div>
<p>The product, quotient and power laws only work when the <strong>bases are the same</strong>. 2<sup>3</sup> × 3<sup>2</sup> cannot be combined into one power; you work out each part: 8 × 9 = 72.</p>"""),
            ("Where do exponent laws show up in Ontario math?", """<ul><li><strong>Grade 9 (MTH1W):</strong> the Number strand introduces powers and the patterns behind the exponent laws.</li>
<li><strong>Grade 10 (MPM2D):</strong> exponent laws are used constantly when expanding, simplifying and factoring expressions such as 3x<sup>2</sup>(2x − 5) in the quadratics unit.</li>
<li><strong>Grade 11 (MCR3U):</strong> the Exponential Functions strand extends the laws to zero, negative and rational exponents, then uses them for exponential growth and decay.</li>
<li><strong>Grade 12 (MHF4U and MCV4U):</strong> logarithms are built directly on exponent laws, and the power rule for derivatives in Calculus depends on rewriting roots and fractions as exponents.</li>
<li><strong>Science:</strong> scientific notation in Chemistry and Physics, such as (3.0 × 10<sup>8</sup>) × (2.0 × 10<sup>−3</sup>) = 6.0 × 10<sup>5</sup>, is exponent laws in action.</li></ul>
<p>This is why a shaky Grade 9 or 10 skill often shows up as a low mark in Grade 11 Functions. See our <a href="/mcr3u-functions-tutor-ottawa/">MCR3U course page</a> for how we coach that unit.</p>"""),
            ("Why are negative and zero exponents confusing?", """<p>Most students accept the product and quotient laws quickly. Zero and negative exponents feel strange because you cannot "use 2 as a factor −3 times". The quotient law explains them:</p>
<ul><li>5<sup>3</sup> ÷ 5<sup>3</sup> = 1, and the quotient law gives 5<sup>3−3</sup> = 5<sup>0</sup>. So 5<sup>0</sup> must equal 1.</li>
<li>5<sup>2</sup> ÷ 5<sup>5</sup> = 1/5<sup>3</sup>, and the quotient law gives 5<sup>2−5</sup> = 5<sup>−3</sup>. So 5<sup>−3</sup> = 1/5<sup>3</sup> = 1/125.</li></ul>
<p>A negative exponent means "take the reciprocal". It never makes the answer negative on its own.</p>"""),
            ("The most common exponent mistakes", """<ul><li><strong>Multiplying exponents instead of adding:</strong> x<sup>3</sup> × x<sup>4</sup> is x<sup>7</sup>, not x<sup>12</sup>.</li>
<li><strong>Forgetting the coefficient:</strong> (2x<sup>3</sup>)<sup>2</sup> is 4x<sup>6</sup>, not 2x<sup>6</sup>. The 2 is squared too.</li>
<li><strong>Treating a negative exponent as a negative number:</strong> 2<sup>−3</sup> is 1/8, not −8.</li>
<li><strong>Mixing up −3<sup>2</sup> and (−3)<sup>2</sup>:</strong> −3<sup>2</sup> = −9, but (−3)<sup>2</sup> = 9. Brackets decide what is squared.</li>
<li><strong>Spreading an exponent over addition:</strong> (a + b)<sup>2</sup> is a<sup>2</sup> + 2ab + b<sup>2</sup>, not a<sup>2</sup> + b<sup>2</sup>. Exponent laws work over multiplication, not addition.</li>
<li><strong>Combining different bases:</strong> 2<sup>3</sup> × 3<sup>2</sup> is not 6<sup>5</sup>.</li></ul>"""),
            ("How to master exponent laws", """<ul><li><strong>Learn the "why", not just the rule.</strong> Writing x<sup>3</sup> × x<sup>4</sup> out as seven x's makes the product law obvious and easy to remember.</li>
<li><strong>Do one step at a time.</strong> Simplify coefficients first, then each variable, then deal with negative exponents last.</li>
<li><strong>Turn roots into exponents.</strong> In Grade 11 and 12, writing √x as x<sup>1/2</sup> makes most questions easier.</li>
<li><strong>Practise mixed questions.</strong> Tests mix all the laws together, so practice should too.</li>
<li><strong>Check with numbers.</strong> If unsure, test the rule with small numbers, like 2<sup>2</sup> × 2<sup>3</sup> = 4 × 8 = 32 = 2<sup>5</sup>.</li></ul>"""),
            ("What parents can do", """<p>You do not need to remember the rules to help:</p>
<ul><li>Ask your teen to explain why x<sup>0</sup> = 1. If they can explain it, they understand it; if not, that is a gap worth fixing.</li>
<li>Encourage ten minutes of mixed practice a few times a week rather than one long session before a test.</li>
<li>Watch for exponent mistakes in Grade 10 and 11 tests. They often look like "careless errors" but are really a missing foundation.</li>
<li>Book a free assessment. We check exponent laws and the other Grade 9 and 10 skills later courses depend on, then send a written plan within 24 hours.</li></ul>"""),
        ],
        "faq": [
            ("Which grade learns exponent laws in Ontario?", "Powers and the patterns behind the exponent laws start in Grade 9 Math (MTH1W). They are used throughout Grade 10 (MPM2D) and extended to negative and rational exponents in Grade 11 Functions (MCR3U)."),
            ("Why does anything to the power of zero equal 1?", "Because dividing a power by itself gives 1, and the quotient law gives an exponent of zero. For example, 4 cubed divided by 4 cubed is 1, and it is also 4 to the power of 0. The rule applies to any non-zero base."),
            ("Do exponent laws matter in Grade 12?", "Yes. Logarithms in MHF4U are built on exponent laws, and the power rule for derivatives in MCV4U depends on writing roots and fractions as exponents."),
            ("Can you help if my child keeps making exponent mistakes?", "Yes. We find exactly which law or step is causing the errors and fix it while covering the current course, 1-on-1 in Ottawa or online."),
        ],
        "related": [("MCR3U", "Grade 11 Functions", "/mcr3u-functions-tutor-ottawa/"), ("MPM2D", "Grade 10 Math", "/mpm2d-math-tutor-ottawa/"), ("MTH1W", "Grade 9 Math", "/mth1w-grade-9-math-tutor-ottawa/"), ("Is MHF4U hard?", "Guide", "/is-mhf4u-hard/"), ("Math", "Tutor in Ottawa", "/math-tutor-ottawa/")],
    },
    {
        "slug": "is-mcv4u-hard", "kind": "guide", "card": "Grade 12 Calculus", "published": "2026-11-15",
        "title": "Is MCV4U Hard? Grade 12 Calculus & Vectors Explained | QueensCoaching",
        "desc": "Is MCV4U (Grade 12 Calculus and Vectors) hard? What makes it challenging, the hardest units, warning signs, how it connects to Advanced Functions (MHF4U) and university, and how to do well. A guide for Ontario families.",
        "h1": "Is Grade 12 Calculus (MCV4U) hard?",
        "sub": "A plain-English guide for Ontario parents and students: what makes Calculus and Vectors challenging, where students get stuck, and how to do well.",
        "answer": "MCV4U is often called the most challenging Grade 12 math course, because it uses everything from earlier math and adds two new topics: calculus and 3D vectors. The calculus ideas are usually not the hardest part. Most lost marks come from algebra, exponents and trigonometry, so students with solid MHF4U skills and steady practice usually do well.",
        "sections": [
            ("What is MCV4U?", """<p>MCV4U is the Ontario Grade 12 Calculus and Vectors course, University Preparation. Advanced Functions (MHF4U) must be taken before it or at the same time. It has three strands:</p>
<ul><li><strong>Rate of Change</strong>: limits, instantaneous rates of change and the definition of the derivative</li>
<li><strong>Derivatives and Their Applications</strong>: derivative rules, curve sketching, and optimization and related problems</li>
<li><strong>Geometry and Algebra of Vectors</strong>: vectors in two and three dimensions, dot and cross products, and lines and planes in space</li></ul>
<p>See the full <a href="/mcv4u-calculus-vectors-tutor-ottawa/">MCV4U course page</a> for how we coach each strand.</p>"""),
            ("Why do students find MCV4U hard?", """<ul><li><strong>It uses all earlier math at once.</strong> A single derivative question can need factoring, exponent laws, fractions and trig in the same solution.</li>
<li><strong>Limits are a new way of thinking.</strong> The idea of "getting closer and closer" feels abstract at first.</li>
<li><strong>It is really two courses in one.</strong> Calculus and vectors use different skills, and the vectors strand asks students to picture lines and planes in 3D.</li>
<li><strong>Word problems.</strong> Optimization questions ask students to build the equation themselves before they can use calculus.</li>
<li><strong>The pace.</strong> Many students take MCV4U at the same time as MHF4U, SPH4U and SCH4U, in the semester that counts for university applications.</li></ul>"""),
            ("Which MCV4U units are hardest?", """<div class="table-wrap"><table class="compare"><thead><tr><th>Unit</th><th>What students find tricky</th><th>The basics behind it</th></tr></thead><tbody>
<tr><td>Limits and rates of change</td><td>Evaluating limits, the first-principles definition</td><td>Factoring, rational expressions, slope</td></tr>
<tr><td>Derivative rules</td><td>Chain rule, quotient rule, simplifying answers</td><td>Exponent laws, fractions with variables</td></tr>
<tr><td>Curve sketching</td><td>Putting first and second derivatives together</td><td>Solving polynomial equations, sign charts</td></tr>
<tr><td>Optimization</td><td>Setting up the equation from a word problem</td><td>Area, volume and perimeter formulas</td></tr>
<tr><td>Derivatives of exponential and trig functions</td><td>Combining rules, special values</td><td>MHF4U logarithms, radians and trig</td></tr>
<tr><td>Vectors, lines and planes</td><td>Picturing 3D, equations of lines and planes, intersections</td><td>Trigonometry, solving systems of equations</td></tr>
</tbody></table></div>
<p>Many students who struggle with calculus are really struggling with algebra. Our <a href="/exponent-laws-guide/">exponent laws guide</a> covers one of the most common gaps.</p>"""),
            ("Signs your teen needs help in MCV4U", """<ul><li>They understand the calculus idea but get the algebra wrong</li>
<li>Marks drop when the chain rule or optimization starts</li>
<li>Word problems feel impossible to start</li>
<li>The vectors strand feels like a completely different course</li>
<li>Homework takes hours, especially alongside MHF4U</li></ul>
<p>Each of these usually points to a specific gap, often from MHF4U or Grade 11, rather than the whole course.</p>"""),
            ("How to do well in MCV4U", """<ul><li><strong>Refresh MHF4U and MCR3U algebra first</strong>: factoring, exponent laws, rational expressions and trig.</li>
<li><strong>Learn each derivative rule with plenty of practice</strong> before mixing them together.</li>
<li><strong>Draw a picture for every word problem</strong> and write what each variable means.</li>
<li><strong>Treat vectors as their own unit.</strong> Sketch in 3D, and keep a page of formulas for dot and cross products, lines and planes.</li>
<li><strong>Do practice tests under time</strong> before every unit test and the final exam, then review every mistake.</li></ul>"""),
            ("Should your teen take MCV4U if math feels hard?", """<p>If a program your teen is considering requires MCV4U, a hard MHF4U year is a reason to prepare, not a reason to drop the course. The usual fix is to close the specific gaps first, such as factoring, rational expressions or trig, in the summer or the first weeks of the semester. If no program on their list needs it, talk with the guidance counsellor about whether another Grade 12 course is a better fit, such as Data Management (MDM4U).</p>"""),
            ("MCV4U and university", """<p>Many Ontario engineering programs, and many math, physical science, computer science and business programs, list MCV4U as a requirement. Some programs that do not require it still recommend it. Requirements differ by program and university, so always check each program's admission page. Our guide <a href="/grade-12-courses-for-university-ontario/">Which Grade 12 courses do I need for university?</a> explains how to plan.</p>"""),
            ("What parents can do", """<ul><li>Check which university programs your teen is considering and whether they list MCV4U.</li>
<li>Ask which MHF4U unit felt hardest. That is usually where MCV4U trouble starts.</li>
<li>If MHF4U and MCV4U are in the same semester, plan support from the first week.</li>
<li>Book a free assessment. We check the algebra, exponent and trig skills MCV4U depends on and send a written plan within 24 hours.</li></ul>"""),
        ],
        "faq": [
            ("Is MCV4U harder than MHF4U?", "Most students find MCV4U harder, because it builds on MHF4U and adds calculus and 3D vectors. Students with strong MHF4U skills often find the jump smaller than expected."),
            ("What is the hardest part of MCV4U?", "For many students it is optimization word problems and the vectors, lines and planes strand. In most cases the real difficulty is the algebra behind the calculus."),
            ("Can you take MCV4U and MHF4U at the same time?", "Yes. The Ontario curriculum allows MHF4U to be taken before or at the same time as MCV4U. Many students find it easier to finish MHF4U first. Your school decides on scheduling."),
            ("Can you help with MCV4U taken online or in summer school?", "Yes. We follow the same Ontario curriculum whether MCV4U is taken in day school, summer school or online."),
        ],
        "related": [("MCV4U", "Calculus & Vectors", "/mcv4u-calculus-vectors-tutor-ottawa/"), ("MHF4U", "Advanced Functions", "/mhf4u-advanced-functions-tutor-ottawa/"), ("Is MHF4U hard?", "Guide", "/is-mhf4u-hard/"), ("SPH4U", "Grade 12 Physics", "/sph4u-physics-tutor-ottawa/"), ("Math", "Tutor in Ottawa", "/math-tutor-ottawa/")],
    },
    {
        "slug": "grade-12-courses-for-university-ontario", "kind": "guide", "card": "University planning", "published": "2026-11-15",
        "title": "Which Grade 12 Courses Do I Need for Engineering or Health Sciences in Ontario? | QueensCoaching",
        "desc": "Which Grade 12 (4U) courses Ontario engineering, health science, nursing and life science programs usually ask for, the Grade 11 prerequisites behind them, and how to plan from Grade 10. A plain-English guide for families.",
        "h1": "Which Grade 12 courses do I need for engineering or health sciences in Ontario?",
        "sub": "A plain-English planning guide for Ontario families: the Grade 12 courses these programs usually ask for, the Grade 11 courses that lead to them, and when to start planning.",
        "answer": "Most Ontario engineering programs ask for Grade 12 English (ENG4U), Advanced Functions (MHF4U), Calculus and Vectors (MCV4U), Chemistry (SCH4U) and Physics (SPH4U). Health science, nursing and life science programs usually ask for English, Biology (SBI4U), Chemistry (SCH4U) and at least one Grade 12 math. Requirements differ by program and university, so always confirm each one before choosing courses.",
        "sections": [
            ("How Ontario university admission works", """<p>Ontario universities usually look at two things:</p>
<ul><li><strong>Program prerequisites</strong>: specific Grade 12 University (U) or University/College (M) courses that a program requires, such as MCV4U for engineering.</li>
<li><strong>An admission average</strong>: many universities calculate it from your six best Grade 12 U or M courses, including the required ones.</li></ul>
<p>Grade 12 English (ENG4U) is required by almost every university program. The best place to check exact requirements is each university's admission page and the Ontario Universities' Info site (ouinfo.ca).</p>"""),
            ("Courses engineering programs usually ask for", """<div class="table-wrap"><table class="compare"><thead><tr><th>Grade 12 course</th><th>Usually</th><th>Grade 11 course before it</th></tr></thead><tbody>
<tr><td>ENG4U English</td><td>Required</td><td>ENG3U</td></tr>
<tr><td><a href="/mhf4u-advanced-functions-tutor-ottawa/">MHF4U Advanced Functions</a></td><td>Required</td><td><a href="/mcr3u-functions-tutor-ottawa/">MCR3U Functions</a></td></tr>
<tr><td><a href="/mcv4u-calculus-vectors-tutor-ottawa/">MCV4U Calculus &amp; Vectors</a></td><td>Required</td><td>MHF4U (before or at the same time)</td></tr>
<tr><td><a href="/sch4u-chemistry-tutor-ottawa/">SCH4U Chemistry</a></td><td>Required at most universities</td><td><a href="/sch3u-chemistry-tutor-ottawa/">SCH3U Chemistry</a></td></tr>
<tr><td><a href="/sph4u-physics-tutor-ottawa/">SPH4U Physics</a></td><td>Required at most universities</td><td><a href="/sph3u-physics-tutor-ottawa/">SPH3U Physics</a></td></tr>
</tbody></table></div>
<p>Some engineering programs accept a different science in place of Chemistry or Physics, and some recommend Computer Science or Biology. Check each program.</p>"""),
            ("Courses health science, nursing and life science programs usually ask for", """<div class="table-wrap"><table class="compare"><thead><tr><th>Grade 12 course</th><th>Usually</th><th>Grade 11 course before it</th></tr></thead><tbody>
<tr><td>ENG4U English</td><td>Required</td><td>ENG3U</td></tr>
<tr><td><a href="/sbi4u-biology-tutor-ottawa/">SBI4U Biology</a></td><td>Required by most</td><td><a href="/sbi3u-biology-tutor-ottawa/">SBI3U Biology</a></td></tr>
<tr><td><a href="/sch4u-chemistry-tutor-ottawa/">SCH4U Chemistry</a></td><td>Required by most</td><td><a href="/sch3u-chemistry-tutor-ottawa/">SCH3U Chemistry</a></td></tr>
<tr><td>A Grade 12 math (often MHF4U)</td><td>Required by most</td><td>MCR3U (for MHF4U)</td></tr>
<tr><td>MCV4U, MDM4U or SPH4U</td><td>Required or recommended by some</td><td>Varies</td></tr>
</tbody></table></div>
<p>Health science programs vary more than engineering. Some ask for a second math course or Physics; others ask only for one math. Kinesiology and life science programs are often similar to health sciences.</p>"""),
            ("Why planning has to start in Grade 10", """<p>Every Grade 12 science and math course in the tables has a Grade 11 prerequisite, and those have Grade 10 prerequisites:</p>
<ul><li><strong>Science:</strong> <a href="/snc2d-grade-10-science-tutor-ottawa/">SNC2D Grade 10 Science</a> leads to SCH3U, SPH3U and SBI3U, which lead to SCH4U, SPH4U and SBI4U.</li>
<li><strong>Math:</strong> <a href="/mpm2d-math-tutor-ottawa/">MPM2D Grade 10 Math</a> leads to MCR3U, then MHF4U, then MCV4U.</li></ul>
<p>If a Grade 11 course is skipped, the Grade 12 course is usually not available without making it up, for example in summer school. That is why course choices in Grade 10 and 11 matter so much.</p>"""),
            ("What if your teen is not sure yet?", """<p>Many Grade 10 and 11 students do not know yet whether they want engineering, health sciences or something else. That is normal. The safest plan is to keep doors open: take SCH3U, SPH3U, SBI3U and MCR3U in Grade 11 if the timetable allows, because they lead to the Grade 12 courses most science, engineering and health programs ask for. It is much easier to drop a Grade 12 course later than to make up a missing Grade 11 prerequisite.</p>
<p>College programs in health, technology and the trades have their own requirements, often Grade 12 College (C) or University (U) courses such as SCH4C or MAP4C. Check each college program's admission page.</p>"""),
            ("Is it the courses or the marks that matter?", """<p>Both. Having the right courses gets an application considered, and the marks in those courses often carry the most weight. Competitive programs may also look at supplementary applications. A strong foundation in Grade 11 chemistry, physics and functions usually makes the Grade 12 marks much easier to earn. Our guides <a href="/is-mhf4u-hard/">Is MHF4U hard?</a>, <a href="/is-mcv4u-hard/">Is MCV4U hard?</a> and <a href="/sch3u-vs-sch4u/">SCH3U vs SCH4U</a> explain where students usually need help.</p>"""),
            ("What parents can do", """<ul><li>Make a short list of programs your teen is curious about, and look up their prerequisites together on ouinfo.ca.</li>
<li>Check that the Grade 11 courses on the timetable lead to every Grade 12 course those programs need.</li>
<li>Talk with your teen's guidance counsellor about timing, summer school and course load.</li>
<li>Look at which math and science courses feel hardest now, and get help early, before the Grade 12 marks that count.</li>
<li>Book a free assessment. We check the math and science foundations behind the Grade 12 courses and send a written plan within 24 hours.</li></ul>"""),
        ],
        "faq": [
            ("Do I need both MHF4U and MCV4U for engineering?", "For most Ontario engineering programs, yes. MCV4U is usually required, and MHF4U must be taken before or at the same time as it. Always check each program's admission requirements."),
            ("Do health science programs need Physics?", "Some do and many do not. Most ask for Biology, Chemistry and at least one Grade 12 math. Check each program, since health science requirements vary widely."),
            ("Can I take a Grade 12 course in summer school or online?", "Many students do. Some competitive programs look at when and how courses were taken, so check the program's admission page and talk with your guidance counsellor."),
            ("Does QueensCoaching help with course planning?", "We are a tutoring service, not a guidance office, but in the free assessment we can talk through which math and science courses lead where. Your school's guidance counsellor and each university are the official sources."),
        ],
        "related": [("MCV4U", "Calculus & Vectors", "/mcv4u-calculus-vectors-tutor-ottawa/"), ("SCH4U", "Grade 12 Chemistry", "/sch4u-chemistry-tutor-ottawa/"), ("SPH4U", "Grade 12 Physics", "/sph4u-physics-tutor-ottawa/"), ("SBI4U", "Grade 12 Biology", "/sbi4u-biology-tutor-ottawa/"), ("Is MCV4U hard?", "Guide", "/is-mcv4u-hard/")],
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
    {
        "slug": "physics-tutor-ottawa", "kind": "hub", "card": "Grade 11 & 12 Physics", "eyebrow": "1-on-1 Physics tutoring", "service": "Physics tutoring",
        "title": "Physics Tutor in Ottawa: Grade 11 & 12 (SPH3U, SPH4U) | QueensCoaching",
        "desc": "1-on-1 Grade 11 and 12 Physics tutoring in Ottawa and online: SPH3U, SPH4U and SPH4C. We rebuild the math behind every formula. Personalized notes and stationery included. Book a free assessment.",
        "h1": "Physics tutor in Ottawa for Grade 11 &amp; 12",
        "sub": "Personalized 1-on-1 SPH3U, SPH4U and SPH4C coaching, in person across Ottawa or live online. We fix the basics while we cover the curriculum.",
        "answer": "QueensCoaching offers 1-on-1 Grade 11 and 12 Physics tutoring in Ottawa and online, following the Ontario curriculum unit by unit. Most physics marks are lost on the math behind the formulas, so every student starts with a free assessment that checks those skills, then gets a written plan within 24 hours.",
        "sections": [
            ("Physics courses we coach", """<div class="grid" style="margin-top:8px">
<article class="card card-feature"><span class="tag">SPH3U</span><h3>Grade 11 Physics</h3><p>Kinematics, forces, energy, waves and sound, electricity and magnetism.</p><a class="card-link" href="/sph3u-physics-tutor-ottawa/">View SPH3U →</a></article>
<article class="card card-feature"><span class="tag">SPH4U</span><h3>Grade 12 Physics</h3><p>Dynamics, energy and momentum, fields, the wave nature of light, modern physics.</p><a class="card-link" href="/sph4u-physics-tutor-ottawa/">View SPH4U →</a></article>
<article class="card"><span class="tag">SPH4C</span><h3>Grade 12 College Physics</h3><p>Practical physics for college technology and trades pathways.</p><a class="card-link" href="/book/">Ask about SPH4C →</a></article>
</div>"""),
            ("How we coach Physics", """<p>Physics is where math meets the real world. Students who struggle usually understand the idea but get stuck on the algebra, trigonometry or vectors needed to solve the problem. We coach both at once:</p>
<ul><li>A starting check of the Grade 10 Math and Science skills physics depends on</li>
<li>Step-by-step problem solving: draw it, list what you know, pick the formula, solve, check the units</li>
<li>Free-body diagrams and vector practice until they feel natural</li>
<li>Personalized notes for every unit, kept in a binder, with all stationery included</li>
<li>Practice tests before every school test and the final exam, plus lab report help</li>
<li>True 1-on-1 attention every session, and a monthly progress note for parents</li></ul>"""),
            ("Why Physics feels hard", """<p>Physics asks students to read a situation, decide which idea applies, and then do the math. If rearranging formulas, trig ratios or exponent laws are shaky, even a well-understood idea turns into a wrong answer. Our <a href="/exponent-laws-guide/">exponent laws guide</a> and <a href="/is-mhf4u-hard/">Is MHF4U hard?</a> cover math skills that show up in SPH4U. Taking Advanced Functions alongside SPH4U helps, and we fill math gaps as we go.</p>"""),
            ("In person across Ottawa, or online", """<p>We coach Physics students in person in <a href="/tutor-kanata-ottawa/">Kanata</a>, <a href="/tutor-barrhaven-ottawa/">Barrhaven</a>, <a href="/tutor-orleans-ottawa/">Orléans</a>, <a href="/tutor-nepean-ottawa/">Nepean</a> and <a href="/tutor-stittsville-ottawa/">Stittsville</a>, and live online with a shared whiteboard anywhere in Ontario or abroad. See <a href="/areas/">all areas</a>.</p>"""),
            ("What parents can do", """<ul><li>Ask your teen to talk you through one homework problem. Where they get stuck shows whether the gap is the physics idea or the math.</li>
<li>Check whether your teen's university plans need SPH4U. Many engineering and physical science programs do. See <a href="/grade-12-courses-for-university-ontario/">Which Grade 12 courses do I need?</a></li>
<li>Get help early, ideally before the Forces unit in SPH3U or the Dynamics unit in SPH4U.</li>
<li>Book a free assessment. We check the math and science foundations and send a written plan within 24 hours.</li></ul>"""),
        ],
        "faq": [
            ("Which Physics courses do you tutor?", "Grade 11 SPH3U, Grade 12 SPH4U and Grade 12 College SPH4C, plus Grade 9 and 10 Science. We also coach AP and IB Physics online."),
            ("Is tutoring 1-on-1?", "Yes. Every session is one coach and one student, in person in Ottawa or live online."),
            ("How much does Physics tutoring cost?", "Every student's needs are different, so we share pricing after the free assessment, along with a written plan."),
            ("Can you help with the Waterloo physics contest?", "Yes. We offer optional practice for the University of Waterloo Sir Isaac Newton (SIN) Exam for senior physics students."),
        ],
        "related": [("SPH3U", "Grade 11 Physics", "/sph3u-physics-tutor-ottawa/"), ("SPH4U", "Grade 12 Physics", "/sph4u-physics-tutor-ottawa/"), ("MHF4U", "Advanced Functions", "/mhf4u-advanced-functions-tutor-ottawa/"), ("MCV4U", "Calculus & Vectors", "/mcv4u-calculus-vectors-tutor-ottawa/"), ("Math", "Tutor in Ottawa", "/math-tutor-ottawa/")],
    },
    {
        "slug": "math-tutor-ottawa", "kind": "hub", "card": "Grade 9–12 Math", "eyebrow": "1-on-1 Math tutoring", "service": "Math tutoring",
        "title": "Math Tutor in Ottawa: Grade 9–12 (MTH1W to MCV4U) | QueensCoaching",
        "desc": "1-on-1 Grade 9–12 Math tutoring in Ottawa and online: MTH1W and EQAO, MPM2D, MCR3U, MHF4U and MCV4U. We fix the basics while we cover the curriculum. Notes and stationery included. Book a free assessment.",
        "h1": "Math tutor in Ottawa for Grade 9–12",
        "sub": "Personalized 1-on-1 high school math coaching, from Grade 9 MTH1W to Grade 12 Calculus, in person across Ottawa or live online. We fix the basics while we cover the curriculum.",
        "answer": "QueensCoaching offers 1-on-1 Grade 9–12 Math tutoring in Ottawa and online, following the Ontario curriculum course by course. Every student starts with a free assessment that finds the earlier skills holding them back, then gets a written plan within 24 hours, personalized notes and all stationery.",
        "sections": [
            ("Math courses we coach", """<div class="grid" style="margin-top:8px">
<article class="card"><span class="tag">MTH1W</span><h3>Grade 9 Math</h3><p>The de-streamed Grade 9 course, with EQAO prep.</p><a class="card-link" href="/mth1w-grade-9-math-tutor-ottawa/">View MTH1W →</a></article>
<article class="card"><span class="tag">MPM2D</span><h3>Grade 10 Math</h3><p>Quadratics, analytic geometry and trigonometry.</p><a class="card-link" href="/mpm2d-math-tutor-ottawa/">View MPM2D →</a></article>
<article class="card"><span class="tag">MCR3U</span><h3>Grade 11 Functions</h3><p>Functions, exponential, discrete and trig functions.</p><a class="card-link" href="/mcr3u-functions-tutor-ottawa/">View MCR3U →</a></article>
<article class="card card-feature"><span class="tag">MHF4U</span><h3>Advanced Functions</h3><p>Logarithms, trig, polynomial and rational functions.</p><a class="card-link" href="/mhf4u-advanced-functions-tutor-ottawa/">View MHF4U →</a></article>
<article class="card card-feature"><span class="tag">MCV4U</span><h3>Calculus &amp; Vectors</h3><p>Derivatives, optimization, vectors, lines and planes.</p><a class="card-link" href="/mcv4u-calculus-vectors-tutor-ottawa/">View MCV4U →</a></article>
</div>
<p>We also coach MFM2P, MBF3C, MDM4U (Data Management) and MAP4C. <a href="/courses/#math">See all Math courses</a>.</p>"""),
            ("How we coach Math", """<p>High school math is a ladder: each course stands on the one before. A student struggling in Grade 11 Functions is often missing a Grade 9 or 10 skill, like integers, exponent laws or factoring. We fix the basics while we cover the curriculum:</p>
<ul><li>A free assessment with a foundations check, shared with parents</li>
<li>A written plan within 24 hours: the gaps to close and the course to cover</li>
<li>Personalized notes for every unit, kept in a binder, with all stationery included</li>
<li>Practice tests before every unit test and the final exam</li>
<li>True 1-on-1 attention every session, and a monthly progress note for parents</li></ul>"""),
            ("Where students usually get stuck", """<div class="table-wrap"><table class="compare"><thead><tr><th>Course</th><th>Common sticking point</th><th>Earlier skill behind it</th></tr></thead><tbody>
<tr><td>MTH1W</td><td>Algebra and linear relations</td><td>Fractions, integers, order of operations</td></tr>
<tr><td>MPM2D</td><td>Factoring and quadratics</td><td>Exponent laws, expanding expressions</td></tr>
<tr><td>MCR3U</td><td>Transformations, exponential functions, trig</td><td>Factoring, exponent laws, Grade 10 trig</td></tr>
<tr><td>MHF4U</td><td>Logarithms, rational functions, trig identities</td><td>MCR3U functions and trig</td></tr>
<tr><td>MCV4U</td><td>Derivative rules, optimization, vectors</td><td>Algebra, exponents and trig from MHF4U</td></tr>
</tbody></table></div>
<p>Read more in our guides: <a href="/exponent-laws-guide/">Exponent laws explained</a>, <a href="/is-mhf4u-hard/">Is MHF4U hard?</a> and <a href="/is-mcv4u-hard/">Is MCV4U hard?</a></p>"""),
            ("In person across Ottawa, or online", """<p>We coach Math students in person in <a href="/tutor-kanata-ottawa/">Kanata</a>, <a href="/tutor-barrhaven-ottawa/">Barrhaven</a>, <a href="/tutor-orleans-ottawa/">Orléans</a>, <a href="/tutor-nepean-ottawa/">Nepean</a> and <a href="/tutor-stittsville-ottawa/">Stittsville</a>, and live online with a shared whiteboard anywhere in Ontario or abroad. See <a href="/areas/">all areas</a>.</p>"""),
            ("What parents can do", """<ul><li>Look at the last few tests together and note which kinds of questions lost marks. That usually points to the gap.</li>
<li>Encourage short, regular practice instead of cramming the night before.</li>
<li>Check the math your teen's university or college plans need. See <a href="/grade-12-courses-for-university-ontario/">Which Grade 12 courses do I need?</a></li>
<li>Book a free assessment. We find the gaps and send a written plan within 24 hours.</li></ul>"""),
        ],
        "faq": [
            ("Which Math courses do you tutor?", "Every Ontario Grade 9–12 math course, from MTH1W and EQAO prep to MPM2D, MCR3U, MHF4U and MCV4U, plus MFM2P, MBF3C, MDM4U and MAP4C. We also coach SAT, AP and IB math online."),
            ("Is tutoring 1-on-1?", "Yes. Every session is one coach and one student, in person in Ottawa or live online."),
            ("How much does Math tutoring cost?", "Every student's needs are different, so we share pricing after the free assessment, along with a written plan."),
            ("Can you help with Waterloo math contests?", "Yes. We offer optional practice for University of Waterloo math contests such as the Euclid Contest for Grade 12 students."),
        ],
        "related": [("MTH1W", "Grade 9 Math", "/mth1w-grade-9-math-tutor-ottawa/"), ("MPM2D", "Grade 10 Math", "/mpm2d-math-tutor-ottawa/"), ("MCR3U", "Grade 11 Functions", "/mcr3u-functions-tutor-ottawa/"), ("MHF4U", "Advanced Functions", "/mhf4u-advanced-functions-tutor-ottawa/"), ("MCV4U", "Calculus & Vectors", "/mcv4u-calculus-vectors-tutor-ottawa/"), ("Physics", "Tutor in Ottawa", "/physics-tutor-ottawa/")],
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
    pub = g.get("published", PUBLISHED)
    byline = '<p class="byline">QueensCoaching parent guide · Updated November 2026</p>' if is_guide else ""
    body = f'''<section class="brand">
  {breadcrumb([("Home", "/"), crumb_mid, (g["h1"].replace("&amp;", "&"), None)])}
  <div class="wrap page-hero">
    <p class="eyebrow">{"Parent guide" if is_guide else g.get("eyebrow", "Signature program")}</p>
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
                   "url": SITE + path, "datePublished": pub, "dateModified": pub, "inLanguage": "en-CA",
                   "author": {"@type": "Organization", "name": "QueensCoaching", "url": SITE + "/"},
                   "publisher": {"@type": "Organization", "@id": f"{SITE}/#business", "name": "QueensCoaching", "logo": {"@type": "ImageObject", "url": SITE + "/logo.png"}},
                   "image": SITE + "/og-image.png"}
    else:
        main_ld = {"@context": "https://schema.org", "@type": "Service", "name": g["h1"].replace("&amp;", "&"), "description": g["desc"],
                   "serviceType": g.get("service", "Chemistry tutoring"), "url": SITE + path,
                   "provider": {"@type": ["EducationalOrganization", "LocalBusiness"], "@id": f"{SITE}/#business", "name": "QueensCoaching", "telephone": "+1-613-297-6844"},
                   "areaServed": [{"@type": "City", "name": "Ottawa"}, {"@type": "State", "name": "Ontario"}] if g["slug"].endswith("-ottawa") else [{"@type": "Country", "name": "Canada"}]}
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
                 "Plain-English guides for Ontario families: Is SCH3U hard? Is MHF4U hard? Is MCV4U hard? Exponent laws, Grade 12 courses for university, and more, from QueensCoaching in Ottawa.",
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

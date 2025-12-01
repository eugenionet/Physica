from pathlib import Path

from shiny import ui


from shiny.express import ui
from shiny import render

with ui.tags.head():
    # Link KaTeX CSS
    ui.tags.link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.css"
    ),
    ui.tags.script(src="https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.js"),
    ui.tags.script(src="https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/contrib/auto-render.min.js"),
    ui.tags.script("""
        document.addEventListener('DOMContentLoaded', function() {
            renderMathInElement(document.body);
        });
    """)
    


app_dir = Path(__file__).parent


# Helper function to restrict width of content
def restrict_width(*args, sm=None, md=None, lg=None, pad_y=5, **kwargs):
    cls = "mx-auto"
    if sm:
        cls += f" col-sm-{sm}"
    if md:
        cls += f" col-md-{md}"
    if lg:
        cls += f" col-lg-{lg}"

    return ui.div(*args, {"class": cls}, {"class": f"py-{pad_y}"}, **kwargs)


# Allow LaTeX to be displayed via MathJax
mathjax = ui.head_content(
    ui.tags.script(
        src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-chtml.js",
        #src="https://mathjax.rstudio.com/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML",
    ),
    ui.tags.script("if (window.MathJax) MathJax.Hub.Queue(['Typeset', MathJax.Hub]);"),
)

prose = ui.markdown(open(app_dir / "prose.md").read())


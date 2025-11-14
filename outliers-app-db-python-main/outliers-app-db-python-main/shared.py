from pathlib import Path

from shiny import ui


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
        #src="https://mathjax.rstudio.com/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
        src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-chtml.js"
    ),
    ui.tags.script("if (window.MathJax) MathJax.Hub.Queue(['Typeset', MathJax.Hub]);"),
)

mathjax_foot = ui.footer_content(
    ui.tags.script(
        src="https://code.jquery.com/jquery-3.7.1.min.js", integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=", crossorigin="anonymous",
        src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-chtml.js", integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz", crossorigin="anonymous"
    ),
)


prose = ui.markdown(open(app_dir / "prose.md").read())

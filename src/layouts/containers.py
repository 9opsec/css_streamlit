import streamlit as st
from textwrap import dedent
from streamlit_monaco import st_monaco
from common import HTML_Template, CopyToClipboard, MainCSS, CodeExportParse

st.header("Containers")
st.html(HTML_Template.base_style.substitute(css=MainCSS.initial_page_styles))


st.write(
    "To style a specific container, assign a value to the `key` argument to create a CSS class.  "
)

st.subheader("Try it!")
code, preview = st.columns(2, border=True, vertical_alignment="top")


with code:
    container_css = dedent(
        """
.st-key-styled_container{
    background-color:grey;
    border-radius:1rem;
    padding:1rem;
    min-height:100px;
    box-shadow: 3px 5px 15px 0px rgba(128, 128, 128, 0.245);
    }

 .st-key-styled_container div[data-testid="stText"] div{
    color:white;
    
}
           """
    ).strip()
    styles = st_monaco(
        value=container_css,
        height="400px",
        language="css",
        lineNumbers=True,
        minimap=False,
    )


def containers_code():
    with st.container(key="styled_container"):
        st.text("This is a styled container")

    with st.container():
        st.text("This is an unstyled container")


st_code = str(CodeExportParse(fn=containers_code).parse_text)

with preview:
    if st.toggle("Preview Style Changes", value=True):
        st.html(HTML_Template.base_style.substitute(css=styles))
    containers_code()
    st.code(st_code)

CopyToClipboard(css_text=styles, streamlit_code=st_code)

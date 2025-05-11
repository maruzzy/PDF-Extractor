import streamlit as st
from PyPDF2 import PdfReader

st.title("PDF Mietvertrag Extraktor")

uploaded_file = st.file_uploader("Lade deinen Mietvertrag hoch", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    st.write("Inhalt des Mietvertrags:")
    st.write(text)

    # Hier kannst du Logik hinzufügen, um wichtige Punkte zu extrahieren
    # Beispiel: Mietbeginn, Mietende, Verlängerungsoption
    st.write("Hier kannst du die extrahierten Punkte anzeigen.")
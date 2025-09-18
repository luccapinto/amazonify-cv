import streamlit as st
from bedrock_analyzer import analisar_cv_com_bedrock

# Interface
st.title("Analisador de CV com IA 🧠")
st.markdown("""
Esta aplicação utiliza o poder da IA generativa da AWS (Amazon Bedrock) para analisar um currículo em relação a uma descrição de vaga,
com foco nos Princípios de Liderança da Amazon.

**Como funciona:**
1.  Cole o texto do currículo no campo "Currículo".
2.  Cole a descrição da vaga no campo "Vaga".
3.  Clique em "Analisar".
4.  Aguarde a análise da IA e veja o resultado abaixo.
""")

st.header("Insira os dados")
texto_cv = st.text_area("Currículo (CV)", height=300, placeholder="Cole o texto do seu currículo aqui...")
texto_vaga = st.text_area("Vaga", height=300, placeholder="Cole a descrição da vaga aqui...")

if st.button("Analisar"):
    if texto_cv and texto_vaga:
        with st.spinner("Analisando seu currículo com a IA... Por favor, aguarde."):
            try:
                resultado_analise = analisar_cv_com_bedrock(texto_cv, texto_vaga)
                st.header("Resultado da Análise")
                st.markdown(resultado_analise)
            except Exception as e:
                st.error(f"Ocorreu um erro durante a análise: {e}")
    else:
        st.warning("Por favor, preencha ambos os campos (Currículo e Vaga) antes de analisar.")

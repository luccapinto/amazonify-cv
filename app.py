import streamlit as st
from bedrock_analyzer import analisar_cv_com_bedrock

# Interface
st.title("🚀 AmazonifyCV - IA Exclusiva para Vagas AWS")
st.markdown("""
<div style="background: linear-gradient(90deg, #FF9900, #232F3E); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
    <h3 style="color: white; margin: 0;">🎯 Sua porta de entrada para a Amazon Web Services</h3>
    <p style="color: white; margin: 5px 0 0 0;">Powered by Amazon Bedrock AI</p>
</div>

**AmazonifyCV** é a plataforma de IA mais avançada para otimizar seu currículo especificamente para oportunidades na **Amazon Web Services**. 

Nossa IA foi treinada com foco nos **14 Princípios de Liderança da Amazon** e nas competências mais valorizadas pela AWS, garantindo que seu perfil se destaque nos processos seletivos.

### 🔥 Por que escolher o AmazonifyCV?
- ✅ **IA Especializada**: Focada exclusivamente em vagas da Amazon AWS
- ✅ **Princípios de Liderança**: Análise baseada nos 14 Leadership Principles da Amazon
- ✅ **Amazon Bedrock**: Powered pela mais avançada IA generativa da AWS
- ✅ **Feedback Personalizado**: Sugestões específicas para maximizar suas chances

### 📋 Como usar:
1. **Cole seu currículo** no campo abaixo
2. **Adicione a descrição da vaga AWS** desejada
3. **Clique em Analisar** e deixe nossa IA trabalhar
4. **Receba insights personalizados** para otimizar seu perfil
""", unsafe_allow_html=True)

st.header("📝 Prepare seu currículo para a AWS")
texto_cv = st.text_area(
    "📄 Seu Currículo", 
    height=300, 
    placeholder="Cole aqui o texto completo do seu currículo atual...",
    help="Inclua todas as suas experiências, habilidades técnicas e conquistas profissionais"
)
texto_vaga = st.text_area(
    "🎯 Descrição da Vaga AWS", 
    height=300, 
    placeholder="Cole aqui a descrição completa da vaga da Amazon AWS que você deseja...",
    help="Inclua todos os requisitos, responsabilidades e qualificações mencionadas na vaga"
)

if st.button("🚀 Analisar com IA da AWS", type="primary"):
    if texto_cv and texto_vaga:
        with st.spinner("🤖 Nossa IA está analisando seu currículo com base nos Princípios de Liderança da Amazon... Aguarde alguns instantes."):
            try:
                resultado_analise = analisar_cv_com_bedrock(texto_cv, texto_vaga)
                st.header("📊 Análise Personalizada - Powered by Amazon Bedrock")
                st.markdown(resultado_analise)
                
                st.success("✅ Análise concluída! Use essas recomendações para otimizar seu currículo e aumentar suas chances na AWS.")
                
                st.markdown("""
                ---
                💡 **Dica Pro**: Implemente as sugestões da nossa IA e execute uma nova análise para ver sua evolução!
                
                🔄 **Quer mais?** Teste com diferentes vagas da AWS para descobrir qual perfil combina melhor com você.
                """)
            except Exception as e:
                st.error(f"❌ Ops! Ocorreu um erro durante a análise: {e}")
                st.info("💬 Tente novamente em alguns instantes. Se o problema persistir, verifique sua conexão.")
    else:
        st.warning("⚠️ Para uma análise completa, preencha tanto seu currículo quanto a descrição da vaga AWS desejada.")

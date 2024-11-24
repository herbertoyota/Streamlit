# arquivo_principal.py

import streamlit as st
import dashboard_vendas
import analise_clientes
import sql_project
import texto
import about_text
import mental
import worldbank

# Configura o layout da página
st.set_page_config(layout="wide")

# Barra lateral para navegação
st.sidebar.title("Herbert Toyota")
st.sidebar.write("Select a section to browse the portfolio:")

# Botões de rádio na barra lateral para selecionar a seção
selecao = st.sidebar.radio(
    "Section",
    ("About", "Education", "Skills", "Experience", "Projects", "Contact")
)

# Função para exibir o conteúdo com base na seleção
def mostrar_secao(secao):
    if secao == "About":
        # Dividindo o layout em duas colunas
        col1, col2 = st.columns([2, 2])

        with col1:
            # Texto à esquerda com espaçamento ajustado entre linhas
            st.title("About")
            st.markdown(
                """
                <p style='line-height: 1.4;'>
                    I am graduated in Business Administration at UNICAMP.
                    During my time at the university, I dedicated time to volunteer teaching, helping students prepare for high school by guiding them in mathematics.<br><br>
                    I also completed a 1 month an exchange program in Fort Lauderdale to improve my English skills, enhancing my experience in international environments.<br><br>
                    In addition, my experience includes working in finance and risk departments, where I honed my skills in analyzing financial data, creating indicators for the risk department, and automating tasks.<br><br>
                    Currently, I am advancing my technical expertise in data analysis, automation, and artificial intelligence.
                    Through this portfolio, I aim to showcase my technical skills and dedication to my professional growth.
                </p>
                """, 
                unsafe_allow_html=True
            )
        with col2:
            for _ in range(6):
                st.write("")
            st.image("Capturar.png")
    elif secao == "Education":
        st.title("Education")
        st.write("**Universidade Estadual de Campinas (UNICAMP)**")
        st.write('Bacharelor of Business Administration: 2015-2019')
    elif secao == "Skills":
        st.title("Skills")
     # Dicionário com as habilidades e níveis de proficiência em porcentagem
     # Dicionário com as habilidades e níveis de proficiência
        skills = {
            "Python": "Good",
            "SQL": "Intermediate",
            "Power BI": "Good",
            "Excel": "Advanced",
            
        }

        # Conversão dos níveis de proficiência em porcentagem para a barra de progresso
        proficiency_levels = {
            "Beginner": 25,
            "Intermediate": 50,
            "Good": 75,
            "Advanced": 90
        }

        # Exibir barras de habilidade com HTML e CSS
        for skill, level in skills.items():
            percentage = proficiency_levels.get(level, 50)  # Padrão para "Intermediate" se o nível não for encontrado
            st.markdown(f"""
                <div style="margin: 10px 0;">
                    <strong>{skill} - {level}</strong>
                    <div style="background-color: #ddd; border-radius: 8px; width: 100%; height: 24px;">
                        <div style="background-color: #4CAF50; width: {percentage}%; height: 100%; border-radius: 8px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    elif secao == "Experience":
        st.title("Experience")
        st.write("**Gradus Consultoria**")
        st.write("**Administrative e Financial Analyst | May/2022 - Ago/2024**")
        st.write("- Created and implemented a system to automatically populate payment information, reducing time spent on manual entries by 30 minutes daily")
        st.write("- Developed, monitored, and regularly updated cash flow projections, including revenue and expense forecasting, to enhance performance predictions")      
        st.write("- Identified opportunities to cut operational costs and expenses, proposing and implementing initiatives that optimized processes and increased financial efficiency")
        st.write("---")
        st.write("**Honda Dealer**")
        st.write("**Financial Assistant | Nov/2020 - Apr/2022**")
        st.write("- Programmed and managed receivables and payments, ensuring accurate and timely processing of transactions")
        st.write("- Conducted thorough credit analysis of suppliers to assess risk, support procurement decisions, and maintain a stable financial base")
        st.write("- Managed collections and addressed delinquencies, implementing strategies to improve recovery rates and reduce outstanding receivables")
        st.write("---")
        st.write("**Koin**")
        st.write("**Risk Analyst | Oct/2019 - Apr/2020**")
        st.write("- Analyzed key performance indicators KPIs for the risk team to evaluate departmental performance and the effectiveness of risk mitigation strategies")
        st.write("- Supported data-driven decision-making by developing insights into risk trends, contributing to a proactive approach in managing company-wide risks")
        st.write("- Prepared and enhanced reports within the risk database, facilitating improved tracking and measurement of risk impact levels across the company")
        st.write("---")
        st.write("**Nextel**")
        st.write("**Audit Intern | Jan/2019 - Jul/2019**")
        st.write("- Contributed to the development of dashboards to visualize key metrics, aiding in the strategic analysis of financial and operational data")
        st.write("- Assisted in executing audit tasks, enhancing compliance and providing valuable insights into financial integrity")
        st.write("- Prepared detailed expense reports for the company’s Corporate Card program, analyzing spending patterns to verify alignment with company policies and support responsible financial management")
    elif secao == "Projects":
        st.title("Projects")

        # Ferramentas e seus respectivos projetos importados
        ferramentas = {
            "Power BI": [dashboard_vendas.project_info, analise_clientes.project_info],
            "SQL": [sql_project.project_info],
            "Python": [texto.project_info, mental.project_info,worldbank.project_info]
        }
        
        # Seleção de Ferramenta
        ferramenta_selecionada = st.radio("Choose a tool to see the projects:", list(ferramentas.keys()))
        
        # Exibe projetos da ferramenta selecionada
        st.subheader(f"Projects in {ferramenta_selecionada}")
        projetos = ferramentas[ferramenta_selecionada]
        
        # Variável para armazenar o projeto selecionado
        projeto_selecionado = None
        
        # Seleciona um projeto através de uma imagem clicável
        cols = st.columns(len(projetos))
        for i, projeto in enumerate(projetos):
            with cols[i]:
                if st.button(projeto["nome"]):
                    projeto_selecionado = projeto
        
        # Verifica se um projeto foi selecionado
        if projeto_selecionado:
            # Exibe os detalhes do projeto selecionado
            st.markdown("---")  # Linha divisória para organizar a página
            st.subheader(projeto_selecionado["nome"])
            st.image(projeto_selecionado["imagem_url"], width=500)
            st.write(projeto_selecionado["descricao"])

            
    elif secao == "Contact":
        st.title("Contact")
        st.write("**Linkedin**: https://www.linkedin.com/in/herbert-toyota-509985162/")
        st.write("")
        st.write("**Github**: https://github.com/herbertoyota")
        st.write("")
        st.write("**Email**: herbertyukihiro@gmail.com")

# Chama a função para exibir a seção selecionada
mostrar_secao(selecao)

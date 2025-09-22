import streamlit as st
import os
from streamlit import session_state as ss


# Configuração da página
st.set_page_config(
    page_title="Homeopatia Integrativa - Catálogo",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)


depoimentos = {
    "Composto detox antiflamatorio emagrecedor": {
        "cliente": "Conceição Aparecida",
        "imagem": "https://via.placeholder.com/200x200?text=Foto+Maria",
        "depoimento": "“Perdi 8kg em 2 meses sem passar fome, minha digestão melhorou e minha pele ficou incrível! Nunca imaginei que um tratamento natural pudesse ser tão eficaz.”"
    },
    "Calmix Calmante Natural antidepressivo": {
        "cliente": "Barbara Monique",
        "imagem": "https://via.placeholder.com/200x200?text=Foto+Carlos",
        "depoimento": "“Depois de anos em antidepressivos, o Calmix me trouxe calma sem efeitos colaterais. Voltei a dormir e a sorrir naturalmente.”"
    },
    "Composto Hipertensão": {
        "cliente": "Cintia Reis",
        "imagem": "https://via.placeholder.com/200x200?text=Foto+Ana",
        "depoimento": "“Minha pressão está estável há 6 meses. Meu cardiologista ficou impressionado!”"
    },
    "Elixir Saúde da mulher": {
        "cliente": "Romeria Souza",
        "imagem": "https://via.placeholder.com/200x200?text=Foto+Juliana",
        "depoimento": "“Ciclos regulares, TPM suave e mais energia. Essencial para toda mulher moderna!”"
    },
    "Complexo Anemia": {
        "cliente": "Roberto M.",
        "imagem": "https://via.placeholder.com/200x200?text=Foto+Roberto",
        "depoimento": "“Meus exames voltaram ao normal em 3 semanas. Tive mais disposição e cor na pele.”"
    },
    "Xarope Fito Saúde Natural": {
        "cliente": "Fernanda T.",
        "imagem": "https://via.placeholder.com/200x200?text=Foto+Fernanda",
        "depoimento": "“Minha filha de 5 anos não toma antibiótico há 1 ano. O xarope natural dela é milagroso!”"
    }
}


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300;400;700;900&family=Lato:wght@300;400&display=swap');


    /* Estilo da logo no sidebar */
    [data-testid="stSidebarHeader"] img {
        border-radius: 50% !important;  /* Borda circular */
        border: 4px solid #D2A25A !important;  /* Borda em mostarda (cor da marca) */
        box-shadow: 0 4px 12px rgba(32, 66, 38, 0.2) !important;
        padding: 2px;
    }

    /* Estilo da logo no modo mobile ou header */
    [data-testid="stHeader"] img {
        border-radius: 50% !important;
        border: 3px solid #204226 !important;
        box-shadow: 0 2px 8px rgba(32, 66, 38, 0.2) !important;
    }       

    html, body, [class*="css"] {
        font-family: 'Lato', sans-serif;
    }

    h1, h2, h3, h4 {
        font-family: 'Merriweather', Georgia, serif;
        color: #204226;
    }

    .product-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #E0BF7E;
        margin-bottom: 0.5rem;
    }

    .product-desc {
        font-size: 1.1rem;
        line-height: 1.6;
        color: white;
        margin-bottom: 1rem;
    }

    .stButton>button {
        background-color:  #B07F39;
        color: white;
        border-radius: 25px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color:  #B07F39;
        transform: scale(1.05);
    }

    /* Botões de depoimento na sidebar */
    .sidebar .stButton>button {
        background-color: #B07F39 !important;  /* Mostarda escuro */
        color: white !important;               /* Texto branco */
        font-weight: 700;
        border: 2px solid #204226;             /* Borda verde escuro (marca) */
        border-radius: 12px;
        padding: 0.5rem 1rem;
        font-family: 'Merriweather', Georgia, serif;
        transition: all 0.3s ease;
    }

    .sidebar .stButton>button:hover {
        background-color: #B07F39 !important;  /* Mais escuro no hover */
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(32, 66, 38, 0.2);
        color: white !important;  /* Mantém branco no hover */
    }

    /* Botão "Fechar depoimento" */
    .stButton>button[kind="secondary"] {
        background-color:linear-gradient(135deg, #204226, #2E5D32);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 0.4rem 1rem;
    }

    .stButton>button[kind="secondary"]:hover {
        background-color: linear-gradient(135deg, #204226, #2E5D32);
    }

    /* Estilo do expander de depoimento */
    .streamlit-expanderHeader {
        background-color: #B07F39 !important;
        border: 2px solid #204226 !important;
        border-radius: 10px !important;
        color: #204226 !important;
        font-weight: 700;
        font-family: 'Merriweather', Georgia, serif;
    }

    .streamlit-expanderContent {
        background-color: #B07F39 !important;
        padding: 1rem;
        border-radius: 0 0 10px 10px;
        border: 1px solid #D2A25A;
    }

    .footer {
        text-align: center;
        padding: 2rem;
        font-size: 0.9rem;
        color: white;
        background-color: #B07F39;
        border-top: 3px solid #204226;
    }

    .header-banner {
        background:  #B07F39 !important;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
            /* Estilo do botão "Comprar Agora" */
    .stLinkButton>button {
        background-color: #204226 !important;  /* Verde escuro da logo */
        color: white !important;               /* Texto branco para contraste */
        border: 2px solid #D2A25A !important;  /* Borda em mostarda para harmonizar */
        border-radius: 25px;
        padding: 0.6rem 1.5rem;
        font-weight: 700;
        font-family: 'Merriweather', Georgia, serif;
        transition: all 0.3s ease;
    }

    .stLinkButton>button:hover {
        background-color: #1B3820 !important;  /* Verde mais escuro no hover */
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(32, 66, 38, 0.3);
        color: white !important;
    }
            
    /* Estilo para o popover de depoimento */
    .popover-depoimento {
        text-align: center;
        padding: 1.5rem;
        max-width: 400px;
    }

    .popover-depoimento img {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        margin: 1rem auto;
        border: 4px solid #D2A25A;
        box-shadow: 0 4px 12px rgba(32, 66, 38, 0.2);
    }

    .popover-depoimento h4 {
        color: #204226;
        font-family: 'Merriweather', Georgia, serif;
        margin: 0.5rem 0;
    }

    .popover-depoimento p {
        font-family: 'Lato', sans-serif;
        color: #4A2F24;
        line-height: 1.6;
        margin: 1rem 0;
        font-style: italic;
    }

    .popover-depoimento .stButton>button {
        background-color: #6B8A59 !important;
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 0.4rem 1rem;
        font-weight: 600;
    }

    .popover-depoimento .stButton>button:hover {
        background-color: #5A754A !important;
    }

    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("""
    <div class="header-banner">
        <h1>🌿 Catálogo Homeopatia Integrativa</h1>
        <p>Tratamentos naturais, holísticos e integrativos para equilibrar corpo, mente e espírito</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar com PDF e testemunhos (versão compatível)
with st.sidebar:
    st.image("./img/logo/logo1.jpg", width=300)
    st.header("📥 Recursos")
    st.markdown(
        "📄 [Baixar Catálogo Completo em PDF](https://example.com/sample.pdf)")
    st.markdown("---")
    st.subheader("💬 Testemunhos Reais")
    st.write("Clique nos botões abaixo para ler experiências de clientes.")

   # Inicializa o estado se não existir
    if "depoimento_aberto" not in st.session_state:
        st.session_state.depoimento_aberto = None

    # Botões que abrem o popover de depoimento
    if st.button("💬 Conceição Aparecida - Detox", key="btn1", use_container_width=True):
        st.session_state.depoimento_aberto = "Composto detox antiflamatorio emagrecedor"
        st.rerun()

    if st.button("💬 Babara Monique - Calmix", key="btn2", use_container_width=True):
        st.session_state.depoimento_aberto = "Calmix Calmante Natural antidepressivo"
        st.rerun()

    if st.button("💬 Cintia Reis - Hipertensão", key="btn3", use_container_width=True):
        st.session_state.depoimento_aberto = "Composto Hipertensão"
        st.rerun()

    if st.button("💬 Romeria Souza - Saúde da Mulher", key="btn4", use_container_width=True):
        st.session_state.depoimento_aberto = "Elixir Saúde da mulher"
        st.rerun()

    if st.button("💬 Roberto M. - Anemia", key="btn5", use_container_width=True):
        st.session_state.depoimento_aberto = "Complexo Anemia"
        st.rerun()

    if st.button("💬 Fernanda T. - Xarope", key="btn6", use_container_width=True):
        st.session_state.depoimento_aberto = "Xarope Fito Saúde Natural"
        st.rerun()


def mostrar_depoimento(item):
    # Verifica se o item está ativo
    if st.session_state.depoimento_aberto != item:
        return  # Não mostra se não estiver aberto

    dados = depoimentos.get(item, {})
    cliente = dados.get("cliente", "Cliente")
    imagem = dados.get(
        "imagem", "https://via.placeholder.com/200x200?text=Sem+Foto")
    depoimento = dados.get("depoimento", "Depoimento não disponível.")

    # Criar popover com controle de visibilidade
    with st.popover(f"💬 {cliente} - Depoimento", use_container_width=True):
        st.markdown('<div class="popover-depoimento">', unsafe_allow_html=True)

        # Nome do cliente
        st.markdown(f"### {cliente}")

        # Imagem centralizada
        st.image(imagem, use_container_width=False)

        # Depoimento
        st.markdown(f"<p>{depoimento}</p>", unsafe_allow_html=True)

        # Botão Fechar
        if st.button("Fechar depoimento", key=f"close_{item}"):
            st.session_state.depoimento_aberto = None  # Fecha o popover
            st.rerun()  # Recarrega a página para aplicar a mudança

        st.markdown('</div>', unsafe_allow_html=True)


# Exibir depoimento selecionado
if st.session_state.depoimento_aberto:
    st.markdown("### 🌿 Depoimento Selecionado")
    mostrar_depoimento(st.session_state.depoimento_aberto)


# Lista de produtos com dados
produtos = [
    {
        "nome": "Composto detox antiflamatorio emagrecedor",
        "descricao": "Composto  detox  e magrecedor 100% Natural é uma fórmula fitoterápica"
        " desenvolvida com ingredientes tradicionalmente reconhecidos por suas propriedades"
        " diuréticas, digestivas e termogênicas. Contendo Cavalinha,  e Espinheira Santa, auxilia"
        " na eliminação de líquidos, redução de inchaço e apoio ao emagrecimento saudável."
        " Para que serve o Composto Diurético Emagrecedor? Este composto é indicado para quem"
        " deseja reduzir medidas, combater a retenção de líquidos, melhorar a digestão e"
        " potencializar dietas de emagrecimento. É uma opção natural para quem busca emagrecer com"
        " saúde e qualidade.",
        "imagem": "./img/produtos/detox-antiinflamatorio-emagrecedor.png",
        "link": "https://sandbox.asaas.com/c/m9lhcxtjutqdgwkl"
    },
    {
        "nome": "Calmix Calmante Natural antidepressivo",
        "descricao": "O calmix foi especialmente desenvolvido para quem busca um alívio natural e eficaz contra os momentos de estresse e ansiedade. Combinando ervas poderosas como Camomila, Capim Cidreira, Erva Cidreira, Passiflora, Mulungu, Capim Limão, Melissa, Erva de São João e Alecrim, esse mix oferece um efeito calmante, relaxante e tranquilizante, promovendo o equilíbrio mental e o bem-estar físico.🍃 Fórmula Natural e Equilibrada – Cada erva tem propriedades únicas que trabalham em sinergia para promover o relaxamento, melhorar o sono e reduzir os níveis de estresse. O Mulungu e a Passiflora são conhecidos por suas ações calmantes, enquanto a Melissa e o Alecrim ajudam a acalmar a mente e melhorar o humor.",
        "imagem": "./img/produtos/calmix-antidepressivo.png",
        "link": "https://pagseguro.com/calmix"
    },
    {
        "nome": "Composto Hipertensão",
        "descricao": "O Composto Hipertensão é uma fórmula fitoterápica desenvolvida especialmente para auxiliar no tratamento da pressão alta, promovendo o equilíbrio da saúde cardiovascular e o bem-estar geral.🔹 Principais BenefíciosAtua como diurético natural, auxiliando na eliminação de líquidos e na redução da sobrecarga do coração.Favorece a saúde cardiovascular, ajudando na regulação da pressão arterial.Contribui para o controle do colesterol, prevenindo complicações circulatórias. Possui ação anti-inflamatória e antioxidante, protegendo as células contra os radicais livres.",
        "imagem": "./img/produtos/composto-hipertensao.png",
        "link": "https://pagseguro.com/hipertensao"
    },
    {
        "nome": "Elixir Saúde da mulher",
        "descricao": "Indicação: Inflamação no útero, corrimento, cólica menstrual, ovário policístico, regulador menstrual, ferida uterina, inflamação da via urinária, inflamação no óvario, menopausa, depurativo de sangue e limpa a pele.Ingredientes:  mamica de cadela, carapiá, erva joão da costa, algodãozinho, barbatimão, vassourinha, catuaba, sangra d'água, chapeu de couro, ipê roxo, agoniada, jatobá, jequitibá e erva de bicho.",
        "imagem": "./img/produtos/elixir-saude-da-mulher.png",
        "link": "https://pagseguro.com/elixir-mulher"
    },
    {
        "nome": "Complexo Anemia",
        "descricao": "O Complexo Anemia foi desenvolvido para auxiliar no tratamento da anemia, promovendo mais saúde e bem-estar de forma natural. Sua fórmula reúne vitaminas essenciais, minerais e extratos de plantas que fortalecem o organismo e ajudam na formação do sangue.🔹 Benefícios principais:Contribui para o tratamento da anemiaAuxilia no aumento da produção de hemoglobinaFortalece o sistema imunológicoFonte de ácido fólico, vitamina C e vitamina B12Combina ervas e nutrientes funcionais que estimulam energia e vitalidade.",
        "imagem": "./img/produtos/complexo-anemia.png",
        "link": "https://pagseguro.com/anemia"
    },
    {
        "nome": "Xarope Fito Saúde Natural",
        "descricao": "O Xarope Fito Saúde Natural é uma fórmula integrativa desenvolvida para fortalecer o sistema respiratório, aliviar sintomas de gripes, resfriados, bronquite asmática, tosse seca, pigarro e viroses, além de contribuir para o bem-estar geral do organismo.",
        "imagem": "./img/produtos/xarope-fito-saude-natural.png",
        "link": "https://pagseguro.com/xarope"
    }
]

# Exibição dos produtos
for i, produto in enumerate(produtos):
    with st.container():
        col1, col2 = st.columns([1, 2], gap="large")

        with col1:
            img_path = produto["imagem"]
            if os.path.exists(img_path):
                st.image(
                    img_path, use_container_width=True)
            else:
                st.error(f"⚠️ Imagem não encontrada: {img_path}")
                st.image("https://via.placeholder.com/400x300?text=Imagem+Indisponível",
                         caption="Imagem indisponível", use_container_width=True)

        with col2:
            st.markdown(
                f"<div class='product-title'>{produto['nome']}</div>", unsafe_allow_html=True)
            st.markdown(
                f"<div class='product-desc'>{produto['descricao']}</div>", unsafe_allow_html=True)
            st.link_button("💳 Comprar Agora",
                           produto["link"], use_container_width=True)
            st.markdown("---")

        if i < len(produtos) - 1:
            st.markdown("<br>", unsafe_allow_html=True)

# Rodapé
st.markdown("""
    <div class="footer">
        <p>🌿 Homeopatia Integrativa — Cuidando de você de forma natural, suave e duradoura.</p>
        <p>📞 (11) 99999-9999 | ✉️ contato@homeopatiaintegrativa.com.br</p>
        <p>📍 São Paulo, Brasil</p>
    </div>
""", unsafe_allow_html=True)

import streamlit as st
from datetime import datetime
def main ():

    st. title("Sistema de CRM e vendas ZapFlow")
    email = st.text_input("Campo inserção email do vendedor")
    data = st.date_input("Campo para selecionar data da compra")
    hora = st.time_input("Campo para selecionar hora da compra")
    valor = st.number_input("Campo numerico para inserir valor monetario da venda realizada")
    quantidade= st.number_input("Campo numerico para inserior quantidade de produtos vendidos")
    produto= st.selectbox("Campo para seleção do produto vendido. ",options=["ZapFlow com Gemini","ZapFlow com ChatGPT","ZapFlow com Lhama 3.0"])

    if st.button("Salvar"):
        
        data_hora = datetime.combine(data,hora)

        st.write("Dados da venda")
        st.write(f"Email do vendedor : {email}")
        st.write(f"Data e hora da compra : {data_hora} ")
        st.write(f"O valor da compra foi de : {valor}")
        st.write(f"A quantidade de produtos foi de : {quantidade}")
        st.write(f"Produto : {produto} ")
  

if  __name__== "__main__":
    main()
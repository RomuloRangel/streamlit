import streamlit as st
from datetime import datetime
from contrato import Vendas
from pydantic import ValidationError


def main ():

    st. title("Sistema de CRM e vendas ZapFlow")
    email = st.text_input("Campo inserção email do vendedor")
    data = st.date_input("Campo para selecionar data da compra")
    hora = st.time_input("Campo para selecionar hora da compra")
    valor = st.number_input("Campo numerico para inserir valor monetario da venda realizada")
    quantidade= st.number_input("Campo numerico para inserior quantidade de produtos vendidos")
    produto= st.selectbox("Campo para seleção do produto vendido. ",options=["ZapFlow com Gemini","ZapFlow com ChatGPT","ZapFlow com Lhama 3.0"])

    if st.button("Salvar"):
            try:
        
                data_hora = datetime.combine(data, hora)
                
                venda = Vendas(
                    email = email,
                    data = data_hora,
                    valor = valor,
                    quantidade = quantidade,
                    produto = produto
                )
                st.write(venda)

                
            except ValidationError as e:
                 st.error(f"Deu error{e}")

       
  

if  __name__== "__main__":
    main()
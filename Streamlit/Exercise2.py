import streamlit as st

def main():
    st.title('Lista Zakupów z Priorytetami')

    if 'shopping_list' not in st.session_state:
        st.session_state.shopping_list = []

    with st.form("add_product_form"):
        new_product = st.text_input("Dodaj nowy produkt", "")
        priority = st.selectbox("Wybierz priorytet", ["Niski", "Średni", "Wysoki"], index=1)
        submit_button = st.form_submit_button(label="Dodaj do listy")

    if submit_button and new_product:
        if new_product not in [item['name'] for item in st.session_state.shopping_list]:
            st.session_state.shopping_list.append({'name': new_product, 'priority': priority, 'purchased': False})
            st.success(f"Dodano: {new_product} z priorytetem {priority}")
        else:
            st.error("Ten produkt jest już na liście!")

    show_products("Do kupienia", False)

    if any(item['purchased'] for item in st.session_state.shopping_list):
        if st.button("Usuń zakupione produkty"):
            st.session_state.shopping_list = [item for item in st.session_state.shopping_list if not item['purchased']]
            st.info("Usunięto zakupione produkty.")

    show_products("Zakupione", True)

def mark_purchased(index):
    st.session_state.shopping_list[index]['purchased'] = True
    st.experimental_rerun()

def show_products(title, purchased_status):
    products = [item for item in st.session_state.shopping_list if item['purchased'] == purchased_status]
    if products:
        st.subheader(title)
        for index, item in enumerate(st.session_state.shopping_list):
            if item['purchased'] == purchased_status:
                if not purchased_status:
                    col1, col2 = st.columns([8, 2])
                    with col1:
                        st.text(f"{item['name']} ({item['priority']})")
                    with col2:
                        if st.checkbox("Kupione", key=f"cb_{index}", value=item['purchased']):
                            mark_purchased(index)
                else:
                    st.text(f"{item['name']} ({item['priority']})")

if __name__ == "__main__":
    main()

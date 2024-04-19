import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Question': [
        "Jaki algorytm używa się do rekomendacji filmów na platformach streamingowych?",
        "Który z tych algorytmów jest przykładem uczenia ze wzmocnieniem?",
        "Co jest głównym zadaniem sieci neuronowych konwolucyjnych?",
        "W jaki sposób przeciwdziałać problemowi nierówności klas w danych uczących?",
        "Jaki typ problemu można rozwiązać za pomocą algorytmu klastrowania?",
        "Co to jest regularyzacja w kontekście uczenia maszynowego?",
        "Jaki jest główny cel stosowania walidacji krzyżowej?",
        "Jakie jest znaczenie funkcji aktywacji w sieciach neuronowych?",
        "Co to jest 'przeklęcie wymiarowości'?",
        "W jaki sposób gradient boosting minimalizuje błąd w uczeniu maszynowym?"
    ],
    'Options': [
        ['Algorytm k-najbliższych sąsiadów', 'Regresja liniowa', 'Random Forest', 'Singular Value Decomposition'],
        ['Q-learning', 'Regresja logistyczna', 'Drzewa decyzyjne', 'SVM'],
        ['Analiza danych tekstowych', 'Detekcja anomalii', 'Rozpoznawanie obrazów', 'Predykcja szeregów czasowych'],
        ['Oversampling', 'PCA', 'Stosowanie niskiego współczynnika uczenia', 'Eliminacja cech'],
        ['Regresja', 'Klasyfikacja', 'Grupowanie', 'Redukcja wymiarów'],
        ['Metoda polegająca na dodaniu stałej do funkcji strat', 'Technika wzmacniania modelu', 'Metoda optymalizacji', 'Technika uczenia nienadzorowanego'],
        ['Zapobieganie przetrenowaniu', 'Zwiększenie szybkości uczenia', 'Redukcja kosztów obliczeniowych', 'Automatyczne dostosowanie parametrów'],
        ['Przekształca dane wejściowe w wyjściowe', 'Reguluje tempo uczenia', 'Zapobiega przetrenowaniu', 'Zapewnia nieliniowość modelu'],
        ['Problem występujący przy zbyt dużej liczbie cech', 'Typ algorytmu uczenia maszynowego', 'Technika wizualizacji danych', 'Metoda selekcji cech'],
        ['Dodaje wyniki wielu modeli', 'Wykorzystuje różne funkcje strat', 'Tworzy sekwencyjne modele na podstawie błędów', 'Stosuje różne szybkości uczenia']
    ],
    'Correct Answer': [
        'Singular Value Decomposition',
        'Q-learning',
        'Rozpoznawanie obrazów',
        'Oversampling',
        'Grupowanie',
        'Metoda polegająca na dodaniu stałej do funkcji strat',
        'Zapobieganie przetrenowaniu',
        'Zapewnia nieliniowość modelu',
        'Problem występujący przy zbyt dużej liczbie cech',
        'Tworzy sekwencyjne modele na podstawie błędów'
    ]
}

quiz_data = pd.DataFrame(data)

# Function to check the answers and display results
def check_answers(responses):
    correct_count = sum(1 for i, row in enumerate(quiz_data.iterrows()) if responses[i] == row[1]['Correct Answer'])
    total_questions = len(quiz_data)
    correct_percentage = (correct_count / total_questions) * 100

    # Create a pie chart for the results
    labels = 'Poprawne odpowiedzi', 'Błędne odpowiedzi'
    sizes = [correct_percentage, 100 - correct_percentage]
    colors = ['green', 'red']
    explode = (0.1, 0)  # explode 1st slice

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)
    ax.axis('equal')  # Ensure that pie is drawn as a circle.

    st.pyplot(fig)

    # Display balloons if score is 50% or more
    if correct_percentage >= 50:
        st.balloons()

# Create the quiz form
with st.form(key='my_form'):
    responses = []
    st.write("# Quiz z podstaw uczenia maszynowego")
    st.write("Odpowiedz na wszystkie pytania, a następnie prześlij swoje odpowiedzi, aby zobaczyć wynik i uczcić swój sukces!")
    
    for index, row in quiz_data.iterrows():
        response = st.radio(f"Pytanie {index + 1}: {row['Question']}", row['Options'], key=f'resp_{index}')
        responses.append(response)
    
    submitted = st.form_submit_button("Sprawdź odpowiedzi")
    if submitted:
        check_answers(responses)

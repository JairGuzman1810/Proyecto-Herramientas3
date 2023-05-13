import streamlit as st

# Crear los campos de entrada

opp_dict = {'Arsenal': 0, 'Aston Villa': 1, 'Brentford': 2, 'Brighton': 3, 'Burnley': 4,
            'Chelsea': 5, 'Crystal Palace': 6, 'Everton': 7, 'Fulham': 8, 'Leeds United': 9,
            'Leicester City': 10, 'Liverpool': 11, 'Manchester City': 12, 'Manchester Utd': 13,
            'Newcastle Utd': 14, 'Norwich City': 15, 'Sheffield Utd': 16, 'Southampton': 17,
            'Tottenham': 18, 'Watford': 19, 'West Brom': 20, 'West Ham': 21, 'Wolves': 22}
day_code_dict = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5, "Domingo": 6}

days_options = list(day_code_dict.keys())
opp_options = list(opp_dict.keys())

def v1():
    st.title("Football Prediction Model")

    # Match information
    st.header("Match Information")
    st.subheader("Match Details")

    col1, col2 = st.columns(2)

    with col1:
        venue_code = st.radio("Venue", options=["Home", "Away"])
        opp_code = st.selectbox('Opponent', options=opp_options)

    with col2:
        hour = st.slider("Hour", 12, 20, 12)
        day_code = st.selectbox("Day", list(day_code_dict.keys()))

    container = st.container()
    container.text_align = 'center'
    with container:
        if st.button("Enviar"):
            # Recopilar los valores de cada campo
            day_code = day_code_dict[day_code]
            venue_code = 1 if venue_code == 'Away' else 0
            opp_code = opp_dict[opp_code]
            st.write("Los valores ingresados son:")
            st.write(f"venue_code: {venue_code}")
            st.write(f"opp_code: {opp_code}")
            st.write(f"hour: {hour}")
            st.write(f"day_code: {day_code}")

def v2():
    st.title("Football Prediction Model")

    # Match information
    st.header("Match Information")
    st.subheader("Match Details")

    col1, col2 = st.columns(2)

    with col1:
        venue_code = st.radio("Venue", options=["Home", "Away"])
        opp_code = st.selectbox('Opponent', options=opp_options)

    with col2:
        hour = st.slider("Hour", 12, 20, 12)
        day_code = st.selectbox("Day", list(day_code_dict.keys()))

    # Team statistics
    st.header("Team Statistics")
    st.subheader("Rolling averages")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gf_rolling = st.number_input("GF", min_value=0.0, step=0.1)
        ga_rolling = st.number_input("GA", min_value=0.0, step=0.1)
    with col2:
        sh_rolling = st.number_input("Shots", min_value=0.0, step=0.1)
        sot_rolling = st.number_input("Shots on Target", min_value=0.0, step=0.1)
    with col3:
        dist_rolling = st.number_input("Distance", min_value=0.0, step=0.1)
        fk_rolling = st.number_input("Free Kicks", min_value=0.0, step=0.1)
    with col4:
        pk_rolling = st.number_input("Penalties Kicks", min_value=0.0, step=0.1)
        pkatt_rolling = st.number_input("Penalties Attempted", min_value=0.0, step=0.1)

    # Crear un botón para enviar los valores


    if st.button("Enviar"):
        # Recopilar los valores de cada campo
        # Hacer algo con los valores, por ejemplo, imprimirlos en pantalla
        day_code = day_code_dict[day_code]
        venue_code = 1 if venue_code == 'Away' else 0
        opp_code = opp_dict[opp_code]

        st.write("Los valores ingresados son:")
        st.write(f"venue_code: {venue_code}")
        st.write(f"opp_code: {opp_code}")
        st.write(f"hour: {hour}")
        st.write(f"day_code: {day_code}")
        st.write(f"gf_rolling: {gf_rolling}")
        st.write(f"ga_rolling: {ga_rolling}")
        st.write(f"sh_rolling: {sh_rolling}")
        st.write(f"sot_rolling: {sot_rolling}")
        st.write(f"dist_rolling: {dist_rolling}")
        st.write(f"fk_rolling: {fk_rolling}")
        st.write(f"pk_rolling: {pk_rolling}")
        st.write(f"pkatt_rolling: {pkatt_rolling}")

# Crear una lista de opciones
options = ["v1", "v2",]

# Crear un sidebar con la lista de opciones
selection = st.sidebar.selectbox("Selecciona un modelo", options, index=0)

# Llamar a diferentes funciones según la opción seleccionada
if selection == "v1":
    v1()
else:
    v2()

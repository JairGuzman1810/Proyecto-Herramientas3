import streamlit as st
import pandas as pd
import model as prediction

# Crear los campos de entrada

teams_dict = {'Arsenal': 0, 'Aston Villa': 1, 'Brentford': 2, 'Brighton': 3, 'Burnley': 4,
              'Chelsea': 5, 'Crystal Palace': 6, 'Everton': 7, 'Fulham': 8, 'Leeds United': 9,
              'Leicester City': 10, 'Liverpool': 11, 'Manchester City': 12, 'Manchester Utd': 13,
              'Newcastle Utd': 14, 'Norwich City': 15, 'Sheffield Utd': 16, 'Southampton': 17,
              'Tottenham': 18, 'Watford': 19, 'West Brom': 20, 'West Ham': 21, 'Wolves': 22}
day_code_dict = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5, "Domingo": 6}

days_options = list(day_code_dict.keys())
opp_options = list(teams_dict.keys())


def v1():
    st.title("Modelo de Predicción de Fútbol")

    # Información del partido
    st.header("Información del Partido")
    st.subheader("Detalles del Partido")

    team = st.selectbox('Elige un equipo', options=opp_options)

    col1v1, col2v1 = st.columns(2)

    with col1v1:
        venue_code = st.radio("Localidad", options=["Local", "Visitante"])
        opp_code = st.selectbox('Rival', options=opp_options)

    with col2v1:
        hour = st.slider("Hora", 12, 22, 12)
        day_code = st.selectbox("Día", list(day_code_dict.keys()))

    if st.button("Enviar"):
        # Recopilar los valores de cada campo
        if team == opp_code:
            st.error("El equipo elegido y el rival no pueden ser el mismo. Por favor, selecciona equipos diferentes.")
            return
        day_code = day_code_dict[day_code]
        venue_code = 0 if venue_code == 'Visitante' else 1
        opp_code = teams_dict[opp_code]

        data = pd.DataFrame({
            "venue_code": [venue_code],
            "opp_code": [opp_code],
            "hour": [hour],
            "day_code": [day_code],
        })

        if prediction.make_predictionsv1(data)[0]:
            st.success(f"¡{team} ganó!")
        else:
            st.error(f"¡{team} perdió! :(")



def v2():
    st.title("Modelo de Predicción de Fútbol")

    # Información del partido
    st.header("Información del Partido")
    st.subheader("Detalles del Partido")

    team = st.selectbox('Elige un equipo', options=opp_options)

    col1v2, col2v2 = st.columns(2)

    with col1v2:
        venue_code = st.radio("Localidad", options=["Local", "Visitante"])
        opp_code = st.selectbox('Rival', options=opp_options)

    with col2v2:
        hour = st.slider("Hora", 12, 22, 12)
        day_code = st.selectbox("Día", list(day_code_dict.keys()))

    # Estadísticas del equipo
    st.header("Estadísticas del Equipo")
    st.subheader("Promedios móviles")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gf_rolling = st.number_input("GF (Goles a favor)", min_value=0.0, step=0.1)
        ga_rolling = st.number_input("GA (Goles en contra)", min_value=0.0, step=0.1)
    with col2:
        sh_rolling = st.number_input("Tiros", min_value=0.0, step=0.1)
        sot_rolling = st.number_input("Tiros al Arco", min_value=0.0, step=0.1)
    with col3:
        dist_rolling = st.number_input("Distancia", min_value=0.0, step=0.1)
        fk_rolling = st.number_input("Tiros Libres", min_value=0.0, step=0.1)
    with col4:
        pk_rolling = st.number_input("Penales", min_value=0.0, step=0.1)
        pkatt_rolling = st.number_input("Penales Intentados", min_value=0.0, step=0.1)

    # Crear un botón para enviar los valores

    if st.button("Enviar"):
        if team == opp_code:
            st.error("El equipo elegido y el rival no pueden ser el mismo. Por favor, selecciona equipos diferentes.")
            return
        # Recopilar los valores de cada campo
        # Hacer algo con los valores, por ejemplo, imprimirlos en pantalla
        day_code = day_code_dict[day_code]
        venue_code = 0 if venue_code == 'Visitante' else 1
        opp_code = teams_dict[opp_code]

        data = pd.DataFrame({
            "venue_code": [venue_code],
            "opp_code": [opp_code],
            "hour": [hour],
            "day_code": [day_code],
            "gf_rolling": [gf_rolling],
            "ga_rolling": [ga_rolling],
            "sh_rolling": [sh_rolling],
            "sot_rolling": [sot_rolling],
            "dist_rolling": [dist_rolling],
            "fk_rolling": [fk_rolling],
            "pk_rolling": [pk_rolling],
            "pkatt_rolling": [pkatt_rolling],
        })

        data = data.astype({'gf_rolling': 'float64',
                            'ga_rolling': 'float64',
                            'sh_rolling': 'float64',
                            'sot_rolling': 'float64',
                            'dist_rolling': 'float64',
                            'fk_rolling': 'float64',
                            'pk_rolling': 'float64',
                            'pkatt_rolling': 'float64'})

        if prediction.make_predictionsv2(data)[0] == 1:
            st.success(f"{team} ganó!")
        else:
            st.error(f"{team} perdió :(")


# Crear una lista de opciones
options = ["v1", "v2"]

# Crear un sidebar con la lista de opciones
selection = st.sidebar.selectbox("Selecciona un modelo", options, index=0)

# Llamar a diferentes funciones según la opción seleccionada
if selection == "v1":
    v1()
else:
    v2()

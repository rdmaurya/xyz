import streamlit as st

# Constants
r = 8.314  # Ideal gas constant in J/(mol*K)


def ideal_gas_pressure(n, v, t):
    """
    Calculate the pressure of an ideal gas using the ideal gas law.

    :param n: Number of moles of the gas (in mol)
    :param v: Volume of the gas (in m^3)
    :param t: Temperature of the gas (in K)
    :return: Pressure of the gas (in Pa)
    """
    return (n * r * t) / v


def real_gas_pressure(n, v, t, a, b):
    """
    Calculate the pressure of a real gas using the Van der Waals equation.

    :param n: Number of moles of the gas (in mol)
    :param v: Volume of the gas (in m^3)
    :param t: Temperature of the gas (in K)
    :param a: Van der Waals constant 'a' (in Pa * m^6 / mol^2)
    :param b: Van der Waals constant 'b' (in m^3 / mol)
    :return: Pressure of the gas (in Pa)
    """
    return ((n * r * t) / (v - n * b)) - (a * n ** 2 / a ** 2)


def main():
    st.title("Gas Pressure Calculator")

    st.sidebar.header("Parameters")
    n = st.sidebar.number_input("Number of moles (n)", value=1.0)
    V = st.sidebar.number_input("Volume (v) in m^3", value=0.0224)
    T = st.sidebar.number_input("Temperature (t) in K", value=273.15)
    a = st.sidebar.number_input("Van der Waals constant 'a' (in Pa * m^6 / mol^2)", value=0.367)
    b = st.sidebar.number_input("Van der Waals constant 'b' (in m^3 / mol)", value=0.0427)

    ideal_pressure = ideal_gas_pressure(n, V, T)
    real_pressure = real_gas_pressure(n, V, T, a, b)

    st.write("### Results")
    st.write(f"Ideal Gas Pressure: {ideal_pressure} Pa")
    st.write(f"Real Gas Pressure: {real_pressure} Pa")


if __name__ == "__main__":
    main()

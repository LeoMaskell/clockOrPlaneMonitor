import streamlit as st
import pandas as pd
import main

# the plan:
# 1: make the 2 needed inputs and then the iterable outputs
# 2: make a page about what the squawks mean
# 3: map with all planes on??

st.title("plane-yo")

DISTANCE = st.slider("distance radius", 0, 100, 1)

postcode = st.text_input(
    label="postcode",
    value="TW6 1EW",
    placeholder="TW6 1EW",
    help="Please enter a valid postcode",
)


try:
    coords = main.postcodeToLattLong(postcode)
    planeLS = main.in_radius(main.planes["states"], coords, DISTANCE)
    if planeLS == []:
        output = "no planes"
    elif len(planeLS) == 1:
        output = "is 1 plane"
    else:
        output = f"are {len(planeLS)} planes"

    st.write(f":orange[There {output} in the vicinity]")

    df = pd.DataFrame(
        {
            "plane no.:",
            "callsign:",
            "altitude:",
            "velocity:",
            "latt:",
            "long:",
            "squawk:",
        }
    )

    i = 0
    for plane in planeLS:
        i += 1
        df.insert(
            i,
            str(i),
            [
                i,
                plane["callsign"],
                plane["alt"],
                plane["velocity"],
                plane["latt"],
                plane["long"],
                plane["squawk"],
            ],
        )

    st.table(df, hide_index=True)
except TypeError:
    st.write("enter a valid poscode.")

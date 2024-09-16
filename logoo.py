import streamlit as st
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Title and description
st.title("Advanced Perplexity Analysis for DNA Sequences")
st.write("""
This tool provides different types of perplexity analysis for DNA sequences, including:
- Conditional Perplexity
- Evolutionary Perplexity
- Structural Perplexity
- Functional Perplexity
- Multiscale Perplexity
- Markov-Based Perplexity
- Weighted Perplexity
- Stochastic Perplexity
""")

# Sidebar for sequence input and analysis options
st.sidebar.header("Input Sequences")
sequence_input = st.sidebar.text_area("Enter sequences (one per line)", value="ACGT\nACGA\nACGT\nACTT\nACGG\nACGA")

sequences = sequence_input.splitlines()

# Perplexity types selection
perplexity_type = st.sidebar.selectbox(
    "Select the type of perplexity analysis:",
    [
        "Conditional Perplexity",
        "Evolutionary Perplexity",
        "Structural Perplexity",
        "Functional Perplexity",
        "Multiscale Perplexity",
        "Markov-Based Perplexity",
        "Weighted Perplexity",
        "Stochastic Perplexity"
    ]
)

# Helper function to calculate simple perplexity for DNA sequences
def calculate_perplexity(sequences):
    sequence_length = len(sequences[0])
    freqs = {pos: Counter([seq[pos] for seq in sequences]) for pos in range(sequence_length)}
    freq_matrix = pd.DataFrame(freqs).T
    # Calculate entropy per position
    entropy = -freq_matrix.applymap(lambda p: p * np.log2(p) if p > 0 else 0).sum(axis=1)
    perplexity = 2 ** entropy
    return perplexity

# Generate perplexity values based on the selected type
if perplexity_type == "Conditional Perplexity":
    st.subheader("Conditional Perplexity")
    st.write("Calculating context-dependent variability.")
    perplexity_values = calculate_perplexity(sequences)

elif perplexity_type == "Evolutionary Perplexity":
    st.subheader("Evolutionary Perplexity")
    st.write("Analyzing sequence dynamics over time.")
    perplexity_values = calculate_perplexity(sequences) # Simulate evolutionary drift using aligned sequences

elif perplexity_type == "Structural Perplexity":
    st.subheader("Structural Perplexity")
    st.write("Considering 3D structure-dependent complexity.")
    perplexity_values = calculate_perplexity(sequences) # Future work: integrate 3D structure data

elif perplexity_type == "Functional Perplexity":
    st.subheader("Functional Perplexity")
    st.write("Correlating with functional outcomes.")
    perplexity_values = calculate_perplexity(sequences) # Functional sites weight perplexity

elif perplexity_type == "Multiscale Perplexity":
    st.subheader("Multiscale Perplexity")
    st.write("Analyzing complexity at different sequence scales.")
    perplexity_values = calculate_perplexity(sequences) # Scale over different sequence lengths

elif perplexity_type == "Markov-Based Perplexity":
    st.subheader("Markov-Based Perplexity")
    st.write("Analyzing higher-order nucleotide dependencies.")
    perplexity_values = calculate_perplexity(sequences) # Implement Markov Chain dependency

elif perplexity_type == "Weighted Perplexity":
    st.subheader("Weighted Perplexity")
    st.write("Prioritizing functionally significant positions.")
    perplexity_values = calculate_perplexity(sequences) # Weighted by significance

elif perplexity_type == "Stochastic Perplexity":
    st.subheader("Stochastic Perplexity")
    st.write("Modeling variability due to genetic drift or mutations.")
    perplexity_values = calculate_perplexity(sequences) # Stochastic processes simulation

# Visualize perplexity
st.subheader(f"Perplexity Values for {perplexity_type}")
if len(sequences) > 0:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(perplexity_values, marker='o')
    ax.set_xlabel("Position")
    ax.set_ylabel("Perplexity")
    st.pyplot(fig)

else:
    st.write("Please enter valid sequences.")

# Option to download the perplexity values as a CSV file
st.sidebar.subheader("Download Perplexity Values")
if st.sidebar.button('Download as CSV'):
    perplexity_df = pd.DataFrame({'Position': range(1, len(perplexity_values) + 1), 'Perplexity': perplexity_values})
    csv = perplexity_df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
        label="Download Perplexity CSV",
        data=csv,
        file_name="perplexity_values.csv",
        mime="text/csv"
    )

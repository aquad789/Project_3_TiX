import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st



load_dotenv("./penn.env")

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Load_Contract Function
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./tixregistry_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract


# Load the contract
contract = load_contract()


st.title("Token Marketplace")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

################################################################################


concerts = ["Bruno Mars", "Fleetwood Mac"]

st.selectbox("### Select Concert", options = concerts)

st.markdown("### Select # of Tickets to Buy")

value = st.number_input("Tokens", value=1, step=1)
# artwork_name = "Test 2"
# artist_name = "Test 2"
# initial_appraisal_value = "100"
artwork_uri = "QmY3TRdBzrvncDFDUcbs3fZXQbXfeQa8CCjCkUPWq1YgQw"
if st.button("Buy Tickets"):
    tx_hash = contract.functions.buy_TIXNFT(
        address,
        # artwork_name,
        # artist_name,
        # int(initial_appraisal_value),
        artwork_uri).transact({
      'from': address, 
      'to': '0x43f06da497Ee05b48192d41E9cC1C2CfE3Be15b8',
      'value':value*1000000000000000000, 
      'gas': 1000000
    })
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    st.write("You can view your ticket(s) & QR Code with the following link")
    st.markdown(f"[ IPFS Ticket QR Code Link](https://gateway.pinata.cloud/ipfs/{artwork_uri})")
st.markdown("---")




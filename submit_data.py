from algosdk.v2client.algod import AlgodClient
from algosdk.atomic_transaction_composer import AccountTransactionSigner, AtomicTransactionComposer
from algokit_utils import ApplicationClient
from algosdk.account import address_from_private_key
# from algosdk.encoding import encode_address
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

algod_token = ''
algod_address = 'https://testnet-api.4160.nodely.dev'
algod_client = AlgodClient(algod_token, algod_address)

app_spec = Path(__file__).parent / 'DataMaxi.arc32.json'

private_key = os.getenv('pk')
signer = AccountTransactionSigner(private_key)

address = address_from_private_key(private_key)

params = algod_client.suggested_params()

app_id = int(os.getenv('app_id'))

app_client = ApplicationClient(
    app_id=app_id,
    algod_client=algod_client,
    app_spec=app_spec,
    signer=signer,
    sender=address,
    suggested_params=params,
)

atc = AtomicTransactionComposer()

#Simulate having 3,584 bytes to store
app_args_data = os.urandom(2042)
note_field_data = os.urandom(1024)

box_refs_data = os.urandom(512)
box_references = [[app_id, box_refs_data[i:i+64]] for i in range(0, len(box_refs_data), 64)]


'''
We previously only had 3,226 bytes of space when using max foreign accounts and remaining references with foreign assets
An additional 358 bytes can be found when using arbitrary box references instead as we do above
'''
#foreign_accounts_data = os.urandom(128)
#foreign_assets_data = os.urandom(64)

#foreign_accounts = [encode_address(foreign_accounts_data[i:i+32]) for i in range(0, len(foreign_accounts_data), 32)]
#foreign_assets = [int.from_bytes(foreign_assets_data[i:i+8], 'big') for i in range(0, len(foreign_assets_data), 8)]


app_client.compose_call(
    atc,
    call_abi_method='passData',
    data=app_args_data,
    transaction_parameters={
        'note': note_field_data,
        'boxes': box_references,
      #  'accounts': foreign_accounts,
      #  'foreign_assets': foreign_assets,
    }
)

results = atc.execute(algod_client, 2)
print(results.tx_ids[0])

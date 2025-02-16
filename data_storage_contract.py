from algopy import ARC4Contract, Bytes, Txn, Global
from algopy.arc4 import abimethod

class DataMaxi(ARC4Contract):
    def __init__(self) -> None:
        pass

    @abimethod
    def passData(self, data: Bytes) -> None:
        assert Txn.sender == Global.creator_address


    @abimethod(allow_actions=['UpdateApplication', 'DeleteApplication'])
    def update_or_delete(self) -> None:
        pass

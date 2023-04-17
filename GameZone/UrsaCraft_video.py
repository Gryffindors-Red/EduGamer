from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from web3 import Web3
import string
import random
import json

# Log settings...
Steps_log = []

# Level Settings
LevelName = 'Project_x'
AutoId = 0

# Input Settings
input_type = int(input("Enter the Type [New(1)/Load(2)] : "))

# Web3 Setups

w3 = Web3(Web3.HTTPProvider(
    'https://polygon-mumbai.g.alchemy.com/v2/K59YdNGK95akCLJrA1m9nYPZ7JYNa8Me'))
my_address = '0x042bDdB896fa2B4F5993e3926b7dD53B27f9321E'
private_key = '0x6021d22205954e378994c07b70dae0afd8e67b5eb61c8f799ebfd24f5f010708'
contract_address = '0x965E36d74f804c57959a2Aa2CD5897dc14BBD0F3'
contract_abi = json.loads('[ { "inputs": [ { "internalType": "string", "name": "_levelName", "type": "string" }, { "internalType": "uint256", "name": "_id", "type": "uint256" } ], "name": "deleteGameLevel", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_levelName", "type": "string" }, { "internalType": "uint256", "name": "_id", "type": "uint256" }, { "internalType": "uint256", "name": "_x", "type": "uint256" }, { "internalType": "uint256", "name": "_y", "type": "uint256" }, { "internalType": "uint256", "name": "_z", "type": "uint256" }, { "internalType": "string", "name": "_texture", "type": "string" }, { "internalType": "string", "name": "_tagName", "type": "string" } ], "name": "storeGameLevel", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_levelName", "type": "string" } ], "name": "retrieveAllGameLevels", "outputs": [ { "internalType": "uint256[]", "name": "", "type": "uint256[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_levelName", "type": "string" }, { "internalType": "uint256", "name": "_id", "type": "uint256" } ], "name": "retrieveGameLevel", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" } ]')
simple_storage = w3.eth.contract(address=contract_address, abi=contract_abi)


def update_value(level, id_, x, y, z, texture, tagName):
    global AutoId
    nonce = w3.eth.getTransactionCount(my_address)
    greeting_transaction = simple_storage.functions.storeGameLevel(
        level, id_, x, y, z, texture, tagName
    ).buildTransaction(
        {
            "chainId": w3.eth.chainId,
            "gasPrice": w3.eth.gas_price,
            "from": my_address,
            "nonce": nonce,  # the initial nonce should "orginal nonce value" after that you should be increase nonce
        }
    )
    print("transaction Success..")

    # sign the transaction with the private key
    signed_txn = w3.eth.account.sign_transaction(
        greeting_transaction, private_key=private_key)

    # send the signed transaction to the network
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # get the transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(tx_receipt.get('transactionHash'))
    AutoId = AutoId+1

    # print the transaction hash and the new storage value
    print(f'Transaction hash: {tx_receipt.transactionHash.hex()}')
    print(tx_hash)


def UniqueCode():
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(characters) for i in range(10))
    return code


def update_steps(Position, Texture, Tag, id):
    global Steps_log
    Steps_logs = {}
    Steps_logs['position'] = list(Position)
    Steps_logs['texture'] = str(Texture)
    Steps_logs['tag'] = Tag
    Steps_logs['id'] = id
    Steps_log.append(Steps_logs)


app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound', loop=False, autoplay=False)
block_pick = 1

window.fps_counter.enabled = False
window.exit_button.visible = False


def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']:
        block_pick = 1
    if held_keys['2']:
        block_pick = 2
    if held_keys['3']:
        block_pick = 3
    if held_keys['4']:
        block_pick = 4

    if held_keys['control'] and held_keys['s']:
        with open(LevelName+'.json', 'w') as f:
            f.write('''"'''.join(str(Steps_log).split("'")))
        f.close()


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture, tag=UniqueCode(), id_=0):
        super().__init__(
            id=id_,
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            tag=tag,
            scale=0.5)
        self.id_ = id_

    def input(self, key,):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1:
                    voxel = Voxel(position=self.position +
                                  mouse.normal, texture=grass_texture)
                    update_steps(self.position + mouse.normal,
                                 grass_texture, UniqueCode(), self.id_)

                if block_pick == 2:
                    uni = UniqueCode()
                    voxel = Voxel(position=self.position +
                                  mouse.normal, texture=stone_texture)
                    update_steps(self.position + mouse.normal,
                                 stone_texture, uni, self.id_)
                    update_value(LevelName, 1, int(self.position.x + mouse.normal.x), int(self.position.y +
                                 mouse.normal.y), int(self.position.z + mouse.normal.z), str(stone_texture), uni)
                if block_pick == 3:
                    voxel = Voxel(position=self.position +
                                  mouse.normal, texture=brick_texture)
                    update_steps(self.position + mouse.normal,
                                 brick_texture, UniqueCode(), self.id_)
                if block_pick == 4:
                    voxel = Voxel(position=self.position +
                                  mouse.normal, texture=dirt_texture)
                    update_steps(self.position + mouse.normal,
                                 dirt_texture, UniqueCode(), self.id_)

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True)


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6))

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


if input_type == 1:
    for z in range(20):
        for x in range(20):
            voxel = Voxel(position=(x, 0, z))
            Steps_logs = {}
            update_steps((x, 0, z), grass_texture, UniqueCode(), AutoId)
            print(voxel.tag, voxel.id)
elif input_type == 2:
    with open('Project_x.json', 'r') as f:
        json_data = json.load(f)
    f.close()
    print(json_data[0])
    for i in json_data:
        voxel = Voxel(position=i['position'],
                      texture=i.get('texture'), tag=i.get('tag'), id_=i.get('id'))
        update_steps(Position=i['position'],
                     Texture=i.get('texture'), Tag=i.get('tag'), id=i.get('id'))


player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()

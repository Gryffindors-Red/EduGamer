from ..models import Blog
from django.shortcuts import render
from .Tool.Tools import get_blog
from EduZone.settings import my_address, private_key
from web3 import Web3, HTTPProvider
import json
from django.core.serializers import serialize
from django.http import JsonResponse


w3 = Web3(Web3.HTTPProvider(
    'https://polygon-mumbai.g.alchemy.com/v2/K59YdNGK95akCLJrA1m9nYPZ7JYNa8Me'))


# ...............Blog........................................
def blog_edit(request):
    return render(request, "BlogBuilder/blog_edit.html")


def save_blog(request):
    ids = ['#title', '#description', '#content', '#Category', '#Thumbnail']
    title = request.POST.get(ids[0])
    description = request.POST.get(ids[1])
    content = request.POST.get(ids[2])
    Category = request.POST.get(ids[3])
    Thumbnail = request.POST.get(ids[4])

    # set the contract address and ABI
    contract_address = '0x6C9e539874f9aD5C4D277cEc5D8DF76349a5028B'
    contract_abi = json.loads('[ { "inputs": [ { "internalType": "string", "name": "title", "type": "string" }, { "internalType": "string", "name": "description", "type": "string" }, { "internalType": "string", "name": "content", "type": "string" }, { "internalType": "string", "name": "blog_profile_img", "type": "string" }, { "internalType": "string", "name": "categories", "type": "string" } ], "name": "createBlogPost", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "blogPosts", "outputs": [ { "internalType": "uint256", "name": "id", "type": "uint256" }, { "internalType": "string", "name": "title", "type": "string" }, { "internalType": "string", "name": "description", "type": "string" }, { "internalType": "string", "name": "content", "type": "string" }, { "internalType": "string", "name": "blog_profile_img", "type": "string" }, { "internalType": "string", "name": "categories", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "id", "type": "uint256" } ], "name": "getBlogPost", "outputs": [ { "internalType": "string", "name": "", "type": "string" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "postCount", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" } ]')

    # create an instance of the contract
    simple_storage = w3.eth.contract(
        address=contract_address, abi=contract_abi)
    nonce = w3.eth.getTransactionCount(my_address)

    print("transaction sucess..")

    greeting_transaction = simple_storage.functions.createBlogPost(
        str(title), str(description), str(
            content), str(Thumbnail), str(Category)
    ).buildTransaction(
        {
            "chainId": w3.eth.chainId,
            'gas': 700000,
            'gasPrice': w3.eth.gas_price,
            "from": my_address,
            # the initial nonce should "orginal nonce value" after that you should be increase nonce
            "nonce": nonce,
        }
    )

    # Wait for the transaction to be mined
    signed_txn = w3.eth.account.sign_transaction(
        greeting_transaction, private_key=private_key)

    # send the signed transaction to the network
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # get the transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_receipt.get('transactionHash'))
    if tx_receipt.blockNumber:
        print("Transaction hash code : ", tx_receipt,
              'Block number : ', tx_receipt.blockNumber)

        obj = Blog(title=title, description=description, content=content,
                   categories=Category, blog_profile_img=Thumbnail, Block_chin_blockNo=tx_receipt.blockNumber, trans_detial=tx_receipt)
        obj.save()

    return JsonResponse({"result": (json.loads(serialize('json', ["page"])))[0]})


def save_edit_blog(request, pk):
    ids = ['#title', '#description', '#content', '#Category', '#Thumbnail']
    title = request.POST.get(ids[0])
    description = request.POST.get(ids[1])
    content = request.POST.get(ids[2])
    Category = request.POST.get(ids[3])
    Thumbnail = request.POST.get(ids[4])

    obj = Blog.objects.get(id=pk)
    obj.content = content
    obj.title = title
    obj.description = description
    obj.categories = Category
    obj.blog_profile_img = Thumbnail
    obj.save()

    print("Saved...........")

    return render(request, "BlogBuilder/blog_edit.html")


def list_blog(request):
    items = get_blog()
    return render(request, "BlogBuilder/Blog.html", {'blogs': items})


def view_blog(request, pk):
    page = Blog.objects.get(id=pk)
    items = get_blog()
    return render(request, "BlogBuilder/view_Blog.html", {'blog': page, 'item': items})


def delete_blog(request):
    bl_id = request.GET.get("id")
    page = Blog.objects.get(id=bl_id)
    page.delete()
    return render(request, "BlogBuilder/view_Blog.html", {'blog': page})


def list_edit_blog(request):
    items = get_blog()
    return render(request, "BlogBuilder/edit_blog_list.html", {'blogs': items})


def edit_blog(request, pk):
    obj = Blog.objects.get(id=pk)
    return render(request, "BlogBuilder/blog_re_edit.html", {'obj': obj})

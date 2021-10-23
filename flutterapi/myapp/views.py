from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

# GET Data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all()  #ดึงข้อมูลจาก moodel Todolist 
    serializer = TodolistSerializer(alltodolist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# POST Data (Save Data to Database)
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def update_todolist(request,TID):
    # localhost:8000/api/update-todolist/13
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=statuscode)





#data = [{'message':'Hello World'},{'message':'Hello Mon'}]
data = [
    {
        "title":"คอมพิวเตอร์ คือ อะไร ?",
        "subtitle":"คอมพิวเตอร์ คือ อุปกรณ์ที่ใช้สำหรับการคำนวณและทำงานอื่นๆ",
        "image_url":"https://raw.githubusercontent.com/NarumonK/BasicAPI/main/macbook.jpg",
        "detail":"คอมพิวเตอร์ คือ อุปกรณ์ทางอิเล็กทรอนิกส์ (electrinic device) ที่มนุษย์ใช้เป็นเครื่องมือช่วยในการจัดการกับข้อมูลที่อาจเป็นได้ ทั้งตัวเลข ตัวอักษร หรือสัญลักษณ์ที่ใช้แทนความหมายในสิ่งต่าง ๆ โดยคุณสมบัติที่สำคัญของคอมพิวเตอร์คือการที่สามารถกำหนดชุดคำสั่งล่วงหน้าหรือโปรแกรมได้ (programmable) นั่นคือคอมพิวเตอร์สามารถทำงานได้หลากหลายรูปแบบ ขึ้นอยู่กับชุดคำสั่งที่เลือกมาใช้งาน ทำให้สามารถนำคอมพิวเตอร์ไปประยุกต์ใช้งานได้อย่างกว้างขวาง เช่น ใช้ในการตรวจคลื่นความถี่ของหัวใจ การฝาก - ถอนเงินในธนาคาร การตรวจสอบสภาพเครื่องยนต์ เป็นต้น ข้อดีของคอมพิวเตอร์ คือ เครื่องคอมพิวเตอร์สามารถทำงานได้อย่างมีประสิทธภาพ มีความถูกต้อง และมีความรวดเร็ว"
    },
    {
        "title":"มาเขียนโปรแกรมกันเถอะ !!",
        "subtitle":"บทความนี้จะแนะนำการเริ่มต้นการเขียนโปรแกรม",
        "image_url":"https://raw.githubusercontent.com/NarumonK/BasicAPI/main/laptop.jpg",
        "detail":"การเขียนโปรแกรมคอมพิวเตอร์ (อังกฤษ: Computer programming) หรือเรียกให้สั้นลงว่า การเขียนโปรแกรม (อังกฤษ: Programming) หรือ การเขียนโค้ด (Coding) เป็นขั้นตอนการเขียน ทดสอบ และดูแลซอร์สโค้ดของโปรแกรมคอมพิวเตอร์ ซึ่งซอร์สโค้ดนั้นจะเขียนด้วยภาษาโปรแกรม ขั้นตอนการเขียนโปรแกรมต้องการความรู้ในหลายด้านด้วยกัน เกี่ยวกับโปรแกรมที่ต้องการจะเขียน และขั้นตอนวิธีที่จะใช้ ซึ่งในวิศวกรรมซอฟต์แวร์นั้น การเขียนโปรแกรมถือเป็นเพียงขั้นหนึ่งในวงจรชีวิตของการพัฒนาซอฟต์แวร์"
    },
    {
        "title":"Flutter คือ ?",
        "subtitle":"Tools สำหรับออกแบบ UI ",
        "image_url":"https://raw.githubusercontent.com/NarumonK/BasicAPI/main/user-interface.png",
        "detail":""
    }
    
]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii': False})
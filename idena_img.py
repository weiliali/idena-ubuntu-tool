import pro_base
import idena_base
print("现在时间是",pro_base.today_time())
print("选择您的操作")
print("1.创建镜像服务器")
print("2.创建镜像")
i=int(input())
if i==1:
    idena_base.img_vps()
elif i==2:
    idena_base.img_build()

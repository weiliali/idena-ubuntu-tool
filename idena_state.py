import  idena_base
print("有效账户数", [idena_base.ture_address() - 1])
m = 2
idena_base.idena_stats(str(m))
while m < idena_base.ture_address():
    m += 1
    idena_base.idena_stats(str(m))
print("完成")

import json
import time
today_time=(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("现在是",today_time)
today_day=(time.strftime("%Y-%m-%d", time.localtime()))

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models
def test(example.txt):
    filename = 'example.txt'  # 文件名
    with open(filename, 'r') as f:
    content = f.read()  # 读取文件内容
    var = content  # 将文件内容赋值给变量
secretId=test(secretId)
secretKey=test(secretKey)
#定义函数
def img_name():
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(secretId, secretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cvm.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = cvm_client.CvmClient(cred, "ap-guangzhou", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeImagesRequest()
        params = {
            "Filters": [
                {
                    "Name": "tag-key",
                    "Values": ["idena"]
                }
            ]
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个DescribeImagesResponse的实例，与请求对象对应
        resp = client.DescribeImages(req)
        # 输出json格式的字符串回包
        a = json.loads(resp.to_json_string())
        b = a['ImageSet']
        c = int(len(b) - 1)
        while c >= 0:
            print(b[c]['ImageId'], b[c]['ImageName'])
            c -= 1
        print()
    except TencentCloudSDKException as err:
        print(err)

Password = input("请输入密码，直接按enter默认Re123456789123") or "Re123456789123"
print("-" * 5)
times = int(input("请输入服务器个数"))
print("-" * 5)
print("idena镜像列表")
img_name()
img = input("请输入镜像")
print("-" * 5)
print("自动今晚22：10注销服务器")
print("请牢记密码为", Password)
print("-" * 5)
while times > 0:
    times -= 1
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(secretId, secretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cvm.ap-guangzhou.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = cvm_client.CvmClient(cred, "ap-guangzhou", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.RunInstancesRequest()
        params = {
            "InstanceChargeType": "POSTPAID_BY_HOUR",
            "DisableApiTermination": False,
            "Placement": {
                "Zone": "ap-guangzhou-6",
                "ProjectId": 0
            },
            "VirtualPrivateCloud": {
                "AsVpcGateway": False,
                "VpcId": "vpc-b8ptxop5",
                "SubnetId": "subnet-ahm3l13o",
                "Ipv6AddressCount": 0
            },
            "InstanceType": "S6.MEDIUM8",
            "ImageId": img,
            "SystemDisk": {
                "DiskSize": 50,
                "DiskType": "CLOUD_BSSD"
            },
            "InternetAccessible": {
                "InternetMaxBandwidthOut": 100,
                "PublicIpAssigned": True,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR"
            },
            "LoginSettings": {
                "Password": Password
            },
            "SecurityGroupIds": ["sg-dbcg6j0n"],
            "InstanceCount": 1,
            "EnhancedService": {
                "SecurityService": {
                    "Enabled": False
                },
                "MonitorService": {
                    "Enabled": False
                },
                "AutomationService": {
                    "Enabled": True
                }
            },
            "ActionTimer": {
                "ActionTime": today_day + " 22:10:00",
                "TimerAction": "TerminateInstances",
                "Externals": {
                    "ReleaseAddress": True
                }
            },
            "TagSpecification": [
                {
                    "ResourceType": "instance",
                    "Tags": [
                        {
                            "Key": "idena",
                            "Value": "idena"
                        }
                    ]
                }
            ]
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个RunInstancesResponse的实例，与请求对象对应
        resp = client.RunInstances(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)


echo "
1.新建服务器
2.导出服务器，并下载文档
3.镜像设置
4.上传idena-all，统计数据,并下载
5.上传idena-all，并导入服务器nodekey
 type in your choose:"
 read num
 if [[ "$num" -eq 1 ]]; then
	    python3 idena_fwq.py
     elif [[ "$num" -eq 2 ]]; then
	    python3 idena_ip.py
	    sz FWQ.prma
     elif [[ "$num" -eq 3 ]]; then
	    python3 idena_img.py
     elif [[ "$num" -eq 4 ]]; then   
	    rm -rf idena-all.xlsx
	    rz 
	    python3 idena_state.py
	    sz idena-all.xlsx
     elif [[ "$num" -eq 5 ]]; then
	    rm -rf idena-all.xlsx          
	    rz
	    python3 idena_nodekey.py

 fi


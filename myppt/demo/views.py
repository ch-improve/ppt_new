import os

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from demo.func import PptTool, push_qiniu
from demo.models import Ppt


class Demo(APIView):
    def get(self, request):
        return Response("哈哈哈哈哈")


class Index(APIView):
    def get(self, request):
        res = request.query_params
        id = res.get('id')
        ppts = Ppt.objects.filter(pid=id).order_by('id')
        re = list()
        for ppt in ppts:
            re.append(ppt.png)
        return Response(re)

    def post(self, request):
        res = request.data
        path = res.get('path')
        id = res.get('id')
        t = PptTool(path)
        try:
            basename, dirpath, re_list = t.run()
        except Exception as e:
            return Response({'errno': 'faild'})
        old_ppt_list = Ppt.objects.filter(pid=id)
        print(old_ppt_list)
        print(len(old_ppt_list))
        wrong_count = 0
        right_count = 0
        for jpg in re_list:
            with open(os.path.join(dirpath, jpg), 'rb') as f:
                file = f.read()
            for i in range(5):
                url = push_qiniu(basename+jpg.split('.')[0], file)
                if url:
                    new_ppt = Ppt(pid=id, png=url)
                    new_ppt.save()
                    right_count += 1
                    os.remove(os.path.join(dirpath, jpg))
                    break
            else:
                os.remove(os.path.join(dirpath, jpg))
                wrong_count += 1
        os.rmdir(dirpath)
        print(old_ppt_list)
        print(len(old_ppt_list))
        for old_ppt in old_ppt_list:
            old_ppt.delete()
        return Response({'errno': 'ok', 'right': right_count, 'wrong': wrong_count})



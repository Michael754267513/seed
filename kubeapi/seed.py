#! encoding: utf-8
import gevent.pywsgi
import pysnooper
from  callback import returnRes
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from kubeapi import kubeBase, manager_res, manager_helm, delete_helm_cmd
from db import dbsql
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# kubernetes connection
token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLTR0Y2JoIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIzYWMyYTkwMS0wZmQxLTExZTktOWUxZi0wMDFhNGExNjQ0MGIiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.vKc_3yMlueYyoh-4JiRll4NJO7-WYdzKSJlXwDyA5gwPkw3m-M-3vylsjCgZ_QnL377-X4JDVDSW7-e-8EVsRBWp3qMqiFu__xfVBOLG1Pf84DZHugPNY-8ezX4LpDuSMK5MFG1bUr2Q7wdpflJM0mzzL-GdVNk1JR-Th728wAj28JZ2FNuts4tQK5qicHqgsytMbXXyC5MQtKbxjV0wI91nL3ukYy-dMWtgapToH0PvdiNM_LcuhSozW9OGa5v3xy1cUxiDqnENcA0mwa_w8y8CwdRCnYsRXYXYairSuZkMdxlB8oUotu10P65OjKeiJ13H6EIjuDxUYlobGwerww"
ssl = True
ca_path="./ca.pem"
host = "https://10.148.181.221:8443"

# db connection
# dbhost = '10.148.140.230'
username = 'root'
dbhost = '127.0.0.1'
password = 'michael76!1.aW'


# kubeconn = kubeBase(token=token, ApiHost=host, ssl=ssl, ca_path=ca_path)
# mysqlconn = dbsql(host=dbhost,username=username,password=password)


# 服务初始化
@app.route('/michael/kubernetes/init/svc', methods=["POST","GET"])
def init_svc():

    if request.method == "POST":
        kubeconn = kubeBase(token=token, ApiHost=host, ssl=ssl, ca_path=ca_path)
        mysqlconn = dbsql(host=dbhost, username=username, password=password)
        project_meta = json.loads(request.get_data())
        project = project_meta["project"]
        env = project_meta["env"]
        owner = project_meta["owner"]
        pod_meta = manager_res(project=project, env=env, owner=owner)
        # 创建环境 namespace
        ns_status = kubeconn.create_namespaces(namespaces=env, lables={"owner": str(owner)})
        # 获取project相关service
        ischeck, data = mysqlconn.get_svc(project=project)
        meta = pod_meta.svc_create(meta=data)
        ischeck, e = mysqlconn.create_deployment(meta=meta)
        # 获取helm 命令
        helm_cmd = pod_meta.helm_create_svc(meta=meta)
        # 执行helm命令
        mysqlconn.close()
        checkRes = manager_helm(helm_cmd)
        return jsonify({"code": 0, "message": "成功"})

    if request.method == 'GET':
        return "ok"


# 应用生命周期管理
@app.route('/michael/kubernetes/update/deployment', methods=["POST","GET"])
def update_deployment():
    
    if request.method == "POST":
        kubeconn = kubeBase(token=token, ApiHost=host, ssl=ssl, ca_path=ca_path)
        mysqlconn = dbsql(host=dbhost, username=username, password=password)
        project_meta = json.loads(request.get_data())
        print project_meta
        project = project_meta["project"]
        env = project_meta["env"]
        owner = project_meta["owner"]
        pod_meta = manager_res(project=project, env=env, owner=owner)
        # 创建环境 namespace
        ns_status = kubeconn.create_namespaces(namespaces=env, lables={"owner": str(owner)})
        env_check = []

        # 判断容器更新的类型(新建/更新/删除)
        if project_meta["coreCreates"] != []:
            # 获取数据处理后的元数据
            p_meta = pod_meta.core_create(corecreate=project_meta["coreCreates"])
            # 判断是否更新过(srp不做判断是更新和新建)
            for meta in p_meta:
                ischeck, check = mysqlconn.check_exist(pkg_meta=meta)
                if check:
                    # 插入数据库 ischeck 表示执行是否成功bool值， e 表示抛出的异常
                    ischeck, e = mysqlconn.create_deployment(meta=[meta])
                    print ischeck
                    # 获取helm 命令
                    helm_cmd = pod_meta.helm_create(meta=[meta])
                    # 执行helm命令
                    checkRes = manager_helm(helm_cmd)
                else:
                    ischeck, e = mysqlconn.update_deployment(meta=[meta])
                    # 获取helm 命令
                    helm_cmd = pod_meta.helm_update(meta=[meta])
                    # 执行helm命令
                    checkRes = manager_helm(helm_cmd)
                env_check.append(checkRes)

        if project_meta["uiCreates"] != []:
            # 获取数据处理后的元数据
            p_meta = pod_meta.ui_create(uicreate=project_meta["uiCreates"])
            # 判断是否更新过(srp不做判断是更新和新建)
            for meta in p_meta:
                ischeck, check = mysqlconn.check_exist(pkg_meta=meta)
                if check:
                    # 插入数据库 ischeck 表示执行是否成功bool值， e 表示抛出的异常
                    ischeck, e = mysqlconn.create_deployment(meta=[meta])
                    # 获取helm 命令
                    helm_cmd = pod_meta.helm_create(meta=[meta])
                    # 执行helm命令
                    checkRes = manager_helm(helm_cmd)
                else:
                    # 插入数据库 ischeck 表示执行是否成功bool值， e 表示抛出的异常
                    ischeck, e = mysqlconn.update_deployment(meta=[meta])
                    # 获取helm 命令
                    helm_cmd = pod_meta.helm_update(meta=[meta])
                    # 执行helm命令
                    checkRes = manager_helm(helm_cmd)
                env_check.append(checkRes)

        if project_meta["coreUpdates"] != []:
            # 获取数据处理后的元数据
            meta = pod_meta.core_updates(coreupdate=project_meta["coreUpdates"])
            # 插入数据库 ischeck 表示执行是否成功bool值， e 表示抛出的异常
            ischeck, e = mysqlconn.update_deployment(meta=meta)
            # 获取helm 命令
            helm_cmd = pod_meta.helm_update(meta=meta)
            # 执行helm命令
            checkRes = manager_helm(helm_cmd)
            env_check.append(checkRes)

        if project_meta["uiUpdates"] != []:
            # 获取数据处理后的元数据
            meta = pod_meta.ui_updates(uiupdate=project_meta["uiUpdates"])
            # 插入数据库 ischeck 表示执行是否成功bool值， e 表示抛出的异常
            ischeck, e = mysqlconn.update_deployment(meta=meta)
            # 获取helm 命令
            helm_cmd = pod_meta.helm_update(meta=meta)
            # 执行helm命令
            checkRes = manager_helm(helm_cmd)
            env_check.append(checkRes)

        if project_meta["deletes"] != []:
            # 获取数据处理后的元数据
            meta = pod_meta.pod_delete(pod_delete=project_meta["deletes"])
            # 插入数据库 ischeck 表示执行是否成功bool值， e 表示抛出的异常
            ischeck, e = mysqlconn.delete_deployment(meta=meta)
            # 获取helm 命令
            helm_cmd = pod_meta.helm_delete(meta=meta)
            # 执行helm命令
            checkRes = manager_helm(helm_cmd)
        print(env_check)
        if 0 in env_check:
            returnRes(env, 0)
        else:
            returnRes(env, 1)

        mysqlconn.close()
        return jsonify({"code": 0, "message": "成功"})

    if request.method == "GET":
        kubeconn = kubeBase(token=token, ApiHost=host, ssl=ssl, ca_path=ca_path)
        mysqlconn = dbsql(host=dbhost, username=username, password=password)
        pod = mysqlconn.get_project()
        podlist = kubeconn.get_pod(pod)
        mysqlconn.close()
        return jsonify(podlist)
        #return render_template('deployment.html', pods=podlist)


# 删除环境和资源
@app.route('/michael/kubernetes/delete/ns', methods=["POST","GET"])
def delete_ns():
    if request.method == "POST":
        mysqlconn = dbsql(host=dbhost, username=username, password=password)
        project_meta = json.loads(request.get_data())
        # 获取环境相关的信息,ischeck 表示执行是否成功bool值， e 表示抛出的异常
        ischeck, data = mysqlconn.get_deployment(meta=project_meta)
        # 获取helm 命令
        helm_cmd = delete_helm_cmd(meta=data)
        # 执行helm命令
        checkRes = manager_helm(helm_cmd)
        # 从数据库删除环境相关的信息
        mysqlconn.delete_env(meta=project_meta)
        # 删除nsmamespaces
        # ns_delete = kubeconn.delete_namespaces(namespaces=project_meta["env"])
        mysqlconn.close()
        return jsonify({"code": 0, "message": "成功"})

    if request.method == "GET":
        return "ok"


@app.route('/api/kubernetes/list/ns', methods=["POST","GET"])
def list_ns():
    if request.method == "GET":
        kubeconn = kubeBase(token=token, ApiHost=host, ssl=ssl, ca_path=ca_path)
        ns_meta = kubeconn.list_ns()
        return jsonify(ns_meta)


@app.route('/api/kubernetes/list/pod', methods=["POST","GET"])
def list_pod():
    if request.method == "POST":
        kubeconn = kubeBase(token=token, ApiHost=host, ssl=ssl, ca_path=ca_path)
        ns_meta = json.loads(request.get_data())
        podlist = kubeconn.list_pod(ns_meta['env'])
        return jsonify(podlist)
        #return render_template('deployment.html', pods=podlist)

@app.route('/api/kubernetes/deployment/list', methods=["POST","GET"])
def list_deployment():
    if request.method == "POST":
        meta = json.loads(request.get_data())
        kubeconn = kubeBase(token=token, ApiHost=host, ssl=ssl, ca_path=ca_path)
        deployment = kubeconn.list_namespaced_deployment(namespace=meta['env'], label_selector="")
        return jsonify(deployment)
    # if request.method == "GET":
    #     kubeconn = kubeBase(token=token, ApiHost=host, ssl=ssl, ca_path=ca_path)
    #     kubeconn.read_namespaced_service(name='hpayfintechport',namespace='bfienv003')
    #     return jsonify({'h':'a'})


@app.route('/api/kubernetes/service/list', methods=["POST","GET"])
def list_service():
    if request.method == "GET":
        kubeconn = kubeBase(token=token, ApiHost=host, ssl=ssl, ca_path=ca_path)
        mysqlconn = dbsql(host=dbhost, username=username, password=password)
        dp_env = mysqlconn.get_env_deployment()
        data = kubeconn.list_svc(dp_env=dp_env)
        return jsonify(data)


@app.route('/api/kubernetes/node/list', methods=["POST","GET"])
def list_nodes():
    if request.method == "GET":
        kubeconn = kubeBase(token=token, ApiHost=host, ssl=ssl, ca_path=ca_path)
        deployment = kubeconn.read_node()
        return jsonify({"a": "a"})



if __name__ == '__main__':
    app.run(debug=True,port=28888,host="10.148.181.214")
    # gevent_server = gevent.pywsgi.WSGIServer(('', 8897), app)  # 提高性能
    # gevent_server.serve_forever()

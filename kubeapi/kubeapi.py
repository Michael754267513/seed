#! encoding: utf-8
from kubernetes import client

import time, json, commands, os

import pysnooper


def manager_helm(cmd):
    check = 1
    for helm_cmd in cmd:
        res = os.system(helm_cmd)
        if res != 0:
            check = 0
    return check


def delete_helm_cmd(meta):
    helm_cmd = []
    for data in meta:
        deployment = data
        helm = '''helm del --purge  %s 
        ''' % (deployment)
        helm_cmd.append(helm)
    return helm_cmd


class kubeBase:

    def __init__(self, token, ApiHost, ssl=False, ca_path=None):

        '''
        :param token: RBAC 授权的用户token
        :param ApiHost: APIService 主机地址
        :param ssl: 是否开始SSL
        :param ca_path: 开启ssl后ca路径
        '''
        token = token
        ApiHost = ApiHost
        ssl = ssl
        ca_path = ca_path
        client_config = client.Configuration()
        client_config.host = ApiHost
        if ssl:
            client_config.verify_ssl = ssl
            if ca_path == None:
                print("ssl is Ture,you must config ca_path!!")
            else:
                client_config.ssl_ca_cert = ca_path
        else:
            client_config.verify_ssl = False
        client_config.api_key = {"authorization": "Bearer " + token}
        try:
            self.aApiClient = client.ApiClient(client_config)
        except Exception as ex:
            print("Connection  APIServer Error: %s" % ex)

    def read_namespaces(self,namespace):
        kubecon = client.CoreV1Api(self.aApiClient)
        try:
            api_response = kubecon.read_namespace(name=namespace)
            if api_response.status.phase == 'Active':
                return 'Active'
            if api_response.status.phase == 'Terminating':
                return 'Terminating'
        except Exception as e:
            print(e)
            return False
        return api_response.status.phase

    def create_namespaces(self, namespaces, lables={}):
        '''
        :param namespaces:  命名空间
        :param lables:  命名空间标签
        :return:
        '''
        kubecon = client.CoreV1Api(self.aApiClient)
        #  判断 ns是否已经创建
        body = client.V1Namespace(
            metadata=client.V1ObjectMeta(name=namespaces,labels=lables),
            spec=client.V1NamespaceSpec(finalizers=[])
        )
        try:
            api_response = kubecon.create_namespace(body=body)
            while True:
                if self.read_namespaces(namespace=namespaces) == 'Active':
                    break
                if self.read_namespaces(namespace=namespaces) == 'Terminating':
                    break
                time.sleep(2)
            return self.read_namespaces(namespace=namespaces)
        except Exception as ex:
            while True:
                if self.read_namespaces(namespace=namespaces) == 'Active':
                    break
                if self.read_namespaces(namespace=namespaces) == 'Terminating':
                    break
                time.sleep(2)
            return self.read_namespaces(namespace=namespaces)

    def delete_namespaces(self, namespaces, grace_period_seconds=0):

        '''
        :param namespaces:  删除的命名空间
        :param grace_period_seconds: 延迟删除时间
        :return:
        '''
        kubecon = client.CoreV1Api(self.aApiClient)
        body = client.V1DeleteOptions(
            grace_period_seconds=grace_period_seconds,
            # propagation_policy='Foreground'
            propagation_policy='Background'
        )
        try:
            api_response = kubecon.delete_namespace(name=namespaces,body=body,propagation_policy='Background')
            return True
        except Exception as e:
            print(e)
            return False

    def get_pod(self, pod):
        kubecon = client.CoreV1Api(self.aApiClient)
        podlist = []
        for dpod in pod:
            name = dpod[1]
            ptype = dpod[2]
            pimage = dpod[3]
            project = dpod[4]
            env = dpod[5]
            owner = dpod[6]
            ing = dpod[7]
            deploy = dpod[8]
            ising = dpod[9]
            label_selector = "owner=%s,project=%s,app.kubernetes.io/instance=%s" % (owner, project, deploy)
            pods = kubecon.list_namespaced_pod(namespace=env,label_selector=label_selector)
            pod_meta = pods.items
            for i in pod_meta:
                pod_deploy = {}
                pod_deploy["name"] = name
                pod_deploy["type"] = ptype
                pod_deploy["project"] = project
                pod_deploy["env"] = env
                pod_deploy["owner"] = owner
                pod_deploy["ingress"] = ing
                pod_deploy["ising"] = ising
                pod_deploy["podip"] = i.status.pod_ip
                pod_deploy["pod_name"] = i.metadata.name
                try:
                    pod_deploy["status"] = i.status.container_statuses[0].state.waiting.reason
                    pod_deploy["message"] = i.status.container_statuses[0].state.waiting.message
                except Exception as e:
                    pod_deploy["status"] = i.status.phase
                    pod_deploy["message"] = None
                if i.status.container_statuses[0].ready:
                    pod_deploy['ready'] = u'成功'
                else:
                    pod_deploy['ready'] = u'启动中'
                    try:
                        pod_deploy["message"] = i.status.container_statuses[0].state.terminated.reason
                    except Exception as e:
                        print e
                pod_deploy['restart_count'] = i.status.container_statuses[0].restart_count
                pod_deploy["nodeip"] = i.status.host_ip
                pod_deploy["image"] = pimage
                pod_deploy["deployment"] = deploy
                # pod_deploy.update(self.read_namespaced_service(name=name, namespace=env))
                podlist.append(pod_deploy)
        return podlist

        # for i in api_response.items:
        #     podlist.append({"podIP": i.status.pod_ip, "image": i.spec.containers[0].image, "namespace": i.metadata.namespace , "podName": i.metadata.name, "nodeName": i.status.host_ip, "podStatus": i.status.phase})
        # return podlist

    def list_ns(self):
        kubecon = client.CoreV1Api(self.aApiClient)
        list_ns = kubecon.list_namespace().items
        nslist = []
        for ns in list_ns:
            ns_meta={}
            ns_meta["lable"] = ns.metadata.name
            ns_meta["value"] = ns.metadata.name
            nslist.append(ns_meta)
        return nslist

    def list_pod(self, env):
        kubecon = client.CoreV1Api(self.aApiClient)
        pod_meta = kubecon.list_namespaced_pod(namespace=env).items
        podlist = []
        for i in pod_meta:
            pod_deploy = {}
            pod_deploy["env"] = env
            pod_deploy["podip"] = i.status.pod_ip
            pod_deploy["pod_name"] = i.metadata.name
            pod_deploy["nodeip"] = i.status.host_ip
            pod_deploy["qos"] = i.status.qos_class
            try:
                pod_deploy["status"] = i.status.container_statuses[0].state.waiting.reason
                pod_deploy["message"] = i.status.container_statuses[0].state.waiting.message
            except Exception as e:
                pod_deploy["status"] = i.status.phase
                pod_deploy["message"] = None
            if i.status.container_statuses[0].ready:
                pod_deploy['ready'] = u'成功'
            else:
                pod_deploy['ready'] = u'启动中'
                try:
                    pod_deploy["message"] = i.status.container_statuses[0].state.terminated.reason
                except Exception as e:
                    print e
            pod_deploy['restart_count'] = i.status.container_statuses[0].restart_count
            podlist.append(pod_deploy)
        return podlist

    def read_namespaced_service(self, name, namespace):
        kubecon = client.CoreV1Api(self.aApiClient)
        svc =  kubecon.read_namespaced_service(name=name, namespace=namespace)
        svc_list = {}
        svc_list['name'] = name
        svc_list['env'] = namespace
        svc_list['svc_ip'] = svc.spec.cluster_ip
        svc_list['svc_type'] = svc.spec.type
        svc_list['svc_port'] = svc.spec.ports[0].port
        if svc_list['svc_type'] == 'NodePort':
            svc_list['svc_nodeport'] = svc.spec.ports[0].node_port
        return svc_list

    def list_svc(self, dp_env):
        svc = []
        for item in dp_env:
            svc.append(self.read_namespaced_service(name=item[0],namespace=item[1]))
        return svc


    def list_namespaced_deployment(self,namespace,label_selector):
        kubecon = client.AppsV1beta1Api(self.aApiClient)
        deployment = kubecon.list_namespaced_deployment(namespace=namespace, label_selector=label_selector).items
        deployment_list = []
        for i in deployment:
            deploy_info = {}
            deploy_info['name'] = i.metadata.name
            deploy_info['env'] = i.metadata.namespace
            deploy_info['max_surge'] = i.spec.strategy.rolling_update.max_surge
            deploy_info['max_unavailable'] = i.spec.strategy.rolling_update.max_unavailable
            deploy_info['available_replicas'] = i.status.available_replicas
            deploy_info['observed_generation'] = i.status.observed_generation
            deploy_info['ready_replicas'] = i.status.ready_replicas
            deploy_info['replicas'] = i.status.replicas
            if i.status.conditions[0].status:
                deploy_info['status'] = u'更新完毕'
            else:
                deploy_info['status'] = u'更新中'
            deploy_info['type'] = i.status.conditions[-1].type
            deploy_info['unavailable_replicas'] = i.status.unavailable_replicas
            deploy_info['updated_replicas'] = i.status.updated_replicas
            deployment_list.append(deploy_info)
        return deployment_list

    def read_node(self):
        kubecon = client.CoreV1Api(self.aApiClient)
        node = kubecon.list_node().items()
        for i in node:
            print i

        return node

class manager_res:

    def __init__(self, project, env, owner):
        '''
        :param project:  项目名称
        :param env:    环境名称
        :param owner: 环境所属人
        '''

        self.project = project
        self.env = env
        self.owner = owner

    def get_pkg(self, metadata, type):
        '''
        :param metadata: 更新类型元数据 list类型
        :return:
        '''
        # 按照处理规则 对镜像进行分解
        meta = []
        for image_meta in metadata:
            pkg_meta = {}
            image = image_meta
            pkg = image_meta.split(":")[0].split("/")[-1]
            if type == "ui":
                ingress_name = pkg
                pkg_meta["ingress"] = True
                pkg_meta["ingress_name"] = ingress_name
            if type == "core":
                ingress_name = pkg
                pkg_meta["ingress"] = False
                pkg_meta["ingress_name"] = ingress_name
            dp_name = self.env + "-" + pkg
            pkg_meta["packagename"] = pkg
            pkg_meta["image"] = image
            pkg_meta["project"] = self.project
            pkg_meta["env"] = self.env
            pkg_meta["owner"] = self.owner
            pkg_meta["type"] = type
            pkg_meta["deployment"] = dp_name.lower()
            meta.append(pkg_meta)
        return meta

    def get_svc(self, metadata, type):
        '''
             :param metadata: 更新类型元数据 list类型
             :return:
             '''
        # 按照处理规则 对镜像进行分解
        meta = []
        for svc_meta in metadata:
            pkg_meta = {}
            svc_name= svc_meta[3]
            helm_repo = svc_meta[2]
            image = svc_meta[1]
            pkg = image.split(":")[0].split("/")[-1]
            if type == "service":
                ingress_name = svc_name
                pkg_meta["ingress"] = False
                pkg_meta["ingress_name"] = ingress_name
            dp_name = self.env + "-" + pkg
            pkg_meta["packagename"] = pkg
            pkg_meta["image"] = image
            pkg_meta["project"] = self.project
            pkg_meta["helm_repo"] = helm_repo
            pkg_meta["env"] = self.env
            pkg_meta["owner"] = self.owner
            pkg_meta["type"] = type
            pkg_meta["deployment"] = dp_name.lower()
            meta.append(pkg_meta)
        return meta

    def ui_updates(self, uiupdate):
        meta = self.get_pkg(metadata=uiupdate,type="ui")
        return meta

    def core_updates(self, coreupdate):
        meta = self.get_pkg(metadata=coreupdate, type="core")
        return meta

    def ui_create(self, uicreate):
        meta = self.get_pkg(metadata=uicreate, type="ui")
        return meta

    def core_create(self, corecreate):
        meta = self.get_pkg(metadata=corecreate,type="core")
        return meta

    def pod_delete(self, pod_delete):
        meta = self.get_pkg(metadata=pod_delete, type="ui")
        return meta

    def svc_create(self, meta):
        meta = self.get_svc(metadata=meta, type="service")
        return meta

    def helm_create_svc(self, meta):
        helm_cmd = []
        for data in meta:
            namespace = data["env"]
            deployment = data["deployment"]
            owner = data["owner"]
            project = data["project"]
            image = data["image"]
            ingress = data["ingress"]
            ingress_name = data["ingress_name"]
            helm_repo = data["helm_repo"]
            helm = '''helm install --name %s \
            --set image=%s  \
            --set namespace=%s \
            --set owner=%s \
            --set project=%s \
            --set ingress.enabled=%s \
            --set ingress.name=%s  \
            michael/%s 
            ''' % (
                deployment, image, namespace, owner, project, ingress, ingress_name, helm_repo
            )
            helm_cmd.append(helm)
        return helm_cmd

    def helm_create(self, meta):
        helm_cmd = []
        for data in meta:
            namespace = data["env"]
            deployment = data["deployment"]
            owner = data["owner"]
            project = data["project"]
            image = data["image"]
            ingress = data["ingress"]
            ingress_name = data["ingress_name"]
            helm = '''helm install --name %s \
            --set image=%s  \
            --set namespace=%s \
            --set owner=%s \
            --set project=%s \
            --set ingress.enabled=%s \
            --set ingress.name=%s  \
            michael/java 
            ''' % (
                deployment, image, namespace, owner, project, ingress, ingress_name
            )
            helm_cmd.append(helm)
        return helm_cmd

    def helm_update(self, meta):
        helm_cmd = []
        for data in meta:
            namespace = data["env"]
            deployment = data["deployment"]
            owner = data["owner"]
            project = data["project"]
            image = data["image"]
            ingress = data["ingress"]
            ingress_name = data["ingress_name"]
            helm = '''helm upgrade %s \
            --set image=%s  \
            --set namespace=%s \
            --set owner=%s \
            --set project=%s \
            --set ingress.enabled=%s \
            --set ingress.name=%s  \
            michael/java 
            ''' % (
                deployment, image, namespace, owner, project, ingress, ingress_name
            )
            helm_cmd.append(helm)
        return helm_cmd

    def helm_delete(self, meta):
        helm_cmd = []
        for data in meta:
            deployment = data["deployment"]
            helm = '''helm del --purge  %s 
            ''' % (deployment)
            helm_cmd.append(helm)
        return helm_cmd


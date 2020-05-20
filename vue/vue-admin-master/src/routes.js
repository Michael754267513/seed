import Login from './views/Login.vue'
import NotFound from './views/404.vue'
import Home from './views/Home.vue'
import Main from './views/Main.vue'
import nslist from './views/nav1/nslist.vue'
import deployment from './views/nav1/deployment.vue'
import pod from './views/nav1/pod.vue'
import svc from './views/nav1/svc.vue'
import echarts from './views/charts/echarts.vue'
import request_deployment from './views/kubernetes/request_deployment.vue'
import test from './views/kubernetes/test.vue'
// 模板列表
import app_netpolicy_tmp from './views/templates/app_netpolicy_tmp.vue'
import base_netpolicy_tmp from './views/templates/base_netpolicy_tmp.vue'
import base_services_tmp from './views/templates/base_services_tmp.vue'
import pkg_att_tmp from './views/templates/pkg_att_tmp.vue'
import public_services_tmp from './views/templates/public_services_tmp.vue'
import pkg_tmp from './views/templates/pkg_tmp.vue'
// 资源列表
import public_services from './views/project/public_services.vue'
import appliction_networkpolicy from './views/project/appliction_networkpolicy.vue'
import appliction_networkpolicy_wait_add from './views/project/appliction_networkpolicy_wait_add.vue'
import appliction_deployment from './views/project/appliction_deployment.vue'
import appliction_networkpolicy_list from './views/project/appliction_networkpolicy_list.vue'
// 容器后台管理
import admin_package from './views/kubernetes/admin_package.vue'
import { request } from 'https';

let routes = [
    {
        path: '/login',
        component: Login,
        name: '',
        hidden: true
    },
    {
        path: '/404',
        component: NotFound,
        name: '',
        hidden: true
    },
    //{ path: '/main', component: Main },
    {
        path: '/',
        component: Home,
        name: '容器清单',
        iconCls: 'el-icon-message',//图标样式class
        children: [
            { path: '/main', component: Main, name: '主页', hidden: true },
            { path: '/kubernetes/environment', component: pod, name: '环境列表'},
            { path: '/kubernetes/namespaces/pod/list', component: nslist, name: '容器列表' },
            { path: '/kubernetes/namespaces/svc/list', component: svc, name: '服务列表' },
            { path: '/kubernetes/namespaces/deployment/list', component: deployment, name: '容器发布状态'},
        ]
    },
    {
        path: '/',
        component: Home,
        name: '容器管理',
        iconCls: 'el-icon-message',//图标样式class
        children: [
            { path: '/kubernetes/namespaces/deployment/request', component: request_deployment, name: '容器发布申请' },
            { path: '/kubernetes/namespaces/deployment/test', component: test, name: '测试' }
        
        ]
    },
    {
        path: '/',
        component: Home,
        name: '容器后台管理',
        iconCls: 'el-icon-message',//图标样式class
        children: [
            { path: '/kubernetes/admin/package', component: admin_package, name: '项目配置' },
        ]
    },
    {
        path: '/',
        component: Home,
        name: '资源管理',
        iconCls: 'el-icon-message',//图标样式class
        children: [
            { path: '/handpay/appliction/networkpolicy/request', component: appliction_networkpolicy, name: '网络权限申请' },
            { path: '/handpay/appliction/networkpolicy/wait_add', component: appliction_networkpolicy_wait_add, name: '待开通网络权限' },
        ]
    },
    {
        path: '/',
        component: Home,
        name: '资源查看',
        iconCls: 'el-icon-message',//图标样式class
        children: [
            { path: '/handpay/public/service', component: public_services, name: '公共服务列表' },
            { path: '/handpay/appliction/networkpolicy/list', component: appliction_networkpolicy_list, name: '应用网络权限查看' },
            { path: '/handpay/appliction/deployment/list', component: appliction_deployment, name: '应用部署列表' },
        ]
    },
    {
        path: '/',
        component: Home,
        name: '模板管理',
        iconCls: 'el-icon-message',//图标样式class
        children: [
            { path: '/handpay/service/templates/base', component: base_services_tmp, name: '基础服务模板' },
            { path: '/handpay/service/templates/public', component: public_services_tmp, name: '公共服务模板' },
            { path: '/handpay/service/templates/networkpolicy/base', component: base_netpolicy_tmp, name: '基础网络模板' },
            { path: '/handpay/package/templates/property', component: pkg_att_tmp, name: '包属性模板' },
            { path: '/handpay/applictions/templates/networkpolicy', component: app_netpolicy_tmp, name: '应用网络权限模板' },
            { path: '/handpay/package/templates/container', component: pkg_tmp, name: '包容器模板' },
        ]
    },
    {
        path: '/',
        component: Home,
        name: 'Charts',
        iconCls: 'fa fa-bar-chart',
        children: [
            { path: '/echarts', component: echarts, name: 'echarts' }
        ]
    },
    {
        path: '*',
        hidden: true,
        redirect: { path: '/404' }
    }
];

export default routes;
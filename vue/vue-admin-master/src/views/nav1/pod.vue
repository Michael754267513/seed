<template>
  <section>
	  	<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-form :inline="true" >
				<el-form-item>
					<el-input  placeholder="应用名"></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" >查询</el-button>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" >新增应用</el-button>
				</el-form-item>
			</el-form>
		</el-col>
  <el-table
    :data="poddata"
	stripe
    style="width: 100%">
	<el-table-column
      prop="name"
      label="应用名"
	  width="185">
    </el-table-column>
    <el-table-column
      prop="project"
      label="项目名">
    </el-table-column>
	<el-table-column
      prop="ready"
      type="text"
      label="状态">
    </el-table-column>
    <el-table-column
      prop="env"
      label="环境">
    </el-table-column>
    <el-table-column
      prop="owner"
      label="所有者">
    </el-table-column>
    <el-table-column
      prop="status"
      label="容器状态">
    </el-table-column>
    <el-table-column
      prop="nodeip"
      label="宿主机地址"
	  width="140">
    </el-table-column>
	<el-table-column
      label="容器信息"
       >
      <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <p>事件消息：{{ scope.row.message }}</p>
          <p>容器地址：{{ scope.row.podip }}</p>
          <p>容器状态：{{ scope.row.status }}</p>
          <p>访问地址: {{ scope.row.ingress }}</p>
          <p>类型: {{ scope.row.type }}</p>
          <p>服务类型: {{ scope.row.ising }}</p>
		      <p>宿主机地址: {{ scope.row.nodeip }}</p>
		      <p>namespace: {{ scope.row.env }}</p>
		      <p>helm名称: {{ scope.row.env +"-"+ scope.row.name }}</p>
		      <p>容器名: {{ scope.row.pod_name }}</p>
          <p>镜像: {{ scope.row.image }}</p>
          <p>deployment名称: {{ scope.row.deployment }}</p>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">容器属性</el-tag>
          </div>
        </el-popover>
      </template>
    </el-table-column>
    <el-table-column
      label="操作">
      <template slot-scope="scope">
        <el-button
          @click.native.prevent="webterminal(scope.$index, poddata)"
          size="mini">
          终端
        </el-button>
		    <el-button
          @click.native.prevent="logterminal(scope.$index, poddata)"
          size="mini">
          日志
        </el-button>
      </template>
    </el-table-column>
  </el-table>
  </section>
</template>

<script>
	import util from '../../common/js/util'
	//import NProgress from 'nprogress'
	import {  getVMS, getPods  } from '../../api/api';

	export default {
		data() {
			return {
		poddata: [],
		testpod: [],
			}
		},
		methods: {
     		 getDatavm () {
      			var api = '/handpay/kubernetes/update/deployment'
      			this.$http.get(api).then((response) => {
        			this.poddata = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
			},
			webterminal: function(podindex, podmeta) {
				this.weburl = "http://10.148.181.214:9395/?arg=" + podmeta[podindex].pod_name + "&arg=/bin/bash&arg=-n&arg="+ podmeta[podindex].env
				window.open(this.weburl, '_blank', 'toolbar=yes, width=900, height=700')
			},
			logterminal: function(podindex, podmeta) {
				this.logurl = "http://10.148.181.214:9388/?arg=" + podmeta[podindex].pod_name + "&arg=-n&arg="+ podmeta[podindex].env
				window.open(this.logurl, '_blank', 'toolbar=yes, width=900, height=700')
			},
		},
		// mounted() {
		// 	this.getUsers();
    // }
    mounted() {
			this.getDatavm()
		}
	}

</script>

<style scoped>

</style>
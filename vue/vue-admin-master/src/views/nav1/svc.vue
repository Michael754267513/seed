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
      prop="env"
      label="环境">
    </el-table-column>
	<el-table-column
      prop="svc_type"
      label="类型"
      >
    </el-table-column>
    <el-table-column
      prop="svc_ip"
      label="服务ip">
    </el-table-column>
    <el-table-column
      prop="svc_port"
      label="容器端口">
    </el-table-column>
    <el-table-column
      prop="svc_nodeport"
      label="对外端口">
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
      			var api = '/api/kubernetes/service/list'
      			this.$http.get(api).then((response) => {
        			// console.log(response.body)
        			this.poddata = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
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
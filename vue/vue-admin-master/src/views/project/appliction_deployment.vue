<template>
  <section>
	  	<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-form :inline="true" >
				<el-form-item>
					<el-input  placeholder="应用查询"></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" >查询</el-button>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" >应用部署查询</el-button>
				</el-form-item>
			</el-form>
		</el-col>
    <el-table
    :data="publicservices"
    style="width: 100%"
    :default-sort = "{prop: 'date', order: 'descending'}"
    >
    <el-table-column
      prop="id"
      label="id"
	  width="100"
      sortable>
    </el-table-column>
    <el-table-column
      prop="warname"
      label="包名"
      sortable>
    </el-table-column>
    <el-table-column
      prop="hostname"
      label="所在主机名"
      sortable>
    </el-table-column>
	<el-table-column
      prop="ip"
      label="地址"
      sortable>
    </el-table-column>
	<el-table-column
      prop="port"
      label="端口"
      >
    </el-table-column>
    <el-table-column
      prop="apptype"
      label="容器类型"
      >
    </el-table-column>
    <el-table-column
      prop="type"
      label="包类型"
      >
    </el-table-column>
	<el-table-column
      prop="warformat"
      label="包格式"
      sortable>
    </el-table-column>
	<el-table-column
      prop="owner"
      label="所属人"
      sortable>
    </el-table-column>
    <el-table-column
      prop="project"
      label="项目"
      >
    </el-table-column>
    <el-table-column
      prop="env"
      label="环境"
      >
    </el-table-column>
  </el-table>
  </section>
</template>

<script>
	import util from '../../common/js/util'

	export default {
		data() {
			return {
		publicservices: [],
			}
		},
		methods: {
     		 getPublicServices () {
      			var api = '/handpay/project/appdeployment'
      			this.$http.get(api).then((response) => {
        			this.publicservices = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
			},
        },
    mounted() {
			this.getPublicServices()
		}
	}

</script>

<style scoped>

</style>
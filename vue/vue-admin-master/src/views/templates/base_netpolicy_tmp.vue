<template>
  <section>
	  	<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-form :inline="true" >
				<el-form-item>
					<el-input  placeholder="服务名"></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" >查询</el-button>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" >新增基础网络权限模板</el-button>
				</el-form-item>
			</el-form>
		</el-col>
    <el-table
    :data="basenetpolicy"
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
      prop="servicename"
      label="服务名"
      sortable>
    </el-table-column>
    <el-table-column
      prop="protocol"
      label="协议"
      >
    </el-table-column>
    <el-table-column
      prop="src"
      label="源地址"
      >
    </el-table-column>
    <el-table-column
      prop="dest"
      label="目标地址"
      >
    </el-table-column>
    <el-table-column
      prop="port"
      label="目标端口"
      >
    </el-table-column>
    <el-table-column
      prop="desc"
      label="描述"
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
		basenetpolicy: [],
			}
		},
		methods: {
     		 getBaseNetPolicy () {
      			var api = '/handpay/templates/basenetpolicy'
      			this.$http.get(api).then((response) => {
        			this.basenetpolicy = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
			},
        },
    mounted() {
			this.getBaseNetPolicy()
		}
	}

</script>

<style scoped>

</style>
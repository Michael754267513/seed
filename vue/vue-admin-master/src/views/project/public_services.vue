<template>
  <section>
	  	<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-form :inline="true" >
				<el-form-item>
					<el-input  placeholder=""></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" >查询</el-button>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" >新增公共服务模板</el-button>
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
      prop="pkgname"
      label="服务包名"
      sortable>
    </el-table-column>
	<el-table-column
      prop="pkgalias"
      label="对外提供服务名"
      sortable>
    </el-table-column>
	<el-table-column
      prop="port"
      label="端口"
      >
    </el-table-column>
    <el-table-column
      prop="version"
      label="版本号"
      >
    </el-table-column>
	<el-table-column
      prop="isCluster"
      label="是否是集群"
      :formatter="formatIsCluster"
      sortable>
    </el-table-column>
	<el-table-column
      prop="nodelist"
      label="节点列表"
      sortable>
    </el-table-column>
    <el-table-column
      prop="env"
      label="IDC环境"
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
          formatIsCluster: function (row, column) {
				return row.isCluster == 0 ? '集群' : row.isCluster == 1 ? '单机' : '未知';
			},
     		 getPublicServices () {
      			var api = '/handpay/project/publicservices'
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
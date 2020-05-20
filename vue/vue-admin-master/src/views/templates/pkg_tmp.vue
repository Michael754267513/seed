
<template>
  <section>
	  	<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-form :inline="true" >
				<el-form-item>
					<el-input  placeholder="基础包名"></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" >查询</el-button>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" >新增基础服务模板</el-button>
				</el-form-item>
			</el-form>
		</el-col>
    <el-table
    :data="pkgcontainer"
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
      prop="runserver"
      label="服务类型"
      sortable>
    </el-table-column>
    <el-table-column
      prop="insname"
      label="实例名"
      >
    </el-table-column>
    <el-table-column
      prop="port"
      label="实例端口"
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
		pkgcontainer: [],
			}
		},
		methods: {
     		 getPkgContainer () {
      			var api = '/handpay/templates/pkgcontainer'
      			this.$http.get(api).then((response) => {
        			this.pkgcontainer = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
			},
        },
    mounted() {
			this.getPkgContainer()
		}
	}

</script>

<style scoped>

</style>
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
    :data="baseservices"
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
      label="基础服务包名"
      sortable>
    </el-table-column>
    <el-table-column
      prop="pkgversion"
      label="版本号"
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
		baseservices: [],
			}
		},
		methods: {
     		 getBaseServices () {
      			var api = '/handpay/templates/baseservices'
      			this.$http.get(api).then((response) => {
        			this.baseservices = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
			},
        },
    mounted() {
			this.getBaseServices()
		}
	}

</script>

<style scoped>

</style>

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
    :data="pkgatt"
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
      prop="name"
      label="包名"
      sortable>
    </el-table-column>
    <el-table-column
      prop="apptype"
      label="容器服务类型"
      >
    </el-table-column>
    <el-table-column
      prop="warformat"
      label="包类型"
      >
    </el-table-column>
    <el-table-column
      prop="type"
      label="服务类型"
      >
    </el-table-column>
    <el-table-column
      prop="owner"
      label="所属人"
      >
    </el-table-column>
    <el-table-column
      prop="project"
      label="所属项目"
      >
    </el-table-column>
    <el-table-column
      prop="sticky"
      label="亲和包"
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
		pkgatt: [],
			}
		},
		methods: {
     		 getPkgAtt () {
      			var api = '/handpay/templates/pkgatt'
      			this.$http.get(api).then((response) => {
                    this.pkgatt = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
			},
        },
    mounted() {
			this.getPkgAtt()
		}
	}

</script>

<style scoped>

</style>
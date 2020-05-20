<template>
<!-- todolist -->
  <section>
	  	<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-form :inline="true" >
				<el-form-item>
					<el-input  placeholder="虚拟机名称"></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" >查询</el-button>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" @@click="vmNew">新增虚拟机</el-button>
				</el-form-item>
			</el-form>
		</el-col>
     <el-table
      ref="multipleTable"
      :default-sort = "{prop: 'vmname', order: 'descending'}"
      :data="vmdata"
      border
       >
       <el-table-column
      type="selection"
       >
    </el-table-column>
      <el-table-column
        fixed
        prop="vmname"
        label="虚拟机名称"
        sortable
        >
      </el-table-column>
	  <el-table-column
        prop="group"
        label="所属组"
        >
      </el-table-column>
      <el-table-column label="资源信息">
      <el-table-column
        prop="cpu_core"
        label="CPU数"
        >
      </el-table-column>
      <el-table-column
        prop="memory"
        label="内存"
        >
      </el-table-column>
      </el-table-column>
      <el-table-column label="网络信息">
      <el-table-column
        prop="address"
        label="ip地址"
        >
      </el-table-column>
      </el-table-column>
      <el-table-column
        label="虚拟机信息"
        >
     <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <p>主机名: {{ scope.row.hostname }}</p>
          <p>ip地址: {{ scope.row.address }}</p>
          <p>掩码:   {{ scope.row.netmask }}</p>
          <p>网关:   {{ scope.row.gateway }}</p>
          <p>vlan号: {{ scope.row.vlanid }}</p>
          <p>DNS:    {{ scope.row.dns_server }}</p>
          <p>域:     {{ scope.row.dns_domain }}</p>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">网络信息</el-tag>
          </div>
        </el-popover>
      </template>
      </el-table-column>

       <el-table-column  fixed="right" label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          >编辑</el-button>
        <el-button
          size="mini"
          type="danger"
          >删除</el-button>
      </template>
    </el-table-column>
    </el-table>
	  <el-col :span="24" class="toolbar">
			<el-button type="danger" >批量删除</el-button>
			<el-pagination layout="prev, pager, next" :page-size="20" style="float:right;">
			</el-pagination>
		</el-col>
    
  </section>
</template>

<script>
export default {
  data () {
    return {
    vmdata: [],
    }
  },
  methods: {
    vmNew: function () {
			},
    setDatavm () {
      var api = 'http://127.0.0.1/api/vm/list'
      this.$http.post(api, 'vue-post-message').then((response) => {
        // console.log(response.body)
        // this.vmdata = response.body
        console.log(this.vmdata)
      },
      function (err) {
        console.log(err)
      }
      )
    },
    getDatavm () {
      var api = 'http://127.0.0.1/api/vm/list'
      this.$http.get(api).then((response) => {
        // console.log(response.body)
        this.vmdata = response.body
        console.log(this.vmdata)
      },
      function (err) {
        console.log(err)
      }
      )
    },
  },
  mounted() {
			this.getDatavm()
		}
}
</script>

<style>
</style>

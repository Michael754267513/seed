<template>
<!-- todolist -->
  <section>
    <el-select v-model="value" filterable @input="nsSelect(value)" placeholder="请选择">
     <el-option
      v-for="item in nslist"
      :key="item.value"
      :label="item.label"
      :value="item.value"
      >
      </el-option>
    </el-select>
       <el-table
    :data="poddata"
	stripe
    style="width: 100%">
    <el-table-column
      prop="name"
      label="发布名称">
    </el-table-column>
    <el-table-column
      prop="env"
      label="环境">
    </el-table-column>
    <el-table-column
      prop="replicas"
      label="实例数">
    </el-table-column>
	<el-table-column
      prop="available_replicas"
      label="运行数">
    </el-table-column>
	<el-table-column
      prop="unavailable_replicas"
      label="不可用数">
    </el-table-column>
	<el-table-column
      prop="updated_replicas"
      label="更新实例数">
    </el-table-column>
	<el-table-column
      prop="observed_generation"
      label="ReplicaSet数">
    </el-table-column>
	<el-table-column
      label="滚动更新策略">
      <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <p>更新新增pod数量: {{ scope.row.max_surge }}</p>
          <p>更新pod不可用数量: {{ scope.row.max_unavailable }}</p>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">滚动更新策略</el-tag>
          </div>
        </el-popover>
      </template>
    </el-table-column>
  </el-table>
  </section>
</template>

<script>
export default {
  data () {
    return {
    nslist: [],
    value: "default",
    poddata: []
    }
  },
  methods: {
    getNSList () {
      var api = '/api/kubernetes/list/ns'
      this.$http.get(api).then((response) => {
        this.nslist = response.body
      },
      function (err) {
        console.log(err)
      }
      )
    },
    nsSelect () {
      var api = '/api/kubernetes/deployment/list'
      this.$http.post(api,{'env':this.value}).then((response) => {
        this.poddata = response.body
      },
      function (err) {
        console.log(err)
      }
      )
    },
    webterminal: function(podindex, podmeta) {
				this.weburl = "http://10.148.181.214:9395/?arg=" + podmeta[podindex].pod_name + "&arg=/bin/bash&arg=-n&arg="+ podmeta[podindex].env
				window.open(this.weburl, '_blank', 'toolbar=yes, width=window.innerWidth, height=window.innerHeight')
			},
		logterminal: function(podindex, podmeta) {
				this.logurl = "http://10.148.181.214:9388/?arg=" + podmeta[podindex].pod_name + "&arg=-n&arg="+ podmeta[podindex].env
				window.open(this.logurl, '_blank', 'toolbar=yes, width=window.innerWidth, height=window.innerHeight')
			},
    
  },
  mounted() {
      this.getNSList(),
      this.nsSelect ()
		}
}
</script>

<style>
</style>

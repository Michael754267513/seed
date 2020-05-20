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
      prop="env"
      label="环境">
    </el-table-column>
    <el-table-column
      prop="pod_name"
      label="容器名">
    </el-table-column>

    <el-table-column
      prop="podip"
      label="容器地址"
	  width="120">
    </el-table-column>
    	<el-table-column
      prop="nodeip"
      label="计算节点">
    </el-table-column>
    <el-table-column
      prop="ready"
      label="状态">
    </el-table-column>
    <el-table-column
      prop="restart_count"
      label="重启次数">
    </el-table-column>
	<el-table-column
      prop="status"
      label="容器状态">
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
        <el-popover trigger="hover" placement="top">
          <p>{{ scope.row.message }}</p>
          <div slot="reference" class="name-wrapper">
            <el-tag size="mini">事件消息</el-tag>
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
      var api = '/api/kubernetes/list/pod'
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

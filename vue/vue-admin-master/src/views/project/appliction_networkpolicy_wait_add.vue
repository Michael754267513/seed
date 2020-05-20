<template>
    <section>
    环境列表:<el-select v-model="env"  @input="OnChange()" placeholder="请选择">
     <el-option
      v-for="item in envlist"
      :key="item.env"
      :label="item.env"
      :value="item.env"
      >
      </el-option>
      </el-select>
    策略状态:<el-select v-model="status"  @input="OnChange()" placeholder="请选择">
     <el-option
      v-for="item in rulestatus"
      :key="item.key"
      :label="item.lable"
      :value="item.value"
      >
      </el-option>
      </el-select>
    <div style="margin: 15px 0;"></div>
      <div style="margin: 15px 0;"></div>
  <el-button type="primary" @click='commitNetRules'>开通策略</el-button>
  <el-button type="primary" @click='delNetRules'>删除策略</el-button>
  <template>
    <el-table
      :data="netPoliceList"
      style="width: 100%"
      @selection-change="handleSelectionChange">
      <el-table-column
      type="selection"
      width="55"
      >
    </el-table-column>
      <el-table-column
        prop="src"
        sortable 
        label="源地址">
      </el-table-column>
      <el-table-column
        prop="dest"
        label="目的地址">
      </el-table-column>
      <el-table-column
        prop="port"
        label="目标端口">
      </el-table-column>
      <el-table-column
        prop="protocol"
        label="协议">
      </el-table-column>
      <el-table-column
        prop="owner"
        label="需求方">
      </el-table-column>
      <el-table-column
        prop="desc"
        label="业务说明">
      </el-table-column>
      <el-table-column
        prop="status"
        :formatter="formatStatus"
        label="策略状态">
      </el-table-column>
    </el-table>
  </template>
</section>  
</template>

<script>
export default {
  data() {
    return {
      env: "grid",
      envlist: [],
      netPoliceList: [],
      status: '',
      multipleSelection: '',
      rulestatus: [{'key':0,'value':'0','lable':'已开通'},{'key':1,'value':'1','lable':'未开通'},{'key':2,'value':'2','lable':'已删除'}]
    };
  },
  methods: {
    formatStatus: function (row, column) {
				return row.status == 0 ? '已开通' : row.status == 1 ? '未开通' :  row.status == 2 ? '已删除': '未知';
			},
    handleSelectionChange(val) {
        this.multipleSelection = val;
        console.log(this.multipleSelection)
      },
        get_env(){
        var api = '/handpay/project/env/list'
      			this.$http.get(api).then((response) => {
                    this.envlist = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
    get_policy_list(){
        var api = '/handpay/project/app/networkpolicy/list'
      			this.$http.get(api).then((response) => {
                    this.netPoliceList = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
    OnChange(){
        var api = '/handpay/project/app/networkpolicy/status'
      	this.$http.post(api,{'status':this.status,'env':this.env}).then((response) => {
            this.netPoliceList = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
    commitNetRules() {
       var api = '/handpay/project/app/networkpolicy/change/status'
      	this.$http.post(api,{'status':0,'rules':this.multipleSelection}).then((response) => {
            this.OnChange()
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
    delNetRules() {
       var api = '/handpay/project/app/networkpolicy/change/status'
      	this.$http.post(api,{'status':2,'rules':this.multipleSelection}).then((response) => {
            this.OnChange()
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
  },
  mounted() {
      this.get_env()
      this.get_policy_list()
  }
};
</script>
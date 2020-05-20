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
      策略类型:<el-select v-model="nptype"  @input="OnChange()" placeholder="请选择">
     <el-option
      v-for="item in nptypelist"
      :key="item.value"
      :label="item.label"
      :value="item.value"
      >
      </el-option>
      </el-select>
      包名查询:<el-select v-model="warname"  @input="OnChange()" filterable  placeholder="请选择">
     <el-option
      v-for="item in pkglist"
      :key="item.warname"
      :label="item.warname"
      :value="item.warname"
      >
      </el-option>
      </el-select>
    <div style="margin: 15px 0;"></div>
    <div style="margin: 15px 0;"></div>
    <template>
    <el-table
      :data="netPoliceList"
      style="width: 100%">
      <el-table-column
        prop="warname"
        label="包名">
      </el-table-column>
      <el-table-column
        prop="ip"
        sortable 
        label="源地址">
      </el-table-column>
      <el-table-column
       v-if="nptype === '内部'"
        prop="nodelist"
        label="目的地址">
      </el-table-column>
      <el-table-column
       v-if="nptype === '外部'"
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
        prop="nptype"
        label="策略类型">
      </el-table-column>
      <el-table-column
        prop="owner"
        label="需求方">
      </el-table-column>
      <el-table-column
        prop="desc"
        label="业务说明">
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
      netPoliceList: [],
      envlist: [],
      nptype: "内部",
      pkglist:[],
      netPoliceList: '',
      warname: '',
      nptypelist: [{ value: "内部", lable: 0 }, { value: "外部", lable: 1 }],
    };
  },
  methods: {
    get_env(){
        var api = '/handpay/project/env/list'
      			this.$http.get(api).then((response) => {
                    this.envlist = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
    get_warname(){
        var api = '/handpay/project/appdeployment/list/src'
      	this.$http.get(api).then((response) => {
            this.pkglist = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
    OnChange(){
        var api = '/handpay/project/netpolicy/list'
      	this.$http.post(api,{'env':this.env,'warname':this.warname,'nptype':this.nptype}).then((response) => {
            this.netPoliceList = response.body
            console.log(this.netPoliceList)
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
  },
  mounted() {
      this.get_env(),
      this.get_warname()
      this.OnChange()
  }
};
</script>
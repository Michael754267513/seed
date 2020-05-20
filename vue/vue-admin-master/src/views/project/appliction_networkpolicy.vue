<template>
    <section>
    策略类型:<el-select v-model="value" @input="OnChange()" placeholder="请选择">
     <el-option
      v-for="item in nptype"
      :key="item.value"
      :label="item.label"
      :value="item.value"
      >
      </el-option>
      </el-select>
    <div style="margin: 15px 0;"></div>
      <div style="margin: 15px 0;"></div>
  <template v-if="value === '内部'">
    <el-form :inline="true" :model="netPolicy" class="demo-form-inline">
     <el-form-item label="需求方">
       <el-input v-model="netPolicy.owner" placeholder="需求方"></el-input>
     </el-form-item>
      <el-form-item label="业务用途">
       <el-input v-model="netPolicy.desc" placeholder="业务用途"></el-input>
     </el-form-item>
      <el-form-item label="源地址">
    <el-select v-model="netPolicy.src" filterable  placeholder="源地址">
      <el-option
      v-for="item in listsrc"
      :key="item.warname"
      :label="item.warname"
      :value="item.warname"
      >
      </el-option>
    </el-select>
    </el-form-item>
    <el-form-item label="目标地址">
    <el-select v-model="netPolicy.dest" filterable @input="SelectDest()" placeholder="目标地址">
      <el-option
      v-for="item in listdest"
      :key="item.pkgalias"
      :label="item.pkgalias"
      :value="item.pkgalias"
      >
      </el-option>
    </el-select>
    </el-form-item>
    <el-form-item label="目标端口">
    <el-select v-model="netPolicy.port"   placeholder="目标端口"></el-select>
    </el-form-item>
    <el-form-item label="协议">
    <el-select v-model="netPolicy.protocol" placeholder="协议">
      <el-option label="TCP"  value="TCP"></el-option>
      <el-option label="UDP" value="UDP"></el-option>
    </el-select>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">确认添加</el-button>
    </el-form-item>
    </el-form>
  </template>
  <template v-if="value === '外部'">
    <el-form :inline="true" :model="netPolicy" class="demo-form-inline">
     <el-form-item label="需求方">
       <el-input v-model="netPolicy.owner" placeholder="需求方"></el-input>
     </el-form-item>
      <el-form-item label="业务用途">
       <el-input v-model="netPolicy.desc" placeholder="业务用途"></el-input>
     </el-form-item>
      <el-form-item label="源地址">
    <el-select v-model="netPolicy.src" filterable  placeholder="源地址">
    <el-option
      v-for="item in listsrc"
      :key="item.warname"
      :label="item.warname"
      :value="item.warname"
      >
      </el-option>
    </el-select>
    </el-form-item>
    <el-form-item label="目标地址">
    <el-input v-model="netPolicy.dest"   placeholder="目标地址"></el-input>
    </el-form-item>
    </el-form-item>
    <el-form-item label="目标端口">
    <el-input v-model="netPolicy.port" placeholder="目标端口"></el-input>
    </el-form-item>
    <el-form-item label="协议">
    <el-select v-model="netPolicy.protocol" placeholder="协议">
      <el-option label="TCP" value="TCP"></el-option>
      <el-option label="UDP" value="UDP"></el-option>
    </el-select>
      <el-button type="primary" @click="onSubmit">确认添加</el-button>
    </el-form-item>
    </el-form>
  </template>
  <el-button type="primary" @click='commitNetRules'>提交策略</el-button>
  <template>
    <el-table
      :data="netPoliceList"
      style="width: 100%">
      <el-table-column
        prop="src"
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
        prop="type"
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
      <el-table-column
      fixed="right"
      label="删除规则"
	  width="100">
      <template slot-scope="scope">
        <el-button
          @click.native.prevent="delNetRule(scope.$index, netPoliceList)"
          type="text"
          size="small">
          确认删除
        </el-button>
      </template>
    </el-table-column>
    </el-table>
  </template>
</section>  
</template>

<script>
export default {
  data() {
    return {
      netPolicy: {
        owner: "",
        desc: "",
        src: "",
        protocol: "TCP",
        dest: "",
        port: "",
      },
      listsrc: [],
      npMessage: '',
      dest: [],
      listdest: [],
      netPoliceList: [],
      value: "内部",
      nptype: [{ value: "内部", lable: 0 }, { value: "外部", lable: 1 }],
    };
  },
  methods: {
    delNetRule: function(index, ruleData){
      this.netPoliceList.pop(index)
    },
    commitNetRules(){
              var api = '/handpay/project/networkpolicy/add'
      			this.$http.post(api,{'netpolicy':this.netPoliceList}).then((response) => {
                    this.npMessage = response.body
                    this.open()
                    this.netPoliceList = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
    OnChange(){
      this.netPolicy.dest = ''
      this.netPolicy.port = ''
    },
    open() {
      this.$alert(this.npMessage, '执行失败列表')
    },
    onSubmit() {
      this.netPoliceList.push({"owner":this.netPolicy.owner,
              "desc":this.netPolicy.desc,
              "src": this.netPolicy.src,
              "dest":  this.netPolicy.dest,
              "port": this.netPolicy.port,
              "protocol": this.netPolicy.protocol,
              "nptype":  this.value,
              })
      console.log(this.netPolicy)
      // this.netPoliceList = this.netPolicy
    },
    get_src(){
        var api = '/handpay/project/appdeployment/list/src'
      			this.$http.get(api).then((response) => {
                    this.listsrc = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
    get_dest(){
        var api = '/handpay/project/appdeployment/list/dest'
      			this.$http.get(api).then((response) => {
                    this.listdest = response.body
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
    SelectDest(){
        var api = '/handpay/project/appdeployment/list/dest/port'
      			this.$http.post(api,{'pkgalias':this.netPolicy.dest}).then((response) => {
                    this.dest = response.body
                    this.netPolicy.port = this.dest['port']
                    console.log(this.netPolicy.port)
	 			 },
				function (err) {
        			console.log(err)
				  })
    },
    
  },
  mounted() {
      this.get_src(),
      this.get_dest()
  }
};
</script>
<template>
    <section>
    策略类型:<el-select v-model="value" placeholder="请选择">
     <el-option
      v-for="item in npSeleteType"
      :key="item.value"
      :label="item.label"
      :value="item.value"
      >
      </el-option>
      </el-select>
    环境:<el-select v-model="env" placeholder="请选择">
     <el-option
      v-for="item in env_list"
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
      <el-form-item label="使用时间">
       <el-input v-model="netPolicy.endTime" placeholder="使用时间"></el-input>
     </el-form-item>
      <el-form-item label="源地址">
    <el-select v-model="netPolicy.srcIP" placeholder="源地址">
      <el-option label="hpaySupport" value="1.1.1.1"></el-option>
      <el-option label="hpayService" value="2.2.2.2"></el-option>
    </el-select>
    </el-form-item>

    <el-form-item label="目标地址">
    <el-select v-model="netPolicy.destIP" placeholder="目标地址">
      <el-option label="riskzk01" value="3.3.3.3"></el-option>
      <el-option label="hpayService" value="2.2.2.2"></el-option>
    </el-select>
    </el-form-item>
    </el-form-item>
    <el-form-item label="目标端口">
    <el-input v-model="netPolicy.destPort" placeholder="目标端口"></el-input>
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
      <el-form-item label="使用时间">
       <el-input v-model="netPolicy.endTime" placeholder="使用时间"></el-input>
     </el-form-item>
      <el-form-item label="源地址">
    <el-select v-model="netPolicy.srcIP" placeholder="源地址">
      <el-option label="riskzk01" value="3.3.3.3"></el-option>
      <el-option label="hpayService" value="2.2.2.2"></el-option>
    </el-select>
    </el-form-item>
    <el-form-item label="目标地址">
    <el-input v-model="netPolicy.destIP" placeholder="目标地址"></el-input>
    </el-form-item>
    </el-form-item>
    <el-form-item label="目标端口">
    <el-input v-model="netPolicy.destPort" placeholder="目标端口"></el-input>
    </el-form-item>
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
        prop="env"
        label="环境">
      </el-table-column>
      <el-table-column
        prop="srcIP"
        label="源地址">
      </el-table-column>
      <el-table-column
        prop="destIP"
        label="目的地址">
      </el-table-column>
      <el-table-column
        prop="destPort"
        label="目标端口">
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
        prop="endTime"
        label="使用时间">
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
        endTime: "",
        srcIP: "",
        destIP: "",
        destPort: "",
      },
      netPoliceList: [],
      value: "内部",
      npSeleteType: [{ value: "内部", lable: 0 }, { value: "外部", lable: 1 }],
      env: "办公",
      env_list: [
        { value: "HPA", lable: 0 }, 
        { value: "HPC", lable: 1 }, 
        { value: "GRID", lable: 2 },
        { value: "杉德", lable: 3 },
        { value: "灾备", lable: 4 },
        { value: "办公", lable: 5 }

        ]
    };
  },
  methods: {
    delNetRule: function(index, ruleData){
      this.netPoliceList.pop(index)
      console.log(this.netPoliceList)
    },
    commitNetRules(){
      console.log(this.netPoliceList)
    },
    onSubmit() {
      this.netPoliceList.push({"owner":this.netPolicy.owner,
              "desc":this.netPolicy.desc,
              "endTime": this.netPolicy.endTime,
              "srcIP": this.netPolicy.srcIP,
              "destIP":  this.netPolicy.destIP,
              "destPort": this.netPolicy.destPort,
              "type":  this.value,
              "env": this.env
              })
      console.log(this.netPolicy)
      // this.netPoliceList = this.netPolicy
    }
  },
  mounted() {}
};
</script>
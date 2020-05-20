<template>
    <section>
    策略类型:<el-select v-model="value"  @input="npType(value)" placeholder="请选择">
     <el-option
      v-for="item in npSeleteType"
      :key="item.value"
      :label="item.label"
      :value="item.value"
      >
      </el-option>
    </el-select>
    <el-input
  type="textarea"
  :rows="2"
  :autosize="{ minRows: 2, maxRows: 6 }"
  placeholder="请输入内容"
  v-model="textarea">
</el-input>
    <div style="margin: 15px 0;"></div>
    <template v-if="value === '内部'">
      源地址:<el-select v-model="src" style="margin-left: 10px;" multiple placeholder="请选择">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  目标地址:<el-select  v-model="dest" multiple collapse-tags
    style="margin-left: 10px;"
    placeholder="请选择">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  目标端口:<el-select v-model="dest_port" multiple collapse-tags
    style="margin-left: 10px;"
    placeholder="请选择">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  <el-button type="primary" >确认添加</el-button>
    </template>
    <template v-if="value === '外部'">
            源地址:<el-select v-model="src" style="margin-left: 10px;" multiple placeholder="请选择">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  目标地址:<el-select  v-model="dest" multiple collapse-tags
    style="margin-left: 10px;"
    placeholder="请选择">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  目标端口:<el-select v-model="dest_port" multiple collapse-tags
    style="margin-left: 10px;"
    placeholder="请选择">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  <el-button type="primary" >确认添加</el-button>
    </template>


    </section> 
</template>

<script>
  
  export default {
 data () {
    return {
     src: '',
     dest: '',
     dest_port: '',
     value: "内部",
     npSeleteType: [{'value': '内部',"lable":0},{'value': '外部',"lable":1}],
     npTypeNum: 0
    }
  },
  methods: {
    npType () {
         
      }
    },
  mounted() {
		}
}


</script>
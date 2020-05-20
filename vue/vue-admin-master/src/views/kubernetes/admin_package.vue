<template>
	<section>
		<!--工具条-->
		<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-form :inline="true">
				<el-form-item>
					<el-button type="primary" @click="handleAddprj">新增项目</el-button>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" @click="handleAddlable">新增标签</el-button>
				</el-form-item>
								<el-form-item>
					<el-button type="primary" @click="handleAddpl">项目标签关联</el-button>
				</el-form-item>
			</el-form>
		</el-col>
	<!-- 项目添加 -->
    <el-dialog title="新增项目" v-model="addFormVisible" :close-on-click-modal="false">
			<el-form :model="addForm" label-width="80px" :rules="addFormRules" ref="addForm">
				<el-form-item label="项目" prop="prjname">
					<el-input v-model="addForm.prjname" auto-complete="off"></el-input>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click.native="addFormVisible = false">取消</el-button>
				<el-button type="primary" @click.native="addSubmitprj" :loading="addLoading">提交</el-button>
			</div>
		</el-dialog>
	<!-- 标签添加 -->
    <el-dialog title="新增项目标签" v-model="addFormVisiblelable" :close-on-click-modal="false">
			<el-form :model="addFormlable" label-width="80px" :rules="addFormRules" ref="addFormlable">
				<el-form-item label="标签" prop="lable">
					<el-input v-model="addFormlable.lable" auto-complete="off"></el-input>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click.native="addFormVisiblelable = false">取消</el-button>
				<el-button type="primary" @click.native="addSubmitlable" :loading="addLoadinglable">提交</el-button>
			</div>
		</el-dialog>
	<!-- 标签项目关联 -->
    <el-dialog title="新增项目标签" v-model="addFormVisiblelable" :close-on-click-modal="false">
			<el-form :model="addFormlable" label-width="80px" :rules="addFormRuleslable" ref="addFormlable">
				<el-form-item label="标签" prop="lable">
					<el-input v-model="addFormlable.lable" auto-complete="off"></el-input>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click.native="addFormVisiblelable = false">取消</el-button>
				<el-button type="primary" @click.native="addSubmitlable" :loading="addLoadinglable">提交</el-button>
			</div>
		</el-dialog>
	</section>
	</section>
</template>

<script>
export default {
  data () {
    return {
		addFormVisiblelable: false,
		addFormVisible: false,//新增界面是否显示
		addFormVisiblepl: false,//新增界面是否显示
		addLoading: false,
		addLoadinglable: false,
		addLoadingpl: false,
		addFormRules: {
			prjname: [
            	{ required: true, message: '必填项目名', trigger: 'blur' },
             // { validator: 'validatAlphabets', message: '请输入字母不区分大小写', trigger: 'blur'}
					],
			lable: [
            	{ required: true, message: '必填项目名', trigger: 'blur' },
					]
				},
		addForm: {
			prjname: '',
			},
		addFormlable: {
			lable: '',
			}
		}
  },
  methods: {
	    handleAddlable: function () {
				this.addFormVisiblelable = true;
				this.addFormlable = {
					lable: '',
				
				};
      },
	    handleAddprj: function () {
				this.addFormVisible = true;
				this.addForm = {
					prjname: '',
				
				};
	  },
   	    handleAddlable: function () {
				this.addFormVisiblelable = true;
				this.addFormlable = {
					lable: '',
				
				};
      },
   	    handleAddprj: function () {
				this.addFormVisible = true;
				this.addForm = {
					prjname: '',
				
				};
	  },
		handleAddpl: function () {
				this.addFormVisible = true;
				this.addForm = {
					prjname: '',
					lable: '',
				
				};
	  },
        addSubmitlable: function () {
				this.$refs.addFormlable.validate((valid) => {
					if (valid) {
						this.$confirm('提交项目名:' + this.addFormlable.lable, '提示', {'提交项目名': this.addFormlable.lable}).then(() => {
							this.addLoadinglable = true;
							this.$http.post('/kubernetes/project/add',{'project':this.addFormlable.lable}).then((res) => {
								this.addLoadinglable = false;
								this.$message({
									message: '提交成功',
									type: 'success'
								});
								this.$refs['addFormlable'].resetFields();
								this.addFormVisiblelable = false;
							});
						});
					}
				});
			},

        addSubmitprj: function () {
				this.$refs.addForm.validate((valid) => {
					if (valid) {
						this.$confirm('提交项目名:' + this.addForm.prjname, '提示', {'提交项目名': this.addForm.prjname}).then(() => {
							this.addLoading = true;
							this.$http.post('/kubernetes/project/lable/add',{'project':this.addForm.prjname}).then((res) => {
								this.addLoading = false;
								// this.addFormVisible = false;
								this.$message({
									message: '提交成功',
									type: 'success'
								});
								this.$refs['addForm'].resetFields();
								this.addFormVisible = false;
							});
						});
					}
				});
			},

  },
  mounted() {
     
		}
}
</script>

<style>
</style>

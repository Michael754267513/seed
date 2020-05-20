<template>
	<section>
		<!--工具条-->
		<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-form :inline="true" :model="filters">
				<el-form-item>
					<el-input v-model="filters.name" placeholder="虚拟机名称"></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" @click="getDatavm">查询</el-button>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" @click="handleAdd">新增虚拟机</el-button>
				</el-form-item>
			</el-form>
		</el-col>

		<!--列表-->
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
		<!--工具条-->
		<el-col :span="24" class="toolbar">
			<el-button type="danger" @click="batchRemove" :disabled="this.sels.length===0">批量删除</el-button>
			<el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20" :total="total" style="float:right;">
			</el-pagination>
		</el-col>

		<!--编辑界面-->
		<el-dialog title="编辑" v-model="editFormVisible" :close-on-click-modal="false">
			<el-form :model="editForm" label-width="80px" :rules="editFormRules" ref="editForm">
				<el-form-item label="姓名" prop="name">
					<el-input v-model="editForm.name" auto-complete="off"></el-input>
				</el-form-item>
				<el-form-item label="性别">
					<el-radio-group v-model="editForm.sex">
						<el-radio class="radio" :label="1">男</el-radio>
						<el-radio class="radio" :label="0">女</el-radio>
					</el-radio-group>
				</el-form-item>
				<el-form-item label="年龄">
					<el-input-number v-model="editForm.age" :min="0" :max="200"></el-input-number>
				</el-form-item>
				<el-form-item label="生日">
					<el-date-picker type="date" placeholder="选择日期" v-model="editForm.birth"></el-date-picker>
				</el-form-item>
				<el-form-item label="地址">
					<el-input type="textarea" v-model="editForm.addr"></el-input>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click.native="editFormVisible = false">取消</el-button>
				<el-button type="primary" @click.native="editSubmit" :loading="editLoading">提交</el-button>
			</div>
		</el-dialog>

		<!--新增界面-->
		<el-dialog title="新增" v-model="addFormVisible" :close-on-click-modal="false">
			<el-form :model="addForm" label-width="100px" :rules="addFormRules" ref="addForm">
				<el-form-item label="虚拟机名称" prop="vmname">
					<el-input auto-complete="off"></el-input>
				</el-form-item>
        <el-form-item label="虚拟机名称" prop="vmname">
					<el-input auto-complete="off"></el-input>
				</el-form-item>
        <el-form-item label="虚拟机名称" prop="vmname">
					<el-input auto-complete="off"></el-input>
				</el-form-item>
        <el-form-item label="虚拟机名称" prop="vmname">
					<el-input auto-complete="off"></el-input>
				</el-form-item>
        <el-form-item label="虚拟机名称" prop="vmname">
					<el-input auto-complete="off"></el-input>
				</el-form-item>
        <el-form-item label="虚拟机名称" prop="vmname">
					<el-input auto-complete="off"></el-input>
				</el-form-item>
        <el-form-item label="虚拟机名称" prop="vmname">
					<el-input auto-complete="off"></el-input>
				</el-form-item>
        <el-form-item label="虚拟机名称" prop="vmname">
					<el-input auto-complete="off"></el-input>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click.native="addFormVisible = false">取消</el-button>
				<el-button type="primary" @click.native="addSubmit" :loading="addLoading">提交</el-button>
			</div>
		</el-dialog>
	</section>
</template>

<script>
	import util from '../../common/js/util'
	//import NProgress from 'nprogress'
	import { getUserListPage, removeUser, batchRemoveUser, editUser, addUser, getVMS } from '../../api/api';

	export default {
		data() {
			return {
        vmdata: [],
				filters: {
					name: ''
				},
				users: [],
				total: 0,
				page: 1,
				listLoading: false,
				sels: [],//列表选中列

				editFormVisible: false,//编辑界面是否显示
				editLoading: false,
				editFormRules: {
					name: [
						{ required: true, message: '请输入姓名', trigger: 'blur' }
					]
				},
				//编辑界面数据
				editForm: {
					id: 0,
					name: '',
					sex: -1,
					age: 0,
					birth: '',
					addr: ''
				},

				addFormVisible: false,//新增界面是否显示
				addLoading: false,
				addFormRules: {
					name: [
						{ required: true, message: '请输入姓名', trigger: 'blur' }
					]
				},
				//新增界面数据
				addForm: {
					name: '',
					sex: -1,
					age: 0,
					birth: '',
					addr: ''
				}

			}
		},
		methods: {
			//性别显示转换
			formatSex: function (row, column) {
				return row.sex == 1 ? '男' : row.sex == 0 ? '女' : '未知';
			},
			handleCurrentChange(val) {
				this.page = val;
				this.getUsers();
			},
			//获取用户列表
			getUsers() {
				let para = {
					page: this.page,
					name: this.filters.name
				};
				this.listLoading = true;
				//NProgress.start();
				getUserListPage(para).then((res) => {
					this.total = res.data.total;
					this.users = res.data.users;
					this.listLoading = false;
					//NProgress.done();
				});
			},
			//删除
			handleDel: function (index, row) {
				this.$confirm('确认删除该记录吗?', '提示', {
					type: 'warning'
				}).then(() => {
					this.listLoading = true;
					//NProgress.start();
					let para = { id: row.id };
					removeUser(para).then((res) => {
						this.listLoading = false;
						//NProgress.done();
						this.$message({
							message: '删除成功',
							type: 'success'
						});
						this.getUsers();
					});
				}).catch(() => {

				});
			},
			//显示编辑界面
			handleEdit: function (index, row) {
				this.editFormVisible = true;
				this.editForm = Object.assign({}, row);
			},
			//显示新增界面
			handleAdd: function () {
				this.addFormVisible = true;
				this.addForm = {
					name: '',
					sex: -1,
					age: 0,
					birth: '',
					addr: ''
				};
			},
			//编辑
			editSubmit: function () {
				this.$refs.editForm.validate((valid) => {
					if (valid) {
						this.$confirm('确认提交吗？', '提示', {}).then(() => {
							this.editLoading = true;
							//NProgress.start();
							let para = Object.assign({}, this.editForm);
							para.birth = (!para.birth || para.birth == '') ? '' : util.formatDate.format(new Date(para.birth), 'yyyy-MM-dd');
							editUser(para).then((res) => {
								this.editLoading = false;
								//NProgress.done();
								this.$message({
									message: '提交成功',
									type: 'success'
								});
								this.$refs['editForm'].resetFields();
								this.editFormVisible = false;
								this.getUsers();
							});
						});
					}
				});
			},
			//新增
			addSubmit: function () {
				this.$refs.addForm.validate((valid) => {
					if (valid) {
						this.$confirm('确认提交吗？', '提示', {}).then(() => {
							this.addLoading = true;
							//NProgress.start();
							let para = Object.assign({}, this.addForm);
							para.birth = (!para.birth || para.birth == '') ? '' : util.formatDate.format(new Date(para.birth), 'yyyy-MM-dd');
							addUser(para).then((res) => {
								this.addLoading = false;
								//NProgress.done();
								this.$message({
									message: '提交成功',
									type: 'success'
								});
								this.$refs['addForm'].resetFields();
								this.addFormVisible = false;
								this.getUsers();
							});
						});
					}
				});
			},
			selsChange: function (sels) {
				this.sels = sels;
			},
			//批量删除
			batchRemove: function () {
				var ids = this.sels.map(item => item.id).toString();
				this.$confirm('确认删除选中记录吗？', '提示', {
					type: 'warning'
				}).then(() => {
					this.listLoading = true;
					//NProgress.start();
					let para = { ids: ids };
					batchRemoveUser(para).then((res) => {
						this.listLoading = false;
						//NProgress.done();
						this.$message({
							message: '删除成功',
							type: 'success'
						});
						this.getUsers();
					});
				}).catch(() => {

				});
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
		// mounted() {
		// 	this.getUsers();
    // }
    mounted() {
			this.getDatavm()
		}
	}

</script>

<style scoped>

</style>